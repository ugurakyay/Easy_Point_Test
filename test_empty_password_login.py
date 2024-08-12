# test_empty_password_login.py
import requests
from config import LOGIN_URL, USERNAME

def empty_password_login():
    response = requests.post(LOGIN_URL, json={"username": USERNAME, "password": ""})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    empty_password_login()
