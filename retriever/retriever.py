from vectorstore.faiss_db import load_faiss_db
from config.config import DB_PATH

#  Load FAISS vector store
_vectorstore = load_faiss_db()


def retrieve_documents(query: str, top_k: int = 3):
    """
    Takes a user query and returns relevant document chunks from FAISS
    """

    if not query or not isinstance(query, str):
        return []

    # 4. Perform similarity search
    retrieved_docs = _vectorstore.similarity_search(
        query=query,
        k=top_k
    )

    return retrieved_docs
