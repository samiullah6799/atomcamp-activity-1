pipeline {
    agent any
    stages {
        stage ('Build') {
            steps {
                echo "Building"
            }
        }

        stage ('Installation') {
            steps {
                echo "Installation"
            }
        }

        stage ('Testing') {
            steps {
                echo "Testing"
            }
        }

        stage ('Deploy') {
            steps {
                script {
                    deploy()
                }
            }
        }
    }
}

def void deploy() {
    println("Atomcamp Class is underway")
}