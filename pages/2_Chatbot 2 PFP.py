# run in windows command prompt: python -m streamlit run main.py

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

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

import warnings
warnings.filterwarnings("ignore")

# un-comment when in vs-code
load_dotenv('.env')
client = Groq(api_key=os.getenv('GROQ_KEY'))

# # for streamlit
# client = Groq(
#     api_key=st.secrets["GROQ_KEY"],)


# # upload file
# filepath = './data/table_np_csv.csv'
# with open(filepath, 'r') as file:
#     # df = pd.read_csv(file)
#     df = pd.read_csv(file, encoding="ISO-8859-1", index_col=0)


# # URL of the raw JSON file on GitHub
# url = 'https://raw.githubusercontent.com/davidseowccc/AI_Bootcamp_2024_DS/main/week-07-david/data/courses-full.json'
# df = pd.read_csv(url, index_col=0, encoding="ISO-8859-1")

def get_completion_by_messages(messages, model="mixtral-8x7b-32768", temperature=0, top_p=1.0, max_tokens=1024, n=1):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=1
    )

    # Models
    # mixtral-8x7b-32768
    # llama-3.2-11b-vision-preview
    # llama-3.1-70b-versatile
    return response.choices[0].message.content


# def generate_response(user_message):
#     # upload file
#     filepath = './data/table_pfpnp_csv.csv'
#     with open(filepath, 'r') as file:
#         # df = pd.read_csv(file)
#         df = pd.read_csv(file, encoding="ISO-8859-1")

    url = 'https://raw.githubusercontent.com/davidseowccc/AIBC2024_Project/main/data/table_pfpnp_csv.csv'
    df = pd.read_csv(url, encoding="ISO-8859-1")
    
    product_details=df

    delimiter = "####"

    system_message = f"""
    Follow these steps to process the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    This terms are interchangeable: 
    1.PFP = Polytechnic Foundation Programme
    2.ELR2B2 = JAE cutoff points or COP
    3.ELMAB3 = PFP cutoff points or COP
    4.EMB3 = ELMB3 = ELMAB3 
    5.Intake = Intake size
    
    This is the understanding when queries ask:
    1. The lower the COP or ELR2B2, the better the student intake quality
    2. Best course are those with lowest cutoff points or COP or ELR2B2.

    Step 1:{delimiter} If the user is asking about course, \
    understand the relevant course(s) from the following list.
    All available courses shown in the data below:
    {product_details}

    Step 2:{delimiter} Use the information about the course to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the course information.
    Your response should be as detail as possible and \
    include information that is useful for customer to better understand the course.

    Step 3:{delimiter}: Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    the customers to make their decision.
    Promote Ngee Ann Polytechnic where applicable.
    Complete with details such as rating, ELR2B2 or ELMAB3 trending and skills to be learnt.
    Use Neural Linguistic Programming to construct your response.

    End the response with the following:
    1.Always tell customer 'This dataset is collated from past JAE/PFPAE data and scraped from Poly/JC COPs 2024 (10 year trend): https://docs.google.com/spreadsheets/d/14b5VLIr9W5teiOp0vCg86B6xxpFiwk8jeIzwbdJmWjU/pubhtml#' 
    2.If you don't know the answer, tell the user to send the query to NP admissions mailbox at 'admissions@np.edu.sg'.

    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_customer = get_completion_by_messages(messages)

    return response_to_customer

#### Function Testing
# Testing the function to make sure it works
# This part should not be included as part of the Python script.

# Sample Queries
# 1. user_query = f"""What are the ELR2B2 trends for Ngee Ann's diploma in engineering science?"""
# 2. user_query = f"""Which Polytechnic have the best engineering courses and what course is it?"""
# 3. user_query = f"""What are the COP trends for Engineering in NP?"""
# 4. user_query = f"""What are the COP trends for Business in NP?"""
# 5. user_query = f"""show the ELR2B2 for marine & offshore technology"""
# 6. user_query = f"""Plot a graph of COP trends for Business Studies in NP?"""
# 7. user_query = f"""What are the intake trends for Ngee Ann?"""
# 8. user_query = f"""Which course is in danger of losing popularity?"""
# 9. user_query = f"""How is the International Qualifications Admissions process like?"""

# user_query = f"""Which Polytechnic have the best engineering courses and what course is it?"""

# response = generate_response(user_query)
# print(response)

####


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="NP PFP COPs 2014-2024  - Chatbot"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("NP PFP COPs 2014-2024  - Chatbot")
st.text("David Seow, 20 Oct 2024")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your query related to PFP COPs and JAE intake of Ngee Ann Polytechnic Courses", height=200)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response = generate_response(user_prompt)
    st.write(response)

    st.divider()

    #df


    # '''
    # Step 1:{delimiter} If the user is asking about course, \
    # understand the relevant course(s) from the following list.
    # All available courses shown in the data below:
    # {product_details}

    # Step 2:{delimiter} Use the information about the course to \
    # generate the answer for the customer's query.
    # You must only rely on the facts or information in the course information.
    # Your response should be as detail as possible and \
    # include information that is useful for customer to better understand the course.

    # Step 3:{delimiter}: Answer the customer in a friendly tone.
    # Make sure the statements are factually accurate.
    # Your response should be comprehensive and informative to help the \
    # the customers to make their decision.
    # Promote Ngee Ann Polytechnic where applicable.
    # Complete with details such as rating, ELR2B2 or ELMAB3 trending and skills to be learnt.
    # Use Neural Linguistic Programming to construct your response.

    # Use the following format:
    # Always tell customer 'This dataset is collated from past JAE/PFPAE data and scraped from Poly/JC COPs 2024 (10 year trend): https://docs.google.com/spreadsheets/d/14b5VLIr9W5teiOp0vCg86B6xxpFiwk8jeIzwbdJmWjU/pubhtml#' 
    # Step 1:{delimiter} <step 1 reasoning>
    # Step 2:{delimiter} <step 2 reasoning>
    # Step 3:{delimiter} <step 3 response to customer>

    # Make sure to include {delimiter} to separate every step.

    # If you don't know the answer, tell the user to send the query to NP admissions mailbox at 'admissions@np.edu.sg'.

    # """
