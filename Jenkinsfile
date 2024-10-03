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
                script {
                    def branchName = '${env.BRANCH_NAME}'
                    def buildNumber = '${env.BUILD_NUMBER}'
                    println('BUILD NUMBER : ${buildNumber}')
                    deploy(branchName)
                }
            }
        }
    }
}

def void deploy(String branchName) {
    println(branchName)
}