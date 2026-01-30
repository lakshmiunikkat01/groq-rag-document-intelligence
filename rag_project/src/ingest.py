import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


DATA_DIR = "data"
DB_DIR = "vectorstore"

documents = []

for filename in os.listdir(DATA_DIR):
    if filename.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(DATA_DIR, filename))
        documents.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_documents(chunks, embeddings)
db.save_local(DB_DIR)

print(" Ingestion complete. Vector store created.")
