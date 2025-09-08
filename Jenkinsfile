pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    environment {
        PROD_ENV     = "/opt/env/.env.uytop"
        IMAGE_NAME   = "uytop"
        TEST_TAG     = "test"
        PROD_TAG     = "latest"
        CONTAINER_DB = "uytop_db_test"
        CONTAINER_WEB = "uytop_web_test"
        CONTAINER_REDIS = "uytop_redis_test"
        STACK_NAME = "uytop"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', credentialsId: 'ssh', url: 'git@github.com:JscorpTech/uytop.git'
                stash includes: 'stack.j2.yaml', name: "stack.j2.yaml"
            }
        }
        stage('Build Image') {
            steps {
                sh '''
                    if [ -e ${PROD_ENV} ]; then
                       echo env exists
                    else
                        mkdir -p $(dirname ${PROD_ENV})
                        cp ./.env.example ${PROD_ENV}
                    fi
                    cp ${PROD_ENV} ./.env
                '''
                sh """
                    docker build -t ${IMAGE_NAME}:${PROD_TAG} -f ./docker/Dockerfile.web .
                """
            }
        }


        stage('Publish to DockerHub') {
            when {
                expression { currentBuild.currentResult == "SUCCESS" }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "${DOCKER_PASS}" | docker login -u "${DOCKER_USER}" --password-stdin
                        docker tag ${IMAGE_NAME}:${PROD_TAG} ${DOCKER_USER}/${IMAGE_NAME}:${BUILD_NUMBER}
                        docker tag ${IMAGE_NAME}:${PROD_TAG} ${DOCKER_USER}/${IMAGE_NAME}:${PROD_TAG}
                        docker push ${DOCKER_USER}/${IMAGE_NAME}:${BUILD_NUMBER}
                        docker push ${DOCKER_USER}/${IMAGE_NAME}:${PROD_TAG}
                    '''
                }
            }
        }
        stage("Generate stack.yaml") {
            when {
                expression { currentBuild.currentResult == "SUCCESS" }
            }
            agent {
                docker {
                    image 'python:3.13-slim'
                    args '-u root'
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    unstash "stack.j2.yaml"
                    sh """
                        pip install jinja2-cli
                        jinja2 stack.j2.yaml -D username=${DOCKER_USER} -D name=${IMAGE_NAME} -D tag=${BUILD_NUMBER} > stack.yaml
                    """
                    stash includes: 'stack.yaml', name: 'stackfile'
                }
            }
        }
        stage('Deploy stack') {
            when {
                expression { currentBuild.currentResult == "SUCCESS" }
            }
            steps {
                unstash 'stackfile'
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                       docker stack deploy -c stack.yaml --env-file .env ${STACK_NAME}
                    '''
                }
            }
        }
 
    }

    post {
        always {
            echo "Pipeline finished: ${currentBuild.currentResult}"
        }

        success {
            withCredentials([
                string(credentialsId: 'bot-token', variable: 'BOT_TOKEN'),
                string(credentialsId: 'chat-id', variable: 'CHAT_ID')
            ]) {
                sh '''
                curl -s -X POST https://api.telegram.org/bot${BOT_TOKEN}/sendMessage \
                -d chat_id=${CHAT_ID} \
                -d text="✅ SUCCESS: ${JOB_NAME} #${BUILD_NUMBER}"
                '''
            }
        }

        failure {
            withCredentials([
                string(credentialsId: 'bot-token', variable: 'BOT_TOKEN'),
                string(credentialsId: 'chat-id', variable: 'CHAT_ID')
            ]) {
                sh '''
                curl -s -X POST https://api.telegram.org/bot${BOT_TOKEN}/sendMessage \
                -d chat_id=${CHAT_ID} \
                -d text="🚨 FAILED: ${JOB_NAME} #${BUILD_NUMBER}"
                '''
            }
        }
    }
}
