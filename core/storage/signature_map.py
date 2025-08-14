import json
import os
import base64
import hashlib
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

DEFAULT_MAP_PATH = '.embedid/signature_map.json'

class SignatureMap:
    """
    Manages an encrypted JSON file for storing signer credentials.

    The map is encrypted using a key derived from a master password, ensuring
    that sensitive code-phrases are not stored in plaintext.
    """

    def __init__(self, master_password: str, map_path: str = DEFAULT_MAP_PATH):
        self.map_path = map_path
        self.key = self._derive_key(master_password)
        self.fernet = Fernet(self.key)

    def _derive_key(self, password: str) -> bytes:
        """Derives a 32-byte key from the master password using PBKDF2."""
        # A fixed salt is acceptable here because we are deriving a key for a specific
        # file, not storing passwords for multiple users.
        salt = b'embedid-map-salt'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))

    def _load_decrypted(self) -> dict:
        """Loads and decrypts the signature map from disk."""
        if not os.path.exists(self.map_path):
            return {}
        try:
            with open(self.map_path, 'rb') as f:
                encrypted_data = f.read()
            decrypted_data = self.fernet.decrypt(encrypted_data)
            return json.loads(decrypted_data.decode('utf-8'))
        except (InvalidToken, json.JSONDecodeError):
            raise ValueError("Failed to decrypt signature map. Incorrect master password or corrupted file.")
        except FileNotFoundError:
            return {}

    def _save_encrypted(self, data: dict):
        """Encrypts and saves the signature map to disk."""
        os.makedirs(os.path.dirname(self.map_path), exist_ok=True)
        json_data = json.dumps(data, indent=2).encode('utf-8')
        encrypted_data = self.fernet.encrypt(json_data)
        with open(self.map_path, 'wb') as f:
            f.write(encrypted_data)

    def add_signer(self, alias: str, code_word: str, code_phrase: str):
        """Adds a new signer to the map and saves it."""
        data = self._load_decrypted()
        if alias in data:
            raise ValueError(f"Signer alias '{alias}' already exists.")
        data[alias] = {'code_word': code_word, 'code_phrase': code_phrase}
        self._save_encrypted(data)
        print(f"✅ Signer '{alias}' added to the signature map.")

    def get_signer(self, alias: str) -> dict:
        """Retrieves credentials for a specific signer."""
        data = self._load_decrypted()
        signer_data = data.get(alias)
        if not signer_data:
            raise ValueError(f"Signer with alias '{alias}' not found in the signature map.")
        return signer_data

    def get_all_signers(self) -> dict:
        """Retrieves all signers and their data."""
        return self._load_decrypted()