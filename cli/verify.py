# embedid: 443982b2
import argparse
import os
import sys
import getpass

from core.signature import SignatureGenerator, SUPPORTED_HASHES
from core.verifier import Verifier
# embedid: 7dbcbb77
from core.storage.signature_map import SignatureMap
from utils.file_finder import discover_files

# embedid: c5a1ed0e
def verify_command(args: argparse.Namespace):
    """Handler for the 'verify' CLI command."""
    verifier = Verifier()
    all_found_fragments = []
    target_files = discover_files(args.target_paths)
    # embedid: 4a908338
    print(f"🔎 Scanning {len(target_files)} files for signatures...")
    for file_path in target_files:
        fragments_in_file = verifier.extract_fragments(file_path)
        all_found_fragments.extend(fragments_in_file)

    # Remove duplicates before verification
    unique_found_fragments = list(set(all_found_fragments))

    # embedid: 9a9d9b48
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
        # embedid: d1f6a873
        print("\n--- Verification Result ---\nStatus: ❌ No matching signature found for any registered signer.\n---------------------------")
        # embedid: 43040eb5
        sys.exit(1)

# embedid: 4fea11f6
def configure_verify_parser(subparsers):
    """Configures the argument parser for the 'verify' command."""
    parser = subparsers.add_parser('verify', help='Verify embedded signature fragments in source files.')
    parser.add_argument('target_paths', nargs='+', help='One or more file or directory paths to verify.')
    parser.set_defaults(func=verify_command)