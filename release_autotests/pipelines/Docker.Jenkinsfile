def FAILED_STAGE
def STAGE_ERROR

pipeline {

    agent {
        label 'the_executor'
    }

    parameters {
        string(name: 'TESTS_BRANCH', defaultValue: 'master', description: 'Tests branch (to execute tests from your branch like IMQA-1111)')
        string(name: 'SANDBOX', defaultValue: 'stage-dev.v3.im-sandbox.devmail.ru', description: 'Sandbox name')
        booleanParam(name: 'USE_ALTER_AUTH', defaultValue: false, description: 'Search OTP token in chat instead of fixed token')
        booleanParam(name: 'USE_MULTI_THREAD', defaultValue: true, description: 'Exec tests in parallel')
        string(name: 'API_VERSION', defaultValue: '', description: 'API versions')
        choice(name: 'LOG_LEVEL', choices: ['WARNING', 'INFO', 'DEBUG'], description: 'Log level in pytest tests')
        string(name: 'PYTEST_MARKER', defaultValue: 'SANDBOX', description: 'Markers to select/deselect autotests')
        string(name: 'JIRA_ISSUE', defaultValue: '', description: 'JIRA issue to link in Allure TestOps')
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
        stage('Preparing docker') {
            steps {
                withCredentials([string(credentialsId: 'allure', variable: 'ALLURE_TOKEN')]) {
                    withEnv([
                        'ALLURE_ENDPOINT=https://allure.vk.team',
                        'ALLURE_PROJECT_ID=7',
                        "ALLURE_TOKEN=${ALLURE_TOKEN}"
                    ]) {
                        sh(script: "docker build --build-arg ALLURE_TOKEN=${ALLURE_TOKEN} -t autotest:latest .")
                    }
                }
            }
        }
        stage('E2E API Autotests with docker'){
            agent {
                docker {
                    image 'autotest:latest'
                    args '-it --entrypoint=""'
                }
            }
            steps {
                script {
                    if (params.API_VERSION.length() != 0) {
                        API_VERSION = params.API_VERSION
                    }
                    API_VERSION = sh(label: '[getBuildApiVersion]', returnStdout: true, script: "curl -k https://${params.SANDBOX}/myteam-config.json | jq '.\"api-version\"' -r").trim()
                    sh(script: "cd /workdir")
                    sh(script: "ls -lh")
                    sh(script: "sh run_pytest.sh -p ${params.PYTEST_MARKER} -s ${params.SANDBOX} -v ${API_VERSION} -l ${params.LOG_LEVEL}")
                }
            }
        }
    }
}
