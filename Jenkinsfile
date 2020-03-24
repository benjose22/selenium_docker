        /* This pipeline creates a docker compose and then executes all the scripts. Note the Jenkins has to be in Linux environment */
node {
    def app

    stage('Clone repository') {

        checkout scm
    }
	
    stage('Start docker-compose') {
		/* Start docker-compose with five instances of Chrome */
	    sh 'docker-compose up -d --scale chrome=5 --scale firefox=0'
	}
	
    stage('Build image') {
        /* This builds an image with all pytest selenium scripts in it */
		def dockerfile = 'pytest.Dockerfile'
        app = docker.build("pytest-with-src","-f ${dockerfile} ./")
    }
	
    stage('Execute script') {
		/* Execute the pytest script. On faliure proceed to next step */
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
            sh 'docker run --network="host" --rm -i -v ${WORKSPACE}/allure-results:/AllureReports pytest-with-src --executor "remote" --browser "chrome" .'
        }
    }
	
	stage('Remove image') {
        /* Delete the image which got created earlier */
        sh 'docker rmi pytest-with-src -f'
    }
    
    stage('Teardown docker-compose') {
		/* Tear down docker compose */
        sh 'docker-compose down --rmi local'
    }
    
	stage('Allure Report') {
        /* Generate Allure Report */
        allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
    }
}
