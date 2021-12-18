pipeline{

  agent any

  stages{

    stage('clean'){
      steps{
        sh "cd /var/lib/jenkins/workspace/"
        checkout scm
      }
    }

    stage('Run Server'){
      steps{
        println("cd ${env.WORKSPACE}/CICD/")
        sh "cd ${env.WORKSPACE}/CICD/;pwd"
        println("Inside WORKSPACE: ${env.WORKSPACE}/CICD")
        sh "ls -lrt;sudo chmod 777 ${env.WORKSPACE}/CICD/runServer.sh"
        sh "sh ${env.WORKSPACE}/CICD/runServer.sh ${env.WORKSPACE}"
      }
    }
  }
}
