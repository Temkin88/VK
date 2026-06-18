import allure
import pytest

from pyvkteamsclient.admin.exceptions import RequestException
from support.markers import SANDBOX


@allure.id("79715")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление группами и каналами")
@allure.title(
    "Получение информации о чате по id",
)
@SANDBOX
@pytest.mark.parametrize(
    "chat_type",
    [
        "bot",
        "group",
        "channel",
    ],
)
@pytest.mark.parametrize("is_chat_public", [True, False])
def test_api_chats_get_by_id_success(
    admin_account,
    chat_type,
    is_chat_public,
    auth_account,
    bot_class,
):
    with allure.step("Получаем ID чата"):
        if chat_type in ["private", "bot"]:
            chat_id = bot_class.uin if chat_type == "bot" else auth_account.uin
        else:
            chat_title = f"[{auth_account.getReqId()}]"
            chat_about = f"[{auth_account.getReqId()}]"
            chat_rules = f"[{auth_account.getReqId()}]"
            chat_id = auth_account.create_chat(
                name=chat_title,
                about=chat_about,
                rules=chat_rules,
                public=is_chat_public,
                defaultRole="member" if chat_type == "group" else "readonly",
            )
            chat_stamp = auth_account.get_chat_stamp(chat_id)

    with allure.step("Пробуем найти его в списке"):
        result = admin_account.api_chats_get_chat_id(
            chat_id=chat_id,
        )["result"]["result"]

        assert chat_id == result["id"], "Wrong chat id"
        assert chat_type == result["type"], "Wrong chat type"
        if chat_type in ["private", "bot"]:
            return
        assert chat_title == result["name"], "Wrong chat name"
        assert chat_stamp == result["stamp"], "Wrong chat stamp"
        assert is_chat_public == result["public"], "Wrong chat public"
        assert chat_about == result["about"], "Wrong chat about"
        assert chat_rules == result["rules"], "Wrong chat rule"


@allure.id("79681")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление группами и каналами")
@allure.title(
    "[Ошибка] Получение информации о чате по id",
)
@SANDBOX
def test_api_chats_get_by_id_error(
    admin_account,
    auth_account,
):
    with allure.step("Пробуем найти его в списке"), pytest.raises(RequestException):
        admin_account.api_chats_get_chat_id(
            auth_account.uin,
        )
