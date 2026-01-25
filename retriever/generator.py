import google.generativeai as genai # type: ignore

from retriever.retriever import retrieve_documents
from retriever.context_builder import build_context
from config.config import LLM_MODEL, GEMINI_API_KEY


# Configure Gemini once
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(LLM_MODEL)


def generate_answer(query: str, top_k: int = 3, max_context_chars: int = 3000) -> str:
    """
    Retrieve relevant documents, build context, and generate answer using Gemini
    """

    if not query or not isinstance(query, str):
        return "Please provide a valid query."

    # 1️⃣ Retrieve documents
    docs = retrieve_documents(query, top_k=top_k)

    # 2️⃣ Build context
    context = build_context(docs, max_chars=max_context_chars)

    if not context:
        return "No relevant information found in the documents."

    # 3️⃣ Prompt
    prompt = f"""
You are a helpful assistant.

Using ONLY the information from the context below,
write a clear, detailed, and well-explained answer to the question.

- Explain the concept in simple terms
- Use multiple sentences
- If the answer is not found in the context, say "I don't know"

Context:
{context}

Question:
{query}

Answer:
"""

    # 4️⃣ Call Gemini
    response = model.generate_content(prompt)

    return response.text.strip()
