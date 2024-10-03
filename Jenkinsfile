pipeline {
    agent any
    stages {
        stage ('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/dev']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/samiullah6799/atomcamp-activity-1.git/']])
            }
        }

        stage ('Build') {
            steps {
               sh 'pip3 install -r requirements.txt'
            }
        }

        stage ('Testing') {
            steps {
                sh 'python3 test.py'
            }
        }

        stage ('Deploy') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
    }
}

def void deploy(String branchName) {
    println(branchName)
}