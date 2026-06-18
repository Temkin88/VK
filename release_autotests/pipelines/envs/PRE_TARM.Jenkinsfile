def FAILED_STAGE
def STAGE_ERROR

pipeline {

    agent {
        label 'tarm-node'
    }

    parameters {
        string(name: 'TESTS_BRANCH', defaultValue: 'master', description: 'Tests branch (to execute tests from your branch like IMQA-1111)')
        booleanParam(name: 'USE_SWA_AUTH', defaultValue: false, description: 'SWA auth')
        booleanParam(name: 'USE_MULTI_THREAD', defaultValue: true, description: 'Exec tests in parallel')
        booleanParam(name: 'PUSH_GATEWAY', defaultValue: false, description: 'Push gateway metrix in victoria DB')
        string(name: 'API_VERSION', defaultValue: '', description: 'API versions')
        string(name: 'SUPPLY_URL', defaultValue: 'https://imqa-supply-prod.mail.msk/api', description: 'URL используемого supply-сервера')
        choice(name: 'LOG_LEVEL', choices: ['WARNING', 'INFO', 'DEBUG'], description: 'Log level in pytest tests')
        string(name: 'PYTEST_MARKER', defaultValue: 'PRE_TARM', description: 'Markers to select/deselect autotests')
        string(name: 'JIRA_ISSUE', defaultValue: '', description: 'JIRA issue to link in Allure TestOps')
        base64File(name: 'DLP_CONFIG', description: 'JSON файл с настройками dlp тестов')
    }

    options {
        skipDefaultCheckout()
        timeout(time: 2, unit: 'HOURS')
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
    }

    stages {

        stage ('Checkout') {
            steps {
                script{
                    try {
                        FAILED_STAGE=env.STAGE_NAME
                        cleanWs()
                        checkout([
                            $class: 'GitSCM',
                            branches: [[name: params.TESTS_BRANCH]],
                            doGenerateSubmoduleConfigurations: true,
                            extensions: scm.extensions + [[$class: 'SubmoduleOption', parentCredentials: true]],
                            userRemoteConfigs: scm.userRemoteConfigs
                        ])
                    } catch (Exception error) {
                        println "[Checkout] $error"
                        STAGE_ERROR="$error"
                        throw error;
                    }
                }
            }
        }
        stage ('Copy dlp config') {
            steps {
                script{
                        if (env.DLP_CONFIG!=null){
                            withFileParameter('DLP_CONFIG') {
                                sh(label: '[write dlp config file]', script: 'cp "$DLP_CONFIG" ./dlp.json')

                            }
                        }

                }
            }
        }
        stage('Preparing python3 requirements') {
            steps {
                script {
                    try {
                        FAILED_STAGE=env.STAGE_NAME
                        sh(label: '[Preparing python3 requirements]', script: "python3 -V")
                        sh(label: '[Preparing python3 requirements]', script: "python3 -m venv venv")

                        def common = load 'pipelines/common.groovy'

                        common.loadVarsFromFile('variables.env')
                        common.python("pip install .")
                    } catch (Exception error) {
                        println "[venv prepare] $error"
                        STAGE_ERROR="$error"
                        throw error;
                    }
                }
            }
        }
        stage('Allure - Creating launch') {
            steps {
                script {
                    try {
                        FAILED_STAGE=env.STAGE_NAME

                        def common = load 'pipelines/common.groovy'

                        common.loadVarsFromFile('variables.env')
                        common.installAllureCtl()

                        common.setLaunchName("TARM (Pre-Production)")
                        common.setLaunchTags("PRE_TARM")
                        common.setBuildName(env.ALLURE_LAUNCH_NAME)

                        common.createLaunch()

                    } catch (Exception error) {
                        println "[venv prepare] $error"
                        STAGE_ERROR="$error"
                        throw error;
                    }
                }
            }
        }
        stage('E2E API Autotests'){
            steps {
                script {
                    try {
                        FAILED_STAGE=env.STAGE_NAME

                        def common = load 'pipelines/common.groovy'

                        common.loadVarsFromFile('variables.env')
                        common.runPytestApiTests('u.tppr.vmailru.net')

                    } catch (Exception error) {
                        println "[api tests] $error"
                        STAGE_ERROR="$error"
                        throw error;
                    }
                }
            }
        }
        stage('E2E API Autotests - last failed tests'){
            when {
                environment name: 'RETRY_FAILED_API_TESTS', value: 'true'
            }
            steps {
                script {
                    try {
                        FAILED_STAGE=env.STAGE_NAME

                        def common = load 'pipelines/common.groovy'

                        common.loadVarsFromFile('variables.env')
                        common.runPytestApiTestsLastFailed('u.tppr.vmailru.net')

                    } catch (Exception error) {
                        println "[api tests] $error"
                        STAGE_ERROR="$error"
                        throw error;
                    }
                }
            }
        }
    }
    post {
        aborted {
            script {
                def common = load 'pipelines/common.groovy'
                common.reportAbortedBuild("AuHdCy4PMxilYSsa")
            }
        }
        unsuccessful {
            script {
                def common = load 'pipelines/common.groovy'
                common.reportFailedBuild("AuHdCy4PMxilYSsa", FAILED_STAGE, STAGE_ERROR)
            }
        }
        success {
            publishHTML (
                target : [allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: '*.html',
                reportName: 'Swagger-Coverage',
                reportTitles: 'Swagger-Coverage']
            )
            script {
                def common = load 'pipelines/common.groovy'
                common.allureLaunchReport("AuHdCy4PMxilYSsa")
            }
        }
        always {
            script {
                sh(label: '[clear dlp config file]', script: 'rm -rf ./dlp.json')
                try {
                    archiveArtifacts artifacts: "reports/playwright/*.*", fingerprint: false
                } catch (Exception error) {
                    println "[archiveArtifacts] - $error"
                }
            }
        }
        cleanup {
            cleanWs()
        }
    }
}
