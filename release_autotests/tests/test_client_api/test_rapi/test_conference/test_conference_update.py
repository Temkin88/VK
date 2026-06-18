import uuid

import allure
import pytest

from pyvkteamsclient.client.exceptions import ServerException, BadRequestException, RequestException
from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("83511")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("role", ["moderator", "speaker"])
@pytest.mark.parametrize("permissions", [31, 255, 1023])
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Обновить параметры конференции")
@allure.title("Обновление параметров конференции")
def test_conference_update(
    auth_account,
    opponent_account,
    role,
    permissions,
    conference_id,
):
    name = f"Test update {uuid.uuid4().hex}"

    with allure.step("Пробуем создать конференцию"):
        auth_account.rapi_conference_update(
            conference_id=conference_id,
            name=name,
            creator=auth_account.uin,
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

    with allure.step("Проверяем что данные изменились"):
        response = auth_account.rapi_conference_get(
            conference_id=conference_id,
        )["results"]

        conference_url = response.get("conferenceUrl")

        assert response["conferenceName"] == name, "Name dont match"
        assert response["members"][opponent_account.uin]["role"] == role, "Role dont match"
        assert response["roles"][role]["permissions"] == permissions, "Permission dont match"
        assert "conferenceUrl" in response, f"Wrong conferenceUrl value: {conference_url}"
        assert conference_url, f"Wrong conferenceUrl value: {conference_url}"


@allure.id("83816")
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
@allure.feature("Обновить параметры конференции")
@allure.title("Обновление параметров конференции с невалидными типами")
def test_conference_update_invalid_type(
    auth_account,
    opponent_account,
    role,
    permissions,
):
    with (
        allure.step("Пробуем создать конференцию"),
        pytest.raises((TypeError, RequestException, ServerException, BadRequestException)),
    ):
        auth_account.rapi_conference_update(
            conference_id=role,
            name=role,
            creator=auth_account.uin,
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
