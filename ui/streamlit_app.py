import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.auth import get_user_role
from app.data_loader import load_documents, create_vector_store
from app.chatbot import build_chatbot
import streamlit as st
st.title("FinSolve Internal Chatbot")

username = st.text_input("Enter your username")
if username:
    role = get_user_role(username)
    st.success(f"Logged in as {username} ({role})")

    if "chatbot" not in st.session_state:
        st.info("Loading documents...")
        allowed_folder = f"./data/general" if role == "employee" else f"./data/{role}"
        docs = load_documents(allowed_folder)
        vectordb = create_vector_store(docs)
        st.session_state.chatbot = build_chatbot(vectordb)

    query = st.text_input("Ask a question:")
    if query:
        response = st.session_state.chatbot.invoke({"query": query})
        st.write("Answer:", response["result"])
        
        

