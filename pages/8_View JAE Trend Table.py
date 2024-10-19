import os
import json
import pandas as pd
import requests
import streamlit as st
import urllib

# # URL of the raw JSON file on GitHub
url = 'https://raw.githubusercontent.com/davidseowccc/AIBC2024_Project/main/data/table_np_csv.csv'
df = pd.read_csv(url, encoding="ISO-8859-1")

# Show row index from 1
df.index += 1

st.title("NP JAE COPs 2014-2024 Table")
st.text("This dataset is collated from past JAE/PFPAE data and scraped from \nPoly/JC COPs 2024 (10 year trend): \nhttps://docs.google.com/spreadsheets/d/14b5VLIr9W5teiOp0vCg86B6xxpFiwk8jeIzwbdJmWjU/pubhtml#")

# Display the DataFrame
st.table(df)
