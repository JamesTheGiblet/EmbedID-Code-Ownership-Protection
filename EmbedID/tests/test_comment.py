from cipher_methods import comment_cipher

def test_embed_and_verify():
    sig = "JamesTheGiblet"
    code = "print('Hello')"
    embedded = comment_cipher.embed(sig, code)
    assert comment_cipher.verify(sig, embedded)
