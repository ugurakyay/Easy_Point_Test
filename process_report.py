import xml.etree.ElementTree as ET
import sys
from datetime import datetime
import os
from config import JENKINS_BASE_URL


def parse_test_report(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"XML ayrıştırma hatası: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("XML dosyası bulunamadı.")
        sys.exit(1)

    # Tüm testleri topla
    tests = root.findall(".//testcase")

    # Geçen testler: 'failure', 'error' veya 'skipped' tag'leri olmayanlar
    passed_tests = [t for t in tests if t.find("failure") is None and t.find("error") is None and t.find("skipped") is None]

    # Başarısız testler: 'failure' veya 'error' tag'i olanlar
    failed_tests = [t for t in tests if t.find("failure") is not None or t.find("error") is not None]

    # Atlanan testler: 'skipped' tag'i olanlar
    skipped_tests = [t for t in tests if t.find("skipped") is not None]

    total_tests = len(tests)
    passed_count = len(passed_tests)
    failed_count = len(failed_tests)
    skipped_count = len(skipped_tests)

    return total_tests, passed_count, failed_count, skipped_count, failed_tests


def generate_html_report(total_tests, passed_count, failed_count, skipped_count, failed_tests, jenkins_url,
                         build_number):
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
        <h1>Jenkins Build Status: {"SUCCESS" if failed_count == 0 else "FAILURE"}</h1>
        <div class="summary">
            <p><strong>Total Tests:</strong> {total_tests}</p>
            <p><strong>Passed:</strong> {passed_count}</p>
            <p><strong>Failed:</strong> {failed_count}</p>
            <p><strong>Skipped:</strong> {skipped_count}</p>
        </div>
    """

    # Eğer başarısız testler varsa bunları listele
    if failed_tests:
        html_content += """
        <div class="failed-tests">
            <h2>Failed Tests:</h2>
            <ul>
        """
        for test in failed_tests:
            html_content += f"<li>{test.attrib['classname']} - {test.attrib['name']}</li>"
        html_content += """
            </ul>
        </div>
        """

    html_content += f"""
        <p class="timestamp">Report generated on: {current_time}</p>
        <p>For more details, please check the Jenkins console output.</p>
        <p><a href="{jenkins_url}/{build_number}/">View Jenkins Build Details</a></p>
    </body>
    </html>
    """

    return html_content
