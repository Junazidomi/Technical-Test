from fastapi import FastAPI
from app.Service.embedding import EmbeddingService
from app.Service.rag import RagWorkflow
from app.Storage.memory import InMemoryDocumentStore
from app.Storage.qdrant import QdrantDocumentStore
from app.api import create_router

app = FastAPI(title="Learning RAG Demo")

embedder = EmbeddingService()

try:
    store = QdrantDocumentStore(
        url="http://localhost:6333",
        collection_name="demo_collection",
        vector_size=128
    )
    qdrant_ready = True
except Exception:
    store = InMemoryDocumentStore()
    qdrant_ready = False

rag = RagWorkflow(store=store, embedder=embedder)
app.include_router(create_router(rag))

@app.get("/")
def root():
    return {"qdrant_ready": qdrant_ready}
