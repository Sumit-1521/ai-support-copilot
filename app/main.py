from fastapi import FastAPI
from app.routes.query import router
from app.services.rag_pipeline import initialize_pipeline
from app.services.retriever import load_faiss
git add .
git commit -m "Fix Render port binding"
git push
app = FastAPI(title="AI Customer Support Copilot")


@app.on_event("startup")
def startup():
    try:
        load_faiss()
    except:
        initialize_pipeline()


app.include_router(router)
