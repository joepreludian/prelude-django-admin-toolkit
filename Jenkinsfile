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
                    args '-e HEADLESS=1'
                }
            }
            steps {
                unstash name: 'build'
                dir('testproject') {
                    sh 'apk add wget build-base gcc cmake linux-headers gcc libffi-dev libressl-dev firefox'
                    sh 'wget https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz && tar zxvf /tmp/geckodriver.tar.gz && mv geckodriver /usr/bin && chmod +x /usr/bin/geckodriver'
                    sh 'poetry install'
                    sh 'poetry run python manage.py check'
                    sh 'poetry run pytest --cov prelude_django_admin_toolkit --cov-report xml'
                    sh 'poetry run python manage.py behave'
                   	
                   	publishCoverage
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

                stash name: 'dist', includes: 'dist/**/*'
            }
        }
        stage('Deploy') {
            agent {
                docker {
                    image 'docker.io/joepreludian/python-poetry:latest'
                }
            }
            when {
                branch 'master'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'pypi-joepreludian', usernameVariable: 'PYPI_USER', passwordVariable: 'PYPI_TOKEN')]) {
                    sh 'poetry config pypi-token.pypi "$PYPI_TOKEN"'
                }

                unstash name: 'dist'
                
                //sh 'poetry publish'
            }
        }
    }
    post {
    	always {
        	sh 'docker container prune -f'
    	}
    }
}
