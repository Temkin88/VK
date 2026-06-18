import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26891")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Администрирование чата")
@allure.feature("Роль пользователя в чате")
@allure.title("Смена роли пользователя в чате")
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.parametrize("new_role", ["moder", "member", "readonly"])
def test_readonly_in_chat(
    chat_type,
    new_role,
    auth_account,
    opponent_account,
    prepare_test_chats_admin_readonly,
):
    """
    Readonly пользователя в чате
    """
    group, channel = prepare_test_chats_admin_readonly

    chat = group if chat_type == "group" else channel

    with allure.step("Пробуем дать новую роль участнику чата"):
        auth_account.rapi_modChatMember(
            memberSn=opponent_account.uin,
            sn=chat,
            role=new_role,
        )

    with allure.step("Проверяем что роль изменена"):
        response = auth_account.rapi_getChatInfo(sn=chat)
        role_opponent = list(filter(lambda x: x["sn"] == opponent_account.uin, response["results"]["members"]))

        assert role_opponent[0]["role"] == new_role, f"Role dont match with {new_role}"

    with allure.step("Возвращаем старую роль"):
        auth_account.rapi_modChatMember(
            memberSn=opponent_account.uin,
            sn=chat,
            role="member" if chat_type == "group" else "readonly",
        )

    with allure.step("Проверяем что роль изменена"):
        response = auth_account.rapi_getChatInfo(sn=chat)
        role_opponent = list(filter(lambda x: x["sn"] == opponent_account.uin, response["results"]["members"]))
        defaul_role = "member" if chat_type == "group" else "readonly"
    assert role_opponent[0]["role"] == defaul_role, f"Default role dont match with {defaul_role}"
