import re
import os

class Verifier:
    """
    Verifies the presence and correctness of signature fragments.
    """
    def extract_fragments(self, file_path: str, template: str, fragment_len: int = 8) -> list[str]:
        """
        Extracts fragments by finding an anchor comment and decoding the
        trailing whitespace on the subsequent lines.
        """
        found_fragments = []
        comment_char = '#' # Assuming Python-style comments
        anchor_text = f"{comment_char} {template}".strip()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except (IOError, UnicodeDecodeError):
            return []

        for i, line in enumerate(lines):
            if line.strip() == anchor_text:
                # Found a potential anchor
                anchor_index = i
                
                # Check if there are enough subsequent lines to hold a fragment
                if anchor_index + 1 + fragment_len > len(lines):
                    continue # Not enough lines after this anchor

                current_fragment_chars = []
                possible = True
                for j in range(fragment_len):
                    data_line = lines[anchor_index + 1 + j]
                    # Count trailing spaces
                    num_spaces = len(data_line) - len(data_line.rstrip(' '))
                    
                    if num_spaces > 0:
                        # Convert space count back to hex value
                        hex_value = num_spaces - 1
                        current_fragment_chars.append(f'{hex_value:x}')
                    else:
                        # Line has no trailing spaces, this can't be a valid fragment block
                        possible = False
                        break
                
                if possible and len(current_fragment_chars) == fragment_len:
                    found_fragments.append("".join(current_fragment_chars))

        return found_fragments

    def verify_fragments(self, found_fragments: list[str], expected_fragments: list[str]) -> tuple[str, int, int]:
        """
        Compares a list of found fragments against a list of expected fragments.
        """
        found_set = set(found_fragments)
        expected_set = set(expected_fragments)
        
        matched_fragments = found_set.intersection(expected_set)
        
        matched_count = len(matched_fragments)
        expected_count = len(expected_set)

        if matched_count == 0:
            return "❌ Not Verified", 0, expected_count
        elif matched_count == expected_count:
            return "✅ Verified", matched_count, expected_count
        else:
            return "⚠️ Partially Verified", matched_count, expected_count
