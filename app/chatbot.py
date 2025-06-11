from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from app.config import HUGGINGFACE_API_KEY
from transformers import pipeline
from langchain.llms import HuggingFacePipeline

def build_chatbot(vectordb):
    retriever = vectordb.as_retriever(search_type="similarity", k=3)
    # Load local pipeline
    hf_pipeline = pipeline(
        model="google/flan-t5-base",
        task="text2text-generation",
        max_length=300,
        temperature=0.5
    )
    llm = HuggingFacePipeline(pipeline=hf_pipeline)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa

    
