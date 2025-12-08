# Quick Start Guide - RAG Test Application

## What Was Fixed

The agent crash was caused by:

1. **Model Download Delays**: HuggingFace sentence-transformers models (90-400MB) download on first use
2. **Silent Initialization**: No feedback during model loading caused timeout/crash perception
3. **Missing Retries**: Test script didn't wait for server startup

## Fixes Applied

### ✅ 1. Enhanced Model Loading (`src/core/factory.py`)

- Added explicit cache directory configuration
- Added proper model parameters for CPU-only operation
- Disabled progress bars that could interfere with output

### ✅ 2. Server Startup Events (`src/main.py`)

- Pre-loads all models during server startup
- Shows clear progress messages with emoji indicators
- Provides visibility into what's happening

### ✅ 3. Improved Test Script (`test_verification.py`)

- Added `wait_for_server()` with exponential backoff (up to 30 retries)
- Better error messages
- Handles first-run model download delays

## How to Run (Correct Order)

### Step 1: Start the Server

```powershell
# Open a terminal and run:
python src/main.py
```

**Expected Output:**

```
INFO:__main__:🚀 Starting IAA API server...
INFO:__main__:📦 Initializing models (this may take a moment on first run)...
INFO:__main__:Loading embedding model...
# ... HuggingFace may download model here (first run only) ...
INFO:__main__:✅ Embedding model loaded successfully
INFO:__main__:Loading LLM...
INFO:__main__:✅ LLM loaded successfully
INFO:__main__:🎉 All models initialized. Server ready!
INFO:     Uvicorn running on http://127.0.0.1:8000
```

⏱️ **First Run:** May take 1-3 minutes to download models  
⏱️ **Subsequent Runs:** Should start in seconds

### Step 2: Run Tests (in a new terminal)

```powershell
# Open a NEW terminal and run:
python test_verification.py
```

**Expected Output:**

```
Waiting for server at http://127.0.0.1:8000/ ...
✅ Server is ready! (attempt 1)

✅ Health Check Passed: {'status': 'active', 'system': 'IAA'}

Testing Document Upload at http://127.0.0.1:8000/api/v1/upload ...
✅ Upload Passed: {'message': 'Document uploaded and indexed successfully'}

Testing Chat at http://127.0.0.1:8000/api/v1/chat ...
✅ Chat Passed!
Answer: [Your AI response here]
```

## Troubleshooting

### Issue: "Server not ready yet, waiting..."

- **Normal on first run** - models are downloading
- Wait up to 5 minutes on slow connections
- Check server terminal for progress

### Issue: "Server failed to start after 30 attempts"

- Check if server is actually running in the other terminal
- Verify port 8000 is not in use: `netstat -ano | findstr :8000`
- Check `.env` file has correct API keys

### Issue: Model download seems stuck

- Check internet connection
- Look at `~/.cache/huggingface/` directory size
- Expected model size: ~90MB for all-MiniLM-L6-v2

### Issue: Import errors

- Run: `pip install -r requirements.txt`
- Ensure sentence-transformers is installed: `pip install sentence-transformers`

## Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                   test_verification.py               │
│  (Tests the API endpoints)                           │
└──────────────────┬──────────────────────────────────┘
                   │ HTTP Requests
                   ▼
┌─────────────────────────────────────────────────────┐
│                   src/main.py (FastAPI)              │
│  • Startup: Pre-loads models                         │
│  • Routes: /api/v1/upload, /api/v1/chat             │
└──────────────────┬──────────────────────────────────┘
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
┌──────────────────┐  ┌──────────────────┐
│  ModelFactory    │  │  RAGEngine       │
│  • get_llm()     │  │  • PDF parsing   │
│  • get_embeddings│  │  • Vector store  │
└──────────────────┘  └──────────────────┘
        │                     │
        ▼                     ▼
┌──────────────────┐  ┌──────────────────┐
│  Groq/Google     │  │  Milvus Lite     │
│  (LLM API)       │  │  (Vector DB)     │
└──────────────────┘  └──────────────────┘
```

## Environment Variables Required

Check your `.env` file contains:

```env
# LLM Provider (groq or google)
LLM_PROVIDER=groq
GROQ_API_KEY=your_key_here

# Embedding Provider (huggingface or google)
EMBEDDING_PROVIDER=huggingface

# Milvus
MILVUS_URI=./volumes/milvus_rag.db
```

## Next Steps

1. ✅ Server starts without crashes
2. ✅ Models load with clear feedback
3. ✅ Tests wait properly for initialization
4. 🚀 Ready to extend with more features!

## Additional Commands

### Check if server is running

```powershell
curl http://127.0.0.1:8000/
```

### View logs with more detail

```powershell
# Set environment variable before starting server:
$env:LOG_LEVEL="DEBUG"
python src/main.py
```

### Clear model cache (force re-download)

```powershell
Remove-Item -Recurse -Force ~\.cache\huggingface
```
