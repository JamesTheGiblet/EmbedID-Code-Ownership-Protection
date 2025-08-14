import argparse
import sys
import os

from core.storage.registry import SignatureRegistry

def view_log_command(args: argparse.Namespace):
    """Handler for the 'registry view' command."""
    registry = SignatureRegistry()
    records = registry.get_records()

    if not records:
        print("Signature registry is empty.")
        return

    print("📜 Signature Embedding Registry Log")
    print("-" * 40)
    for record in reversed(records): # Show most recent first
        print(f"Timestamp: {record['timestamp_utc']}")
        print(f"  File:    {record['file_path']}")
        print(f"  Signer:  {record['signer_alias']}")
        print(f"  Hash:    {record['hash_algo']}")
        print(f"  Count:   {record['fragment_count']}")
        print("-" * 40)

def configure_registry_parser(subparsers):
    """Configures the argument parser for the 'registry' command."""
    registry_parser = subparsers.add_parser('registry', help='Interact with the signature embedding registry.')
    registry_subparsers = registry_parser.add_subparsers(dest='registry_command', required=True)

    # 'registry view' command
    view_parser = registry_subparsers.add_parser('view', help='View the log of all signature embeddings.')
    view_parser.set_defaults(func=view_log_command)