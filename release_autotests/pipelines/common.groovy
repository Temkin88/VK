#!/usr/bin/env groovy
import hudson.model.AbstractProject
import hudson.tasks.Mailer
import hudson.model.User

@NonCPS
def getCurrentDate() {
    println "[getCurrentDate]"
    def CURRENT_DATE = new Date().format("MM/dd/yyyy HH:mm:ss")
    println "[getCurrentDate] $CURRENT_DATE"
    return CURRENT_DATE
}


def python(String cmd, Boolean returnStdout = false) {
    println "[python] cmd: ${cmd}, returnStdout: ${returnStdout}";
    def result = null;
    withEnv([
        "PIP_TRUSTED_HOST=pypi.org gitlab.corp.mail.ru",
        "PIP_INDEX_URL=https://pypi.org/simple/",
        "PIP_EXTRA_INDEX_URL=https://__token__:9sB-zvU818WmFwkXechX@gitlab.corp.mail.ru/api/v4/groups/3011/-/packages/pypi/simple",
        "PIP_DEBUG=1"
    ]) {
        result = sh(label: '[python]', returnStatus: true, returnStdout: returnStdout, script: ". venv/bin/activate; ${cmd}")
    }
    return result;
}


def report_python(String cmd, Boolean returnStdout = false) {
    println "[python] cmd: ${cmd}, returnStdout: ${returnStdout}";
    def result = null;
    result = sh(label: '[python]', returnStdout: returnStdout, script: ". venv/bin/activate; ${cmd}")
    return result;
}


@NonCPS
def setLaunchName(String buildType)
{
    println "[setLaunchName] buildType: ${buildType}";
    def LAUNCH_NAME = '';
    def CURRENT_DATE = getCurrentDate();

    if (buildType == 'SANDBOX' || buildType == 'DEV' || buildType == 'CORPCLOUD') {
        def SANDBOX = getSandboxName();
        LAUNCH_NAME = "#${BUILD_ID} ${buildType} (${SANDBOX}) ${CURRENT_DATE}"
    } else {
        LAUNCH_NAME = "#${BUILD_ID} ${buildType} ${CURRENT_DATE}"
    }

    setBuildName(LAUNCH_NAME);

    env.ALLURE_LAUNCH_NAME = LAUNCH_NAME;
}


@NonCPS
def setLaunchTags(String buildType)
{
    println "[setLaunchTags] buildType: ${buildType}";
    if (buildType == 'SANDBOX' || buildType == 'DEV' || buildType == 'CORPCLOUD') {
        def SANDBOX = getSandboxName();
        env.ALLURE_LAUNCH_TAGS = "night_release,${buildType},${SANDBOX}"
    } else {
        env.ALLURE_LAUNCH_TAGS = "night_release,${buildType}"
    }
}


@NonCPS
def setBuildName(String name)
{
    println "[setBuildName] name: ${name}";
    currentBuild.displayName = name;
}


@NonCPS
def getSandboxName()
{
    println "[getSandboxName]"
    if (params.SANDBOX) {
        return params.SANDBOX.split('\\.')[0];
    } else {
        return null;
    }
}


@NonCPS
def getPytestMarks()
{
    println "[getPytestMarks]"
    return params.PYTEST_MARKER
}


@NonCPS
def getEnvironmentName()
{
    println "[getEnvironmentName]"

    switch (params.PYTEST_MARKER) {
        default:
            return 'UNKNOWN'
        case { it.contains('SANDBOX') }:
            return 'SANDBOX'
        case { it.contains('PRE_SAAS') }:
            return 'PRE_SAAS'
        case { it.contains('SAAS') }:
            return 'SAAS'
        case { it.contains('PRE_VKTI') }:
            return 'PRE_VKTI'
        case { it.contains('VKTI') }:
            return 'VKTI'
        case { it.contains('PRE_TARM') }:
            return 'PRE_TARM'
        case { it.contains('TARM') }:
            return 'TARM'
    }
}


def saveLaunchId()
{
    println "[saveLaunchId]"
    println "[saveLaunchId] ALLURE_LAUNCH_ID: ${env.ALLURE_LAUNCH_ID}"
    writeFile(file: "job_run_id.txt", text: env.ALLURE_LAUNCH_ID, encoding: "UTF-8")
}


def readLaunchId()
{
    println "[readLaunchId]"
    def job_run_id = readFile(file: "job_run_id.txt", encoding: "UTF-8").trim();
    println "[readLaunchId] ALLURE_LAUNCH_ID: ${job_run_id}";
    return job_run_id.toInteger();
}


def allureLaunchReport(String chatId, String JOB_RUN_ID = null)
{
    println "[allureLaunchReport]"
    def message = '';
    if (ALLURE_LAUNCH_ID) {
        env.ALLURE_LAUNCH_ID = ALLURE_LAUNCH_ID
    } else {
        env.ALLURE_LAUNCH_ID = readLaunchId()
    }
    if (env.BUILD_START_USER == null || env.BUILD_START_USER == '') {
		env.BUILD_START_USER = getBuildStartUser()
    }
    env.RUNNING_TIME = "${currentBuild.durationString.replace(' and counting', '')}"
	withCredentials([string(credentialsId: 'allure', variable: 'ALLURE_TOKEN')]) {
		withEnv([
			'ALLURE_ENDPOINT=https://allure.vk.team',
			'ALLURE_PROJECT_ID=7',
			"ALLURE_TOKEN=${ALLURE_TOKEN}"
		]) {
			try {
				message = report_python("python allure_report.py", true).trim()
			} catch (Exception error) {
				try {
					sh(label: '[allureLaunchReport]', script: "python3 -m pip install requests")
					sh(label: '[allureLaunchReport]', script: "python3 allure_report.py")
				} catch (Exception intern_error) {
					println "[allureLaunchReport][message] - $error - $intern_error"
					message = "[allureLaunchReport][message] - $error - $intern_error"
				}
			}
		}
	}
    imSendMessage(
        CHAT_ID: chatId,
        MESSAGE: message
    )
    if (params.JIRA_ISSUE) {

        def VAR_JIRA_ISSUES = params.JIRA_ISSUE.split(';')

        def toJson = {
            input ->
            groovy.json.JsonOutput.toJson(input)
        }

        VAR_JIRA_ISSUES.eachWithIndex { CURRENT_JIRA_ISSUE, index ->

            def post_data = [
                "issue_key": CURRENT_JIRA_ISSUE,
                "text": message
            ]

            httpRequest httpMode: 'POST',
                url: "https://im-qa-helper.mail.msk/api/v1/jira/jira/comment",
                acceptType: "APPLICATION_JSON",
                contentType: "APPLICATION_JSON",
                requestBody: toJson(post_data),
                validResponseCodes: '200',
                wrapAsMultipart: false,
                ignoreSslErrors: true,
                consoleLogResponseBody: true

        }
    }
}


@NonCPS
def setBuildDescription(String description)
{
    println "[setBuildDescription] description: ${description}"
    try {
        currentBuild.description = description;
    } catch (Exception error) {
        println "[setBuildDescription] error: ${error}"
    }
}


def getBuildApiVersion(String target = '')
{
    println "[getBuildApiVersion] target: ${target}"

    if (params.API_VERSION.length() != 0) {
        return params.API_VERSION
    }

    try {
        switch( target ) {
            case null:
                println "curl -k -m 5 -vvv https://${params.SANDBOX}/myteam-config.json | jq '.\"api-version\"' -r"
                API_VERSION = sh(label: '[getBuildApiVersion]', returnStdout: true, script: "curl -k https://${params.SANDBOX}/myteam-config.json | jq '.\"api-version\"' -r").trim()
                break
            case target.length() == 0:
                println "curl -k -m 5 -vvv https://${params.SANDBOX}/myteam-config.json | jq '.\"api-version\"' -r"
                API_VERSION = sh(label: '[getBuildApiVersion]', returnStdout: true, script: "curl -k https://${params.SANDBOX}/myteam-config.json | jq '.\"api-version\"' -r").trim()
                break
            default:
                println "curl -k -m 5 -vvv https://${target}/myteam-config.json | jq '.\"api-version\"' -r"
                API_VERSION = sh(label: '[getBuildApiVersion]', returnStdout: true, script: "curl -k https://${target}/myteam-config.json | jq '.\"api-version\"' -r").trim()
                break
        }
        env.API_VERSION = API_VERSION
        return API_VERSION
    } catch (Exception error) {
        println "[getBuildApiVersion] $error"
        env.API_VERSION = '120'
        return '120'
    }
}


@NonCPS
def getBuildStartUser()
{
    println "[getBuildStartUser]"
    try {
        def userId = currentBuild.rawBuild.getCause(Cause.UserIdCause).getUserId()
        User u = User.get(userId)
        def umail = u.getProperty(Mailer.UserProperty.class)
        def email = umail.getAddress()
        return email
    } catch (Exception error) {
        println "[getBuildStartUser] $error"
        return ''
    }
}


@NonCPS
def getAbortUser()
{
    println "[getAbortUser]"
    def causee = ''
    def actions = currentBuild.getRawBuild().getActions(jenkins.model.InterruptedBuildAction)
    for (action in actions) {
        def causes = action.getCauses()

        // on cancellation, report who cancelled the build
        for (cause in causes) {
            causee = cause.getUser().getDisplayName()
            cause = null
        }
        causes = null
        action = null
    }
    actions = null

    return causee
}


def reportAbortedBuild(String chatId)
{
    println "[reportAbortedBuild] chatId: ${chatId}"
    def buildUser = getBuildStartUser();
    def abortUser = getAbortUser();
    def message = """Build: ${currentBuild.displayName}

Started by: @[${buildUser}]
Aborted by: @[${abortUser}]
Status: ${currentBuild.currentResult}
"""

    imSendMessage(
        CHAT_ID: chatId,
        MESSAGE: message
    )
}


def reportFailedBuild(String chatId, String stage = null, String error = null)
{
    println "[reportFailedBuild] chatId: ${chatId}, stage: ${stage}, error: ${error}"
    if (currentBuild.currentResult != 'ABORTED') {
        def buildUser = getBuildStartUser()
        def message = """Build: ${currentBuild.displayName}

Started by: @[${buildUser}]
Status: ${currentBuild.currentResult}
Stage: ${stage}Error: ${error}
"""

        imSendMessage(
            CHAT_ID: chatId,
            MESSAGE: message
        )
    }
}


def getApiPytestShellCmd(String target = null)
{
    println "[getApiPytestShellCmd] target: ${target}"

    def API_VERSION = getBuildApiVersion(target)

    def PYTEST_MARKER = getPytestMarks()

    def ENVIRONMENT = getEnvironmentName()

    def SHELL_CMD = """./allurectl watch --ci-type jenkins --ignore-passed-test-attachments --skip-too-big -l 20 -- pytest \
                            -m '${PYTEST_MARKER}' \
                            --sandbox=${params.SANDBOX} \
                            --api=${API_VERSION} \
                            --force-flaky \
                            --max-runs=2 \
                            --min-passes=1 \
                            --clean-alluredir \
                            --log-cli-level=${params.LOG_LEVEL} \
                            --swagger-name=${ENVIRONMENT} \
                            --swagger-report=./reports \
                            --swagger-prefix=v${API_VERSION} \
                            --swagger-exclude-json=im.swagger.spy.exclude_path/${ENVIRONMENT}.json \
                            --swagger-url=https://myteam.mail.ru/botapi/api.yaml \
                            --swagger-url=https://autotests.im-sandbox.devmail.ru/client/v${API_VERSION}/u/api.yaml \
                            --swagger-url=https://autotests.im-sandbox.devmail.ru/client/v${API_VERSION}/ub/api.yaml \
                            --swagger-url=https://autotests.im-sandbox.devmail.ru/internal-service/myteam-admin/swagger.yaml \
                            --swagger-url=https://autotests.im-sandbox.devmail.ru/internal-service/serverside-api/swagger.yaml \
                            --swagger-url=https://autotests.im-sandbox.devmail.ru/internal/u/api.yaml \
                            --swagger-url=https://autotests.im-sandbox.devmail.ru/internal/admin/api.yaml \
                            --supply-url=${params.SUPPLY_URL}"""

//                             --swagger-url=https://autotests.im-sandbox.devmail.ru/internal-service/org_structure/swagger.yaml

    if (params.DLP_CONFIG != "") {
        SHELL_CMD = SHELL_CMD + " --dlp-config-file=dlp.json"
    }


    if (params.USE_ALTER_AUTH) {
        SHELL_CMD = SHELL_CMD + " --sandbox-alter"
    }
    if (params.USE_MULTI_THREAD) {
        SHELL_CMD = SHELL_CMD + " -n=10 --dist=loadgroup"
    }
    def EXCLUDE_PATH = []
    if (params.USE_SSO_AUTH) {
        SHELL_CMD += " --use-sso"
        SHELL_CMD += " --swagger-exclude-json=im.swagger.spy.exclude_path/${ENVIRONMENT}.json"
    }
    else {
        SHELL_CMD += " --swagger-exclude-json=im.swagger.spy.exclude_path/${ENVIRONMENT}.json"
        SHELL_CMD += " --swagger-exclude-json=im.swagger.spy.exclude_path/SSO.json"
    }

    if (params.USE_SSO_AUTH) {
        SHELL_CMD = SHELL_CMD + " --use-swa"
    }

    if (params.DOMAIN_PAID) {
        SHELL_CMD = SHELL_CMD + " --domain-paid=${params.DOMAIN_PAID}"
    }

    if (params.FEDERATION_CONFIG) {
        SHELL_CMD = SHELL_CMD + " --federation-config=${params.FEDERATION_CONFIG}"
    }
    println "[getApiPytestShellCmd] SHELL_CMD: ${SHELL_CMD}";

    return SHELL_CMD;

}


def runPytestApiTests(
    String target = null
)
{
    println "[runPytestApiTests] target: ${target}"
    sh(label: '[runPytestApiTests]', script: "set")
    sh(label: '[runPytestApiTests]', script: "pwd")
    sh(label: '[runPytestApiTests]', script: "ls -lh")
    sh(label: '[runPytestApiTests]', script: "ls -lh tests")

    saveLaunchId()

    def SHELL_CMD = getApiPytestShellCmd(target)

    result = python(SHELL_CMD)

    if (result == 0) {
        env.RETRY_FAILED_API_TESTS = 'false'
    } else {
        env.RETRY_FAILED_API_TESTS = 'true'
    }

    def PUSH_GATEWAY_URL = ""

    if (params.PUSH_GATEWAY) {
        PUSH_GATEWAY_URL = "https://victoria-dev.imdevops.ru/prometheus/api/v1/import/prometheus"
    }

    println "pytest result: ${result}"
    println "env.RETRY_FAILED_API_TESTS = ${env.RETRY_FAILED_API_TESTS}"

    python("im_swagger_spy build ${PUSH_GATEWAY_URL} || true")
}


def runPytestApiTestsLastFailed(
    String target = null
)
{
    println "[runPytestApiTests] target: ${target}"
    sh(label: '[runPytestApiTests]', script: "set")

    saveLaunchId()

    def SHELL_CMD = getApiPytestShellCmd(target) + " --lf"

    result = python(SHELL_CMD)

    def PUSH_GATEWAY_URL = ""

    if (params.PUSH_GATEWAY) {
        PUSH_GATEWAY_URL = "https://victoria-dev.imdevops.ru/prometheus/api/v1/import/prometheus"
    }

    println "pytest result: ${result}"

    python("im_swagger_spy build ${PUSH_GATEWAY_URL} || true")
}


def getWebPytestShellCmd(String target = null)
{
    println "[getWebPytestShellCmd] target: ${target}"

    def PYTEST_MARKER = getPytestMarks()

    def API_VERSION = getBuildApiVersion(target)

    def SHELL_CMD = """pytest tests/test_web \
                                        -m '${PYTEST_MARKER}' \
                                        --api=${API_VERSION} \
                                        --sandbox=${params.SANDBOX} \
                                        --force-flaky \
                                        --max-runs=3 \
                                        --min-passes=1 \
                                        --log-cli-level=${params.LOG_LEVEL} \
                                        --output=reports/playwright \
                                        --screenshot=only-on-failure \
                                        --video=retain-on-failure"""

    if (params.USE_ALTER_AUTH) {
        SHELL_CMD = SHELL_CMD + " --sandbox-alter"
    }

    println SHELL_CMD;

    return SHELL_CMD;

}


def runPytestWebTests(String target = null)
{
    println "[runPytestWebTests] target: ${target}"
    sh(label: '[runPytestApiTests]', script: "set")

    def SHELL_CMD = getWebPytestShellCmd(target)

    if (params.USE_MULTI_THREAD) {
        python(SHELL_CMD + " -n=auto --dist=loadgroup")
        python(SHELL_CMD + " --lf")
    } else {
        python(SHELL_CMD)
        python(SHELL_CMD + " --lf")
    }
}

def installAllureCtl()
{
    println '[installAllureCtl] Trying to install allurectl from Github'
    sh(label: '[installAllureCtl] download', script: "wget https://github.com/allure-framework/allurectl/releases/latest/download/allurectl_linux_amd64 -O ./allurectl")
    sh(label: '[installAllureCtl] setting exec rights', script: "chmod +x ./allurectl")

    withCredentials([string(credentialsId: 'allure', variable: 'ALLURE_TOKEN')]) {
        withEnv([
            'ALLURE_ENDPOINT=https://allure.vk.team',
            'ALLURE_PROJECT_ID=7',
            "ALLURE_TOKEN=${ALLURE_TOKEN}"
        ]) {

            sh(label: '[installAllureCtl] login', script: './allurectl auth login')

        }
    }

    println '[installAllureCtl] allurectl successfully installed'
}

def createLaunch()
{
    println '[createLaunch] Trying to start launch in Allure TestOps'

    def ALLURE_LAUNCH_ID = sh(label: '[createLaunch] create', script: "./allurectl launch create -o json | jq '.[].id'", returnStdout: true)
    env.ALLURE_LAUNCH_ID = ALLURE_LAUNCH_ID

    def ALLURE_ENV_TEXT = sh(label: '[createLaunch] set env', script: './allurectl ci env set', returnStdout: true)
    loadVarsFromText(ALLURE_ENV_TEXT)

    println "[createLaunch] launch created - ID ${env.ALLURE_LAUNCH_ID}"
}

private void loadVarsFromFile(String path) {
    def file = readFile(path)
        .replaceAll("(?m)^\\s*\\r?\\n", "")  // skip empty line
        .replaceAll("(?m)^#[^\\n]*\\r?\\n", "")  // skip commented lines
    file.split('\n').each { envLine ->
        def (key, value) = envLine.tokenize('=')
        env."${key}" = "${value.trim().replaceAll('^\"|\"$', '')}"
    }
}

private void loadVarsFromText(String text) {
    text.split('\n').each { envLine ->
        def (key, value) = envLine.tokenize(' = ')
        env."${key}" = "${value}"
    }
}

return this;