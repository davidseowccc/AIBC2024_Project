import streamlit as st


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="About this App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Course Query Chatbot")
# st.text("This project is created by David Seow on 20 Sep 2024 \nwith skills obtained from the AI Bootcamp 2024.")

with st.expander("Credits"):
    st.write('''
        This project is created by David Seow on 20 Oct 2024 \nwith skills obtained from the AI Bootcamp 2024.
    ''')

with st.expander("How to use this app"):
    st.write('''
        #### Main
        1. Enter your prompt or query in the text area.
        2. Click "Submit".
        3. A response would be generated.
        
        #### View
        1. This page views the listing of courses in a table format.
    ''')

with st.expander("Project Details required by AI Bootcamp"):
    st.write('''
        #### Project Scope
        1. This project is a chatbot specifically for Ngee Ann Polytechnic Admissions related to 
        Joint Polytechnic Admissions Exercise (JAE) and Poly foundation Programme Admissions Exercise (PFPAE).
        2. The data are from open source, online data compiled from MOE website data. Details are in the below tab.
        3. Retrieval-Augmented-Generation (RAG) using GROQ and Huggingface LLMs are deployed in this project. 
        
        #### Objectives
        1. To create a one-stop query portal for admissions related query, course and job prospects from Public.
        2. At least 2 use-case chatbots are operational. 2 Chatbots for the 2 separate admissions exercise are operational.
        The 3rd chatbot on course brochure is still work in progress due to dependencies issues (while it works well in colab, 
        it does not seem to function well when deployed on streamlit). 
        
        #### Data Sources
        1. Admissions Data
        For the 2 admissions exercises, the data source is from open source:
        https://docs.google.com/spreadsheets/d/14b5VLIr9W5teiOp0vCg86B6xxpFiwk8jeIzwbdJmWjU/pubhtml#
            
            a. Screencapture and computer-vision parsing has to be done to extract the data
            
            b. Thereafter data prep and cleansing has to be done.
            
            c. The data is loaded via pandas and used in RAG operations within the LLM chatbot
        2. Ngee Ann Polytechnic Course Brochure
            
            a. For the course brochure, various brochures from ngee ann polytechnic websites were downloaded and merged. 
            
            b. Pdf parsing were conducted in python script and stored as vector database for the RAG LLM chatbot. 
                
        #### Features
        1. Data Preparation and Loading using computer vision and parsing
        2. RAG operations using pandas tables and Chroma Vector Stores
        3. GROQ and Huggingface LLMs were deployed
    ''')

