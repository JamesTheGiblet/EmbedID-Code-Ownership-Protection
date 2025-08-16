#!/usr/bin/env python3
import argparse
import hashlib
import datetime
import re
import sys

# ─────────────────────────────────────────────────────────────
# 🧱 CONFIG — Customize your EmbedID defaults here
AUTHOR = "James 'The Giblet' Mavric"
LICENSE = "Builder Sovereignty License v1.0"
EMBEDID_PREFIX = "JTM-2025"
# ─────────────────────────────────────────────────────────────

def generate_embed_block(file_path):
    timestamp = datetime.datetime.now(datetime.UTC).isoformat()
    embed_id = f"{EMBEDID_PREFIX}-{file_path.replace('.py', '').replace('/', '_')}"

    # Phase 1: Inject block with placeholder hash
    placeholder_block = f'''
"""
────────────────────────────────────────────────────────────
🛡️ Authored by {AUTHOR}
🔗 EmbedID: {embed_id}
📜 License: {LICENSE}
📅 Timestamp: {timestamp}
🔒 SHA256: [TO_BE_FILLED]
────────────────────────────────────────────────────────────
"""
'''
    with open(file_path, "r+", encoding="utf-8") as f:
        original = f.read()
        f.seek(0)
        f.write(placeholder_block + "\n" + original)

    # Phase 2: Calculate hash of full file
    with open(file_path, "rb") as f:
        full_content = f.read()
        file_hash = hashlib.sha256(full_content).hexdigest()

    # Phase 3: Replace placeholder with actual hash
    with open(file_path, "r+", encoding="utf-8") as f:
        updated = f.read().replace("SHA256: [TO_BE_FILLED]", f"SHA256: {file_hash}")
        f.seek(0)
        f.write(updated)
        f.truncate()

    print(f"✅ EmbedID block added and locked to {file_path}")

def extract_hash_from_block(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        match = re.search(r"SHA256: ([a-fA-F0-9]+)", content)
        return match.group(1) if match else None

def verify_file_integrity(file_path):
    expected_hash = extract_hash_from_block(file_path)
    if not expected_hash:
        print("❌ No EmbedID hash found. File may be unsigned.")
        return

    with open(file_path, "rb") as f:
        content = f.read()
        actual_hash = hashlib.sha256(content).hexdigest()

    if actual_hash == expected_hash:
        print("✅ Verified: File integrity and authorship intact.")
    else:
        print("⚠️ Tamper detected: File hash mismatch.")

def main():
    parser = argparse.ArgumentParser(
        prog="embedid",
        description="EmbedID CLI — Authorship & Integrity Protocol"
    )
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add EmbedID block to file")
    add_parser.add_argument("file", help="Target file to embed")

    verify_parser = subparsers.add_parser("verify", help="Verify file integrity")
    verify_parser.add_argument("file", help="Target file to verify")

    args = parser.parse_args()

    if args.command == "add":
        generate_embed_block(args.file)
    elif args.command == "verify":
        verify_file_integrity(args.file)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()