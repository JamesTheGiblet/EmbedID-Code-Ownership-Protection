# ✅ EmbedID AI Assistance Checklist

Each task below includes a modular prompt for AI generation.  
Tick off tasks as you complete or remix them.

---

## 🔹 Phase 1: Core Logic

- [x] Fragment generator (code-word + code-phrase)  
  🧠 Prompt: "Generate a Python module that creates fragmented code signatures using a code-word and code-phrase."

- [x] Hashing logic (SHA3, BLAKE3)  
  🧠 Prompt: "Implement SHA3 and BLAKE3 hashing for signature fragments."

- [x] Embedder interface (comment-based, semantic)  
  🧠 Prompt: "Embed fragments as comments in source files. Add semantic AST support."

- [x] Dry-run preview  
  🧠 Prompt: "Add a CLI dry-run preview that shows embedded fragments without modifying files."

---

## 🔹 Phase 2: Multi-Signature & Storage

- [x] Encrypted signature map  
  🧠 Prompt: "Design an encrypted `.embedid/signature_map.json` format for multiple authors."

- [x] Multi-signer support  
  🧠 Prompt: "Support multiple signers with unique keys and fragment sets."

- [x] Local verification CLI  
  🧠 Prompt: "Build CLI commands to verify embedded fragments locally."

- [x] Signature registry  
  🧠 Prompt: "Create a local registry of embedded signatures and their metadata."

---

## 🔹 Phase 3: Advanced Embedding

- [ ] Semantic embedding  
  🧠 Prompt: "Use AST nodes and whitespace for signature placement."

- [ ] Steganographic embedding  
  🧠 Prompt: "Embed signatures in images, audio, or binary files using steganography."

- [ ] Embed preview tool  
  🧠 Prompt: "Create a tool to preview embedded fragments in various formats."

- [ ] Strategy selector  
  🧠 Prompt: "Add CLI option to choose embedding strategy."

---

## 🔹 Phase 4: Governance

- [ ] Manifest schema  
  🧠 Prompt: "Define a manifest schema (`manifest.json`) for authorship, remix lineage, and revocation."

- [ ] Revocation CLI  
  🧠 Prompt: "Build CLI tools to revoke signatures and update manifest."

- [ ] Fork tracking  
  🧠 Prompt: "Track forks and remix lineage in the manifest."

- [ ] Remix lineage explorer  
  🧠 Prompt: "Create a module to visualize remix history and contributor chains."

---

## 🔹 Phase 5: CLI & UX

- [ ] CLI help and examples  
  🧠 Prompt: "Add help commands and usage examples to the CLI."

- [ ] Passphrase prompt  
  🧠 Prompt: "Prompt user for passphrase when signing or verifying."

- [ ] Dry-run diff viewer  
  🧠 Prompt: "Show diff between original and embedded file in dry-run mode."

- [ ] Config presets  
  🧠 Prompt: "Allow users to save and load CLI config presets."

---

## 🔹 Phase 6: CI Integration

- [ ] Git pre-commit hook  
  🧠 Prompt: "Build a Git pre-commit hook that runs EmbedID verification."

- [ ] GitHub Actions template  
  🧠 Prompt: "Create a GitHub Actions workflow for EmbedID verification."

- [ ] GitLab CI and Jenkins support  
  🧠 Prompt: "Add CI templates for GitLab and Jenkins."

- [ ] CI verification badge  
  🧠 Prompt: "Generate a badge showing verification status in CI."

---

## 🔹 Phase 7: Remote API

- [ ] FastAPI server  
  🧠 Prompt: "Develop a FastAPI server for remote verification and manifest viewing."

- [ ] Web UI  
  🧠 Prompt: "Create a web interface for file upload and signature inspection."

- [ ] Remote manifest viewer  
  🧠 Prompt: "Build a viewer for remote manifest inspection."

- [ ] Client CLI  
  🧠 Prompt: "Add CLI commands for remote verification and manifest sync."

---

## 🔹 Phase 8: Testing

- [ ] Test suite generator  
  🧠 Prompt: "Generate unit and integration tests for EmbedID modules."

- [ ] Fuzzing logic  
  🧠 Prompt: "Add fuzz testing for signature embedding and verification."

- [ ] Performance benchmarks  
  🧠 Prompt: "Benchmark signature generation and verification speed."

- [ ] Remix test coverage  
  🧠 Prompt: "Test remix scenarios and fork lineage integrity."

---

## 🔹 Phase 9: IDE Plugins

- [ ] VSCode plugin  
  🧠 Prompt: "Create a VSCode extension to preview embedded signatures and edit manifests."

- [ ] Vim plugin  
  🧠 Prompt: "Build a Vim plugin for EmbedID preview and verification."

- [ ] LSP support  
  🧠 Prompt: "Add Language Server Protocol support for EmbedID features."

- [ ] Embed preview in editor  
  🧠 Prompt: "Show embedded fragments inline in the editor."

---

## 🔹 Phase 10: Documentation & Release

- [ ] User guide  
  🧠 Prompt: "Write a user guide for installing and using EmbedID."

- [ ] Developer docs  
  🧠 Prompt: "Document internal modules, CLI commands, and manifest logic."

- [ ] GitHub README  
  🧠 Prompt: "Finalize the README with protocol spec, roadmap, and remix invitation."

- [ ] Patreon content  
  🧠 Prompt: "Draft premium tutorials and roadmap previews for Patreon tiers."

- [ ] Website demo + portal  
  🧠 Prompt: "Design a demo site with file upload, verification UI, and manifest gallery."

---

## 🧬 Sovereign Builder Tasks

- [ ] LICENSE.md  
  🧠 Prompt: "Draft a Sovereign Builder License for remixable code with governance rules."

- [ ] setup_embedid.py  
  🧠 Prompt: "Create a script to scaffold the full EmbedID workspace."

- [ ] manifest.json template  
  🧠 Prompt: "Generate a sample manifest with fields for authorship, remix lineage, and revocation."

- [ ] GitHub Pages README  
  🧠 Prompt: "Format README for GitHub Pages with collapsible sections and remix logic."

- [ ] Patreon tiers  
  🧠 Prompt: "Define tiered access model for EmbedID features and content."

- [ ] Demo site  
  🧠 Prompt: "Build a demo site with verification tools and builder manifest explorer."
