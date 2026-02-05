pipeline{
    agent any
    environment{
        BUCK="viresh28"
    }
        stages{
            stage('Hello'){
                steps{
                    echo "Hello This is start of pipeline"
                }
            }
            stage('git clone'){
                steps{
                    git branch: 'main', url: 'https://github.com/VireshDhuri01/Alldevopsprac.git'
                }
            }
            stage('Check or make Bucket'){
                steps{
                    sh'''
                    if aws s3 ls s3://${BUCK}; then
                    echo "Buck already exists"
                    else
                    aws s3 mb s3://${BUCK}
                    fi
                    '''
                }
            }
            stage('Deploy into  Bucket'){
                steps{
                    sh'aws s3 sync . s3://${BUCK}/'
                }
            }
            stage('Check Pipeline'){
                steps{
                    sh'''
                    echo "Hey, The Trigger and Pipeline is working fine" >> result.txt
                    '''
                }
            }
        }
    }
