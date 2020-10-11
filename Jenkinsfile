pipeline {
    agent any
    stages {
        stage('Node Build') { 
            agent {
                docker {
                    image 'docker.io/node:alpine'
                }
            }
            steps {
                sh 'apt-get update && apt-get install tree -y && apt-get clean all'
                sh 'npm install'
                sh 'npx gulp build_production'
                sh 'tree prelude_django_admin_toolkit'
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'docker.io/joepreludian/python-poetry:latest'
                }
            }
            steps {
                sh 'poetry -V'
            }
        }
        stage('Build') {
            agent {
                docker {
                    image 'docker.io/joepreludian/python-poetry:latest'
                }
            }
            steps {
                sh 'poetry build'
                sh 'tree dist'
            }
        }
    }
}
