import requests
from config import BASE_URL, LOGIN_URL, GET_POSTS_URL, REPORT_FILE_PATH, USERNAME, PASSWORD
from datetime import datetime

def log_report(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REPORT_FILE_PATH, "a") as report_file:
        report_file.write(f"[{timestamp}] {message}\n")

def get_token():
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
    headers = {"Authorization": f"Bearer {token}"}
    get_posts_body = {
        "status": [5],
        "limit": 10
    }
    response = requests.post(GET_POSTS_URL, json=get_posts_body, headers=headers)

    if response.status_code != 200:
        log_report(f"Posts alma isteği başarısız oldu: {response.status_code} - {response.text}")
        raise Exception(f"Posts alma isteği başarısız oldu: {response.status_code} - {response.text}")

    response_json = response.json()
    result = response_json.get("result", [])
    log_report(f"Posts alındı: {response_json}")

    hepsiburada_posts = [
        {"id": post.get("id"), "barcode": post.get("barcode")}
        for post in result
        if post.get("dataEntranceType") == "Hepsiburada API" and post.get("status") == 5
    ]

    if not hepsiburada_posts:
        log_report("Hepsiburada API için uygun post bulunamadı.")
        raise Exception("Hepsiburada API için uygun post bulunamadı.")

    log_report(f"Filtrelenmiş Hepsiburada post detayları: {hepsiburada_posts}")
    return hepsiburada_posts[0]  # İlk uygun olanı al

def search_barcode(token, barcode):
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
