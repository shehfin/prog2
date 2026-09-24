pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-credentials',
                    url: 'https://github.com/shehfin/prog2.git'
            }
        }

        stage('Generate Report') {
            steps {
                bat 'echo BUILD_NUMBER=%BUILD_NUMBER%'
                bat 'echo JOB_NAME=%JOB_NAME%'
                bat 'echo WORKSPACE=%WORKSPACE%'
                bat 'python app.py'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'build_report.txt',
                                 fingerprint: true
            }
        }
    }
}