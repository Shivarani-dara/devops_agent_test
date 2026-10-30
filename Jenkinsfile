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

    post {
        failure {
            withCredentials([
                string(
                    credentialsId: 'jenkins-failure-token',
                    variable: 'JENKINS_FAILURE_TOKEN'
                )
            ]) {
                sh '''
                    set +x
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                    curl --fail --silent --show-error \
                        --connect-timeout 20 \
                        --max-time 40 \
                        -X POST \
                        "http://127.0.0.1:5000/jenkins-failure" \
                        -H "Content-Type: application/json" \
                        -H "X-Jenkins-Token: $JENKINS_FAILURE_TOKEN" \
                        --data "{\\"job_name\\":\\"$JOB_NAME\\",\\"build_number\\":$BUILD_NUMBER}" \
                    || echo "WARNING: Could not notify the repair agent."
                '''
            }
        }
    }
}
