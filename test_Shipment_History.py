import requests
from datetime import datetime, timedelta
from config import BASE_URL, REPORT_FILE_PATH, USERNAME, PASSWORD

# URL'ler
LOGIN_URL = f"{BASE_URL}/login"
GET_POSTS_URL = f"{BASE_URL}/posts/get"

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

def get_shipment_history(token):
    """Fetch the shipment history based on the provided criteria."""
    headers = {"Authorization": f"Bearer {token}"}

    # Calculate dates
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

    request_body = {
        "status": [1, 5, 9, 16, 21],
        "startDate": start_date,
        "endDate": end_date,
        "orderBy": "inBranch",
        "limit": 10
    }

    response = requests.post(GET_POSTS_URL, json=request_body, headers=headers)

    if response.status_code != 200:
        log_report(f"Shipment history request failed: {response.status_code} - {response.text}")
        raise Exception(f"Shipment history request failed: {response.status_code} - {response.text}")

    response_json = response.json()
    log_report(f"Shipment history response: {response_json}")

    if response_json.get("status") is True:
        log_report("Shipment history retrieval successful.")
    else:
        log_report("Shipment history retrieval failed.")
        raise Exception("Shipment history retrieval failed.")

def execute_shipment_history_scenario():
    """Execute the shipment history scenario."""
    try:
        token = get_token()
        log_report(f"Retrieved token: {token}")

        get_shipment_history(token)
        log_report("Shipment history scenario completed successfully.")
    except Exception as e:
        log_report(f"Shipment history test failed: {str(e)}")
        raise e

if __name__ == "__main__":
    execute_shipment_history_scenario()
