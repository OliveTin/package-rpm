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

			copyArtifacts(projectName: "/OliveTin/OliveTin-rc-builder/main", filter: "dist/OliveTin-*linux-amd64.tar.gz")

			sh 'cp OliveTin*.tar.gz ~/rpmbuild/SOURCES/'
            sh 'make'
          }
      }
  }
}
