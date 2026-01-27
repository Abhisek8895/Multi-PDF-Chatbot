import os
import shutil
import asyncio
import streamlit as st

# ---- Fix Streamlit async loop issue ----
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# ---- Project imports ----
from config.config import DB_PATH
from loaders.pdf_loader import load_multiple_pdfs
from processing.text_splitter import split_documents
from vectorstore.faiss_db import create_faiss_db, load_faiss_db
from retriever.generator import generate_answer

# ---- Streamlit UI ----
st.set_page_config(page_title="📚 Multi PDF Chatbot", page_icon="🤖")
st.title("📚 Multi PDF Chatbot")

# ---- App constants ----
MAX_CONTEXT_CHARS = 3000

# ---- File uploader ----
uploaded_files = st.file_uploader(
    "Upload one or more PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# ---- Handle PDF upload & FAISS creation ----
if uploaded_files:
    # Always reset FAISS and session on new upload
    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH)

    st.session_state.clear()

    with st.spinner("Processing PDFs..."):
        # 1️⃣ Load PDFs
        documents = load_multiple_pdfs(uploaded_files)

        # 2️⃣ Split into chunks
        chunks = split_documents(documents)

        # 3️⃣ Create & save FAISS
        create_faiss_db(chunks, DB_PATH)

        # 4️⃣ Store session state
        st.session_state["vectorstore_ready"] = True
        st.session_state["chunk_count"] = len(chunks)

    st.success(f"Indexed {len(chunks)} chunks from uploaded PDFs")

# ---- Ask question ----
query = st.text_input("Ask a question based on the uploaded PDFs")

if query:
    if "vectorstore_ready" not in st.session_state:
        st.warning("Please upload PDFs first.")
    else:
        with st.spinner("Thinking..."):
            vectorstore = load_faiss_db(DB_PATH)

            if vectorstore is None:
                st.error("Vector database not found. Please upload PDFs again.")
            else:
                answer = generate_answer(
                    query=query,
                    max_context_chars=MAX_CONTEXT_CHARS
                )

                st.markdown("### 🤖 Answer")
                st.write(answer)

# ---- Debug info ----
if "chunk_count" in st.session_state:
    st.caption(f"🔍 Indexed chunks: {st.session_state['chunk_count']}")
