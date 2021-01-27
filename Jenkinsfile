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
        stage('Compile i18n') { 
            agent {
                docker {
                    image 'docker.io/joepreludian/python-poetry:latest'
                    args '-e HEADLESS=1'
                }
            }
            steps {
                unstash name: 'build'
                
           		echo 'Compiling messages...'
           		sh 'apk add gettext build-base gcc cmake python3-dev linux-headers gcc libffi-dev libressl-dev'
                sh 'poetry install'
                sh 'poetry run python manage.py compilemessages'
             	
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
                
           		echo 'Compiling messages'
                sh 'poetry install'
                sh 'poetry run python manage.py compilemessages'
             	stash name: 'build', includes: 'prelude_django_admin_toolkit/**/*'
                
                dir('testproject') {
                    sh 'apk add wget build-base gcc cmake linux-headers gcc libffi-dev libressl-dev firefox'
                    sh 'wget https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz && tar zxvf /tmp/geckodriver.tar.gz && mv geckodriver /usr/bin && chmod +x /usr/bin/geckodriver'
                    sh 'poetry install'
                    sh 'poetry run python manage.py check'
                    sh 'poetry run pytest --cov prelude_django_admin_toolkit --cov-report html --cov-report xml'
                    sh 'poetry run python manage.py behave'
                
                	withCredentials([string(credentialsId: 'codecov-joepreludian-prelude_bruh', variable: 'CODECOV_TOKEN')]) {
                	    sh 'apk add curl bash git && curl -s https://codecov.io/bash -o codecov.sh'
                	    sh 'bash codecov.sh'
                	}
                		
                	publishHTML (target: [
						allowMissing: false,
						alwaysLinkToLastBuild: true,
						keepAll: true,
						reportDir: 'htmlcov',
						reportFiles: 'index.html',
						reportName: "Pytest Coverage"
					])	
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
            	script {
	
	                withCredentials([usernamePassword(credentialsId: 'pypi-joepreludian', usernameVariable: 'PYPI_USER', passwordVariable: 'PYPI_TOKEN')]) {
	                    sh 'poetry config pypi-token.pypi "$PYPI_TOKEN"'
	                }
	
	                unstash name: 'dist'
	                
	                poetry_publish_log = sh (script: 'poetry publish', returnStdout: true).trim()
	                
	                slackSend(color: "good", message: "prelude_django_admin_toolkit Deployed to Pypi! \n\n${poetry_publish_log}")
				}
            }
        }
    }
    post {
    	success {
	        slackSend(color: "good", message: "Build of prelude_django_admin_toolkit succeed!")
	    }
	 	failure {
	 	    slackSend(color: "bad", message: "prelude_django_admin_toolkit Failed. Please verify!")
	 	}
    	always {
        	sh 'docker container prune -f'
    	}
    }
}
