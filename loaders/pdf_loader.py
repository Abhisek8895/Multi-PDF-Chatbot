from langchain_community.document_loaders import PyPDFLoader # type: ignore
import os
import tempfile


def load_multiple_pdfs(uploaded_files):
    documents = []

    for uploaded_file in uploaded_files:
        # Create a temporary file for each uploaded PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        # Load PDF using PyPDFLoader
        loader = PyPDFLoader(tmp_file_path)
        pdf_docs = loader.load()

        for doc in pdf_docs:
            doc.metadata["source"] = uploaded_file.name
            documents.append(doc)

        # Clean up temp file
        os.remove(tmp_file_path)

    return documents
