import pytest
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
from deliver_with_new_otp import deliver_with_new_otp as _test_deliver_with_new_otp
from test_return import execute_return_scenario as _test_return_scenario
from campaign import execute_campaign_scenario as _test_campaign_scenario
from test_Shipment_History import execute_shipment_history_scenario as _test_shipment_history_scenario
from test_update_profile import execute_update_profile_scenario as _test_update_profile_scenario
from test_technical_support import execute_technical_support_scenario as _test_technical_support_scenario
from test_user_profile import execute_user_profile_scenario as _test_user_profile_scenario
from test_fetch_posts import execute_fetch_posts_scenario as _test_fetch_posts_scenario  # Import the fetch posts scenario
from test_get_posts_with_taken_name import execute_get_posts_scenario as _test_get_posts_scenario

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
def test_successful_login_scenario(log_report):
    log_report("Successful login test starts.")
    _test_successful_login()
    log_report("Successful login test completed.")

@pytest.mark.order(2)
def test_wrong_password_login_scenario(log_report):
    log_report("Wrong password login test starts.")
    _test_wrong_password_login()
    log_report("Wrong password login test completed.")

@pytest.mark.order(3)
def test_empty_username_login_scenario(log_report):
    log_report("Empty username login test starts.")
    _test_empty_username_login()
    log_report("Empty username login test completed.")

@pytest.mark.order(4)
def test_empty_password_login_scenario(log_report):
    log_report("Empty password login test starts.")
    _test_empty_password_login()
    log_report("Empty password login test completed.")

@pytest.mark.order(5)
def test_empty_username_password_login_scenario(log_report):
    log_report("Empty username and password login test starts.")
    _test_empty_username_password_login()
    log_report("Empty username and password login test completed.")

@pytest.mark.order(6)
def test_complete_order_scenario(log_report):
    try:
        _execute_order()
        log_report("Complete Order scenario completed successfully.")
    except Exception as e:
        log_report(f"Complete Order test failed: {str(e)}")
        pytest.fail(f"Complete Order test failed: {str(e)}")

@pytest.mark.order(7)
def test_take_in_possession_scenario(log_report):
    try:
        _test_take_in_possession()
        log_report("Take in possession scenario completed successfully.")
    except Exception as e:
        log_report(f"Take in possession test failed: {str(e)}")
        pytest.fail(f"Take in possession test failed: {str(e)}")

@pytest.mark.order(8)
def test_deliver_with_new_otp_scenario(log_report):
    try:
        _test_deliver_with_new_otp()
        log_report("Deliver with new OTP scenario completed successfully.")
    except Exception as e:
        log_report(f"Deliver with new OTP test failed: {str(e)}")
        pytest.fail(f"Deliver with new OTP test failed: {str(e)}")

@pytest.mark.order(9)
def test_return_scenario(log_report):
    try:
        _test_return_scenario()
        log_report("Return scenario completed successfully.")
    except Exception as e:
        log_report(f"Return test failed: {str(e)}")
        pytest.fail(f"Return test failed: {str(e)}")

@pytest.mark.order(10)
def test_campaign_scenario(log_report):
    try:
        _test_campaign_scenario()
        log_report("Campaign scenario completed successfully.")
    except Exception as e:
        log_report(f"Campaign test failed: {str(e)}")
        pytest.fail(f"Campaign test failed: {str(e)}")

@pytest.mark.order(11)
def test_shipment_history_scenario(log_report):
    try:
        _test_shipment_history_scenario()
        log_report("Shipment History scenario completed successfully.")
    except Exception as e:
        log_report(f"Shipment History test failed: {str(e)}")
        pytest.fail(f"Shipment History test failed: {str(e)}")

@pytest.mark.order(12)
def test_update_profile_scenario(log_report):
    try:
        _test_update_profile_scenario()
        log_report("Update Profile scenario completed successfully.")
    except Exception as e:
        log_report(f"Update Profile test failed: {str(e)}")
        pytest.fail(f"Update Profile test failed: {str(e)}")

@pytest.mark.order(13)
def test_view_profile_scenario(log_report):
    try:
        _test_user_profile_scenario()
        log_report("View Profile scenario completed successfully.")
    except Exception as e:
        log_report(f"View Profile test failed: {str(e)}")
        pytest.fail(f"View Profile test failed: {str(e)}")

@pytest.mark.order(14)
def test_technical_support_scenario(log_report):
    try:
        _test_technical_support_scenario()
        log_report("Technical Support scenario completed successfully.")
    except Exception as e:
        log_report(f"Technical Support test failed: {str(e)}")
        pytest.fail(f"Technical Support test failed: {str(e)}")

@pytest.mark.order(15)
def test_fetch_posts_scenario(log_report):
    try:
        _test_fetch_posts_scenario()
        log_report("Fetch Posts scenario completed successfully.")
    except Exception as e:
        log_report(f"Fetch Posts test failed: {str(e)}")
        pytest.fail(f"Fetch Posts test failed: {str(e)}")

@pytest.mark.order(16)
def test_get_posts_scenario(log_report):
    try:
        _test_get_posts_scenario()
        log_report("Get Posts with takenName scenario completed successfully.")
    except Exception as e:
        log_report(f"Get Posts with takenName test failed: {str(e)}")
        pytest.fail(f"Get Posts with takenName test failed: {str(e)}")