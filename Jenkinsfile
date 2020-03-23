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
	
    stage('Test image') {
        
        app.inside() {
            echo "Tests passed"
        }
    }
}