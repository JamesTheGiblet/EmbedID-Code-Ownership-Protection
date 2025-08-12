from cipher_methods import vigenere_cipher

def test_embed_and_verify():
    sig = "JamesTheGiblet"
    code = "print('Hello')"
    embedded = vigenere_cipher.embed(sig, code)
    assert vigenere_cipher.verify(sig, embedded)
