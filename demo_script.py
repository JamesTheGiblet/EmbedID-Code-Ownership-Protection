
"""
────────────────────────────────────────────────────────────
🛡️ Authored by James 'The Giblet' Mavric
🔗 EmbedID: JTM-2025-demo_script
📜 License: Builder Sovereignty License v1.0
📅 Timestamp: 2025-08-14T19:49:21.323765+00:00
🔒 SHA256: 6dece4064e15d030cc3e1ece143958159cb5d93c54bbb54479de55288f4d9f66
────────────────────────────────────────────────────────────
"""


"""
────────────────────────────────────────────────────────────
🛡️ Authored by James 'The Giblet' Mavric
🔗 EmbedID: JTM-2025-demo_script
📜 License: Builder Sovereignty License v1.0
📅 Timestamp: 2025-08-14T19:46:35.283374
🔒 SHA256: 60d75775018655916cb88a59ba85a6b74d01c439162eb96bc89231851cb55691
────────────────────────────────────────────────────────────
"""

import os
import string

class TextProcessor:
    def __init__(self, text):
        self.original = text
        self.cleaned = self._clean_text(text)

    def _clean_text(self, text):
        return text.strip().lower().translate(str.maketrans('', '', string.punctuation))

    def word_count(self):
        return len(self.cleaned.split())

    def unique_words(self):
        return set(self.cleaned.split())

    def summary(self):
        return {
            "original": self.original,
            "cleaned": self.cleaned,
            "word_count": self.word_count(),
            "unique_words": list(self.unique_words())
        }

def read_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_summary(summary, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("Text Summary\n")
        f.write("============\n")
        f.write(f"Original: {summary['original']}\n")
        f.write(f"Cleaned: {summary['cleaned']}\n")
        f.write(f"Word Count: {summary['word_count']}\n")
        f.write(f"Unique Words: {', '.join(summary['unique_words'])}\n")

def process_file(input_path, output_path):
    try:
        text = read_file(input_path)
        processor = TextProcessor(text)
        summary = processor.summary()
        write_summary(summary, output_path)
        print(f"✅ Summary written to {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Example usage
    input_file = "sample_input.txt"
    output_file = "summary_output.txt"
    process_file(input_file, output_file)