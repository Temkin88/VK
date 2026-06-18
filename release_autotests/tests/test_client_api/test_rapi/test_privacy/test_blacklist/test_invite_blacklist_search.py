import uuid

import allure
import pytest

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26908")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Настройки приватности")
@allure.feature("Черный список")
@allure.title("Поиск по черному списку")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.BOT_API
def test_search_invite_blacklist(auth_account):
    """
    Поиск по черному списку
    """

    uins_list = [
        "1000000001",
        "1000000002",
    ]

    with allure.step("Добавляем uin в черный список"):
        auth_account.rapi_privacy_groups_inviteBlacklist_add(uins_list)

    with allure.step("Проверяем что uin появились в черном списке"):
        response = auth_account.rapi_privacy_groups_inviteBlacklist_get(10)

        assert response["status"]["code"] == 20000, "Failed request"
        assert all(uin in response["results"]["blacklist"] for uin in uins_list), "Uin not in blacklist"

    with allure.step("Проверяем что все uin найдены в черном списке"):
        response_all_uin = auth_account.rapi_privacy_groups_inviteBlacklist_search(
            keyword="100000000",
            pageSize=10,
        )

        assert response_all_uin["status"]["code"] == 20000, "Failed request"
        assert all(uin in response_all_uin["results"]["blacklist"] for uin in uins_list), "Uin not in blacklist"

    with allure.step("Проверяем что uin найден в черном списке"):
        response_uin_01 = auth_account.rapi_privacy_groups_inviteBlacklist_search(
            keyword=uins_list[0],
            pageSize=10,
        )

        assert response_uin_01["status"]["code"] == 20000, "Failed request"
        assert uins_list[0] in response_uin_01["results"]["blacklist"], f"{uins_list[0]} not in blacklist"
        assert uins_list[1] not in response_uin_01["results"]["blacklist"], f"{uins_list[1]} in blacklist"


@allure.id("79752")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Настройки приватности")
@allure.feature("Черный список")
@allure.title("Поиск несуществующего пользователя в черном списке")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.BOT_API
def test_search_invalid_invite_blacklist(
    auth_account,
):
    """
    Поиск несуществующего пользователя в черном списке
    """

    with allure.step("Проверяем что не найден uin которого не было в черном списке"):
        response_failed_uin = auth_account.rapi_privacy_groups_inviteBlacklist_search(
            keyword=f"{uuid.uuid4().hex}",
            pageSize=10,
        )

        assert response_failed_uin["status"]["code"] == 20000, "Failed request"
        assert not response_failed_uin["results"]["blacklist"], "empty search list"

    with allure.step("Пробуем отправить невалидный запрос"), pytest.raises(BadRequestException):
        auth_account.rapi_privacy_groups_inviteBlacklist_search(
            keyword=3,
            pageSize=10,
        )
