from langgraph.graph import StateGraph, END
from typing import Dict
from app.Service.embedding import EmbeddingService
from app.Storage.base import DocumentStore

class RagWorkflow:
    def __init__(self, store: DocumentStore, embedder: EmbeddingService):
        self._store = store
        self._embedder = embedder
        self._chain = self._build_graph()

    def _build_graph(self):
        def retrieve(state: Dict):
            embedding = self._embedder.embed(state["question"])
            state["context"] = self._store.search(embedding)
            return state

        def answer(state: Dict):
            context = state.get("context", [])
            if context:
                state["answer"] = f"I found this: '{context[0][:100]}...'"
            else:
                state["answer"] = "Sorry, I don't know."
            return state

        graph = StateGraph(dict)
        graph.add_node("retrieve", retrieve)
        graph.add_node("answer", answer)
        graph.set_entry_point("retrieve")
        graph.add_edge("retrieve", "answer")
        graph.add_edge("answer", END)
        return graph.compile()

    def ask(self, question: str) -> Dict:
        return self._chain.invoke({"question": question})

    def add_document(self, text: str) -> int:
        embedding = self._embedder.embed(text)
        return self._store.add(text, embedding)

    def status(self) -> Dict:
        return {
            "documents_count": self._store.count(),
            "graph_ready": self._chain is not None
        }
