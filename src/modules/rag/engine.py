# src/modules/rag/engine.py
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Milvus
from src.core.factory import ModelFactory
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.config import settings

class RAGEngine:
    def __init__(self):
        """
        Initialize vector store connection and LLM.
        """
        self.embeddings = ModelFactory.get_embeddings()
        self.llm = ModelFactory.get_llm()

    def load_and_split_pdf(self, file_path):
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        return splits

    def get_vector_store(self, splits):
        # Milvus Vector Store
        vector_store = Milvus.from_documents(
            splits,
            embedding=self.embeddings,
            connection_args={"uri": settings.MILVUS_URI}, 
            collection_name="rag_collection",
            drop_old=True 
        )
        return vector_store

    def get_rag_chain(self, vector_store):
        retriever = vector_store.as_retriever()
        
        system_prompt = (
            "You are an assistant for question-answering tasks. "
            "Use the following pieces of retrieved context to answer "
            "the question. If you don't know the answer, say that you "
            "don't know. Use three sentences maximum and keep the "
            "answer concise."
            "\n\n"
            "{context}"
        )
        
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )
        
        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        return rag_chain

    def process_document(self, file_path: str):
        """
        Main entry point to process a document and return a runnable chain.
        """
        splits = self.load_and_split_pdf(file_path)
        vector_store = self.get_vector_store(splits)
        return self.get_rag_chain(vector_store)
