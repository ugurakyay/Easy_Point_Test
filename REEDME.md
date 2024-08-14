# API Test Automation Project

This project contains a set of automated API tests for a system that includes user authentication, post management, and return processes. The tests are written in Python using `pytest` and `requests`, and they include scenarios for logging in, completing orders, handling returns, and more.

## Project Structure

- **config.py**: Contains configuration settings like API URLs, credentials, and the path to the report file.
- **conftest.py**: Defines fixtures and global setup/teardown logic for the tests, including report initialization.
- **test_successful_login.py**: Contains the test for a successful login scenario.
- **test_wrong_password_login.py**: Contains the test for login with a wrong password.
- **test_empty_username_login.py**: Contains the test for login with an empty username.
- **test_empty_password_login.py**: Contains the test for login with an empty password.
- **test_empty_username_password_login.py**: Contains the test for login with both username and password empty.
- **test_complete_order.py**: Contains the test for completing an order.
- **test_take_in_possession.py**: Contains the test for taking an item into possession.
- **deliver_with_new_otp.py**: Contains the test for delivering an item with a new OTP.
- **test_return.py**: Contains the test for handling return scenarios.
- **test_.py**: The main test runner that aggregates all the individual test scenarios and generates the `report.html`.

## Prerequisites

- Python 3.9+
- `pip` (Python package installer)

### Python Packages

- `requests`: For making HTTP requests.
- `pytest`: For running the tests.
- `pytest-html`: For generating HTML test reports.
- `pytest-order`: For ordering the test execution.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repository/api-automation.git
   cd api-automation


Create a virtual environment:
python3 -m venv .venv
source .venv/bin/activate


Install the required packages:
pip install -r requirements.txt


Running the Tests
pytest


Run a specific test

pytest -k test_successful_login


Test Scenarios
The project covers the following scenarios:

Successful Login: Tests a successful login with valid credentials.
Login with Wrong Password: Tests login with an incorrect password.
Login with Empty Username: Tests login with an empty username field.
Login with Empty Password: Tests login with an empty password field.
Login with Both Username and Password Empty: Tests login with both fields empty.
Complete Order: Logs in, fetches posts, and completes an order using a specific post ID and OTP.
Take in Possession: Simulates taking an item into possession.
Deliver with New OTP: Tests the delivery process with a newly generated OTP.
Return Process: Logs in, fetches a post with a return status, and completes the return process.




### Explanation

- **Installation**: Provides steps to set up the project and install dependencies.
- **Test Scenarios**: Describes each test scenario briefly.
- **Running the Tests**: Explains how to execute tests and generate reports.
- **Project Structure**: Outlines the structure of the project, making it easier for contributors or users to understand.
- **Contribution Guidelines**: Encourages contributions and provides guidelines.

You can customize this `README.md` further to match your project's specific needs.

