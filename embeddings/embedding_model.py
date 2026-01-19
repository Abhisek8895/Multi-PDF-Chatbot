from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config.config import GEMENI_API_KEY, EMBEDDING_MODEL


def get_embedding_model():
    """
    Returns Gemini embedding model
    """
    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GEMENI_API_KEY
    )
