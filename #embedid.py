import argparse
import sys

from cli.embed import configure_embed_parser
from cli.verify import configure_verify_parser
from cli.signer import configure_signer_parser
from cli.registry import configure_registry_parser

def main():
    """Main CLI entry point for the EmbedID tool."""
    parser = argparse.ArgumentParser(
        description="🧬 EmbedID: A modular protocol for embedding and verifying code signatures.",
        epilog="Use 'python embedid.py <command> --help' for more information on a specific command."
    )
    subparsers = parser.add_subparsers(dest='command', required=True, help='Available commands')

    # Configure subparsers from command modules
    configure_embed_parser(subparsers)
    configure_verify_parser(subparsers)
    configure_signer_parser(subparsers)
    configure_registry_parser(subparsers)
    # Future commands like 'revoke' will be configured here.

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()