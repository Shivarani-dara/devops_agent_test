pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest tests/test_app.py'
            }
        }

       stage('Docker Build & Run') {
            steps {
                sh 'docker build -t devops-agent-test .'
                sh 'docker run --rm devops-agent-test'
            }
       }
    }
}
