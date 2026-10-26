echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
pipeline {
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
    agent any
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"

echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
    stages {
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
        stage('Install Dependencies') {
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
            steps {
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                sh 'python3 -m pip install -r requirements.txt'
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
            }
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
        }
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"

echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
        stage('Run Tests') {
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
            steps {
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                sh 'python3 -m pytest tests/test_app.py'
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
            }
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
        }
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"

echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
        stage('Docker Build & Run') {
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
            steps {
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                sh 'docker build -t devops-agent-test .'
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                sh 'docker run --rm devops-agent-test'
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
            }
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
        }
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
    }
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"

echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
    post {
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
        failure {
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
            withCredentials([
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                string(
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                    credentialsId: 'jenkins-failure-token',
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                    variable: 'JENKINS_FAILURE_TOKEN'
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                )
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
            ]) {
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                sh '''
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                    set +x
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                    curl --fail --silent --show-error \
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                        --connect-timeout 20 \
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                        --max-time 40 \
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                        -X POST \
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                        "https://surgeons-lamb-medium-fda.trycloudflare.com/jenkins-failure" \
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                        -H "Content-Type: application/json" \
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                        -H "X-Jenkins-Token: $JENKINS_FAILURE_TOKEN" \
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                        --data "{\"job_name\":\"$JOB_NAME\",\"build_number\":$BUILD_NUMBER}" \
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                    || echo "WARNING: Could not notify the repair agent."
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
                '''
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
            }
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
        }
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
    }
echo "JOB_NAME=[$JOB_NAME] BUILD_NUMBER=[$BUILD_NUMBER]"
}
