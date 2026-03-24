from fastapi import FastAPI
from app.routes.query import router
from app.services.rag_pipeline import initialize_pipeline
from app.services.retriever import load_faiss
import os

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 10000))

    uvicorn.run("app.main:app", host="0.0.0.0", port=port)

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


app.include_router(router)
