import requests
from datetime import datetime
import json
from config import BASE_URL, LOGIN_URL, GET_POSTS_URL, COMPLETE_ORDER_URL, USERNAME, PASSWORD, REPORT_FILE_PATH

def initialize_report():
    """Initialize the report file by clearing its content and writing the start time."""
    with open(REPORT_FILE_PATH, "w") as report_file:
        report_file.write(f"Rapor Başlangıcı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

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
    try:
        response = requests.post(LOGIN_URL, json=login_data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        log_report(f"Login isteği başarısız oldu: {str(e)}")
        raise

    response_json = response.json()
    result = response_json.get("result", {})
    token = result.get("token")

    if not token:
        log_report(f"Token alınamadı: {response_json}")
        raise Exception(f"Token alınamadı: {response_json}")

    log_report(f"Login token alındı: {token}")
    return token

def call_service(token, url, data=None, method="GET"):
    """Call a service with the provided token, URL, data, and HTTP method."""
    headers = {"Authorization": f"Bearer {token}"}
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        else:  # POST method
            response = requests.post(url, json=data, headers=headers)

        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        log_report(f"{url} servisine istek başarısız: {str(e)}")
        raise

    try:
        response_json = response.json()
    except ValueError:
        log_report(f"Geçersiz JSON cevabı alındı: {response.text}")
        raise

    log_report(f"{url} servisine istek atıldı. Cevap: {response.status_code} - {response_json}")
    return response_json

def execute_order():
    """Execute the complete order process by logging in, fetching posts, and completing an order."""
    initialize_report()

    try:
        # Adım 1: Token al
        token = get_token()
        log_report(f"Alınan token: {token}")

        # Adım 2: Postları al
        get_posts_body = {
            "status": [5],
            "limit": 3
        }
        posts_response = call_service(token, GET_POSTS_URL, data=get_posts_body, method="POST")

        result = posts_response.get("result", [])
        if not isinstance(result, list) or not result:
            log_report(f"Beklenen formatta olmayan veya boş yanıt: {posts_response}")
            raise Exception("Beklenen formatta olmayan veya boş yanıt alındı.")

        # Hepsiburada API'ye ait uygun postları filtrele
        hepsiburada_posts = [
            post for post in result
            if post.get("dataEntranceType") == "Hepsiburada API" and post.get("status") == "5"
        ]

        if not hepsiburada_posts:
            log_report("Hepsiburada API'ye ait uygun post bulunamadı.")
            raise Exception("Hepsiburada API'ye ait uygun post bulunamadı.")

        # Adım 3: İlk uygun post için işlem yap
        for post in hepsiburada_posts:
            post_id = post.get("id")
            verification_code = post.get("verificationCode")

            if not post_id or not verification_code:
                log_report("Post için ID veya doğrulama kodu bulunamadı.")
                continue

            log_report(f"Post ID: {post_id}, Verification Code: {verification_code}")

            # Adım 4: Complete order isteği gönder
            complete_order_body = {
                "postID": post_id,
                "otpType": "EasypointOTP",
                "otp": verification_code
            }

            log_report(f"Complete Order servisine istek atılıyor: {json.dumps(complete_order_body, indent=2)}")

            final_response = call_service(token, COMPLETE_ORDER_URL, data=complete_order_body, method="POST")

            log_report(f"Son istekten dönen cevap: {json.dumps(final_response, indent=2)}")
            log_report(f"Complete servisinde kullanılan postID: {post_id}, otp: {verification_code}")

    except Exception as e:
        log_report(f"Hata: {str(e)}")
        raise e

if __name__ == "__main__":
    execute_order()
