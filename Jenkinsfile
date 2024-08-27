pipeline {
    agent any

    triggers {
        cron('*/5 * * * *')  // Pipeline'ı her saat çalıştırmak için
    }

   stages {
        stage('Clone Repository') {
            steps {
                // Depoyu klonla
                git 'https://github.com/ugurakyay/Easy_Point_Test'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Sanal ortam oluştur ve bağımlılıkları yükle
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Testleri çalıştır ve Allure raporu oluştur
                sh '. .venv/bin/activate && pytest --alluredir=allure-results --junitxml=report.xml'
            }
        }
    }

    post {
        always {
            // Test sonuçlarını göster
            junit 'report.xml'

            // Allure raporlarını yayınla
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]

            // Test raporunu oku ve HTML formatına dönüştür
            script {
                def testReport = readFile('report.xml')
                def emailBody = parseTestReport(testReport)

                // E-posta gönder
                mail to: 'ugurakyay@gmail.com',
                     subject: "Jenkins Build ${currentBuild.fullDisplayName}",
                     mimeType: 'text/html',
                     body: emailBody
            }
        }
    }
}

// HTML formatında e-posta içeriği oluşturma işlevi
def parseTestReport(String xmlReport) {
    def xml = new XmlParser().parseText(xmlReport)
    def tests = xml.testsuite.testcase
    def passedTests = tests.findAll { !it.failure && !it.error && !it.skipped }
    def failedTests = tests.findAll { it.failure || it.error }
    def skippedTests = tests.findAll { it.skipped }

    def summary = """
    <h2>Test Report Summary</h2>
    <p><strong>Total Tests:</strong> ${tests.size()}</p>
    <p><strong>Passed:</strong> ${passedTests.size()}</p>
    <p><strong>Failed:</strong> ${failedTests.size()}</p>
    <p><strong>Skipped:</strong> ${skippedTests.size()}</p>
    <h3>Failed Tests:</h3>
    <ul>
    """

    failedTests.each { test ->
        summary += "<li>${test.@classname} - ${test.@name}</li>"
    }

    summary += "</ul>"

    return """
    <html>
    <body>
        <h1>Jenkins Build Status: ${currentBuild.currentResult}</h1>
        ${summary}
        <p>For more details, please check the Jenkins console output.</p>
    </body>
    </html>
    """
}
