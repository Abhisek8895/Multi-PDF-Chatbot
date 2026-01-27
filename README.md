# Multi-PDF Chatbot

A conversational AI system that allows users to upload **multiple PDFs** and ask questions about their content. The system leverages **document embeddings**, **FAISS vector store**, and **Generative AI** for accurate, context-aware responses.

---

## Features

* Upload **one or more PDF documents**.
* Automatically split PDFs into **text chunks** for better retrieval.
* Generate **vector embeddings** for text chunks using a custom embedding model.
* Store embeddings in a **FAISS vector database** for fast retrieval.
* Ask questions and get **context-aware answers** from your uploaded documents.
* Easily extendable to **new documents** without retraining the model.

---

## Folder Structure

```
Multi-PDF-Chatbot/
│
├─ app.py                       # Main Streamlit app for the chatbot
├─ requirements.txt             # Python dependencies
├─ config/
│   └─ config.py                # Configuration variables (paths, models, etc.)
├─ data/                        # Folder where PDFs are stored
├─ embeddings/
│   └─ embedding_model.py       # Custom embedding model
├─ loaders/
│   └─ pdf_loader.py            # PDF loading logic
├─ processing/
│   └─ text_splitter.py         # Split PDF text into chunks
├─ retrieve/
│   ├─ context_builder.py       # Build context for queries
│   ├─ generator.py             # Generate answers using LLM
│   └─ retriever.py             # Retrieve relevant chunks from FAISS
└─ vectorstore/
    └─ faiss_db.py              # Create or load FAISS database
```

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/Multi-PDF-Chatbot.git
cd Multi-PDF-Chatbot
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv myvenv
myvenv\Scripts\activate       # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Configuration

Update the `config/config.py` file with your paths and model names:

```python
DATA_FOLDER = "data/"
FAISS_PATH = "vectorstore/faiss_index"
EMBEDDING_MODEL = "embeddings/embedding_model.py"
MAX_CONTEXT_CHARS = 1500  # Maximum characters per retrieved context
```

---

## Usage (Streamlit)

1. **Run the app**

```bash
streamlit run app.py
```

2. **Open the Streamlit interface**
   Visit the URL provided in the terminal (usually `http://localhost:8501`).

3. **Upload PDFs and ask questions**
   Use the upload button to add PDFs and type your query in the input box to get context-aware answers.

---

## Key Components

* **PDF Processing**: Uses `loaders/pdf_loader.py` to extract text from PDFs.
* **Text Chunking**: Uses `processing/text_splitter.py` to split long documents into smaller chunks.
* **Embeddings**: `embeddings/embedding_model.py` converts text chunks into vectors.
* **FAISS Vector Store**: `vectorstore/faiss_db.py` stores vectors for fast similarity search.
* **Retriever & Generator**: `retrieve/` folder retrieves relevant chunks and generates answers using a generative model.

---

## Future Improvements

* Add **multi-user support** with session-based vector stores.
* Integrate **more embedding models** for better semantic understanding.
* Support **other document formats** like DOCX, TXT, and HTML.
* Implement **real-time streaming responses** for large documents.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Abhisek Mishra**

Data Scientist | Python Developer | Generative AI Developer

[LinkedIn](https://www.linkedin.com/in/abhisek-mishra/-) | [GitHub](https://github.com/Abhisek8895)
