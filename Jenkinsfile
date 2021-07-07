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
                script {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    def encodedPassword = URLEncoder.encode("$GITHUB_CREDS_PSW",'UTF-8')
                    sh "git config user.name $GITHUB_CREDS_USR"
                    sh "git config user.email $GITHUB_CREDS_USR"
                    sh "git checkout main"
                    sh "git add viewer.ipynb tranql_output/*"
                    sh "git commit -m 'Jenkins run output for build  #${env.BUILD_NUMBER}'"
                    sh "git push https://$GITHUB_CREDS_USR:$e$GITHUB_CREDS_PSW@github.com/helxplatform/heal_translator_queries.git"
                    }
                }
            }
        }
    }
}