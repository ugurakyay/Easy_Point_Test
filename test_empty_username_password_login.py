# test_empty_username_password_login.py
import requests
from config import BASE_URL

def empty_username_password_login():
    response = requests.post(BASE_URL, json={"username": "", "password": ""})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    empty_username_password_login()
