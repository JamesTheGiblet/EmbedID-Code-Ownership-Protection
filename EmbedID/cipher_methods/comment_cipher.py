def embed(signature, content):
    comment = f"# Signature: {signature}\n"
    return comment + content

def verify(signature, content):
    return f"# Signature: {signature}" in content
