# from langchain_community.embeddings import HuggingFaceEmbeddings 
from langchain_huggingface import HuggingFaceEmbeddings # type: ignore


def get_embedding_model():
    """
    Local embedding model
    """
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
