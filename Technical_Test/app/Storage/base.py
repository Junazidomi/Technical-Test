from abc import ABC, abstractmethod
from typing import List

class DocumentStore(ABC):

    @abstractmethod
    def add(self, text: str, embedding: List[float]) -> int:
        pass

    @abstractmethod
    def search(self, embedding: List[float], limit: int = 2) -> List[str]:
        pass

    @abstractmethod
    def count(self) -> int:
        pass
