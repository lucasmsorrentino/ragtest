# RAG Chatbot

## Setup

1.  **Install Dependencies**:
    Dependencies should already be installed. If not, run:
    ```bash
    pip install -r requirements.txt
    ```

2.  **API Key**:
    - Rename `.env.example` to `.env`.
    - Open `.env` and paste your Google API Key:
      ```
      GOOGLE_API_KEY=AIzaSy...
      ```

3.  **Run the API**:
    ```bash
    python src/main.py
    ```

4.  **Use**:
    - Open your browser at `http://localhost:8000/docs`.
    - Use the Swagger UI to test:
      - `POST /api/v1/upload` (Upload PDF)
      - `POST /api/v1/chat` (Ask questions)
