from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FinSolve Chatbot is live"}
