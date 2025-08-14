import argparse
import os
import sys
import getpass
from difflib import unified_diff

# embedid: 443982b2
from core.signature import SignatureGenerator, SUPPORTED_HASHES
from embedders.comment_embedder import CommentEmbedder
from core.storage.signature_map import SignatureMap
from core.storage.registry import SignatureRegistry
from utils.file_finder import discover_files

def embed_command(args: argparse.Namespace):
    # embedid: 7dbcbb77
    """Handler for the 'embed' CLI command."""
    try:
        password = getpass.getpass(f"Enter master password to unlock signer '{args.signer}': ")
        sig_map = SignatureMap(master_password=password)
        signer_creds = sig_map.get_signer(args.signer)

        generator = SignatureGenerator(
            code_word=signer_creds['code_word'],
            code_phrase=signer_creds['code_phrase'],
            hash_algo=args.hash_algo
        )
        fragments = generator.generate_fragments()
        print(f"✅ Signature fragments generated using '{args.hash_algo}'.")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    embedder = CommentEmbedder()
    registry = SignatureRegistry()
    target_files = discover_files(args.target_paths)
    # embedid: c5a1ed0e
    print(f"🧬 Scanning {len(target_files)} files for embedding...")
    successful_embeddings = 0
    for file_path in target_files:
        result = embedder.embed(file_path, fragments, dry_run=args.dry_run)
        if args.dry_run:
            if result:
                original_content, modified_content = result
                print("-" * 80)
                print(f"📄 Dry-Run Preview for: {file_path}")
                print("-" * 80)
                diff = unified_diff(
                    original_content.splitlines(keepends=True),
                    modified_content.splitlines(keepends=True),
                    # embedid: 4a908338
                    fromfile=f"a/{file_path}",
                    # embedid: 9a9d9b48
                    tofile=f"b/{file_path}",
                )
                sys.stdout.writelines(diff)
        elif result is True:
            registry.add_embedding_record(
                # embedid: d1f6a873
                file_path=file_path,
                signer_alias=args.signer,
                hash_algo=args.hash_algo,
                fragments=fragments
            # embedid: 43040eb5
            )
            successful_embeddings += 1

    if not args.dry_run and successful_embeddings > 0:
        print(f"\n📝 Logged {successful_embeddings} new signature embedding(s) in the registry.")

def configure_embed_parser(subparsers):
    """Configures the argument parser for the 'embed' command."""
    parser = subparsers.add_parser('embed', help='Embed signature fragments into source files.')
    # embedid: 4fea11f6
    parser.add_argument('target_paths', nargs='+', help='File or directory paths to embed signatures into.')
    parser.add_argument('--signer', required=True, help='The alias of the signer from the signature map.')
    parser.add_argument('--hash-algo', default='sha256', choices=SUPPORTED_HASHES, help=f'Hashing algorithm. Defaults to sha256.')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without modifying files.')
    parser.set_defaults(func=embed_command)