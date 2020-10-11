pipeline {
    agent any
    stages {
        stage('Node Build') { 
            agent {
                docker {
                    image 'docker.io/node:latest'
                }
            }
            steps {
                sh 'apt-get update && apt-get install tree -y && apt-get clean all'
                sh 'npm install'
                sh 'npx gulp build_production'
                sh 'tree prelude_django_admin_toolkit'
                stash name: 'build', includes: 'prelude_django_admin_toolkit/**/*'
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'docker.io/joepreludian/python-poetry:latest'
                }
            }
            steps {
                unstash name: 'build'
                dir('testproject') {
                    sh 'apk add build-base gcc cmake linux-headers gcc libffi-dev libressl-dev'
                    sh 'poetry install'
                    sh 'poetry run python manage.py check'
                }
            }
        }
        stage('Build') {
            agent {
                docker {
                    image 'docker.io/joepreludian/python-poetry:latest'
                }
            }
            steps {
                unstash name: 'build'
                sh 'poetry build'
                sh 'ls -lh dist'
            }
        }
    }
}
