pipeline {
    agent any

    stages {
        stage('Deploy and test the develop branch') {
            steps {
                bat 'docker-compose up -d --build'
            }
            steps {
                bat 'cd frontend && npm install && npm test -- --bail --ci'
            }
        }
        stage('Merge develop branch into a release branch') {
            steps {
                bat 'git checkout develop'
                bat 'git pull'
                bat 'git checkout release/jenkins'
                bat 'git merge develop'
                withCredentials([usernamePassword(credentialsId: 'GitHub', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    bat "git push http://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/ealeixoc-99/engineering-toxicity-monitor.git"
                }
            }
        }
        stage('Merge release branch into master') {
            steps {
                bat 'git checkout release/jenkins'
                bat 'git pull'
                bat 'git checkout master'
                bat 'git merge release/jenkins'
                withCredentials([usernamePassword(credentialsId: 'GitHub', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    bat "git push http://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/ealeixoc-99/engineering-toxicity-monitor.git"
                }
            }
        }
        stage('Deploy master branch') {
            steps {
                bat 'docker-compose up -d --build'
            }
        }
    }
}