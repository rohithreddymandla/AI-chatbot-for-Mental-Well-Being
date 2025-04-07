# 🧠 AI Chatbot for Mental Well-Being

A conversational AI assistant designed to support users with mental and emotional well-being through empathetic, intelligent dialogue. Built using state-of-the-art NLP and LLMs (Large Language Models), the chatbot integrates deep learning, retrieval-augmented generation (RAG), and memory management to provide meaningful, context-aware conversations.

---

## ✨ Features

- 💬 **Intent Classification** with BERT-based classifiers
- 🧠 **LLM-Powered Conversations** using OpenAI or local LLMs via LangChain
- 🔁 **Conversation Memory** with `ConversationBufferMemory` for persistent chat context
- 📚 **RAG (Retrieval-Augmented Generation)** to ground answers in relevant information
- 🧘 **Emotion-aware response generation** to enhance empathy and well-being
- 🔐 Optional integration with Twilio for SMS or WhatsApp chat support

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- Langchain (Integration of LLMs with application)
- Hugging Face Vector Embeddings
- OpenAI API key (or other supported LLM provider)

### 📦 Installation

```bash
git clone https://github.com/rohithreddymandla/AI-chatbot-for-Mental-Well-Being.git
cd AI-chatbot-for-Mental-Well-Being

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

#Running the Chatbot
python run.py

# 📁 Project Structure
AI-chatbot-for-Mental-Well-Being/
│
├── Application/                 # Core app routes and logic
├── bert_intent_classification.py
├── run.py                       # Entry point
├── train_jsonl.jsonl            # Sample training data
├── rag_emotional_index/         # RAG vector store
├── requirements.txt
├── .gitignore
└── README.md
```
### 🙌 Acknowledgments
---

`LangChain` for LLM chaining and memory management

`Hugging Face` Transformers for BERT

`OpenAI` API for chat capabilities

`Twilio` API for multi-platform integration

### 🤝 Contributing
---

Would you like me to:
- Embed a usage GIF or screenshot of the chat experience?
- Add setup instructions for Streamlit or FastAPI version?
- Include Hugging Face Spaces deployment?

Let me know how you'd like to present it — I can generate a `README.md` file directly if you want to drop it into your repo.
