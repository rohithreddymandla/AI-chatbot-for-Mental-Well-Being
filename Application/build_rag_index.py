import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

# Load your dataset
df = pd.read_csv("counsel_data_merged_dataset.csv", encoding="ISO-8859-1")

# Combine question and answer
df["content"] = df.apply(lambda row: f"Q: {row['questionText']}\nA: {row['answerText']}", axis=1)

# Turn into LangChain Documents
docs = [Document(page_content=txt) for txt in df["content"]]

# Split long entries
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)

# Initialize HuggingFace Embeddings
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Build FAISS vector store
vectorstore = FAISS.from_documents(split_docs, embedding)
vectorstore.save_local("rag_emotional_index")

print("✅ FAISS vector store saved to 'rag_emotional_index/'")