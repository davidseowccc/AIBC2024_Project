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
