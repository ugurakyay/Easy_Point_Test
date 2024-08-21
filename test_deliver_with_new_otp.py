import requests
from config import BASE_URL, REPORT_FILE_PATH, USERNAME, PASSWORD
from datetime import datetime


def log_report(message):
    """Log a message to the report file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REPORT_FILE_PATH, "a") as report_file:
        report_file.write(f"[{timestamp}] {message}\n")


def get_token():
    """Authenticate using the login service and retrieve a token."""
    login_url = f"{BASE_URL}/login"
    login_data = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = requests.post(login_url, json=login_data)

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


def get_hepsiburada_post_details(token):
    """Fetch post details with status '5' and filter by Hepsiburada API."""
    headers = {"Authorization": f"Bearer {token}"}
    get_posts_url = f"{BASE_URL}/posts/get"
    get_posts_body = {
        "status": [5],
        "limit": 10
    }
    response = requests.post(get_posts_url, json=get_posts_body, headers=headers)

    if response.status_code != 200:
        log_report(f"Failed to fetch posts: {response.status_code} - {response.text}")
        raise Exception(f"Failed to fetch posts: {response.status_code} - {response.text}")

    response_json = response.json()
    result = response_json.get("result", [])
    log_report(f"Posts fetched: {response_json}")

    for post in result:
        if post.get("dataEntranceType") == "Hepsiburada API" and post.get("status") == '5':
            post_id = post.get("id")
            barcode = post.get("barcode")
            log_report(f"Selected Post ID: {post_id}, Barcode: {barcode}")
            return post_id, barcode

    log_report("No suitable Hepsiburada API post found.")
    raise Exception("No suitable Hepsiburada API post found.")


def recreate_delivery_password(token, post_id):
    """Request to recreate the delivery password for a given post ID."""
    url = f"{BASE_URL}/flow/post-recreate-deliver-password"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "postID": post_id
    }
    response = requests.post(url, json=body, headers=headers)

    if response.status_code != 200:
        log_report(f"Failed to recreate delivery password: {response.status_code} - {response.text}")
        raise Exception(f"Failed to recreate delivery password: {response.status_code} - {response.text}")

    response_json = response.json()
    log_report(f"Recreate delivery password result: {response_json}")

    otp = response_json.get("result", "")
    if not otp:
        log_report(f"Failed to retrieve OTP: {response_json}")
        raise Exception("Failed to retrieve OTP.")
    return otp


def complete_order(token, post_id, otp):
    """Complete an order using the post ID and OTP."""
    url = f"{BASE_URL}/posts/complete"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "postID": post_id,
        "otpType": "EasypointOTP",
        "otp": otp
    }
    response = requests.post(url, json=body, headers=headers)

    if response.status_code != 200:
        log_report(f"Failed to complete order: {response.status_code} - {response.text}")
        raise Exception(f"Failed to complete order: {response.status_code} - {response.text}")

    response_json = response.json()
    log_report(f"Order completion result: {response_json}")


def deliver_with_new_otp():
    """Main function to deliver with a new OTP."""
    try:
        token = get_token()
        log_report(f"Retrieved token: {token}")

        post_id, barcode = get_hepsiburada_post_details(token)

        otp = recreate_delivery_password(token, post_id)
        log_report(f"Retrieved OTP: {otp}")

        complete_order(token, post_id, otp)
        log_report("Deliver with new OTP scenario completed successfully.")
    except Exception as e:
        log_report(f"Deliver with new OTP test failed: {str(e)}")
        raise e


if __name__ == "__main__":
    deliver_with_new_otp()
