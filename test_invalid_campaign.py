import pytest
import requests
from config import BASE_URL

INVALID_TOKEN = "invalid_token"
INVALID_CAMPAIGN_ID = "invalid_campaign_id"

def test_campaign_with_invalid_token():
    response = requests.get(f"{BASE_URL}/campaigns/get-campaigns", headers={"Authorization": f"Bearer {INVALID_TOKEN}"})
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def test_campaign_with_empty_token():
    response = requests.get(f"{BASE_URL}/campaigns/get-campaigns", headers={"Authorization": ""})
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def test_campaign_with_invalid_campaign_id():
    response = requests.get(f"{BASE_URL}/campaigns/get-campaigns", headers={"Authorization": f"Bearer {INVALID_TOKEN}"}, params={"campaignId": INVALID_CAMPAIGN_ID})
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
