pipelipipeline {
    agent any
    
    environment {
        IMAGE_NAME = "mlops-api"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Dang lay code tu GitHub...'
                // Jenkins tu dong lam buoc nay
            }
        }
        
        stage('Build Image') {
            steps {
                script {
                    echo 'Dang build Docker...'
                    sh 'docker compose build'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    echo 'Dang Deploy...'
                    // Start container
                    sh 'docker compose down || true'
                    sh 'docker compose up -d'
                }
            }
        }
        
        stage('Unit Test') {
            steps {
                script {
                    echo 'Chay Unit Test (Pytest)...'
                    // Đợi 5s cho container ổn định
                    sleep 5
                    // Chạy lệnh pytest bên trong container đang chạy
                    sh 'docker compose exec -T api pytest'
                }
            }
        }

        stage('Integration Test') {
            steps {
                script {
                    echo 'Kiem tra ket noi (Curl)...'
                    // Test xem web có sống không
                    sh 'curl -f http://localhost:8000 || exit 1'
                }
            }
        }
    }
}ne {
    agent any
    environment {
        IMAGE_NAME = "mlops-api"
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Dang lay code tu GitHub...'
                // Jenkins tu dong lam buoc nay
            }
        }
        stage('Build Image') {
            steps {
                script {
                    echo 'Dang build Docker...'
                    sh 'docker compose build'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    echo 'Dang Deploy...'
                    sh 'docker compose down || true'
                    sh 'docker compose up -d'
                }
            }
      
