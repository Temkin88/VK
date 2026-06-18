import allure
import pytest

from pyvkteamsclient.client.exceptions import RequestException
from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("37336")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Создание и редактирование чата")
@allure.title("Проверка занятости stamp чата (Занято)")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_check_chat_stamp_fail(
    auth_account,
    prepare_test_chats,
    chat_type,
):
    _, _, group, channel = prepare_test_chats

    chat_id = group if chat_type == "group" else channel

    with allure.step("Получаем stamp чата"):
        chat_info = auth_account.rapi_getChatInfo(sn=chat_id)

        chat_stamp = chat_info["results"]["stamp"]

    with allure.step("Проверяем stamp чата"), pytest.raises(RequestException):
        auth_account.rapi_checkGroupStamp(
            stamp=chat_stamp,
        )


@allure.id("37337")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Создание и редактирование чата")
@allure.title("Проверка занятости stamp чата (Свободно)")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_check_chat_stamp_success(
    auth_account,
):
    with allure.step("Проверяем занятость stamp"):
        auth_account.rapi_checkGroupStamp(
            stamp="totally_nobody_stamp",
        )
