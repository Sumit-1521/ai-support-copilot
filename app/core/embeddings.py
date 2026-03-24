from sentence_transformers import SentenceTransformer
from functools import lru_cache

# ✅ DEFINE MODEL FIRST (GLOBAL)
model = SentenceTransformer("all-MiniLM-L6-v2")


@lru_cache(maxsize=1000)
def cached_embedding(text):
    return model.encode([text])[0]


def get_embedding(texts):
    return [cached_embedding(t) for t in texts]