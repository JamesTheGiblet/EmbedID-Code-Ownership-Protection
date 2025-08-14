import re
from typing import List, Tuple

# The prefix used to identify embedid fragments in comments.
# This should be kept in sync with the CommentEmbedder.
EMBED_ID_PREFIX = ""

class Verifier:
    """
    Verifies the presence and integrity of embedded signature fragments in files.
    """

    def extract_fragments(self, file_path: str) -> List[str]:
        """
        Extracts all EmbedID fragments from a given file.

        Args:
            file_path (str): The path to the file to scan.

        Returns:
            A list of found fragments.
        """
        found_fragments = []
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    if EMBED_ID_PREFIX in line:
                        # Use regex to robustly find the fragment after the prefix
                        match = re.search(f"{re.escape(EMBED_ID_PREFIX)}(\\S+)", line)
                        if match:
                            found_fragments.append(match.group(1))
        except FileNotFoundError:
            # This can be noisy, so we fail silently. The CLI can report it.
            pass
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
        return found_fragments

    def verify_fragments(self, found_fragments: List[str], expected_fragments: List[str]) -> Tuple[str, int, int]:
        """
        Compares found fragments against a set of expected fragments.

        Returns:
            A tuple containing (status_message, num_matched, num_expected).
        """
        if not found_fragments:
            return ("❌ No signature found", 0, len(expected_fragments))

        # Convert to sets for efficient comparison
        found_set = set(found_fragments)
        expected_set = set(expected_fragments)

        # Check for unexpected fragments, which indicates tampering.
        if not found_set.issubset(expected_set):
            rogue_fragments = found_set - expected_set
            return (f"❌ Tampered: Found {len(rogue_fragments)} unexpected fragment(s).", 0, len(expected_fragments))

        # Check for matches
        matched_fragments = found_set.intersection(expected_set)
        num_matched = len(matched_fragments)
        num_expected = len(expected_set)

        if num_matched == num_expected:
            return (f"✅ Verified", num_matched, num_expected)
        elif num_matched > 0:
            return (f"⚠️ Partial match", num_matched, num_expected)
        else:
            # This case should not be reached due to the initial check, but for safety:
            return ("❌ No signature found", 0, num_expected)