import faiss
import numpy as np
from models.embeddings import get_embedding

class VectorStore:
    def __init__(self, dim=384):
        self.index = faiss.IndexFlatL2(dim)
        self.text_data = []

    def add_text(self, text: str):
        embedding = get_embedding(text)
        embedding = np.array([embedding]).astype("float32")

        self.index.add(embedding)
        self.text_data.append(text)

    def search(self, query: str, top_k=3):
        query_embedding = get_embedding(query)
        query_embedding = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.text_data):
                results.append(self.text_data[idx])

        return results
