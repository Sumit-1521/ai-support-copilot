from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_pipeline import query_pipeline

router = APIRouter()

class QueryRequest(BaseModel):
    question: str


@router.post("/query")
def query_rag(request: QueryRequest):
    return query_pipeline(request.question)