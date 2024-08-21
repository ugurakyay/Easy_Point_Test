import requests
from datetime import datetime
from config import BASE_URL, REPORT_FILE_PATH, USERNAME, PASSWORD

# URLs
LOGIN_URL = f"{BASE_URL}/login"
GET_POSTS_URL = f"{BASE_URL}/posts/get"
RETURN_COMPLETE_URL = f"{BASE_URL}/flow/post-return-complete"

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

def get_barcode(token):
    """Fetch the barcode from a post with status 9."""
    headers = {"Authorization": f"Bearer {token}"}
    get_posts_body = {
        "status": [9],
        "limit": 1
    }
    response = requests.post(GET_POSTS_URL, json=get_posts_body, headers=headers)

    if response.status_code != 200:
        log_report(f"Failed to fetch posts: {response.status_code} - {response.text}")
        raise Exception(f"Failed to fetch posts: {response.status_code} - {response.text}")

    response_json = response.json()
    result = response_json.get("result", [])
    log_report(f"Posts fetched: {response_json}")

    if not result:
        log_report("No posts found with status 9.")
        raise Exception("No posts found with status 9.")

    barcode = result[0].get("barcode")
    if not barcode:
        log_report("Barcode not found in the post data.")
        raise Exception("Barcode not found in the post data.")

    log_report(f"Selected Barcode: {barcode}")
    return barcode

def complete_return(token, barcode):
    """Complete the return process using the barcode."""
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "barcode": barcode
    }
    response = requests.post(RETURN_COMPLETE_URL, json=body, headers=headers)

    if response.status_code != 200:
        log_report(f"Failed to complete return: {response.status_code} - {response.text}")
        raise Exception(f"Failed to complete return: {response.status_code} - {response.text}")

    response_json = response.json()
    log_report(f"Return completion result: {response_json}")

def execute_return_scenario():
    """Execute the return scenario."""
    try:
        token = get_token()
        log_report(f"Retrieved token: {token}")

        barcode = get_barcode(token)

        complete_return(token, barcode)
        log_report("Return scenario completed successfully.")
    except Exception as e:
        log_report(f"Return test failed: {str(e)}")
        raise e

if __name__ == "__main__":
    execute_return_scenario()
