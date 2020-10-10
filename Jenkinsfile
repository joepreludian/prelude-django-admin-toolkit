pipeline {
    agent any 
    stages {
        stage('Build Gulp') { 
            agent {
                docker {
                    image 'node:latest'
                    //args  '-v /tmp:/tmp'
                }
            }
            steps {
                sh 'npm install --dev'
                sh 'ls -lah'
                sh 'gulp build_production'
            }
        }
        stage('Test') { 
            steps {
                sh 'ls -lh'
            }
        }
        stage('Deploy') { 
            steps {
                sh 'ls -lh'
            }
        }
    }
}
