def FAILED_STAGE
def STAGE_ERROR

pipeline {

    agent {
        label 'saas-node'
    }

    parameters {
        string(name: 'TESTS_BRANCH', defaultValue: 'master', description: 'Tests branch (to execute tests from your branch like IMQA-1111)')
        string(name: 'API_VERSION', defaultValue: '125', description: 'API versions')
        booleanParam(name: 'USE_SSO_AUTH', defaultValue: false, description: 'SSO auth')
        booleanParam(name: 'PUSH_GATEWAY', defaultValue: false, description: 'Push gateway metrix in victoria DB')
        string(name: 'SUPPLY_URL', defaultValue: 'https://imqa-supply-prod.mail.msk/api', description: 'URL используемого supply-сервера')
        string(name: 'PYTEST_MARKER', defaultValue: "PRE_SAAS", description: 'Markers to select/deselect autotests')
        choice(name: 'LOG_LEVEL', choices: ['WARNING', 'INFO', 'DEBUG'], description: 'Log level in pytest tests')
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
                        sh(label: '[Preparing python3 requirements]', script: "python3.11 -V")
                        sh(label: '[Preparing python3 requirements]', script: "python3.11 -m venv venv")

                        def common = load 'pipelines/common.groovy'

                        common.loadVarsFromFile('variables.env')
                        common.python("pip install -U . --trusted-host mirror.i")
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

                        common.setLaunchName("SAAS (Pre-Production)")
                        common.setLaunchTags("PRE_SAAS")
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
                        common.runPytestApiTests()

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
                        common.runPytestApiTestsLastFailed()

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
                common.reportAbortedBuild("AuHdGV8wgxPGXpsR")
            }
        }
        unsuccessful {
            script {
                def common = load 'pipelines/common.groovy'
                common.reportFailedBuild("AuHdGV8wgxPGXpsR", FAILED_STAGE, STAGE_ERROR)
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
                common.allureLaunchReport("AuHdGV8wgxPGXpsR")
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
