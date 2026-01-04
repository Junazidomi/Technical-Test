from typing import List
from .base import DocumentStore

class InMemoryDocumentStore(DocumentStore):
    def __init__(self):
        self._documents: List[str] = []

    def add(self, text: str, embedding: List[float]) -> int:
        doc_id = len(self._documents)
        self._documents.append(text)
        return doc_id

    def search(self, embedding: List[float], limit: int = 2) -> List[str]:
        # fallback behavior sama seperti kode awal
        return self._documents[:limit] if self._documents else []

    def count(self) -> int:
        return len(self._documents)
