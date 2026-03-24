from fastapi import FastAPI
from app.routes.query import router

app = FastAPI(title="AI Customer Support Copilot")


@app.get("/")
def home():
    return {"message": "AI Customer Support Copilot is running 🚀"}


<<<<<<< HEAD
app.include_router(router)
=======
app.include_router(router)
>>>>>>> e0209a8 (Removed large files and fixed repo size)
