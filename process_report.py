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

    tests = root.findall(".//testcase")
    passed_tests = [t for t in tests if not t.find("failure") and not t.find("error")]
    failed_tests = [t for t in tests if t.find("failure") or t.find("error")]
    skipped_tests = [t for t in tests if t.find("skipped")]

    total_tests = len(tests)
    passed_count = len(passed_tests)
    failed_count = len(failed_tests)
    skipped_count = len(skipped_tests)

    return total_tests, passed_count, failed_count, skipped_count, failed_tests


def generate_html_report(total_tests, passed_count, failed_count, skipped_count, failed_tests, jenkins_url,
                         build_number):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # HTML ve CSS ayarlarınız burada yer almalı...
    # HTML içeriğinizi burada oluşturduğunuzdan emin olun...
    return html_content


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Kullanım: python script.py [input.xml] [output.html]")
        sys.exit(1)

    xml_file = sys.argv[1]
    output_file = sys.argv[2]

    # Jenkins yapı numarası
    build_number = os.environ.get('BUILD_NUMBER', 'bilinmeyen')

    try:
        total_tests, passed_count, failed_count, skipped_count, failed_tests = parse_test_report(xml_file)
        report_html = generate_html_report(total_tests, passed_count, failed_count, skipped_count, failed_tests,
                                           JENKINS_BASE_URL, build_number)

        with open(output_file, 'w') as f:
            f.write(report_html)
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        sys.exit(1)
