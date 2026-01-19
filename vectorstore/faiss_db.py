import os
from langchain_community.vectorstores import FAISS # type: ignore
from embeddings.embedding_model import get_embedding_model


def create_faiss_db(chunks, db_path="vectorstore/faiss_index"):
    """
    Create and save FAISS vector database
    """
    embeddings = get_embedding_model()
    vector_db = FAISS.from_documents(chunks, embeddings)
    vector_db.save_local(db_path)
    return vector_db


def load_faiss_db(db_path="vectorstore/faiss_index"):
    """
    Load existing FAISS vector database
    """
    embeddings = get_embedding_model()
    return FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
