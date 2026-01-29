groq-rag-document-intelligence
==============================

LLM-powered document intelligence system built using Retrieval-Augmented Generation (RAG).  
This project enables question answering over PDF documents with grounded responses and source references using Groq-hosted LLaMA models.

---

Overview
--------

The system ingests PDF documents, converts them into semantic embeddings, stores them in a FAISS vector database, and retrieves relevant content at query time to generate accurate, non-hallucinated answers using a large language model.

---

Features
--------

- PDF document ingestion
- Semantic chunking of text
- Vector similarity search using FAISS
- Retrieval-Augmented Generation (RAG)
- Groq-hosted LLaMA 3.1 for low-latency inference
- Source-aware answers
- Supports single or multiple PDF files

---

Architecture
------------

PDF Documents  
→ Text Chunking  
→ Embeddings (HuggingFace)  
→ FAISS Vector Store  
→ Retriever  
→ Groq LLaMA 3.1  
→ Answer with Sources

---

Tech Stack
----------

- Python 3.11  
- LangChain  
- Groq (LLaMA-3.1-8b-instant)  
- FAISS  
- HuggingFace Sentence Transformers  
- PyPDF  

---

Project Structure
---------------
groq-rag-document-intelligence/
│
├── data/                  
│   └── policy.pdf
│
├── ingest.py              
├── retrieve_generate.py    
├── vectorstore/           
└── README.md

Usage
-----

1. Place PDF files inside the `data/` folder.

2. Run document ingestion:
```bash
py -3.11 ingest.py



3. Ask questions over documents:
```bash
py -3.11 retrieve_generate.py



Type `exit` to stop the program.

---

Sample Output
-------------

Ask a question (type 'exit' to quit): What is this document about?
The response is generated using retrieved document chunks and includes source references for grounding.



--------------------

