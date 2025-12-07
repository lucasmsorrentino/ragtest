# Task Checklist

## 0. Project Setup & Core RAG
- [x] Initialize Project Environment
- [x] Install Core Dependencies (`langchain`, `streamlit`, `pymilvus`, `google-genai`)
- [x] Build Basic RAG Engine (`rag_engine.py`)
- [x] Documentation (`README.md`, `walkthrough.md`) <!-- Updated for FastAPI -->

## 1. System Improvements (Immediate)
- [ ] **API Migration (FastAPI)**
    - [ ] Install `fastapi`, `uvicorn`.
    - [ ] Create `src/api` module.
    - [ ] Expose RAG engine via REST API (`POST /chat`).
- [ ] **Persistent Memory**
    - [ ] Create SQLite database connection.
    - [ ] Store chat sessions in DB.
    - [ ] Allow users to view past conversations.
- [ ] **File Management**
    - [ ] Add support for deleting/managing uploaded PDFs.
    - [ ] Support for other formats (DOCX, TXT).

## 2. Email Automation Module
- [ ] **Setup**
    - [ ] Research Gmail API vs SMTP/IMAP.
    - [ ] Create `email_agent.py` module.
- [ ] **Features**
    - [ ] Implement `read_emails()` function.
    - [ ] Implement `send_email()` tool for the Agent.
    - [ ] Create "Draft Reply" workflow using RAG context.

## 3. Web & Systems Automation (Playwright)
- [ ] **Setup**
    - [ ] Add `playwright` to `requirements.txt`.
    - [ ] Run `playwright install` to download browsers.
- [ ] **Web Scraper**
    - [ ] Build a tool to fetch URL content (`web_loader.py`) using Playwright.
    - [ ] Implement robust error handling and retries.
    - [ ] Add fetched web content to Milvus.
- [ ] **Automation Logic**
    - [ ] Create specialized scripts for target web systems (e.g. login, fill forms).

## 4. Orchestration
- [ ] **Agentic Workflow**
    - [ ] Upgrade from simple Chains to **LangGraph**.
    - [ ] Define "Router" to decide if query needs RAG, Email, or Web.
