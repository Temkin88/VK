import allure
import pytest

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("79708")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Настройки приватности")
@allure.feature("Черный список")
@allure.title("Удаление из черного списка")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_del_invite_blacklist(auth_account):
    """
    Удаление из черного списка
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

    with allure.step("Удаляем uin из черного списка"):
        auth_account.rapi_privacy_groups_inviteBlacklist_del(uins_list)

        assert response["status"]["code"] == 20000, "Failed request"

    with allure.step("Проверяем что uin появились не в черном списке"):
        response = auth_account.rapi_privacy_groups_inviteBlacklist_get(10)

        assert response["status"]["code"] == 20000, "Failed request"
        assert all(uin not in response["results"]["blacklist"] for uin in uins_list), "Uin in blacklist"


@allure.id("79751")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Настройки приватности")
@allure.feature("Черный список")
@allure.title("Проверяем неверный формат запроса в черном списке")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_del_invalid_param_invite_blacklist(
    auth_account,
    clear_blacklist,
):
    """
    Проверяем неверный формат запроса в черном списке
    """
    with allure.step("Проверяем что черный список пустой"):
        response = auth_account.rapi_privacy_groups_inviteBlacklist_get(10)
        assert response["status"]["code"] == 20000, "Failed request"
        assert not response["results"]["blacklist"], "Not empty blacklist"

    with allure.step("Удаляем несуществующего uin из черного списка"):
        response = auth_account.rapi_privacy_groups_inviteBlacklist_del(["12345"])
        assert response["status"]["code"] == 20000, "Failed request"

    with allure.step("Пробуем отправить неверный формат запроса"), pytest.raises(BadRequestException):
        auth_account.rapi_privacy_groups_inviteBlacklist_del("12345")
