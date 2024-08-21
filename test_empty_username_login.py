# test_empty_username_login.py
import requests
from config import BASE_URL, PASSWORD

def empty_username_login():
    response = requests.post(BASE_URL, json={"username": "", "password": PASSWORD})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    empty_username_login()
