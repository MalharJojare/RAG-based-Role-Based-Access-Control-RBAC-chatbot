from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os
from langchain.embeddings import HuggingFaceEmbeddings



def load_documents(folder_path):
    documents = []
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                clean_path = os.path.abspath(os.path.join(root, file)).replace("\\", "/")
                loader = TextLoader(clean_path, encoding='utf-8')
                documents.extend(loader.load())

    return documents

def create_vector_store(docs, persist_directory="vector_store"):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(docs)

    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(
        texts, embedding=embedding, persist_directory=persist_directory
    )
    vectordb.persist()
    return vectordb
