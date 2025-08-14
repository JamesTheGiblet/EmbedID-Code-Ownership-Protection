import os
import random
from typing import Dict, List, Optional, Tuple, Union

class CommentEmbedder:
    """
    Embeds signature fragments into source code files as comments.

    This implementation supports multiple common programming languages and
    preserves indentation. It operates in both a "write" mode and a "dry-run"
    mode for previewing changes.
    """
    COMMENT_STYLES: Dict[str, str] = {
        '.py': '#', '.rb': '#', '.sh': '#', '.pl': '#',
        '.js': '//', '.ts': '//', '.java': '//', '.c': '//', '.cpp': '//',
        '.h': '//', '.hpp': '//', '.go': '//', '.rs': '//', '.swift': '//',
    }
    EMBED_ID_PREFIX = ""

    def get_comment_style(self, file_path: str) -> Optional[str]:
        """Gets the comment syntax for a given file extension."""
        _, ext = os.path.splitext(file_path)
        return self.COMMENT_STYLES.get(ext.lower())

    def embed(self, file_path: str, fragments: List[str], dry_run: bool = False) -> Union[Optional[Tuple[str, str]], bool]:
        """
        Embeds fragments into a file.

        In dry-run mode, it returns the original and modified content as strings.
        Otherwise, it modifies the file in-place and returns None.

        Args:
            file_path (str): The path to the file to modify.
            fragments (List[str]): The list of signature fragments to embed.
            dry_run (bool): If True, no changes are written to disk.

        Returns:
            - A tuple of (original, modified) content in dry-run mode on success, else None.
            - A boolean indicating success or failure in write mode.
        """
        comment_style = self.get_comment_style(file_path)
        if not comment_style:
            print(f"Warning: Unsupported file type for embedding: {file_path}")
            return None if dry_run else False

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return None if dry_run else False

        if any(self.EMBED_ID_PREFIX in line for line in lines):
            print(f"Info: Signature fragments already found in {file_path}. Skipping.")
            return None if dry_run else False

        valid_indices = [i for i, line in enumerate(lines) if line.strip()]
        if len(valid_indices) < len(fragments):
            print(f"Warning: Not enough non-empty lines in {file_path} to embed all fragments. Skipping.")
            return None if dry_run else False

        insertion_indices = sorted(random.sample(valid_indices, len(fragments)))

        new_lines = lines[:]
        offset = 0
        for i, fragment in zip(insertion_indices, fragments):
            original_line = lines[i]
            indent = len(original_line) - len(original_line.lstrip(' '))
            comment = f"{'' * indent}{comment_style} {self.EMBED_ID_PREFIX} {fragment}\n"
            new_lines.insert(i + offset, comment)
            offset += 1

        original_content = "".join(lines)
        modified_content = "".join(new_lines)

        if dry_run:
            return original_content, modified_content
        else:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                print(f"Success: Embedded signature in {file_path}")
                return True
            except Exception as e:
                print(f"Error writing to file {file_path}: {e}")
            return False