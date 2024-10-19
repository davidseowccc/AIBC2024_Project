import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Project Methodology"
)
# endregion <--------- Streamlit App Configuration --------->

url = 'https://raw.githubusercontent.com/davidseowccc/AIBC2024_Project/main/data/FlowChart.jpg'

st.title("Project Methodology")
# st.text("This project is created by David Seow on 20 Sep 2024 \nwith skills obtained from the AI Bootcamp 2024.")
st.write("\n")
st.image(url, caption="Methodology Flowchart")

st.write('''
\n\n1. The flowchart depicts the programme logic for the RAG-LLM chatbot and the 3 use cases; namely,
    \n\ta. chatbot for Joint Admissions Exercise (JAE) related queries
    \n\tb. chatbot for Poly Foundation Programme Admissions Exercise (PFP) related queries
    \n\tc. chatbot for Ngee Ann Polytechnic Course queries on course details and prospects     

2. The first and second decision flows (a and b) is a LLM-powered chatbot 
based on open source data from the web. The data table is uploaded via PANDAS and
the LLM references it closely and deploys a Chain of Thought (COT) prompting technique 
before replying the user.
         
3. The third decision flow (currently able to work on colab) is a LLM-powered chatbot
based on open source documents compiled into one PDF. The pdf document is uploaded via
PDF loader, split-&-chunk and transformed to vector embeddings in a vector store. The LLM
references this vector store before replying the user.
COLAB link: https://colab.research.google.com/drive/1xaVeD4VCX_MqQ9f98FUPi4YekSRbRIVT?usp=sharing
        
''')
