pipeline {
    agent any
    stages {
        stage ('Building') {
            steps {
                echo "It is Building"
            }
        }

        stages('Installation') {
            steps {
                echo "It is installing all packages"
            }
        }

        stages('Testing') {
            steps {
                echo "It is performing automatic testing"
            }
        }

        stages('Deploy') {
            steps {
                echo "It is deploying your system"
            }
        }
    }
}