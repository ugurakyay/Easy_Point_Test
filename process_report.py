import xml.etree.ElementTree as ET
import sys
from datetime import datetime

def parse_test_report(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    tests = root.findall(".//testcase")
    passed_tests = [t for t in tests if not t.find("failure") and not t.find("error")]
    failed_tests = [t for t in tests if t.find("failure") or t.find("error")]
    skipped_tests = [t for t in tests if t.find("skipped")]

    total_tests = len(tests)
    passed_count = len(passed_tests)
    failed_count = len(failed_tests)
    skipped_count = len(skipped_tests)

    return total_tests, passed_count, failed_count, skipped_count, failed_tests

def generate_html_report(total_tests, passed_count, failed_count, skipped_count, failed_tests):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            h1 {{
                color: #4CAF50;
            }}
            .summary {{
                margin-bottom: 20px;
            }}
            .bar-container {{
                width: 100%;
                background-color: #f3f3f3;
                border-radius: 25px;
            }}
            .bar {{
                text-align: center;
                padding: 10px;
                color: white;
                border-radius: 25px;
            }}
            .passed {{
                width: {passed_count / total_tests * 100}%;
                background-color: #4CAF50;
            }}
            .failed {{
                width: {failed_count / total_tests * 100}%;
                background-color: #f44336;
            }}
            .skipped {{
                width: {skipped_count / total_tests * 100}%;
                background-color: #ff9800;
            }}
            .failed-tests {{
                color: #f44336;
            }}
            .timestamp {{
                font-size: 12px;
                color: #888;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <h1>Jenkins Build Status: SUCCESS</h1>
        <div class="summary">
            <p><strong>Total Tests:</strong> {total_tests}</p>
            <p><strong>Passed:</strong> {passed_count}</p>
            <p><strong>Failed:</strong> {failed_count}</p>
            <p><strong>Skipped:</strong> {skipped_count}</p>
        </div>
        <div class="bar-container">
            <div class="bar passed">Passed: {passed_count}</div>
        </div>
        <div class="bar-container">
            <div class="bar failed">Failed: {failed_count}</div>
        </div>
        <div class="bar-container">
            <div class="bar skipped">Skipped: {skipped_count}</div>
        </div>
        <div class="failed-tests">
            <h2>Failed Tests:</h2>
            <ul>
    """

    for test in failed_tests:
        html_content += f"<li>{test.attrib['classname']} - {test.attrib['name']}</li>"

    html_content += """
            </ul>
        </div>
        <p class="timestamp">Report generated on: {current_time}</p>
        <p>For more details, please check the Jenkins console output.</p>
    </body>
    </html>
    """

    return html_content

if __name__ == "__main__":
    xml_file = sys.argv[1]
    output_file = sys.argv[2]

    total_tests, passed_count, failed_count, skipped_count, failed_tests = parse_test_report(xml_file)

    report_html = generate_html_report(total_tests, passed_count, failed_count, skipped_count, failed_tests)

    with open(output_file, 'w') as f:
        f.write(report_html)
