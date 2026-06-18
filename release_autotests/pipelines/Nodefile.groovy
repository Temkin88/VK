#!/usr/bin/env groovy
import hudson.model.*
import groovy.time.TimeCategory
import groovy.time.TimeDuration
import org.jenkinsci.plugins.pipeline.modeldefinition.Utils
import hudson.tasks.test.AbstractTestResultAction
import hudson.model.Actionable


@NonCPS
def addProductNameBadge() {
    /*
    Set product icon to jenkins build job
    */
    def _badge_text
    def _badge_icon

    if (params.ENV_PLATFORM == "SANDBOX" || params.ENV_PLATFORM == "VKTI" || params.ENV_PLATFORM == "PRE_VKTI") {
        _badge_text = "VK Teams"
        _badge_icon = "/userContent/product_icons/vkteams_32x32.png"
    } else if (params.ENV_PLATFORM == "TARM" || params.ENV_PLATFORM == "PRE_TARM") {
        _badge_text = "ARMGS"
        _badge_icon = "/userContent/product_icons/armgs_32x32.png"
    } else {
        _badge_text = program_name
        _badge_icon = ""
        println "Unknown badge icon"
    }

    //Add badge with product name
    addBadge(icon: _badge_icon, text: _badge_text)
}



def prepare_stage_by_api_version(api_version) {
    return {
        stage("API Version ${api_version}") {
            jobBuild = build job: "Free type Night Release autotests",
                parameters: [
                    string(name: 'ENV_PLATFORM', value: params.ENV_PLATFORM),
                    string(name: 'SANDBOX', value: params.SANDBOX),
                    string(name: 'API_VERSION', value: api_version),
                    string(name: 'FORCED_IP', defaultValue: '', description: 'IP address for pre-production environments'),
                    string(name: 'LOG_LEVEL', value: params.LOG_LEVEL),
                    string(name: 'ALLURE_JOB_RUN_ID', value: env.ALLURE_JOB_RUN_ID)
                ],
                propagate: false,
                wait: true
        }
    }
}


node("the_executor"){
    properties(
        [
            parameters([
                    choice(name: 'ENV_PLATFORM', choices: ['VKTI', 'PRE_VKTI', 'TARM', 'PRE_TARM', 'SANDBOX'], description: 'VKTI, TARM or SANDBOX'),
                    string(name: 'SANDBOX', defaultValue: 'vkorobov.v3.im-sandbox.devmail.ru', description: 'Sandbox name'),
                    string(name: 'API_VERSIONS', defaultValue: '102', description: 'comma-separated API versions'),
                    choice(name: 'LOG_LEVEL', choices: ['WARNING', 'INFO', 'DEBUG'], description: 'Log level in pytest tests')
            ])
        ]
    )
    timeout(time: 1, unit: 'HOURS') {
        stage('Tests') {
            def API_VERSIONS_LIST = params.API_VERSIONS.split(',')
            def SUITES_LIST = [:]
            API_VERSIONS_LIST.each { item ->
                SUITES_LIST.put(
                    "API Version ${item}", prepare_stage_by_api_version(item)
                )
            }

//             addProductNameBadge()

            def now = new Date()
            def date_and_time = now.format("yyyy.MM.dd HH:mm")
            def date = now.format("yyyy.MM.dd")

            def LAUNCH_NAME = "#${BUILD_ID} ${params.ENV_PLATFORM} | ${date_and_time}"
            def LAUNCH_TAGS = "night_release,${params.ENV_PLATFORM},${date}"

            if (params.ENV_PLATFORM == "SANDBOX") {
                def SANDBOX = params.SANDBOX.split('\\.')[0];
                LAUNCH_NAME = "#${BUILD_ID} ${params.ENV_PLATFORM} (${SANDBOX}) | ${date_and_time}"
                LAUNCH_TAGS = "night_release,${params.ENV_PLATFORM},${date},${SANDBOX}"
            }

            withAllureLaunch(
                projectId: '7',
                name: LAUNCH_NAME,
                tags: LAUNCH_TAGS,
            ) {
                parallel(SUITES_LIST)
            }
        }
    }
}