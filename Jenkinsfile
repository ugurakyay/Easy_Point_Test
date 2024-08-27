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

            // Test raporunu oku
            script {
                def testReport = readFile('report.xml')
                def emailBody = """
                    Jenkins build status: ${currentBuild.currentResult}

                    Test Report Summary:

                    ${testReport}

                    For more details, please check the Jenkins console output.
                """
                // E-posta gönder
                mail to: 'ugurakyay@gmail.com',
                     subject: "Jenkins Build ${currentBuild.fullDisplayName}",
                     body: emailBody
            }
        }
    }
}
