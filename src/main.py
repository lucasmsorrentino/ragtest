import sys
import os

# Add project root to sys.path to allow 'from src...' imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from src.api.routes.rag import router as rag_router
from src.core.factory import ModelFactory
import uvicorn
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="IAA - Intelligent Automation Agent API", version="1.0.0")

app.include_router(rag_router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    """
    Pre-load models during startup to avoid delays on first request.
    """
    logger.info("🚀 Starting IAA API server...")
    logger.info("📦 Initializing models (this may take a moment on first run)...")
    
    try:
        # Pre-initialize embeddings and LLM
        logger.info("Loading embedding model...")
        _ = ModelFactory.get_embeddings()
        logger.info("✅ Embedding model loaded successfully")
        
        logger.info("Loading LLM...")
        _ = ModelFactory.get_llm()
        logger.info("✅ LLM loaded successfully")
        
        logger.info("🎉 All models initialized. Server ready!")
    except Exception as e:
        logger.error(f"❌ Error during model initialization: {e}")
        raise

@app.get("/")
def health_check():
    return {"status": "active", "system": "IAA"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
