import os
import pathspec
from typing import List

def _get_gitignore_spec() -> pathspec.PathSpec:
    """
    Loads patterns from .gitignore in the current directory and adds defaults.
    """
    patterns = []
    gitignore_path = os.path.join(os.getcwd(), '.gitignore')
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            patterns.extend(f.readlines())
    
    # Add default patterns that should always be ignored
    default_ignores = ['.git/', '.embedid/']
    patterns.extend(default_ignores)
    
    return pathspec.PathSpec.from_lines('gitwildmatch', patterns)

def discover_files(target_paths: List[str]) -> List[str]:
    """
    Recursively finds all files in the given paths, respecting .gitignore.
    """
    spec = _get_gitignore_spec()
    found_files = set()
    
    for path in target_paths:
        abs_path = os.path.abspath(path)
        if not os.path.exists(abs_path):
            print(f"Warning: Path not found, skipping: {path}")
            continue
            
        if os.path.isfile(abs_path):
            if not spec.match_file(abs_path):
                found_files.add(abs_path)
        elif os.path.isdir(abs_path):
            for root, dirs, files in os.walk(abs_path, topdown=True):
                dirs[:] = [d for d in dirs if not spec.match_file(os.path.join(root, d))]
                for file in files:
                    file_path = os.path.join(root, file)
                    if not spec.match_file(file_path):
                        found_files.add(file_path)
                        
    return sorted(list(found_files))