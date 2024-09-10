import pytest
from datetime import datetime

# Rapor dosyası yolu
REPORT_FILE_PATH = "report.txt"

@pytest.fixture(scope="session", autouse=True)
def reset_report():
    # Rapor dosyasını sıfırla
    with open(REPORT_FILE_PATH, "w") as report_file:
        report_file.write(f"Rapor Başlangıcı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

@pytest.fixture
def log_report():
    def _log_report(message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(REPORT_FILE_PATH, "a") as report_file:
            report_file.write(f"[{timestamp}] {message}\n")
    return _log_report

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        if call.excinfo is not None and call.excinfo.typename == "Timeout":
            item.user_properties.append(("category", "Timeout"))
            allure.attach(f"Test failed due to timeout after {item.config.getini('timeout')} seconds", name="Timeout", attachment_type=allure.attachment_type.TEXT)
        elif call.excinfo is None:
            item.user_properties.append(("category", "Passed"))
        else:
            item.user_properties.append(("category", "Failed"))
