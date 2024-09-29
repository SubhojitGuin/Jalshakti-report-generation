import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API = st.secrets["general"]["API"]

def get_data_from_sql(question, sessionId):
    url = f"{API}/api/v1/sql_dataframe"
    payload = {
        "question": question,
        "language": "English",
        "sessionid": sessionId
    }
    response = requests.post(url, json=payload)
    return response.json()["response"]

def get_data_from_text(question, sessionId):
    url = f"{API}/api/v1/text"
    payload = {
        "question": question,
        "language": "English",
        "sessionid": sessionId
    }
    response = requests.post(url, json=payload)
    return response.json()["response"]

if __name__=="__main__":
    question = "What is the population of India?"
    sessionId = "1234"
    print(get_data_from_sql(question, sessionId))