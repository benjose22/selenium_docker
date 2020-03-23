node {
    def app

    stage('Clone repository') {
        /* Cloning the Repository to our Workspace */

        checkout scm
    }
	
    stage('Build image') {
        /* This builds the actual image */
		def dockerfile = 'pytest.Dockerfile'
        app = docker.build("pytest-with-src","-f ${dockerfile} ./")
    }
	
    stage('Execute script') {
        
        sh 'docker run --network="host" --rm pytest-with-src --browser "chrome" --executor "remote"'
    }
	
	stage('Remove image') {
        
        sh 'docker rmi pytest-with-src -f'
        }
    }
}