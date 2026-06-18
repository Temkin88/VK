import allure
import pytest

from support.markers import SANDBOX


@allure.id("79679")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление группами и каналами")
@allure.title(
    "Смена роли пользователя",
)
@SANDBOX
@pytest.mark.parametrize(
    "chat_type",
    [
        "group",
        "channel",
    ],
)
def test_api_chats_update_member_role(
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
        response = auth_account.rapi_getChatInfo(sn=chat_id)
        assert response["results"]["you"]["role"] == "admin"

    with allure.step("Пробуем получить список участников чата"):
        admin_account.api_chats_update_member_role(
            chat_id=chat_id,
            member_sn=opponent_account.uin,
            role="creator",
        )
        response = auth_account.rapi_getChatInfo(sn=chat_id)
        assert response["results"]["you"]["role"] == "moder"
        response = opponent_account.rapi_getChatInfo(sn=chat_id)
        assert response["results"]["you"]["role"] == "admin"
