from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

class Retriever:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.vectorstore = FAISS(self.embeddings)

    def retrieve(self, query, k=5):
        return self.vectorstore.similarity_search(query, k=k)