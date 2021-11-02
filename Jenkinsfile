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

			sh 'rm -rf ~/rpmbuild/ && mkdir -p ~/rpmbuild/SOURCES/'
			sh 'cp OliveTin*.tar.gz ~/rpmbuild/SOURCES/'
            sh 'make'
	
			archiveArtifacts artifacts: '/root/rpmbuild/RPMS/x86_64/*.rpm', fingerprint: false
          }
      }
  }
}
