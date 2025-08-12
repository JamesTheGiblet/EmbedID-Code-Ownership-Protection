from cipher_methods import comment_cipher, invisible_cipher, vigenere_cipher

methods = {
    "comment": comment_cipher,
    "invisible": invisible_cipher,
    "vigenere": vigenere_cipher
}

def embed(method, signature, content):
    return methods[method].embed(signature, content)

def verify(method, signature, content):
    return methods[method].verify(signature, content)
