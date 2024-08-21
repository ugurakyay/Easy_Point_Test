pipeline {
    agent any

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
                sh '. .venv/bin/activate && pip install allure-pytest'  // Allure-Pytest kütüphanesini yükle
            }
        }
        stage('Run Tests') {
            steps {
                // Testleri çalıştır ve Allure raporunu oluştur
                sh '. .venv/bin/activate && pytest --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            // Test sonuçlarını göster
            junit 'allure-results/*.xml'

            // Allure raporlarını arşivle
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
