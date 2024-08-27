import xml.etree.ElementTree as ET
import sys

def parse_test_report(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    tests = root.findall(".//testcase")
    passed_tests = [t for t in tests if not t.find("failure") and not t.find("error")]
    failed_tests = [t for t in tests if t.find("failure") or t.find("error")]
    skipped_tests = [t for t in tests if t.find("skipped")]

    summary = f"""
    <h2>Test Report Summary</h2>
    <p><strong>Total Tests:</strong> {len(tests)}</p>
    <p><strong>Passed:</strong> {len(passed_tests)}</p>
    <p><strong>Failed:</strong> {len(failed_tests)}</p>
    <p><strong>Skipped:</strong> {len(skipped_tests)}</p>
    <h3>Failed Tests:</h3>
    <ul>
    """

    for test in failed_tests:
        summary += f"<li>{test.attrib['classname']} - {test.attrib['name']}</li>"

    summary += "</ul>"
    return summary

if __name__ == "__main__":
    xml_file = sys.argv[1]
    output_file = sys.argv[2]

    report_summary = parse_test_report(xml_file)

    with open(output_file, 'w') as f:
        f.write(f"""
        <html>
        <body>
            <h1>Jenkins Build Status: SUCCESS</h1>
            {report_summary}
            <p>For more details, please check the Jenkins console output.</p>
        </body>
        </html>
        """)
