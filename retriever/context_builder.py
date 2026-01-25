from typing import List
from langchain_core.documents import Document


def build_context(
    docs: List[Document],
    max_chars: int = 3000
) -> str:
    """
    Build context string from retrieved documents.
    Limits total characters to avoid prompt overflow.
    """

    if not docs:
        return ""

    context_chunks = []
    current_length = 0

    for doc in docs:
        text = doc.page_content.strip()
        if not text:
            continue

        if current_length + len(text) > max_chars:
            break

        context_chunks.append(text)
        current_length += len(text)

    return "\n\n".join(context_chunks)
