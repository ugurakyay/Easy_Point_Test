import requests
from config import BASE_URL, REPORT_FILE_PATH, USERNAME, PASSWORD
from datetime import datetime

# URL Tanımlaması
LOGIN_URL = f"{BASE_URL}/login"
USER_PROFILE_URL = f"{BASE_URL}/users/get-profile"

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

def get_user_profile(token):
    """Retrieve the user's profile using the provided token."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(USER_PROFILE_URL, headers=headers)

    if response.status_code != 200:
        log_report(f"User profile request failed: {response.status_code} - {response.text}")
        raise Exception(f"User profile request failed: {response.status_code} - {response.text}")

    response_json = response.json()
    log_report(f"User profile retrieved: {response_json}")
    return response_json

def execute_user_profile_scenario():
    """Execute the user profile retrieval scenario."""
    try:
        token = get_token()
        log_report(f"Retrieved token: {token}")

        user_profile = get_user_profile(token)
        log_report(f"User profile retrieval successful: {user_profile}")
    except Exception as e:
        log_report(f"User profile retrieval test failed: {str(e)}")
        raise e

if __name__ == "__main__":
    execute_user_profile_scenario()
