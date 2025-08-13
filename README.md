# 🧬 `README.md`

```markdown
# 🧬 EmbedID

**Modular Code Signature Protocol**  
Embed, Verify, and Trace Sovereign Identity Across Codebases

---

## 🔹 What Is EmbedID?

EmbedID is a tamper-resistant, remixable identity protocol for codebases.  
It lets you embed jumbled signatures across your files—then verify authorship, detect tampering, trace remix lineage, and enforce remix governance.

Built for sovereign builders, remixers, and digital mavericks.

---

## 📦 Project Setup

To initialize the EmbedID project structure:

```bash
python setup_embedid.py
```

This creates all necessary directories, stub files, and a sample `.embedid/` workspace.

---

## 🧰 Directory Overview

```plaintext
embedid/
├── cli/                 # CLI commands and interface
├── core/                # Signature logic, crypto, verification
├── embedders/           # Embedding strategies (comments, semantic, etc.)
├── governance/          # Manifest, revocation, fork tracking
├── integrations/        # Git hooks, CI workflows
├── server/              # Remote verification API and web UI
├── client/              # Remote verification client
├── tests/               # Unit, integration, performance tests
├── tools/               # Test suite generator and utilities
├── .embedid/            # Signature map, manifest, logs
├── plugins/             # IDE integrations (VSCode, vim, LSP)
├── templates/ci/        # CI templates (GitHub, GitLab, Jenkins)
├── README.md            # Protocol spec and roadmap
├── embedid.py           # CLI entry point
```

---

## 🧪 Quickstart Commands

```bash
python embedid.py embed --code-word txGq --code-phrase flux --dry-run
python embedid.py verify --diff
python embedid.py revoke --manifest .embedid/manifest.json
python embedid.py hook --install --type pre-commit
```

---

## 🚨 Tamper Detection Outcomes

| Condition               | Result            |
|------------------------|-------------------|
| All fragments present   | ✅ Verified        |
| Some fragments missing  | ⚠️ Partial match   |
| Hash mismatch           | ❌ Tampered        |
| Decoys only             | ❌ No signature    |
| Manifest mismatch       | ⚠️ Remix drift     |
| Manifest revoked        | ❌ Revoked         |
| Fork without override   | ⚠️ Unverified fork |

---

## 🧭 Implementation Roadmap

EmbedID is being built in 10 modular phases:

1. **Core Logic** — Signature fragments, hashing, embedding engine  
2. **Multi-Signature & Storage** — Encrypted maps, registry, verification  
3. **Advanced Embedding** — Semantic, whitespace, steganographic methods  
4. **Governance** — Manifest schema, revocation, fork tracking  
5. **CLI & UX** — Dry-run, passphrase prompt, help system  
6. **CI Integration** — Git hooks, GitHub Actions, workflow automation  
7. **Remote API** — FastAPI server, web UI, client tools  
8. **Testing** — Unit, integration, fuzz, performance  
9. **IDE Plugins** — VSCode, vim, LSP  
10. **Documentation & Release** — User guide, dev docs, packaging

See [`docs/dev/roadmap.md`](docs/dev/roadmap.md) for full breakdown.

---

## 💰 Product Strategy

EmbedID will launch as a three-tiered offering:

### 🔹 GitHub (Free Tier)

- EmbedID CLI scaffold  
- README and protocol spec  
- Sample `.embedid/` workspace  
- Remix invitation

### 🔹 Patreon (Premium Tier)

- Full roadmap implementation  
- Setup scripts and automation tools  
- Technical documentation and tutorials  
- Early access to new features

### 🔹 EmbedID Website

- Live demo showcase  
- File upload + verification UI  
- Subscription portal  
- Builder manifest gallery  
- Remix lineage explorer

---

## 💳 Monetization Model

- **Subscription** — Monthly/yearly access to premium features  
- **Pay-per-file** — Metered verification or embed operations  
- **One-time license** — Annual offline CLI + governance tools

---

## 🧾 Licensing

- **Protocol Spec** — Open and remixable  
- **CLI Core** — MIT or Sovereign Builder License  
- **Premium Modules** — Commercial license  
- **Manifests** — Builder-owned, remixable under terms

---

## 🧬 Remix Invitation

EmbedID is modular. Fork it, remix it, override it.  
Build your own embed logic, verification flow, or ledger backend.

Every signature is a sovereign badge.  
Every fragment is proof of authorship.  
Every manifest is an invitation to remix with respect.  
Every revocation is a boundary worth honoring.
