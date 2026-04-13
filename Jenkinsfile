pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                cleanWs()
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run Training') {
            steps {
                sh 'python3 train.py'
            }
        }

        stage('Evaluate Model') {
            steps {
                sh 'python3 evaluate.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("radhika2193/mlops-app")
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        docker.image("radhika2193/mlops-app").push('latest')
                    }
                }
            }
        }

        stage('Print Details') {
            steps {
                echo "Name: Radhika Nambiar"
                echo "Roll No: 2022bcs0148"
            }
        }
    }
}