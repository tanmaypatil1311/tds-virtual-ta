from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.storage.docstore import SimpleDocumentStore
import os

app = FastAPI()

# Load markdown files and build index once
documents = SimpleDirectoryReader("tds_markdown").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

@app.post("/")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question")
    if not question:
        return JSONResponse(content={"error": "No question provided"}, status_code=400)
    
    response = query_engine.query(question)
    return {"answer": str(response)}
