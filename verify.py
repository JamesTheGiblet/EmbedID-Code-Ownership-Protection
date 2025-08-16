import hashlib
import re

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

# Example usage
verify_file_integrity("your_script.py")