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
                    curl --fail --silent --show-error \
                        --connect-timeout 5 \
                        --max-time 15 \
                        -X POST \
                        "https://delivers-statements-driver-pork.trycloudflare.com/jenkins-failure" \
                        -H "Content-Type: application/json" \
                        -H "X-Jenkins-Token: $JENKINS_FAILURE_TOKEN" \
                        --data "{\"job_name\":\"$JOB_NAME\",\"build_number\":$BUILD_NUMBER}" \
                    || echo "WARNING: Could not notify the repair agent."
                '''
            }
        }
    }
}
