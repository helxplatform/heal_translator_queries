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
                    def encodedPassword = URLEncoder.encode("${env.GITHUB_CREDS_PSW}",'UTF-8')
                    sh "git config user.name ${env.GITHUB_CREDS_USR}"
                    sh "git add viewer.ipynb tranql_output/*"
                    sh "git commit -m 'Jenkins run output: ${env.BUILD_NUMBER}'"
                    sh "git push https://${env.GITHUB_CREDS_USR}:${encodedPassword}github.com/helxplatform/heal_translator_queries.git"
                    }
                }
            }
        }
    }
}