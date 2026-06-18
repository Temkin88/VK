import allure
import pytest

from pyvkteamsclient.admin.exceptions import ServerException, RequestException
from support.markers import SANDBOX


@allure.id("79717")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление группами и каналами")
@allure.title(
    "Получение списка участников чата",
)
@SANDBOX
@pytest.mark.parametrize(
    "chat_type",
    [
        "group",
        "channel",
    ],
)
def test_api_chats_get_members_success(
    admin_account,
    chat_type,
    auth_account,
    opponent_account,
):
    members_list = [auth_account, opponent_account]

    with allure.step("Получаем ID чата"):
        chat_id = auth_account.create_chat(
            name=f"[{auth_account.getReqId()}]",
            members=members_list,
            defaultRole="member" if chat_type == "group" else "readonly",
        )

    with allure.step("Пробуем получить список участников чата"):
        response = admin_account.api_chats_get_chat_id_members(
            chat_id=chat_id,
        )
        response_members_list = [x["anketa"]["SN"] for x in response["result"]["members"]]

        assert all(member.uin in response_members_list for member in members_list), "Not all members listed"


@allure.id("79682")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление группами и каналами")
@allure.title(
    "[Ошибка] Получение списка участников чата",
)
@SANDBOX
@pytest.mark.parametrize("chat_type", ["bot", "private"])
def test_api_chats_get_members_error(
    admin_account,
    auth_account,
    bot_class,
    chat_type,
):
    with allure.step("Пробуем получить список участников чата"), pytest.raises((ServerException, RequestException)):
        admin_account.api_chats_get_chat_id_members(
            auth_account.uin if chat_type == "private" else bot_class.uin,
        )
