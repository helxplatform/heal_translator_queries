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
                GITHUB_CREDS = credentials('rencibuild_dockerhub_machine_user')
            }
            steps {
                sh '''
                git config user.name $GITHUB_CREDS_USR
                git config user.email $GITHUB_CREDS_USR
                git checkout main
                git add viewer.ipynb tranql_output/*
                git commit -m 'Jenkins run output for build  #${env.BUILD_NUMBER}'
                git push https://$GITHUB_CREDS_USR:$GITHUB_CREDS_PSW@github.com/helxplatform/heal_translator_queries.git
            }
        }
    }
}