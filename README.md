# Intelligent Automation Agent (IAA) 🤖

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-green)
![LangChain](https://img.shields.io/badge/LangChain-0.2%2B-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

A modular, scalable AI Agent built with **FastAPI** and **LangChain**. Currently features a robust RAG (Retrieval-Augmented Generation) engine for analyzing PDF documents, with planned expansions for Web and Email automation.

## 🚀 Features

- **RAG Engine**: Upload and query PDF documents using Google Gemini 1.5 Pro.
- **Vector Search**: efficient retrieval using Milvus Lite.
- **API-First Design**: Fully documented REST API (Swagger UI).
- **Modular Architecture**: Designed for easy expansion (Web, Email, Orchestration).

## 🛠️ Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/lucasmsorrentino/ragtest.git
    cd ragtest
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    # Mac/Linux
    source .venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuration

1. Create a `.env` file in the root directory.
2. Add your Google Gemini API Key:

    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

## 🏃‍♂️ Usage

1. **Start the API Server**

    ```bash
    python src/main.py
    ```

2. **Access the Interface**
    Open your browser to the interactive Swagger UI:
    👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

3. **Endpoints**
    - `POST /api/v1/upload`: Upload a PDF file to the knowledge base.
    - `POST /api/v1/chat`: Ask a question about the uploaded document.

## 🗺️ Roadmap

- [x] Core RAG Engine (PDF)
- [x] FastAPI Integration
- [ ] **Web Automation**: Playwright integration for browsing.
- [ ] **Email Tools**: Gmail/IMAP integration for reading and sending emails.
- [ ] **Agent Orchestrator**: Central brain to route tasks between tools.

## 📄 License

This project is licensed under the MIT License.
