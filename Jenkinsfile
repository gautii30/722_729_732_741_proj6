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
                
                
                
                // Build and push uc1
                sh 'docker build -t gautii30/uc1:latest ./uc1'
                sh 'docker push gautii30/uc1:latest'
                
                // Build and push uc2
                sh 'docker build -t gautii30/uc2:latest ./uc2'
                sh 'docker push gautii30/uc2:latest'
                
                // Build and push uc3
                sh 'docker build -t gautii30/uc3:latest ./uc3'
                sh 'docker push gautii30/uc3:latest'
                
                // Build and push frontend
                sh 'docker build -t gautii30/frontend:latest ./frontend'
                sh 'docker push gautii30/frontend:latest'
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
