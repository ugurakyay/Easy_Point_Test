import pytest
import allure
from datetime import datetime
from conftest import REPORT_FILE_PATH

# Import all modules
from test_successfuL_login import successful_login as _test_successful_login
from test_wrong_password_login import wrong_password_login as _test_wrong_password_login
from test_empty_username_login import empty_username_login as _test_empty_username_login
from test_empty_password_login import empty_password_login as _test_empty_password_login
from test_empty_username_password_login import empty_username_password_login as _test_empty_username_password_login
from test_complete_order import execute_order as _execute_order
from test_take_in_possession import take_in_possession as _test_take_in_possession
from test_deliver_with_new_otp import deliver_with_new_otp as _test_deliver_with_new_otp
from test_return import execute_return_scenario as _test_return_scenario
from test_campaign import execute_campaign_scenario as _test_campaign_scenario
from test_Shipment_History import execute_shipment_history_scenario as _test_shipment_history_scenario
from test_update_profile import execute_update_profile_scenario as _test_update_profile_scenario
from test_technical_support import execute_technical_support_scenario as _test_technical_support_scenario
from test_user_profile import execute_user_profile_scenario as _test_user_profile_scenario
from test_fetch_posts import execute_fetch_posts_scenario as _test_fetch_posts_scenario
from test_get_posts_with_taken_name import execute_get_posts_scenario as _test_get_posts_scenario

# Import negative test modules
from test_invalid_campaign import (
    test_campaign_with_invalid_token as _test_invalid_campaign_with_invalid_token,
    test_campaign_with_empty_token as _test_invalid_campaign_with_empty_token,
    test_campaign_with_invalid_campaign_id as _test_invalid_campaign_with_invalid_campaign_id,
)
from test_invalid_complete_order import (
    test_complete_order_with_invalid_otp as _test_invalid_complete_order_with_invalid_otp,
    test_complete_order_with_empty_otp as _test_invalid_complete_order_with_empty_otp,
    test_complete_order_with_invalid_post_id as _test_invalid_complete_order_with_invalid_post_id,
)
from test_invalid_fetch_posts import (
    test_fetch_posts_with_invalid_token as _test_invalid_fetch_posts_with_invalid_token,
    test_fetch_posts_with_empty_token as _test_invalid_fetch_posts_with_empty_token,
    test_fetch_posts_with_invalid_parameters as _test_invalid_fetch_posts_with_invalid_parameters,
)

@pytest.fixture(scope="session", autouse=True)
def initialize_report():
    with open(REPORT_FILE_PATH, 'w') as report_file:
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        report_file.write(f"Rapor Başlangıcı: {start_time}\n")

def log_report(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REPORT_FILE_PATH, "a") as report_file:
        report_file.write(f"[{timestamp}] {message}\n")

@pytest.mark.order(1)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_successful_login_scenario():
    log_report("1. Successful login test starts.")
    _test_successful_login()
    log_report("1. Successful login test completed.")

@pytest.mark.order(2)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_wrong_password_login_scenario():
    log_report("2. Wrong password login test starts.")
    _test_wrong_password_login()
    log_report("2. Wrong password login test completed.")

@pytest.mark.order(3)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_empty_username_login_scenario():
    log_report("3. Empty username login test starts.")
    _test_empty_username_login()
    log_report("3. Empty username login test completed.")

@pytest.mark.order(4)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_empty_password_login_scenario():
    log_report("4. Empty password login test starts.")
    _test_empty_password_login()
    log_report("4. Empty password login test completed.")

@pytest.mark.order(5)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_empty_username_password_login_scenario():
    log_report("5. Empty username and password login test starts.")
    _test_empty_username_password_login()
    log_report("5. Empty username and password login test completed.")

@pytest.mark.order(6)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_complete_order_scenario():
    log_report("6. Complete Order scenario starts.")
    try:
        _execute_order()
        log_report("6. Complete Order scenario completed successfully.")
    except Exception as e:
        log_report(f"6. Complete Order test failed: {str(e)}")
        pytest.fail(f"6. Complete Order test failed: {str(e)}")

@pytest.mark.order(7)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_take_in_possession_scenario():
    log_report("7. Take in possession scenario starts.")
    try:
        _test_take_in_possession()
        log_report("7. Take in possession scenario completed successfully.")
    except Exception as e:
        log_report(f"7. Take in possession test failed: {str(e)}")
        pytest.fail(f"7. Take in possession test failed: {str(e)}")

@pytest.mark.order(8)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_deliver_with_new_otp_scenario():
    log_report("8. Deliver with new OTP scenario starts.")
    try:
        _test_deliver_with_new_otp()
        log_report("8. Deliver with new OTP scenario completed successfully.")
    except Exception as e:
        log_report(f"8. Deliver with new OTP test failed: {str(e)}")
        pytest.fail(f"8. Deliver with new OTP test failed: {str(e)}")

@pytest.mark.order(9)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_return_scenario():
    log_report("9. Return scenario starts.")
    try:
        _test_return_scenario()
        log_report("9. Return scenario completed successfully.")
    except Exception as e:
        log_report(f"9. Return test failed: {str(e)}")
        pytest.fail(f"9. Return test failed: {str(e)}")

@pytest.mark.order(10)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_campaign_scenario():
    log_report("10. Campaign scenario starts.")
    try:
        _test_campaign_scenario()
        log_report("10. Campaign scenario completed successfully.")
    except Exception as e:
        log_report(f"10. Campaign test failed: {str(e)}")
        pytest.fail(f"10. Campaign test failed: {str(e)}")

@pytest.mark.order(11)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_shipment_history_scenario():
    log_report("11. Shipment History scenario starts.")
    try:
        _test_shipment_history_scenario()
        log_report("11. Shipment History scenario completed successfully.")
    except Exception as e:
        log_report(f"11. Shipment History test failed: {str(e)}")
        pytest.fail(f"11. Shipment History test failed: {str(e)}")

@pytest.mark.order(12)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_update_profile_scenario():
    log_report("12. Update Profile scenario starts.")
    try:
        _test_update_profile_scenario()
        log_report("12. Update Profile scenario completed successfully.")
    except Exception as e:
        log_report(f"12. Update Profile test failed: {str(e)}")
        pytest.fail(f"12. Update Profile test failed: {str(e)}")

@pytest.mark.order(13)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_view_profile_scenario():
    log_report("13. View Profile scenario starts.")
    try:
        _test_user_profile_scenario()
        log_report("13. View Profile scenario completed successfully.")
    except Exception as e:
        log_report(f"13. View Profile test failed: {str(e)}")
        pytest.fail(f"13. View Profile test failed: {str(e)}")

@pytest.mark.order(14)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_technical_support_scenario():
    log_report("14. Technical Support scenario starts.")
    try:
        _test_technical_support_scenario()
        log_report("14. Technical Support scenario completed successfully.")
    except Exception as e:
        log_report(f"14. Technical Support test failed: {str(e)}")
        pytest.fail(f"14. Technical Support test failed: {str(e)}")

@pytest.mark.order(15)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_fetch_posts_scenario():
    log_report("15. Fetch Posts scenario starts.")
    try:
        _test_fetch_posts_scenario()
        log_report("15. Fetch Posts scenario completed successfully.")
    except Exception as e:
        log_report(f"15. Fetch Posts test failed: {str(e)}")
        pytest.fail(f"15. Fetch Posts test failed: {str(e)}")

@pytest.mark.order(16)
@allure.tag('positive')
@allure.label('category', 'Positive Tests')
def test_get_posts_scenario():
    log_report("16. Get Posts with takenName scenario starts.")
    try:
        _test_get_posts_scenario()
        log_report("16. Get Posts with takenName scenario completed successfully.")
    except Exception as e:
        log_report(f"16. Get Posts with takenName test failed: {str(e)}")
        pytest.fail(f"16. Get Posts with takenName test failed: {str(e)}")


# Negative tests

@pytest.mark.order(17)
@allure.tag('negative')
@allure.label('category', 'Negative Tests')
def test_invalid_campaign_with_invalid_token_scenario():
    log_report("17. Invalid Campaign with Invalid Token scenario starts.")
    try:
        _test_invalid_campaign_with_invalid_token()
        log_report("17. Invalid Campaign with Invalid Token scenario completed.")
    except Exception as e:
        log_report(f"17. Invalid Campaign with Invalid Token test failed: {str(e)}")
        pytest.fail(f"17. Invalid Campaign with Invalid Token test failed: {str(e)}")

@pytest.mark.order(18)
@allure.tag('negative')
@allure.label('category', 'Negative Tests')
def test_invalid_campaign_with_empty_token_scenario():
    log_report("18. Invalid Campaign with Empty Token scenario starts.")
    try:
        _test_invalid_campaign_with_empty_token()
        log_report("18. Invalid Campaign with Empty Token scenario completed.")
    except Exception as e:
        log_report(f"18. Invalid Campaign with Empty Token test failed: {str(e)}")
        pytest.fail(f"18. Invalid Campaign with Empty Token test failed: {str(e)}")

@pytest.mark.order(19)
@allure.tag('negative')
@allure.label('category', 'Negative Tests')
def test_invalid_campaign_with_invalid_campaign_id_scenario():
    log_report("19. Invalid Campaign with Invalid Campaign ID scenario starts.")
    try:
        _test_invalid_campaign_with_invalid_campaign_id()
        log_report("19. Invalid Campaign with Invalid Campaign ID scenario completed.")
    except Exception as e:
        log_report(f"19. Invalid Campaign with Invalid Campaign ID test failed: {str(e)}")
        pytest.fail(f"19. Invalid Campaign with Invalid Campaign ID test failed: {str(e)}")

@pytest.mark.order(20)
@allure.tag('negative')
@allure.label('category', 'Negative Tests')
def test_invalid_complete_order_with_invalid_otp_scenario():
    log_report("20. Invalid Complete Order with Invalid OTP scenario starts.")
    try:
        _test_invalid_complete_order_with_invalid_otp()
        log_report("20. Invalid Complete Order with Invalid OTP scenario completed.")
    except Exception as e:
        log_report(f"20. Invalid Complete Order with Invalid OTP test failed: {str(e)}")
        pytest.fail(f"20. Invalid Complete Order with Invalid OTP test failed: {str(e)}")

@pytest.mark.order(21)
@allure.tag('negative')
@allure.label('category', 'Negative Tests')
def test_invalid_complete_order_with_empty_otp_scenario():
    log_report("21. Invalid Complete Order with Empty OTP scenario starts.")
    try:
        _test_invalid_complete_order_with_empty_otp()
        log_report("21. Invalid Complete Order with Empty OTP scenario completed.")
    except Exception as e:
        log_report(f"21. Invalid Complete Order with Empty OTP test failed: {str(e)}")
        pytest.fail(f"21. Invalid Complete Order with Empty OTP test failed: {str(e)}")

@pytest.mark.order(22)
@allure.tag('negative')
@allure.label('category', 'Negative Tests')
def test_invalid_complete_order_with_invalid_post_id_scenario():
    log_report("22. Invalid Complete Order with Invalid Post ID scenario starts.")
    try:
        _test_invalid_complete_order_with_invalid_post_id()
        log_report("22. Invalid Complete Order with Invalid Post ID scenario completed.")
    except Exception as e:
        log_report(f"22. Invalid Complete Order with Invalid Post ID test failed: {str(e)}")
        pytest.fail(f"22. Invalid Complete Order with Invalid Post ID test failed: {str(e)}")

@pytest.mark.order(23)
@allure.tag('negative')
@allure.label('category', 'Negative Tests')
def test_invalid_fetch_posts_with_invalid_token_scenario():
    log_report("23. Invalid Fetch Posts with Invalid Token scenario starts.")
    try:
        _test_invalid_fetch_posts_with_invalid_token()
        log_report("23. Invalid Fetch Posts with Invalid Token scenario completed.")
    except Exception as e:
        log_report(f"23. Invalid Fetch Posts with Invalid Token test failed: {str(e)}")
        pytest.fail(f"23. Invalid Fetch Posts with Invalid Token test failed: {str(e)}")

@pytest.mark.order(24)
@allure.tag('negative')
@allure.label('category', 'Negative Tests')
def test_invalid_fetch_posts_with_empty_token_scenario():
    log_report("24. Invalid Fetch Posts with Empty Token scenario starts.")
    try:
        _test_invalid_fetch_posts_with_empty_token()
        log_report("24. Invalid Fetch Posts with Empty Token scenario completed.")
    except Exception as e:
        log_report(f"24. Invalid Fetch Posts with Empty Token test failed: {str(e)}")
        pytest.fail(f"24. Invalid Fetch Posts with Empty Token test failed: {str(e)}")

@pytest.mark.order(25)
@allure.tag('negative')
@allure.label('category', 'Negative Tests')
def test_invalid_fetch_posts_with_invalid_parameters_scenario():
    log_report("25. Invalid Fetch Posts with Invalid Parameters scenario starts.")
    try:
        _test_invalid_fetch_posts_with_invalid_parameters()
        log_report("25. Invalid Fetch Posts with Invalid Parameters scenario completed.")
    except Exception as e:
        log_report(f"25. Invalid Fetch Posts with Invalid Parameters test failed: {str(e)}")
        pytest.fail(f"25. Invalid Fetch Posts with Invalid Parameters test failed: {str(e)}")
