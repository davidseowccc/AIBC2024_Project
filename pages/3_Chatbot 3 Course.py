# run in windows command prompt: python -m streamlit run main.py

# https://discuss.streamlit.io/t/issues-with-chroma-and-sqlite/47950/4
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# Set up and run this Streamlit App
import streamlit as st
import os
import pandas as pd
import requests
from dotenv import load_dotenv


# import libraries
from groq import Groq
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.memory import ConversationBufferMemory

# from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

import warnings
warnings.filterwarnings("ignore")

# un-comment when in vs-code
load_dotenv('.env')
API_KEY = os.getenv('GROQ_KEY')
# client = Groq(api_key=os.getenv('GROQ_KEY'))

url = 'https://raw.githubusercontent.com/davidseowccc/AIBC2024_Project/main/data/2024NP_merged.pdf'
loader = PyPDFLoader(url)

data = loader.load_and_split()
# text_splitter = CharacterTextSplitter(chunk_size=512, chunk_overlap=128)
# OR
text_splitter = CharacterTextSplitter(chunk_size=512)
texts = text_splitter.split_documents(data)

# 110M parameters
# Strong performance on tasks that require understanding of sentence structure, syntax, and semantics
# embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# OR
# 22M parameters
# Strong performance on tasks that require fast and accurate text classification, sentiment analysis, and language modeling
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


# # on local
# vectorstore = Chroma.from_documents(
#     # collection_name="about_JAE2025",
#     # documents=texts,
#     documents=data,
#     embedding=embedding,
# )

######################################################################
# Reference:
# 1. https://gist.github.com/gettingstartedwithai/b5be6af064801d695592648259b3d2ba
# 2. https://docs.trychroma.com/integrations/streamlit
# 3. 

# Load the Chroma database from disk
vectorstore = Chroma(persist_directory="data", 
                   embedding_function=embedding,
                   collection_name="lc_chroma_demo")

# Get the collection from the Chroma database
collection = vectorstore.get()

# If the collection is empty, create a new one
if len(collection['ids']) == 0:
    # Create a new Chroma database from the documents
    vectorstore = Chroma.from_documents(
        documents=data, 
        embedding=embedding, 
        persist_directory="data1",
        collection_name="lc_chroma_demo"
    )

    # Save the Chroma database to disk
    vectorstore.persist()

######################################################################

# model1="llama-3.1-70b-versatile"
# model1="llama-3.2-11b-vision-preview"
model1="mixtral-8x7b-32768"

llm = ChatGroq(
    model=model1,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=API_KEY
    # other params...
)

qa = RetrievalQA.from_chain_type(
    llm,
    retriever=vectorstore.as_retriever(k=20),
    return_source_documents=True
)


# from google.colab import output

def process_user_message(user_prompt):
    query = input(user_prompt)
    result = qa({"query": query})
    
    return result


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="NP Course Query - 2024 Edition"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Course Query Chatbot [Work In Progress]")
st.text("David Seow, 15 Oct 2024")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt/query here", height=200)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response, course_details = process_user_message(user_prompt)
    st.write(response)

    st.divider()
