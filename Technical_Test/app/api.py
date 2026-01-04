import time
from fastapi import APIRouter, HTTPException
from app.model import QuestionRequest, DocumentRequest
from app.Service.rag import RagWorkflow

def create_router(rag: RagWorkflow):
    router = APIRouter()

    @router.post("/ask")
    def ask(req: QuestionRequest):
        start = time.time()
        try:
            result = rag.ask(req.question)
            return {
                "question": req.question,
                "answer": result["answer"],
                "context_used": result.get("context", []),
                "latency_sec": round(time.time() - start, 3)
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.post("/add")
    def add(req: DocumentRequest):
        try:
            doc_id = rag.add_document(req.text)
            return {"id": doc_id, "status": "added"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.get("/status")
    def status():
        return rag.status()

    return router
