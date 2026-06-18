import allure
import pytest

from pyvkteamsclient.client.exceptions import RequestException, BadRequestException
from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS

MIN_PIN_API_VERSION = 100


@allure.id("28158")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("conf_type", ["equitable", "webinar"])
@pytest.mark.parametrize("callback", [True, False])
@pytest.mark.parametrize("pin_required", [True, False])
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Создание конференций")
@allure.title("Создание ссылки на звонок")
def test_conference_create(
    auth_account,
    opponent_account,
    conf_type,
    callback,
    pin_required,
):
    with allure.step("Пробуем создать конференцию"):
        response = auth_account.rapi_conference_create(
            name="Test conference",
            _type=conf_type,
            participants=[
                opponent_account.uin,
            ],
            callParticipants=callback,
            pinRequired=pin_required,
        )

        results = response["results"]

        conference_url = results.get("conferenceUrl")

    with allure.step("Проверяем ответ сервера"):
        assert "conferenceUrl" in results, f"Wrong conferenceUrl value: {conference_url}"
        assert conference_url, f"Wrong conferenceUrl value: {conference_url}"


@allure.id("83510")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("conf_type", ["equitable", "webinar"])
@pytest.mark.parametrize("pin_required", [True, False])
@pytest.mark.parametrize("role", ["moderator", "speaker"])
@pytest.mark.parametrize("permissions", [1, 64, 512, 2048])
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Создание конференций")
@allure.title("Создание ссылки на звонок новая")
def test_conference_create_new(
    auth_account,
    opponent_account,
    conf_type,
    role,
    permissions,
    pin_required,
):
    with allure.step("Пробуем создать конференцию"):
        results = auth_account.rapi_conference_create_new(
            name="Test conference",
            type=conf_type,
            pinRequired=pin_required,
            members={
                opponent_account.uin: {
                    "role": role,
                },
            },
            roles={
                role: {
                    "permissions": permissions,
                },
                "default": {
                    "permissions": 10,
                },
            },
        )["results"]
        conference_url = results.get("conferenceUrl")

    with allure.step("Проверяем ответ сервера"):
        assert "conferenceUrl" in results, f"Wrong conferenceUrl value: {conference_url}"
        assert conference_url, f"Wrong conferenceUrl value: {conference_url}"


@allure.id("83507")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Создание конференций")
@allure.title("Создание ссылки на звонок новая c невалидными параметрами")
@pytest.mark.parametrize("permissions", [-1, 2049])
def test_conference_create_new_invalid_params(
    auth_account,
    opponent_account,
    permissions,
):
    with allure.step("Пробуем создать конференцию"):
        results = auth_account.rapi_conference_create_new(
            name="Test conference",
            type="test",
            pinRequired=True,
            members={
                opponent_account.uin: {
                    "role": "test",
                },
            },
            roles={
                "test": {
                    "permissions": permissions,
                },
                "default": {
                    "permissions": permissions,
                },
            },
        )["results"]
        conference_url = results.get("conferenceUrl")

    with allure.step("Проверяем ответ сервера"):
        assert "conferenceUrl" in results, f"Wrong conferenceUrl value: {conference_url}"
        assert conference_url, f"Wrong conferenceUrl value: {conference_url}"


@allure.id("493509")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Создание конференций")
@allure.title("Создание ссылки на звонок c 0 permissions")
def test_conference_create_new_with_zero(
    auth_account,
    opponent_account,
):
    with allure.step("Пробуем создать конференцию"), pytest.raises(BadRequestException):
        auth_account.rapi_conference_create_new(
            name="Test conference",
            type="test",
            pinRequired=True,
            members={
                opponent_account.uin: {
                    "role": "test",
                },
            },
            roles={
                "test": {
                    "permissions": 0,
                },
                "default": {
                    "permissions": 0,
                },
            },
        )


@allure.id("83509")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("role", ["", [], {}, 1234, None])
@pytest.mark.parametrize("permissions", ["", [], {}, None])
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Создание конференций")
@allure.title("Создание ссылки на звонок новая с невалидными типами")
def test_conference_create_new_invalid_type(
    auth_account,
    opponent_account,
    role,
    permissions,
):
    with allure.step("Пробуем создать конференцию"), pytest.raises((TypeError, RequestException, BadRequestException)):
        auth_account.rapi_conference_create_new(
            name="Test conference",
            type=role,
            pinRequired=True,
            members={
                opponent_account.uin: {
                    "role": role,
                },
            },
            roles={
                role: {
                    "permissions": permissions,
                },
                "default": {
                    "permissions": permissions,
                },
            },
        )
