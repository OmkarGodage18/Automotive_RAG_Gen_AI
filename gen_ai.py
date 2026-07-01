#!/usr/bin/env python
# coding: utf-8

# In[6]:


#get_ipython().system('pip install python-dotenv')


# In[7]:


from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA




# In[11]:


# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY is None:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to your .env file."
    )
def get_llm(pdf_path):

    # =========================
    # LOAD PDF FILE
    # =========================

    from langchain_community.document_loaders import PyPDFLoader

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    print("Total Pages:", len(documents))

    # =========================
    # SPLIT DOCUMENTS
    # =========================

    from langchain_text_splitters import RecursiveCharacterTextSplitter

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,chunk_overlap=300)

    docs = text_splitter.split_documents(documents)

    print("Total Chunks:", len(docs))

    # =========================
    # EMBEDDINGS
    # =========================

    from langchain_community.embeddings import HuggingFaceEmbeddings

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Embeddings Created Successfully")

    # =========================
    # VECTOR DATABASE
    # =========================

    from langchain_community.vectorstores import FAISS

    vectorstore = FAISS.from_documents(
        docs,
        embeddings
    )

    print("FAISS Database Ready")

    # =========================
    # RETRIEVER
    # =========================

    retriever = vectorstore.as_retriever(search_type="similarity",search_kwargs={"k": 6})

    print("Retriever Ready")

    # =========================
    # GEMINI MODEL
    # =========================

    from langchain_google_genai import ChatGoogleGenerativeAI

    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)

    print("Model Loaded")
    
    from langchain.prompts import PromptTemplate
    prompt_template = """
    Use the following context to answer the question accurately.
    If the answer is present in the context, answer directly and clearly.
    Do not add extra information.

    Context:
    {context}

    Question:
    {question}
  
    Answer:
    
        """
   
    PROMPT = PromptTemplate(template=prompt_template,input_variables=["context", "question"])

    
        

    # =========================
    # QA CHAIN
    # =========================

    from langchain.prompts import PromptTemplate
    from langchain.chains import RetrievalQA
    
    qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": PROMPT}
)

    print("RAG Pipeline Ready")

    return qa_chain


# In[ ]:



