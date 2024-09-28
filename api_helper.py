import requests

def get_data_from_sql(question, sessionId):
    url = "http://127.0.0.1:8080/api/v1/sql"
    payload = {
        "question": question,
        "language": "English",
        "sessionid": sessionId
    }
    response = requests.post(url, json=payload)
    return response.json()["response"]

def get_data_from_text(question, sessionId):
    url = "http://127.0.0.1:8080/api/v1/text"
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