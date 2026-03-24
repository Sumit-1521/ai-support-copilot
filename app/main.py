from fastapi import FastAPI
from app.routes.query import router

app = FastAPI(title="AI Customer Support Copilot")


@app.get("/")
def home():
    return {"message": "AI Customer Support Copilot is running 🚀"}


app.include_router(router)