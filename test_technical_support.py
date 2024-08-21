import os
import base64
import requests
from datetime import datetime
from config import BASE_URL, REPORT_FILE_PATH, USERNAME, PASSWORD

# URL Tanımlamaları
LOGIN_URL = f"{BASE_URL}/login"
CREATE_TICKET_URL = f"{BASE_URL}/support/create-ticket"

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

def create_technical_support_ticket(token):
    """Create a technical support ticket using the provided token."""
    headers = {"Authorization": f"Bearer {token}"}
    title = ["Technical Issue", "API Bug"]
    description = f"Automation test - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    # Set the actual file path here
    file_path = REPORT_FILE_PATH  # Use the report file path from config

    if not os.path.exists(file_path):
        log_report(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "rb") as file:
        encoded_file = base64.b64encode(file.read()).decode('utf-8')

    files = [encoded_file]

    body = {
        "title": title,
        "description": description,
        "files": files,
        "type": "Easy Point Esnaf App"
    }

    response = requests.post(CREATE_TICKET_URL, json=body, headers=headers)

    if response.status_code != 200:
        log_report(f"Failed to create technical support ticket: {response.status_code} - {response.text}")
        raise Exception(f"Failed to create technical support ticket: {response.status_code} - {response.text}")

    response_json = response.json()
    log_report(f"Technical support ticket created: {response_json}")

def execute_technical_support_scenario():
    """Execute the technical support scenario."""
    try:
        token = get_token()
        log_report(f"Retrieved token: {token}")

        create_technical_support_ticket(token)
        log_report("Technical Support scenario completed successfully.")
    except Exception as e:
        log_report(f"Technical Support test failed: {str(e)}")
        raise e

if __name__ == "__main__":
    execute_technical_support_scenario()
