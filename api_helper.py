import streamlit as st
import requests
import os
import logging


# API = os.environ["API"]
# os.environ["API"] = st.secrets["API"]

API = st.secrets["general"]["api"]


def get_data_from_sql(question, sessionId):
    logging.info(f"API : {API}")
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