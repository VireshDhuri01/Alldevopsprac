pipeline {
    agent {
        label 'slave10'
    }
    environment {
  BUCK = "cicd-pipeline-buck28"
}
    stages {
        stage('git clone') {
            steps {
                echo 'Hello World'
                git branch: 'main', url: 'https://github.com/VireshDhuri01/Alldevopsprac.git'
            }
        }
        stage('check buck or not') {
            steps {
                echo 'Hello World'
                sh '''
                if aws s3 ls s3://${BUCK}; then
                    echo "Buck Already Exists"
                else
                    aws s3 mb s3://${BUCK}
                fi
                '''
            }
        }
        stage('deploy to both'){
            parallel{
                stage('deploy to s3') {
            steps {
                echo 'Hello World'
                sh 'aws s3 sync . s3://${BUCK}/'
               
            }
        }
        stage('deploy to ec2') {
            steps {
                echo 'Hello World'
                sh 'sudo rm -rf /var/www/html/*'
                sh 'sudo cp -r . /var/www/html'
               
            }
        }
            }
        }
    }
}
