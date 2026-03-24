import faiss
import numpy as np
import os
import pickle
from app.core.config import VECTOR_DB_PATH

index = None
documents_store = []


# ✅ BUILD FAISS INDEX
def build_faiss(embeddings, documents):
    global index, documents_store

    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))
    documents_store = documents

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)

    faiss.write_index(index, os.path.join(VECTOR_DB_PATH, "index.faiss"))

    with open(os.path.join(VECTOR_DB_PATH, "docs.pkl"), "wb") as f:
        pickle.dump(documents_store, f)


# ✅ LOAD FAISS INDEX
def load_faiss():
    global index, documents_store

    index = faiss.read_index(os.path.join(VECTOR_DB_PATH, "index.faiss"))

    with open(os.path.join(VECTOR_DB_PATH, "docs.pkl"), "rb") as f:
        documents_store = pickle.load(f)


# ✅ SEARCH FUNCTION
def search(query_embedding, k=3):
    global index, documents_store

    if index is None:
        raise ValueError("FAISS index not loaded")

    D, I = index.search(np.array([query_embedding]), k)

    results = [
        documents_store[i]
        for i in I[0]
        if i < len(documents_store)
    ]

    return results