<div align="center">

# 🧠 Local-Brain-Search

### *Your personal second brain, powered by Local RAG.*

[![Python CI](https://github.com/USER_REPLACE/local-brain-search/actions/workflows/python-ci.yml/badge.svg)](https://github.com/USER_REPLACE/local-brain-search/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Community](https://img.shields.io/badge/Community-Standards-blue.svg)](./CONTRIBUTING.md)

**Local-Brain-Search** is a "God-Tier" Python utility that indexes your local folders (Markdown, PDF, TXT) and allows you to perform natural language queries against your personal notes—**100% offline.**

[Setup Instructions](#-setup) • [Features](#-features) • [Contributing](#-contributing)

---

</div>

## ✨ Features

- 🏎️ **Ultra-Fast Indexing**: Scans and embeds thousands of chunks in seconds.
- 🔒 **Privacy First**: No data ever leaves your machine. Everything is stored in a local `ChromaDB`.
- 📚 **Multi-Format**: Seamlessly handles `.md`, `.txt`, and `.pdf`.
- 🔗 **Smart Citations**: Every answer comes with a direct link (absolute path) to the local source file.
- 🎨 **Beautiful CLI**: Interactive and colorful terminal interface using `Rich`.

---

## 🚀 Setup

### 1. Clone & Install
```bash
git clone https://github.com/your-username/local-brain-search.git
cd local-brain-search
pip install -r requirements.txt
```

### 2. Index Your Brain
Point it at your notes folder:
```bash
python src/main.py index "C:/Users/You/Documents/Notes"
```

### 3. Search Anything
```bash
python src/main.py search "When did I meet with the external project lead?"
```

---

## 🛠️ Architecture

Local-Brain-Search uses industry-standard RAG patterns:
1. **Document Loading**: `LangChain` loaders for Markdown and PDF.
2. **Text Splitting**: `RecursiveCharacterTextSplitter` to maintain context.
3. **Embeddings**: HuggingFace `all-MiniLM-L6-v2` (high performance, low memory).
4. **Vector Store**: `ChromaDB` for persistent, serverless vector storage.

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](./CONTRIBUTING.md) and [Security Policy](./SECURITY.md).

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

⭐ If this project helps you, please give it a star!
