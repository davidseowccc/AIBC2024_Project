# run in windows command prompt
# 1. change directory: cd\PyCode2023\AIBC_Project\AIBC_venv\Scripts
# 2. activate venv: D:\PyCode2023\AIBC_Project\AIBC_venv\Scripts>activate.bat
# 3. (AIBC_venv) D:\PyCode2023\AIBC_Project\AIBC_venv>python -m streamlit run main.py
# Project - David Seow 20 Oct 2024

import streamlit as st

st.set_page_config(
    layout="centered",
    page_title="Ngee Ann Polytechnic Virtual Course Counselling Chatbots",
    page_icon="👋",
)

st.title("Ngee Ann Polytechnic Virtual Course Counselling Chatbots")
st.write("Welcome! 👋")
st.text("Powered by Groq LLM and David Seow 20 Oct 2024")

st.markdown(
    """
    This chatbot app deploys Streamlit as the web framework deploying Llama3.1 or later as LLM from Groq.
     It details chatbots to query NP courses (TBC: that could be found in the 'View all courses' tab).

    **👈 Select a page from the sidebar** for all this app can do!
    
    #### Main                       - Menu page (Current page)
    #### NP JAE COPs 2014-2024      - Chatbot
    #### NP PFP COPs 2022-2024      - Chatbot
    #### NP Course Brochure         - Chatbot (under construction)
    #### View PFP COP Table         - view all courses from 2014-2022
    #### View PFP COP Table         - view all courses from 2022-2022
    #### About                      - about this App
    """
)
