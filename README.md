# Automotive_RAG_Gen_AI
#  Generative AI PDF Chatbot using Gemini, LangChain & FAISS

A Retrieval-Augmented Generation (RAG) chatbot that enables users to ask natural language questions about PDF documents and receive accurate, context-aware answers. The application leverages **Google Gemini 2.5 Flash**, **LangChain**, **FAISS**, and **HuggingFace Embeddings** to build an intelligent document question-answering system.

---

##  Features

-  Load and process PDF documents
-  Intelligent text chunking using RecursiveCharacterTextSplitter
-  Semantic search with HuggingFace Embeddings
-  Fast vector similarity search using FAISS
-  Context-aware responses powered by Google Gemini 2.5 Flash
-  Retrieval-Augmented Generation (RAG) architecture
-  Flask-based web interface
-  Secure API key management using environment variables

---

##  Project Architecture

```
PDF Document
      │
      ▼
PyPDFLoader
      │
      ▼
Text Chunking
      │
      ▼
HuggingFace Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Retriever
      │
      ▼
Google Gemini 2.5 Flash
      │
      ▼
Flask Web Application
```

---

##  Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| LLM | Google Gemini 2.5 Flash |
| Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | HuggingFace (all-MiniLM-L6-v2) |
| Backend | Flask |
| PDF Processing | PyPDFLoader |
| Environment | python-dotenv |

---

##  Project Structure

```
GenAI-PDF-Chatbot/

│── app.py
│── gen_ai.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env.example
│ ── index.html
└── sample.pdf
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/GenAI-PDF-Chatbot.git

cd GenAI-PDF-Chatbot
```

### 2. Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

### 5. Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000/
```

---

##  How It Works

1. Load the PDF document.
2. Split the document into overlapping chunks.
3. Generate semantic embeddings using HuggingFace.
4. Store embeddings inside FAISS.
5. Retrieve the most relevant chunks.
6. Send retrieved context to Gemini.
7. Generate accurate answers using RAG.

---

##  Screenshots

### Home Page

(Add Screenshot)

---

### Asking a Question

(Add Screenshot)

---

### Generated Answer

(Add Screenshot)

---

##  Skills Demonstrated

- Python Programming
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- LangChain
- Google Gemini API
- Vector Databases (FAISS)
- Semantic Search
- Flask REST API
- HuggingFace Embeddings
- Document Question Answering
- Software Development
- Environment Variable Management

---

##  Future Improvements

- Upload PDF through the web interface
- Persistent FAISS index storage
- Multi-document support
- Chat history and conversation memory
- Docker containerization
- User authentication
- Cloud deployment (AWS/Azure)

---

##  Author

**Omkar Vikram Godage**

 Email: omkargodage18@gmail.com

 GitHub: https://github.com/OmkarGodage18

---

##  License

This project is developed for learning and portfolio purposes.
