pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Depoyu klonla
                git 'https://github.com/ugurakyay/EasyPointApiAutomation.git'
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
                // Testleri çalıştır ve HTML raporu ile birlikte XML raporu oluştur
                sh '. .venv/bin/activate && pytest --html=report.html --self-contained-html --junitxml=report.xml'
            }
        }
    }

    post {
        always {
            // Test raporlarını arşivle
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true

            // Test sonuçlarını göster
            junit 'report.xml'
        }
    }
}
