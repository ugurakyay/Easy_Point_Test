# test_wrong_password_login.py
import requests
from config import LOGIN_URL, USERNAME

def wrong_password_login():
    wrong_password = "wrongPassword123"
    response = requests.post(LOGIN_URL, json={"username": USERNAME, "password": wrong_password})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    wrong_password_login()
