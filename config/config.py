import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "models/gemini-flash-latest"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

DB_PATH = "vectorstore/faiss_index"