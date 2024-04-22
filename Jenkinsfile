pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS = credentials('docker-credentials')
    }
    stages {
        stage('Build') {
            steps {
                bat 'copy.sh'
                bat 'docker build -t uc1 ./uc1'
                bat 'docker login -u ${gautii30} -p ${sarafgautam051539} ${https://index.docker.io/v1/}'
                bat 'docker tag uc1 rhea19/uc1:latest'
                bat 'docker push rhea19/uc1:latest'
                bat 'docker build -t uc2 ./uc2'
                bat 'docker tag uc1 rhea19/uc2:latest'
                bat 'docker push rhea19/uc2:latest'
                bat 'docker build -t uc3 ./uc3'
                bat 'docker tag uc3 rhea19/uc3:latest'
                bat 'docker push rhea19/uc3:latest'
                bat 'docker build -t frontend ./frontend'
                bat 'docker tag frontend rhea19/frontend:latest'
            }
        }
        
        stage('Deploy') {
            steps {
                 bat 'kubectl apply -f kubernetes.yaml'
            }
        }
    }
    
    post {
        failure {
            echo 'Pipeline failed'
        }
    }
}


