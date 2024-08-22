import pytest
import requests
from config import BASE_URL

INVALID_TOKEN = "invalid_token"

def test_get_posts_with_invalid_taken_name():
    response = requests.post(f"{BASE_URL}/posts/get", headers={"Authorization": f"Bearer {INVALID_TOKEN}"}, json={
        "takenName": "invalid_name",
        "status": [5]
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def test_get_posts_with_empty_taken_name():
    response = requests.post(f"{BASE_URL}/posts/get", json={
        "takenName": "",
        "status": [5]
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def test_get_posts_with_invalid_token():
    response = requests.post(f"{BASE_URL}/posts/get", headers={"Authorization": f"Bearer {INVALID_TOKEN}"}, json={
        "takenName": "valid_name",
        "status": [5]
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
