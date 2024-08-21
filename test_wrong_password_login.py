import requests
from config import BASE_URL, USERNAME, PASSWORD

# URL Tanımlaması
LOGIN_URL = f"{BASE_URL}/login"

def wrong_password_login():
    """Attempt login with an incorrect password."""
    wrong_password = "wrongPassword123"  # Yanlış şifre
    response = requests.post(LOGIN_URL, json={"username": USERNAME, "password": wrong_password})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    wrong_password_login()
