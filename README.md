## **Project: EmbedID**

A Simple Tool to Watermark Your Source Code

#### **The Problem**

You write a clever piece of code, post it on a blog or GitHub, and a week later you see it in someone else's project with their name on it. How do you prove you wrote it first? You need a way to sign your work without breaking the code.

-----

#### **The Solution**

A simple Python tool that embeds a hidden or visible signature directly into your source code files. It's a way to watermark your work so you can prove it's yours later. It does this without affecting how the code runs.

-----

#### **What It Does**

  * **Embeds Your Signature:** Takes your signature text and embeds it into a file using one of several methods.
  * **Verifies Your Signature:** Checks a file to see if your signature is present and hasn't been tampered with.
  * **Multiple Methods:** You can choose how you want to embed your signature:
      * **Comments:** Simple, human-readable, but easy to remove.
      * **Invisible Characters:** Sneaky. Uses zero-width spaces to hide your signature where no one can see it.
      * **Vigenère Cipher:** A simple cipher to obfuscate the signature within a comment.
  * **Simple Web UI:** Comes with a basic **Flask** web interface to embed and verify signatures by uploading files.
  * **Test Suite:** Includes a full `pytest` suite to make sure everything works as expected.

-----

#### **How to Install It**

**Prerequisites:**

  * Python 3.10+
  * Flask and Pytest

Run this from the project's directory:

```bash
pip install -r requirements.txt
```

-----

#### **How to Use It**

##### **1. The Web Interface**

This is the easiest way.

```bash
python app.py
```

Now open your browser to `http://127.0.0.1:5000`. You'll see simple forms to upload a file, enter your signature, and either embed it or verify it.

##### **2. As a Python Module**

You can also use it directly in your own scripts.

```python
from ciphers_manager import embed, verify

file_content = "def hello(): print('Hello, world!')"
signature = "JamesTheGiblet-2025"

# Embed the signature
embedded_content = embed("invisible", signature, file_content)

# Verify the signature
is_valid = verify("invisible", signature, embedded_content)
print(f"Signature is valid: {is_valid}")
```

-----

#### **The File Structure**

The project is organized simply:

```
EmbedID/
│── app.py                # The Flask web app
│── ciphers_manager.py    # Main logic for embedding/verifying
│── cipher_methods/       # Each embedding method is its own module
│   │── comment_cipher.py
│   └── invisible_cipher.py
│── static/               # CSS and images for the web app
│── templates/            # HTML files for the web app
│── tests/                # The pytest test suite
└── requirements.txt      # Dependencies
```

-----

#### **The Roadmap**

**Perfect is the imaginary friend of never shipped**, but here's where it could go:

  * Integrate **AES encryption** for a much stronger signature.
  * Add **Git integration** to automatically embed a signature on commit.
  * Support for embedding multiple signatures in one file.
  * A "live preview" in the web UI to see where the signature is being embedded.

-----

#### **How to Contribute**

This is an open project. Feel free to fork it, add a new cipher method, or fix a bug.

1.  Fork the repo.
2.  Create your feature branch.
3.  Submit a pull request.

-----

#### **License**

This project is licensed under the **MIT License**. Use it, share it, improve it.

It’s a straightforward way to stamp your name on your work. **The code is the proof**, and this tool helps you embed that proof directly.
