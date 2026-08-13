pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t swain77/my_app:${BUILD_NUMBER} .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push swain77/my_app:${BUILD_NUMBER}'
            }
        }
    }
}
