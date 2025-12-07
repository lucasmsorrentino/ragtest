import sys
import os

# Add project root to sys.path to allow 'from src...' imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from src.api.routes.rag import router as rag_router
import uvicorn

app = FastAPI(title="IAA - Intelligent Automation Agent API", version="1.0.0")

app.include_router(rag_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "active", "system": "IAA"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
