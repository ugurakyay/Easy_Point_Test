import requests
from config import BASE_URL, REPORT_FILE_PATH, USERNAME, PASSWORD, TAKEN_NAME
from datetime import datetime

LOGIN_URL = f"{BASE_URL}/login"
GET_POSTS_URL = f"{BASE_URL}/posts/get"

def log_report(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REPORT_FILE_PATH, "a") as report_file:
        report_file.write(f"[{timestamp}] {message}\n")

def get_token():
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

def get_posts_with_taken_name(token):
    headers = {"Authorization": f"Bearer {token}"}
    get_posts_body = {
        "status": [1, 5, 9, 16, 21],
        "limit": 10000,
        "takenName": TAKEN_NAME
    }
    response = requests.post(GET_POSTS_URL, json=get_posts_body, headers=headers)

    if response.status_code != 200:
        log_report(f"Get posts request failed: {response.status_code} - {response.text}")
        raise Exception(f"Get posts request failed: {response.status_code} - {response.text}")

    response_json = response.json()
    log_report(f"Posts retrieved: {response_json}")
    return response_json

def execute_get_posts_scenario():
    try:
        token = get_token()
        log_report(f"Retrieved token: {token}")

        posts = get_posts_with_taken_name(token)
        log_report(f"Get posts with takenName successful: {posts}")
    except Exception as e:
        log_report(f"Get posts with takenName test failed: {str(e)}")
        raise e

if __name__ == "__main__":
    execute_get_posts_scenario()
