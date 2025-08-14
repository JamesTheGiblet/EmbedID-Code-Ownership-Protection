import json
import os
from datetime import datetime, timezone
from typing import List, Dict

DEFAULT_REGISTRY_PATH = '.embedid/registry.json'

class SignatureRegistry:
    """
    Manages a local JSON-based registry of signature embedding events.
    This provides an audit trail of who signed which files and when.
    """

    def __init__(self, registry_path: str = DEFAULT_REGISTRY_PATH):
        self.registry_path = registry_path

    def _load_registry(self) -> List[Dict]:
        """Loads the registry from disk."""
        if not os.path.exists(self.registry_path):
            return []
        try:
            with open(self.registry_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save_registry(self, data: List[Dict]):
        """Saves the registry to disk."""
        os.makedirs(os.path.dirname(self.registry_path), exist_ok=True)
        with open(self.registry_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def add_embedding_record(self, file_path: str, signer_alias: str, hash_algo: str, fragments: List[str]):
        """Adds a new record to the registry for a successful embedding action."""
        registry = self._load_registry()
        new_record = {
            'timestamp_utc': datetime.now(timezone.utc).isoformat(),
            'file_path': os.path.abspath(file_path),
            'signer_alias': signer_alias,
            'hash_algo': hash_algo,
            'fragment_count': len(fragments),
            'fragments': fragments
        }
        registry.append(new_record)
        self._save_registry(registry)

    def get_records(self) -> List[Dict]:
        """Retrieves all records from the registry."""
        return self._load_registry()