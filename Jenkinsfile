pipeline {
    agent any
    environment {
        // Assuming 'docker-credentials' is the ID of your credentials in Jenkins
        DOCKER_HUB_CREDS = credentials('docker-credentials')
    }
    stages {
        stage('Build and Push Docker Images') {
            steps {
                // Assuming 'copy.sh' is a shell script that needs to be executed
                sh './copy.sh'
                
                // Log in to Docker Hub
                withCredentials([usernamePassword(credentialsId: DOCKER_HUB_CREDS, usernameVariable: 'DOCKER_HUB_USER', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                    sh 'echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USER --password-stdin'
                }
                
                // Build and push uc1
                sh 'docker build -t rhea19/uc1:latest ./uc1'
                sh 'docker push rhea19/uc1:latest'
                
                // Build and push uc2
                sh 'docker build -t rhea19/uc2:latest ./uc2'
                sh 'docker push rhea19/uc2:latest'
                
                // Build and push uc3
                sh 'docker build -t rhea19/uc3:latest ./uc3'
                sh 'docker push rhea19/uc3:latest'
                
                // Build and push frontend
                sh 'docker build -t rhea19/frontend:latest ./frontend'
                sh 'docker push rhea19/frontend:latest'
            }
        }
        
        stage('Deploy') {
            steps {
                // Apply Kubernetes configurations
                sh 'kubectl apply -f kubernetes.yaml'
            }
        }
    }
    
    post {
        failure {
            echo 'Pipeline failed'
        }
    }
}
