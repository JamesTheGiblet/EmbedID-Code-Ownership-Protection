# 🧭 EmbedID Development Roadmap

This roadmap outlines the phased development of EmbedID:  
A modular protocol for embedding, verifying, and governing code authorship.

Each phase is remixable, overrideable, and designed for sovereign extension.

---

## 🔹 Phase 1: Core Logic

**Goal:**  
Build the foundation—fragmented signatures, hashing, and embedding engine.

**Deliverables:**  

- Fragment generator (code-word + code-phrase)  
- Hashing logic (SHA3, BLAKE3)  
- Embedder interface (comment-based, semantic)  
- Dry-run preview

**Remix Potential:**  

- Custom hash functions  
- Alternate fragment formats  
- Language-specific embedders

---

## 🔹 Phase 2: Multi-Signature & Storage

**Goal:**  
Support multiple authors, encrypted maps, and local verification.

**Deliverables:**  

- Encrypted `.embedid/signature_map.json`  
- Multi-signer support  
- Local verification CLI  
- Signature registry

**Remix Potential:**  

- External key vaults  
- Group signatures  
- Offline verification modes

---

## 🔹 Phase 3: Advanced Embedding

**Goal:**  
Expand embedding strategies beyond comments.

**Deliverables:**  

- Semantic embedding (AST nodes, whitespace)  
- Steganographic embedding (image, audio, binary)  
- Embed preview tool  
- Embed strategy selector

**Remix Potential:**  

- Language-specific AST plugins  
- Obfuscated embed logic  
- Embed-to-QR or embed-to-emoji

---

## 🔹 Phase 4: Governance

**Goal:**  
Introduce manifest logic, revocation, and remix lineage.

**Deliverables:**  

- Manifest schema (`manifest.json`)  
- Revocation CLI  
- Fork tracking  
- Remix lineage explorer

**Remix Potential:**  

- Manifest as smart contract  
- Fork voting or override logic  
- Remix reputation scoring

---

## 🔹 Phase 5: CLI & UX

**Goal:**  
Polish the CLI, improve UX, and add help system.

**Deliverables:**  

- CLI help and examples  
- Passphrase prompt  
- Dry-run diff viewer  
- Config presets

**Remix Potential:**  

- GUI wrapper  
- Voice-activated CLI  
- CLI as Discord bot

---

## 🔹 Phase 6: CI Integration

**Goal:**  
Automate verification via Git hooks and CI workflows.

**Deliverables:**  

- Git pre-commit hook  
- GitHub Actions template  
- GitLab CI and Jenkins support  
- CI verification badge

**Remix Potential:**  

- Custom badge logic  
- CI-triggered revocation  
- CI-based remix scoring

---

## 🔹 Phase 7: Remote API

**Goal:**  
Enable remote verification and public signature registry.

**Deliverables:**  

- FastAPI server  
- Web UI for file upload + verification  
- Remote manifest viewer  
- Client CLI for remote ops

**Remix Potential:**  

- Decentralized registry  
- P2P verification mesh  
- EmbedID as browser extension

---

## 🔹 Phase 8: Testing

**Goal:**  
Ensure robustness via unit, integration, fuzz, and performance tests.

**Deliverables:**  

- Test suite generator  
- Fuzzing logic  
- Performance benchmarks  
- Remix test coverage

**Remix Potential:**  

- Remix-specific test cases  
- Tamper simulation engine  
- Signature stress tests

---

## 🔹 Phase 9: IDE Plugins

**Goal:**  
Integrate EmbedID into developer workflows.

**Deliverables:**  

- VSCode plugin  
- Vim plugin  
- LSP support  
- Embed preview in editor

**Remix Potential:**  

- IDE-based governance  
- Manifest editing UI  
- Signature visualization

---

## 🔹 Phase 10: Documentation & Release

**Goal:**  
Finalize docs, publish packages, and launch product tiers.

**Deliverables:**  

- User guide  
- Developer docs  
- GitHub README  
- Patreon content  
- Website demo + portal

**Remix Potential:**  

- Docs as interactive CLI  
- Remixable tutorials  
- Builder manifest gallery

---

## 🧬 Remix Invitation

Every phase is modular.  
Fork it. Override it. Extend it.  
EmbedID is a protocol, not a prison.
