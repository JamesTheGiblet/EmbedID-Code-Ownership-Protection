# What is EmbedID?

EmbedID is a **Modular Code Signature Protocol** that allows you to embed, verify, and trace sovereign identity within your codebases. It achieves this by embedding jumbled signatures across files to verify authorship, detect tampering, and trace remix lineage.

-----

## Step 1: Add a Signer

Before you can embed a signature, you must register a **signer** in the encrypted signature map. This command stores a `code-word` and `code-phrase` under a unique alias, which are used to generate the signature fragments.

**Example:**

```bash
python embedid.py signer add --alias giblet --code-word some_code --code-phrase some_phrase
```

After you enter a master password, you will see a success message: `✅ Signer 'giblet' added to the signature map.`.

You can list all registered signers using `python embedid.py signer list`.

-----

### Step 2: Embed Signatures

Once a signer is registered, you can embed its signature fragments into your source code files. The tool uses a `CommentEmbedder` to insert the fragments as comments in supported file types.

**Example:**

```bash
python embedid.py embed ./cli/ --signer giblet
```

After entering your master password, the tool will generate signature fragments and scan the specified path. It will either report success for each file it modifies or inform you that fragments are already present, in which case it will skip the file.

-----

### Step 3: Verify Signatures

This is the core of the protocol. The `verify` command scans files for embedded signature fragments and compares them against the generated fragments of all registered signers. This allows you to confirm the integrity and authorship of the code.

**Example:**

```bash
python embedid.py verify ./cli/
```

The output shows the verification results for each signer found in your signature map. The `Status: ✅ Verified` message indicates that all fragments found in the files match the expected fragments for a given signer, confirming the signature's integrity.

-----

### Step 4: View the Registry

The `registry view` command allows you to view an audit trail of all successful signature embedding events. This log includes the timestamp, file path, signer alias, and other metadata for each embedding.

**Example:**

```bash
python embedid.py registry view
```

This command provides a detailed log of when and by whom each signature was embedded.
