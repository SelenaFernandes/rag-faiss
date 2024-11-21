import faiss
import numpy as np

class DocumentStore:
    def __init__(self, embedding_dim=384):
        self.index = faiss.IndexFlatL2(embedding_dim)

    def add_embeddings(self, embeddings):
        self.index.add(np.array(embeddings))

    def search_similar(self, query_embedding, top_k=5):
        D, I = self.index.search(np.array([query_embedding]), top_k)
        return I 

if __name__ == "__main__":
    store = DocumentStore()
    