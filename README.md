# 🤖 AI Customer Support Copilot (RAG + FastAPI)

An intelligent AI-powered customer support system that uses Retrieval-Augmented Generation (RAG) to answer queries based on business documents.

## 🚀 Features

- 🔍 Semantic search using FAISS
- 🧠 Context-aware responses using Gemini LLM
- ⚡ FastAPI backend for real-time API responses
- 📄 Handles unstructured documents (TXT/PDF)
- 💬 Conversational memory support
- 📊 Source-based answer grounding (reduces hallucination)

---

## 🏗️ Architecture

User Query → Embedding → FAISS Search → Top-K Docs → LLM → Response

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Vector DB:** FAISS
- **Embeddings:** Sentence Transformers (MiniLM)
- **LLM:** Gemini API
- **Language:** Python

---

## 📦 Installation

```bash
git clone <your-repo>
cd ai-support-copilot
pip install -r requirements.txt