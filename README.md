# 🧠 FinSolve RBAC Chatbot

An internal AI-powered chatbot for FinSolve Technologies built using Retrieval-Augmented Generation (RAG) and Role-Based Access Control (RBAC). It enables secure, department-specific data access and intelligent responses across Finance, Marketing, HR, Engineering, C-Level, and General Employees.

---

## 🚀 Features

- 🔐 **Role-Based Access Control** – Each user sees only what their department is allowed to access.
- 🤖 **RAG Architecture** – Combines vector similarity search with LLMs for accurate, context-rich answers.
- 🧾 **Source-Aware Responses** – Retrieves from markdown documents and shows relevant context.
- 🛠️ **Streamlit Frontend** – Clean and interactive chat interface.
- 🧠 **OpenAI-Free** – Runs on HuggingFace models like Flan-T5 (works offline after first use).
- 🧩 **Modular Architecture** – Built using FastAPI, LangChain, Chroma, and Transformers.

---

## 🧰 Tech Stack

| Layer        | Tools Used                          |
|--------------|-------------------------------------|
| Language Model | `flan-t5-base` via HuggingFace Transformers |
| Embeddings   | `all-MiniLM-L6-v2` via Sentence Transformers |
| Vector DB    | `ChromaDB`                          |
| Backend API  | `FastAPI`                           |
| Frontend     | `Streamlit`                         |
| Auth & Config| `dotenv`, `RBAC` logic              |

---

## 📁 Folder Structure

finchatbot/
├── app/
│ ├── auth.py # Role mapping
│ ├── chatbot.py # RAG logic
│ ├── data_loader.py # Embedding + loading docs
│ ├── access_control.py # RBAC rules
│ ├── config.py # Loads .env keys
│ └── main.py # FastAPI server (optional)
│
├── ui/
│ └── streamlit_app.py # Streamlit chatbot UI
│
├── data/
│ ├── finance/
│ ├── hr/
│ ├── marketing/
│ ├── engineering/
│ └── general/
│
├── .env # API keys
├── requirements.txt
└── README.md


---

## 🛠️ Setup Instructions

1. **Clone Repo**
```bash
git clone https://github.com/MalharJojare/finchatbot.git
cd finchatbot

Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # or `source venv/bin/activate` on Mac/Linux

Install Dependencies
pip install -r requirements.txt

Create .env File
HUGGINGFACEHUB_API_TOKEN=your_token_here

Run the App
streamlit run ui/streamlit_app.py
