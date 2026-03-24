import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "documents")
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vectorstore")