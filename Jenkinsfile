pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
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