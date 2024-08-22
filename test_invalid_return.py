import pytest
import requests
from config import BASE_URL

INVALID_POST_ID = "invalid_post_id"
INVALID_OTP = "000000"
VALID_POST_ID = "valid_post_id"  # Replace this with an actual valid post ID

def test_return_with_invalid_post_id():
    response = requests.post(f"{BASE_URL}/post/return", json={
        "postID": INVALID_POST_ID,
        "otpType": "EasypointOTP",
        "otp": "valid_otp"  # Replace with a valid OTP
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def test_return_with_empty_post_id():
    response = requests.post(f"{BASE_URL}/post/return", json={
        "postID": "",
        "otpType": "EasypointOTP",
        "otp": "valid_otp"  # Replace with a valid OTP
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"

def test_return_with_invalid_otp():
    response = requests.post(f"{BASE_URL}/post/return", json={
        "postID": VALID_POST_ID,
        "otpType": "EasypointOTP",
        "otp": INVALID_OTP
    })
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
