from typing import List
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from .base import DocumentStore

class QdrantDocumentStore(DocumentStore):
    def __init__(self, url: str, collection_name: str, vector_size: int):
        self._collection = collection_name
        self._client = QdrantClient(url)

        self._client.recreate_collection(
            collection_name=self._collection,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )
        self._counter = 0

    def add(self, text: str, embedding: List[float]) -> int:
        doc_id = self._counter
        self._counter += 1

        self._client.upsert(
            collection_name=self._collection,
            points=[
                PointStruct(
                    id=doc_id,
                    vector=embedding,
                    payload={"text": text}
                )
            ]
        )
        return doc_id

    def search(self, embedding: List[float], limit: int = 2) -> List[str]:
        hits = self._client.search(
            collection_name=self._collection,
            query_vector=embedding,
            limit=limit
        )
        return [hit.payload["text"] for hit in hits]

    def count(self) -> int:
        return self._counter
