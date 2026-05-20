pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Shruti-Asgekar/placement_prediction_project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Training') {
            steps {
                bat 'python train_model.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t placement-app .'
            }
        }

    }
}