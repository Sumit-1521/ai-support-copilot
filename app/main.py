from fastapi import FastAPI
from app.routes.query import router
from app.services.rag_pipeline import initialize_pipeline
from app.services.retriever import load_faiss

app = FastAPI(title="AI Customer Support Copilot")


@app.on_event("startup")
def startup():
    try:
        load_faiss()
    except:
        initialize_pipeline()


@app.get("/")
def home():
    return {"message": "AI Customer Support Copilot is running 🚀"}


<<<<<<< HEAD
app.include_router(router)
=======
app.include_router(router)
>>>>>>> e0209a8 (Removed large files and fixed repo size)
