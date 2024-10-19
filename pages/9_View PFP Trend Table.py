import os
import json
import pandas as pd
import requests
import streamlit as st


# # Load the JSON file
# filepath = './data/courses-full.json'
# with open(filepath, 'r') as file:
#     json_string = file.read()
#     dict_of_courses = json.loads(json_string)

# upload file
filepath = './data/table_pfpnp_csv.csv'
with open(filepath, 'r') as file:
    # df = pd.read_csv(file)
    df = pd.read_csv(file, encoding="ISO-8859-1")

# # URL of the raw JSON file on GitHub
# url = 'https://raw.githubusercontent.com/davidseowccc/AI_Bootcamp_2024_DS/main/week-07-david/data/courses-full.json'

# # Fetch the JSON file from GitHub
# response = requests.get(url)
# json_string = response.text

# # Parse the JSON string into a Python dictionary
# dict_of_courses = json.loads(json_string)

# # Create the DataFrame and Transpose Table
# df = pd.DataFrame(dict_of_courses).T

# # Reset the index to bring the course name as a column
# df.reset_index(drop=True, inplace=True)

# Display the DataFrame
df.index += 1

st.title("NP PFP COPs 2022-2024 Table")
st.text("This dataset is collated from past JAE/PFPAE data and scraped from \nPoly/JC COPs 2024 (10 year trend): https://docs.google.com/spreadsheets/d/14b5VLIr9W5teiOp0vCg86B6xxpFiwk8jeIzwbdJmWjU/pubhtml#")

# df
st.table(df)
