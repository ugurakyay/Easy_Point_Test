import pytest
import requests
from config import BASE_URL
from base64 import b64encode

INVALID_TOKEN = "invalid_token"

def test_technical_support_with_empty_title():
    response = requests.post(f"{BASE_URL}/support/create-ticket", json={
        "title": [],
        "description": "Automation test description",
        "files": [],
        "type": "Easy Point Esnaf App"
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def test_technical_support_with_invalid_file_format():
    response = requests.post(f"{BASE_URL}/support/create-ticket", json={
        "title": ["Test"],
        "description": "Automation test description",
        "files": [{"name": "file.txt", "content": b64encode(b"invalid content").decode("utf-8")}],
        "type": "Easy Point Esnaf App"
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def test_technical_support_with_invalid_token():
    response = requests.post(f"{BASE_URL}/support/create-ticket", headers={"Authorization": f"Bearer {INVALID_TOKEN}"}, json={
        "title": ["Test"],
        "description": "Automation test description",
        "files": [],
        "type": "Easy Point Esnaf App"
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
