import requests
from config import BASE_URL, REPORT_FILE_PATH, USERNAME, PASSWORD
from datetime import datetime

LOGIN_URL = f"{BASE_URL}/login"
FETCH_POSTS_URL = f"{BASE_URL}/posts/get"

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

def fetch_posts(token):
    """Fetch posts using the provided token."""
    headers = {"Authorization": f"Bearer {token}"}
    fetch_posts_body = {
        "status": [3, 5, 9],
        "limit": 10
    }
    response = requests.post(FETCH_POSTS_URL, json=fetch_posts_body, headers=headers)

    if response.status_code != 200:
        log_report(f"Fetching posts request failed: {response.status_code} - {response.text}")
        raise Exception(f"Fetching posts request failed: {response.status_code} - {response.text}")

    response_json = response.json()
    log_report(f"Posts fetched successfully: {response_json}")
    return response_json

def execute_fetch_posts_scenario():
    """Execute the fetch posts scenario."""
    try:
        token = get_token()
        log_report(f"Retrieved token: {token}")

        posts = fetch_posts(token)
        log_report(f"Posts fetch scenario completed successfully: {posts}")
    except Exception as e:
        log_report(f"Posts fetch scenario failed: {str(e)}")
        raise e

if __name__ == "__main__":
    execute_fetch_posts_scenario()
