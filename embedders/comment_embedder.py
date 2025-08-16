import os
import random
import sys

from core.verifier import Verifier
class CommentEmbedder:
    """
    Embeds signature fragments into files using whitespace steganography.
    """

    def embed(self, file_path: str, fragments: list[str], template: str, dry_run: bool = False) -> bool | tuple[str, str]:
        """
        Embeds a signature fragment by appending trailing whitespace to lines
        following a hidden anchor comment.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                original_content = "".join(lines)
        except (IOError, UnicodeDecodeError) as e:
            print(f"Warning: Could not read {file_path}, skipping. Reason: {e}")
            return False

        # Check if a signature already exists to prevent re-embedding.
        verifier = Verifier()
        if verifier.extract_fragments(file_path, template):
            print(f"Info: Signature fragments already found in {file_path}. Skipping.")
            return False

        fragment_to_embed = random.choice(fragments)
        fragment_len = len(fragment_to_embed)
        comment_char = '#' # Assuming Python-style comments

        # Find a location to insert the anchor and the following data block.
        # The block needs to be long enough for the anchor + fragment.
        block_size = fragment_len + 1
        candidate_indices = [i for i, line in enumerate(lines) if not line.strip()]

        if not candidate_indices:
            print(f"Warning: Could not find a suitable place to embed in {file_path}. Skipping.")
            return False

        insertion_index = random.choice(candidate_indices)

        # Create a block with an anchor and space for the data lines
        anchor_comment = f"{comment_char} {template}\n"
        # We will modify the lines *after* the insertion point.
        modified_lines = lines[:]
        modified_lines.insert(insertion_index, anchor_comment)

        # Ensure there are enough lines after the anchor
        if insertion_index + fragment_len >= len(modified_lines):
            # Not enough lines, append blank lines to make space
            needed = (insertion_index + fragment_len + 1) - len(modified_lines)
            modified_lines.extend(['\n'] * needed)

        # Encode each character as trailing whitespace on the lines following the anchor
        for i, char in enumerate(fragment_to_embed):
            # Number of spaces = hex value + 1 (so '0' is 1 space)
            num_spaces = int(char, 16) + 1
            line_index = insertion_index + 1 + i
            modified_lines[line_index] = modified_lines[line_index].rstrip() + (' ' * num_spaces) + '\n'

        modified_content = "".join(modified_lines)

        if dry_run:
            return original_content, modified_content

        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            return True
        except IOError as e:
            print(f"Error: Could not write to {file_path}. Reason: {e}")
            return False
