import os
from dotenv import load_dotenv

load_dotenv()

GEMENI_API_KEY = os.getenv("GEMINI_API_KEY")

EMBEDDING_MODEL = "models/embedding-001"
LLM_MODEL = "gemini-1.5-flash"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
