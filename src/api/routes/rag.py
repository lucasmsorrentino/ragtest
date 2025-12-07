from fastapi import APIRouter, UploadFile, File, HTTPException
from src.modules.rag.engine import RAGEngine
from src.api.schemas.rag import ChatRequest, ChatResponse, UploadResponse
import shutil
import os
import uuid

router = APIRouter()
rag_engine = RAGEngine()

# In-memory storage for chains (for prototype simplicity)
# In production, this should be handled by the Orchestrator/Memory module
active_chains = {} 

@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    try:
        # Save temp file
        file_path = f"data/temp_{uuid.uuid4()}_{file.filename}"
        os.makedirs("data", exist_ok=True)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Process document
        chain = rag_engine.process_document(file_path)
        active_chains["default"] = chain # Simple single-user session for now
        
        # Cleanup
        os.remove(file_path)
        
        return UploadResponse(filename=file.filename, message="Document processed successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    chain = active_chains.get(request.session_id)
    if not chain:
        raise HTTPException(status_code=400, detail="No document processed for this session. Please upload a PDF first.")
        
    response = chain.invoke({"input": request.message})
    return ChatResponse(answer=response["answer"], context=[d.page_content for d in response.get("context", [])])
