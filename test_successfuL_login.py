# test_successfuL_login.py
import requests
from config import LOGIN_URL, USERNAME, PASSWORD

def successful_login():
    response = requests.post(LOGIN_URL, json={"username": USERNAME, "password": PASSWORD})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    successful_login()
