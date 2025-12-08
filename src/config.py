import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    # Options: "google", "groq"
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "google")
    
    # Options: "google", "huggingface"
    EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "google")

    MILVUS_URI = "http://localhost:19530"
    DB_URL = "sqlite:///./data/app.db"

settings = Settings()
