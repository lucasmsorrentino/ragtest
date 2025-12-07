import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    MILVUS_URI = "./data/milvus/milvus_demo.db"
    DB_URL = "sqlite:///./data/app.db"

settings = Settings()
