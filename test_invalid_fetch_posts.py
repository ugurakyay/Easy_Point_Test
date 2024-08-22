import pytest
import requests
from config import BASE_URL

INVALID_TOKEN = "invalid_token"

def test_fetch_posts_with_invalid_token():
    response = requests.post(f"{BASE_URL}/posts/get", headers={"Authorization": f"Bearer {INVALID_TOKEN}"}, json={
        "status": [5],
        "limit": 10000
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def test_fetch_posts_with_empty_token():
    response = requests.post(f"{BASE_URL}/posts/get", headers={"Authorization": ""}, json={
        "status": [5],
        "limit": 10000
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def test_fetch_posts_with_invalid_parameters():
    response = requests.post(f"{BASE_URL}/posts/get", json={
        "status": "invalid_status",
        "limit": "invalid_limit"
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
