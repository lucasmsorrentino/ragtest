from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from src.config import settings

class ModelFactory:
    @staticmethod
    def get_llm():
        provider = settings.LLM_PROVIDER.lower()
        
        if provider == "groq":
            if not settings.GROQ_API_KEY:
                raise ValueError("GROQ_API_KEY is missing in environment variables.")
            # Groq Llama 3 model
            return ChatGroq(
                model="llama-3.3-70b-versatile", 
                temperature=0,
                groq_api_key=settings.GROQ_API_KEY
            )
        
        elif provider == "google":
            return ChatGoogleGenerativeAI(
                model="gemini-1.5-pro", 
                temperature=0, 
                google_api_key=settings.GOOGLE_API_KEY
            )
        
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")

    @staticmethod
    def get_embeddings():
        provider = settings.EMBEDDING_PROVIDER.lower()
        
        if provider == "huggingface":
            # Runs locally, free.
            # Configure HuggingFace to show download progress and handle caching properly
            import os
            cache_dir = os.path.join(os.path.expanduser("~"), ".cache", "huggingface")
            os.makedirs(cache_dir, exist_ok=True)
            
            return HuggingFaceEmbeddings(
                model_name="all-MiniLM-L6-v2",
                cache_folder=cache_dir,
                model_kwargs={'device': 'cpu'},
                encode_kwargs={'normalize_embeddings': True}
            )
            
        elif provider == "google":
            return GoogleGenerativeAIEmbeddings(
                model="models/embedding-001", 
                google_api_key=settings.GOOGLE_API_KEY
            )
            
        else:
            raise ValueError(f"Unsupported Embedding provider: {provider}")
