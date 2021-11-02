pipeline {
  agent any

	options {
		skipDefaultCheckout(true)
	}

  stages {
      stage ('Build') {
          steps {
            cleanWs()
            checkout scm

			copyArtifacts(projectName: "/OliveTin/OliveTin-rc-builder/main", filter: "dist/OliveTin-*linux-amd64.tar.gz", flatten: true)

			sh 'mkdir SOURCES && cp OliveTin*.tar.gz ./SOURCES/'
            sh 'make'
	
			archiveArtifacts artifacts: 'RPMS/x86_64/**.rpm', fingerprint: false
          }
      }
  }
}
