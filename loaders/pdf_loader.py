from langchain_community.document_loaders import PyPDFLoader # type: ignore
import os


def load_multiple_pdfs(pdf_dir: str):
    documents = []

    for file_name in os.listdir(pdf_dir):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(pdf_dir, file_name)
            loader = PyPDFLoader(file_path)
            pdf_docs = loader.load()

            for doc in pdf_docs:
                doc.metadata["source"] = file_name
                documents.append(doc)

    return documents