# Project Roadmap: Intelligent Automation Agent (IAA)

## 1. Executive Summary

The goal is to evolve the current RAG Chatbot into a fully-fledged **Intelligent Automation Agent**. This agent will not only answer questions from documents but also actively interact with external systems (Email, Web APIs) to perform tasks.

## 2. Architecture Overview

```mermaid
graph TD
    User[User] -->|HTTP Requests| UI[FastAPI / Swagger UI]
    UI -->|Queries| Agent[Main Agent Orchestrator]
    
    subgraph "Brain (RAG)"
        Agent -->|Retrieve Context| Milvus[Milvus Vector DB]
        Agent -->|Generate Answer| Gemini[Google Gemini LLM]
        PDFs[PDF Documents] -->|Indexer| Milvus
    end

    subgraph "Capabilities (Tools)"
        Agent -->|Send/Read| Email[Email Service]
        Agent -->|Scrape/Act| Web[Web Browser/APIs]
        Agent -->|Query/Store| SQL[Relational DB (History/Logs)]
    end
```

## 3. Modules & Features

### Phase 1: Core RAG (Current State)

- [x] PDF Ingestion & Indexing
- [x] Vector Search (Milvus)
- [x] LLM Integration (Gemini)
- [x] Basic Q&A Interface

### Phase 2: Enhanced interaction & Memory

- **Chat History**: Persistent conversation memory (using an SQL database or file-based).
- **Context Awareness**: Ability to remember user preferences.
- **Multi-modal Support**: Handling images in PDFs.

### Phase 3: Email Automation

- **SMTP/IMAP Integration**:
  - Read unread emails.
  - Draft and send responses based on RAG knowledge.
  - Summarize long threads.
- **Triggers**: Auto-reply to specific senders.

### Phase 4: Web Systems Integration

- **Web Browsing**: Using **Playwright** for robust, headless browser automation.
- **Handling JS**: Playwright is excellent for modern dynamic websites (SPA).
- **API Connectors**: connecting to tools like Slack, Trello, or internal CRMs.
- **Data Scraping**: Extracting data from websites to update the RAG knowledge base.

## 4. Technology Stack Expansion

- **Database**: SQLite (dev) / PostgreSQL (prod) for app state, users, and logs.
- **Email**: `smtplib`, `imaplib`, or Gmail API.
- **Web Automation**: `playwright` (Python).
