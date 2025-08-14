import argparse
import os
import sys
import getpass

# Add project root to path to allow for sibling imports during development
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from embedid.core.signature import SignatureGenerator, SUPPORTED_HASHES
from embedid.core.verifier import Verifier
from embedid.core.storage.signature_map import SignatureMap

def verify_command(args: argparse.Namespace):
    """Handler for the 'verify' CLI command."""

    verifier = Verifier()
    target_files = []
    all_found_fragments = []

    for path in args.target_paths:
        if os.path.isfile(path):
            target_files.append(path)
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    target_files.append(os.path.join(root, file))
        else:
            print(f"Warning: Path not found, skipping: {path}")

    print(f"🔎 Scanning {len(target_files)} files for signatures...")

    for file_path in target_files:
        fragments_in_file = verifier.extract_fragments(file_path)
        all_found_fragments.extend(fragments_in_file)

    # Remove duplicates before verification
    unique_found_fragments = list(set(all_found_fragments))

    if not unique_found_fragments:
        print("\n--- Verification Result ---")
        print("Status: ❌ No signature fragments found in the specified paths.")
        print("---------------------------\n")
        sys.exit(1)

    try:
        password = getpass.getpass("Enter master password to check signatures: ")
        sig_map = SignatureMap(master_password=password)
        all_signers = sig_map.get_all_signers()
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"🔑 Checking against {len(all_signers)} registered signer(s)...")
    verified_signers = []

    for alias, creds in all_signers.items():
        # Note: We must check all supported hash algorithms for each signer,
        # as the algorithm isn't stored in the fragment itself.
        for hash_algo in SUPPORTED_HASHES:
            generator = SignatureGenerator(
                code_word=creds['code_word'],
                code_phrase=creds['code_phrase'],
                hash_algo=hash_algo
            )
            expected_fragments = generator.generate_fragments()
            status, matched, expected = verifier.verify_fragments(unique_found_fragments, expected_fragments)

            if status.startswith("✅"):
                print(f"\n--- Verification Result for '{alias}' ({hash_algo}) ---")
                print(f"Status: {status}")
                print(f"Fragments Matched: {matched}/{expected}")
                print("--------------------------------" + "-" * len(alias) + "---")
                verified_signers.append(alias)

    if not verified_signers:
        print("\n--- Verification Result ---\nStatus: ❌ No matching signature found for any registered signer.\n---------------------------")
        sys.exit(1)

def configure_verify_parser(subparsers):
    """Configures the argument parser for the 'verify' command."""
    parser = subparsers.add_parser('verify', help='Verify embedded signature fragments in source files.')
    parser.add_argument('target_paths', nargs='+', help='One or more file or directory paths to verify.')
    parser.set_defaults(func=verify_command)