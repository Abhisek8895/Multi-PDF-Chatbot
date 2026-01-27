from vectorstore.faiss_db import load_faiss_db


def retrieve_documents(query: str, top_k: int = 3):
    """
    Takes a user query and returns relevant document chunks from FAISS
    """

    if not query or not isinstance(query, str):
        return []

    # Load FAISS at runtime (NOT at import time)
    vectorstore = load_faiss_db()

    if vectorstore is None:
        return []

    retrieved_docs = vectorstore.similarity_search(
        query=query,
        k=top_k
    )

    return retrieved_docs
