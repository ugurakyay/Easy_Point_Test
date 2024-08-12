# test_.py
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
from test_return import execute_return_scenario as _test_return_scenario  # Import the return scenario

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
