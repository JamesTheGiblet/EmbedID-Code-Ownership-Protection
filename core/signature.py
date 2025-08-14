import hashlib
import binascii

SUPPORTED_HASHES = {'sha256', 'sha3_256', 'blake2b'}

class SignatureGenerator:
    """
    Generates cryptographic signature fragments from a code-word and code-phrase.

    The process is deterministic, meaning the same inputs will always produce
    the same output fragments, which is essential for verification.
    """

    def __init__(self, code_word: str, code_phrase: str, salt_len: int = 16, iterations: int = 100000, hash_algo: str = 'sha256'):
        """
        Initializes the generator with user-provided identity elements.

        Args:
            code_word (str): A public or semi-public word used to derive the salt.
            code_phrase (str): A secret phrase used for generating the signature key.
            salt_len (int): The length of the salt to be generated.
            iterations (int): The number of iterations for the PBKDF2 algorithm.
            hash_algo (str): The hashing algorithm to use for key derivation.
        """
        if not code_word or not code_phrase:
            raise ValueError("Code-word and code-phrase cannot be empty.")

        if hash_algo not in SUPPORTED_HASHES:
            raise ValueError(f"Unsupported hash algorithm: {hash_algo}. Supported are: {SUPPORTED_HASHES}")

        self.code_word = code_word
        self.code_phrase = code_phrase
        self.hash_algo = hash_algo
        self.salt = self._derive_salt(code_word, salt_len)
        self.iterations = iterations

    def _derive_salt(self, code_word: str, salt_len: int) -> bytes:
        """
        Derives a deterministic salt from the code-word.

        Uses the specified hash algorithm to derive a salt from the code-word.
        This ensures that for a given code-word and hash algorithm, the salt
        is always the same, allowing for reproducible key generation.
        """
        hasher = hashlib.new(self.hash_algo)
        hasher.update(code_word.encode('utf-8'))
        return hasher.digest()[:salt_len]

    def _generate_master_key(self, key_len: int = 32) -> bytes:
        """
        Generates the master signature key using PBKDF2.

        PBKDF2 (Password-Based Key Derivation Function 2) is used to securely
        derive a cryptographic key from a password (the code-phrase). It helps
        protect against brute-force and dictionary attacks.
        """
        key = hashlib.pbkdf2_hmac(
            self.hash_algo,
            self.code_phrase.encode('utf-8'),
            self.salt,
            self.iterations,
            dklen=key_len
        )
        return key

    def generate_fragments(self, num_fragments: int = 8, fragment_len: int = 8) -> list[str]:
        """
        Generates a set of signature fragments from the master key.

        Args:
            num_fragments (int): The number of fragments to generate.
            fragment_len (int): The length of each fragment string (in characters).

        Returns:
            list[str]: A list of signature fragments.
        """
        if num_fragments <= 0 or fragment_len <= 0:
            raise ValueError("Number of fragments and fragment length must be positive.")

        # Calculate the required length of the master key in bytes.
        # Each byte of the key becomes 2 hex characters.
        required_key_len_bytes = (num_fragments * fragment_len + 1) // 2

        master_key = self._generate_master_key(key_len=required_key_len_bytes)
        hex_key = binascii.hexlify(master_key).decode('utf-8')

        fragments = [hex_key[i * fragment_len : (i + 1) * fragment_len] for i in range(num_fragments)]

        return fragments

if __name__ == '__main__':
    # Example Usage based on the README.md quickstart command.
    try:
        # Using the new blake2b hashing algorithm
        generator = SignatureGenerator(code_word="txGq", code_phrase="flux", hash_algo='blake2b')
        fragments = generator.generate_fragments(num_fragments=8, fragment_len=8)

        print("🧬 EmbedID Signature Fragment Generator")
        print("-" * 40)
        print(f"Code-Word: '{generator.code_word}'")
        print(f"Code-Phrase: '****' (hidden for security)")
        print(f"Hash Algorithm: {generator.hash_algo}")
        print(f"Salt (hex): {binascii.hexlify(generator.salt).decode('utf-8')}")
        print(f"Generated {len(fragments)} fragments:")
        for i, fragment in enumerate(fragments):
            print(f"  Fragment {i+1}: {fragment}")

    except ValueError as e:
        print(f"Error: {e}")