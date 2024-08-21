import requests
from config import BASE_URL, REPORT_FILE_PATH, USERNAME, PASSWORD
from datetime import datetime

# URL Tanımlamaları
LOGIN_URL = f"{BASE_URL}/login"
UPDATE_PROFILE_URL = f"{BASE_URL}/users/update-profile"

counter = 1  # To keep track of the incrementing name suffix across multiple runs

def log_report(message):
    """Log a message to the report file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REPORT_FILE_PATH, "a") as report_file:
        report_file.write(f"[{timestamp}] {message}\n")

def get_token():
    """Authenticate using the login service and retrieve a token."""
    login_data = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = requests.post(LOGIN_URL, json=login_data)

    if response.status_code != 200:
        log_report(f"Login request failed: {response.status_code} - {response.text}")
        raise Exception(f"Login request failed: {response.status_code} - {response.text}")

    response_json = response.json()
    result = response_json.get("result", {})
    token = result.get("token")

    if not token:
        log_report(f"Failed to retrieve token: {response_json}")
        raise Exception(f"Failed to retrieve token: {response_json}")

    log_report(f"Login token retrieved: {token}")
    return token

def update_user_profile(token, count):
    """Update the user's profile with the given token and count."""
    headers = {"Authorization": f"Bearer {token}"}
    profile_data = {
        "name": f"automation{count}",
        "lastname": "TestLastName",
        "mallID": "123456",
        "email": f"automation{count}@example.com",
        "corporationID": "78910",
        "isAdministrator": True,
        "branchID": "branch123",
        "phone": "+905551234567"
    }
    response = requests.post(UPDATE_PROFILE_URL, json=profile_data, headers=headers)

    if response.status_code != 200:
        log_report(f"User profile update request failed: {response.status_code} - {response.text}")
        raise Exception(f"User profile update request failed: {response.status_code} - {response.text}")

    response_json = response.json()
    log_report(f"User profile update response: {response_json}")
    return response_json

def execute_update_profile_scenario():
    """Execute the user profile update scenario."""
    global counter
    try:
        token = get_token()
        log_report(f"Retrieved token: {token}")

        update_response = update_user_profile(token, counter)
        log_report(f"User profile update successful: {update_response}")
        counter += 1  # Increment the counter for the next run
    except Exception as e:
        log_report(f"User profile update test failed: {str(e)}")
        raise e

if __name__ == "__main__":
    execute_update_profile_scenario()
