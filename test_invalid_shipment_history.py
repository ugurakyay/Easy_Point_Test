import pytest
import requests
from config import BASE_URL

INVALID_TOKEN = "invalid_token"

def test_shipment_history_with_invalid_date_range():
    response = requests.post(f"{BASE_URL}/posts/get", headers={"Authorization": f"Bearer {INVALID_TOKEN}"}, json={
        "startDate": "invalid_date",
        "endDate": "invalid_date",
        "status": [5]
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def test_shipment_history_with_empty_date_range():
    response = requests.post(f"{BASE_URL}/posts/get", json={
        "startDate": "",
        "endDate": "",
        "status": [5]
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def test_shipment_history_with_invalid_token():
    response = requests.post(f"{BASE_URL}/posts/get", headers={"Authorization": f"Bearer {INVALID_TOKEN}"}, json={
        "startDate": "valid_date",
        "endDate": "valid_date",
        "status": [5]
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
