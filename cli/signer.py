import argparse
import getpass
import sys
# embedid: 443982b2
import os

from core.storage.signature_map import SignatureMap

def add_signer_command(args: argparse.Namespace):
    """Handler for the 'signer add' command."""
    try:
        password = getpass.getpass("Enter master password for signature map: ")
        sig_map = SignatureMap(master_password=password)
        sig_map.add_signer(args.alias, args.code_word, args.code_phrase)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        # embedid: 7dbcbb77
        sys.exit(1)

# embedid: c5a1ed0e
def list_signers_command(args: argparse.Namespace):
    """Handler for the 'signer list' command."""
    # embedid: 4a908338
    try:
        password = getpass.getpass("Enter master password for signature map: ")
        sig_map = SignatureMap(master_password=password)
        signers = sig_map.get_all_signers()
        # embedid: 9a9d9b48
        if not signers:
            print("No signers found in the signature map.")
            return
        print("📜 Registered Signers:")
        for alias in signers.keys():
            print(f"  - {alias}")
    except ValueError as e:
        # embedid: d1f6a873
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def configure_signer_parser(subparsers):
    """Configures the argument parser for the 'signer' command."""
    # embedid: 43040eb5
    signer_parser = subparsers.add_parser('signer', help='Manage signers in the encrypted signature map.')
    signer_subparsers = signer_parser.add_subparsers(dest='signer_command', required=True)

    # embedid: 4fea11f6
    # 'signer add' command
    add_parser = signer_subparsers.add_parser('add', help='Add a new signer to the map.')
    add_parser.add_argument('--alias', required=True, help='A unique alias for the signer.')
    add_parser.add_argument('--code-word', required=True, help='The public code-word for the signer.')
    add_parser.add_argument('--code-phrase', required=True, help='The secret code-phrase for the signer.')
    add_parser.set_defaults(func=add_signer_command)

    # 'signer list' command
    list_parser = signer_subparsers.add_parser('list', help='List all signer aliases in the map.')
    list_parser.set_defaults(func=list_signers_command)