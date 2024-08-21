import requests
from config import BASE_URL, REPORT_FILE_PATH, USERNAME, PASSWORD
from datetime import datetime

# URL tanımlamaları
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
        "username": USERNAME,  # config.py'den alınıyor
        "password": PASSWORD   # config.py'den alınıyor
    }
    response = requests.post(LOGIN_URL, json=login_data)

    if response.status_code != 200:
        log_report(f"Login isteği başarısız oldu: {response.status_code} - {response.text}")
        raise Exception(f"Login isteği başarısız oldu: {response.status_code} - {response.text}")

    response_json = response.json()
    result = response_json.get("result", {})
    token = result.get("token")

    if not token:
        log_report(f"Token alınamadı: {response_json}")
        raise Exception(f"Token alınamadı: {response_json}")

    log_report(f"Login token alındı: {token}")
    return token

def get_hepsiburada_post_details(token):
    """Retrieve Hepsiburada post details."""
    headers = {"Authorization": f"Bearer {token}"}
    get_posts_body = {
        "status": [5],
        "limit": 1
    }
    response = requests.post(GET_POSTS_URL, json=get_posts_body, headers=headers)

    if response.status_code != 200:
        log_report(f"Posts alma isteği başarısız oldu: {response.status_code} - {response.text}")
        raise Exception(f"Posts alma isteği başarısız oldu: {response.status_code} - {response.text}")

    response_json = response.json()
    result = response_json.get("result", [])
    log_report(f"Posts alındı: {response_json}")

    if not result:
        log_report("Hepsiburada API için uygun post bulunamadı.")
        raise Exception("Hepsiburada API için uygun post bulunamadı.")

    post_details = result[0]
    barcode = post_details.get("barcode")

    if not barcode:
        log_report("Barcode bilgisi bulunamadı.")
        raise Exception("Barcode bilgisi bulunamadı.")

    log_report(f"Filtrelenmiş Hepsiburada post detayları: {post_details}")
    return post_details

def search_barcode(token, barcode):
    """Search for a barcode."""
    url = f"{BASE_URL}/flow/post-search-barcode-v2"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "barcode": [barcode]
    }
    response = requests.post(url, json=body, headers=headers)

    if response.status_code != 200:
        log_report(f"Barcode arama isteği başarısız oldu: {response.status_code} - {response.text}")
        raise Exception(f"Barcode arama isteği başarısız oldu: {response.status_code} - {response.text}")

    response_json = response.json()
    log_report(f"Barcode arama sonucu: {response_json}")
    return response_json

def take_in_possession():
    """Execute the take in possession scenario."""
    try:
        token = get_token()
        log_report(f"Alınan token: {token}")

        post_details = get_hepsiburada_post_details(token)
        post_id = post_details["id"]
        barcode = post_details["barcode"]
        log_report(f"Seçilen Post ID: {post_id}, Barcode: {barcode}")

        search_result = search_barcode(token, barcode)
        log_report(f"Barcode {barcode} için arama sonucu: {search_result}")

        log_report("Take in possession scenario completed successfully.")
    except Exception as e:
        log_report(f"Take in possession test failed: {str(e)}")
        raise e

if __name__ == "__main__":
    take_in_possession()
