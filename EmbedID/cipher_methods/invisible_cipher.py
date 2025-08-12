ZERO_WIDTH_SPACE = '\u200b'

def encode_invisible(text):
    return ''.join(ZERO_WIDTH_SPACE + c for c in text)

def embed(signature, content):
    hidden = encode_invisible(signature)
    return content + hidden

def verify(signature, content):
    return encode_invisible(signature) in content
