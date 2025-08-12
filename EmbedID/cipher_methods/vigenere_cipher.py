KEY = "EmbedID"

def vigenere_encrypt(text, key):
    return ''.join(
        chr((ord(c) + ord(key[i % len(key)])) % 256)
        for i, c in enumerate(text)
    )

def embed(signature, content):
    encrypted = vigenere_encrypt(signature, KEY)
    return f"# Signature: {encrypted}\n" + content

def verify(signature, content):
    encrypted = vigenere_encrypt(signature, KEY)
    return f"# Signature: {encrypted}" in content
