import time
from app.utils.loader import load_documents
from app.utils.chunking import chunk_text
from app.core.embeddings import get_embedding
from app.services.retriever import build_faiss, load_faiss, search
from app.services.llm import generate_answer
from app.core.config import DATA_PATH

# ✅ cache
cache = {}

# ✅ memory
conversation_history = []

# ✅ lazy init flag
is_initialized = False


def initialize_pipeline():
    print("🔄 Initializing pipeline...")

    documents = load_documents(DATA_PATH)

    chunks = []
    for doc in documents:
        chunks.extend(chunk_text(doc))

    embeddings = get_embedding(chunks)

    build_faiss(embeddings, chunks)

    print("✅ FAISS index built")


def query_pipeline(query):
    global conversation_history, is_initialized

    start_time = time.time()

    # ✅ LAZY INITIALIZATION (CRITICAL FIX)
    if not is_initialized:
        print("⚡ First-time setup...")
        try:
            load_faiss()
        except:
            initialize_pipeline()
        is_initialized = True

    # ✅ Cache check
    if query in cache:
        print("⚡ Cache hit")
        return cache[query]

    print(f"🔍 Query: {query}")

    try:
        query_embedding = get_embedding([query])[0]

        docs = search(query_embedding, k=3)

        history_text = "\n".join(conversation_history[-4:])
        combined_context = docs + [history_text]

        answer = generate_answer(query, combined_context)

        conversation_history.append(f"Q: {query}")
        conversation_history.append(f"A: {answer}")

        result = {
            "question": query,
            "answer": answer,
            "sources": docs,
            "num_sources": len(docs)
        }

        cache[query] = result

        print(f"⏱️ Time: {time.time() - start_time:.2f}s")

        return result

    except Exception as e:
        print(f"❌ Error: {str(e)}")

        return {
            "question": query,
            "answer": "Something went wrong",
            "sources": [],
            "num_sources": 0
        }