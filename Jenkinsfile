pipeline {
    agent any
    stages {
        stage ('Building') {
            steps {
                echo "It is Building"
            }
        }

        stage ('Installation') {
            steps {
                echo "It is installing all packages"
            }
        }

        stage ('Testing') {
            steps {
                echo "It is performing automatic testing"
            }
        }

        stage ('Deploy') {
            steps {
                deploy('dev')
            }
        }
    }
}


def void deploy(String branchName) {
    println(branchName)
}