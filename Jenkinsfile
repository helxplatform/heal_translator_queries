pipeline {
    agent {
        kubernetes {
            cloud 'kubernetes'
            label 'agent-docker'
            defaultContainer 'agent-docker'
        }
    }
    stages {
        stage('Install') {
            steps {
                sh '''
                make install
                '''
            }
        }
        stage('Run') {
            steps {
                sh '''
                make run
                '''
            }
        }
        stage('Publish') {
            environment {
            }
            steps {
                sh '''
                echo "need to add git push of the output and notebook"
                '''
            }
        }
    }
}