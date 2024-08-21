import requests
from config import BASE_URL, USERNAME

def empty_password_login():
    login_url = f"{BASE_URL}/login"  # LOGIN_URL'yi doğrudan config'den almanıza gerek kalmadı
    response = requests.post(login_url, json={"username": USERNAME, "password": ""})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    empty_password_login()
