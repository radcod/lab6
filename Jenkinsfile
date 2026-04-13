pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("your-dockerhub-username/mlops-app")
                }
            }
        }

        stage('Run Training') {
            steps {
                sh 'python train.py'
            }
        }

        stage('Evaluate Model') {
            steps {
                sh 'python evaluate.py'
            }
        }

        stage('Print Details') {
            steps {
                echo "Name: YOUR NAME"
                echo "Roll No: YOUR ROLL NO"
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        docker.image("your-dockerhub-username/mlops-app").push('latest')
                    }
                }
            }
        }
    }
}