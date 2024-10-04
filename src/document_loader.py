import os
from PyPDF2 import PdfReader

class DocumentLoader:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir

    def load_documents(self):
        documents = []
        for filename in os.listdir(self.data_dir):
            filepath = os.path.join(self.data_dir, filename)
            if filename.endswith(".txt"):
                with open(filepath, 'r', encoding='utf-8') as file:
                    documents.append(file.read())
            elif filename.endswith(".pdf"):
                documents.append(self._load_pdf(filepath))
        return documents

    def _load_pdf(self, filepath):
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

if __name__ == "__main__":
    loader = DocumentLoader()
    docs = loader.load_documents()
    for doc in docs:
        print(f"Documento carregado com {len(doc)} caracteres")