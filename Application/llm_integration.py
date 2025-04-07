from langchain_google_vertexai import VertexAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
import os


class ChatAssistant:
    def __init__(self):
        # Initialize VertexAI Chat Model (Gemini)
        self.llm = VertexAI(
            model_name="gemini-pro",
            temperature=0.7,
            max_output_tokens=256,
            project=os.getenv("VERTEX_PROJECT_ID"),
            location=os.getenv("VERTEX_LOCATION"),
        )

        # Load emotional RAG index built with HuggingFace embeddings
        embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = FAISS.load_local(
    		folder_path="rag_emotional_index",
    		embeddings=embedding,
    		allow_dangerous_deserialization=True
	)
        self.retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

        # Memory buffer for conversation
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # Prompt for emotional intelligence
        self.prompt = PromptTemplate(
    input_variables=["chat_history", "question", "context"],
    template="""
You are iFriend, a compassionate and emotionally intelligent mental health assistant.
Always respond in English, even if the question is asked in another language.

Use the following context from prior interactions and emotional support resources to guide your response. Always be kind, empathetic, and supportive.

Context:
{context}

Conversation History:
{chat_history}

Human: {question}
iFriend:"""
)
        # Conversational Retrieval-Augmented Generation (RAG) chain
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.retriever,
            memory=self.memory,
            combine_docs_chain_kwargs={"prompt": self.prompt},
            return_source_documents=False,
            verbose=True
        )

    def get_response(self, user_input):
        result = self.chain.invoke({"question": user_input})
        return result["answer"]

# Create a singleton instance for use in routes
chat_assistant = ChatAssistant()