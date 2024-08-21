import requests
from config import BASE_URL, REPORT_FILE_PATH, USERNAME, PASSWORD
from datetime import datetime

def log_report(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REPORT_FILE_PATH, "a") as report_file:
        report_file.write(f"[{timestamp}] {message}\n")

def get_token():
    login_data = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = requests.post(f"{BASE_URL}/login", json=login_data)  # LOGIN_URL yerine doğrudan oluşturuldu

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

def execute_campaign_scenario():
    try:
        token = get_token()
        log_report(f"Retrieved token: {token}")

        url = f"{BASE_URL}/campaigns/get-campaigns"
        headers = {"Authorization": f"Bearer {token}"}
        data = {
            "audiences": ["esnaf"],
            "status": True
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code != 200:
            log_report(f"Failed to fetch campaigns: {response.status_code} - {response.text}")
            raise Exception(f"Failed to fetch campaigns: {response.status_code} - {response.text}")

        response_json = response.json()
        log_report(f"Campaign response: {response_json}")

    except Exception as e:
        log_report(f"Campaign test failed: {str(e)}")
        raise e

if __name__ == "__main__":
    execute_campaign_scenario()
