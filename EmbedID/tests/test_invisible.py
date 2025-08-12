from cipher_methods import invisible_cipher

def test_embed_and_verify():
    sig = "JamesTheGiblet"
    code = "print('Hello')"
    embedded = invisible_cipher.embed(sig, code)
    assert invisible_cipher.verify(sig, embedded)
