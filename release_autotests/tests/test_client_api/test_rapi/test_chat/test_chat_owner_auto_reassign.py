import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("2226160")
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
@allure.feature("Выход владельца из чата")
@allure.title("Автоматическая смена владельца чата")
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_owner_auto_reassign(
    chat_type,
    auth_account,
    opponent_account,
    prepare_test_chats_owner_auto_reassign,
    myteam_config,
):
    is_feature_enabled = (
        "assign-chat-owner-rights-enabled" in myteam_config
        and myteam_config["assign-chat-owner-rights-enabled"]
        and "chat-owner-auto-reassign-enabled" in myteam_config
        and myteam_config["chat-owner-auto-reassign-enabled"]
    )
    is_api_version_high_enough = "api-version" not in myteam_config or myteam_config["api-version"] >= 138
    if not (is_feature_enabled and is_api_version_high_enough):
        pytest.skip("Chat owner transfer is disabled")

    group, channel = prepare_test_chats_owner_auto_reassign
    chat = group if chat_type == "group" else channel

    with allure.step("Делаем участника чата админом"):
        assert auth_account.rapi_modChatMember(
            sn=chat,
            memberSn=opponent_account.uin,
            role="moder",
        )

    with allure.step("Удаляемся из чата"):
        assert auth_account.rapi_group_members_delete(
            sn=chat,
            members=[auth_account.uin],
        )

    with allure.step("Проверяем что владелец изменен"):
        response = opponent_account.rapi_getChatInfo(sn=chat)
        role_opponent = list(filter(lambda x: x["sn"] == opponent_account.uin, response["results"]["members"]))
        assert role_opponent[0]["role"] == "admin", "Role don't match with admin"

    with allure.step("Возвращаемся в чат"):
        chat_info_before_join = opponent_account.rapi_getChatInfo(sn=chat)
        stamp = chat_info_before_join["results"]["stamp"]
        response = auth_account.rapi_joinChat(stamp=stamp)
        assert response["status"]["code"] == 20000, "Response code error"

    with allure.step("Возвращаем прежнего владельца"):
        opponent_account.rapi_modChatMember(
            sn=chat,
            memberSn=auth_account.uin,
            role="owner",
        )

    with allure.step("Проверяем что владелец изменен"):
        response = auth_account.rapi_getChatInfo(sn=chat)
        role_opponent = list(filter(lambda x: x["sn"] == auth_account.uin, response["results"]["members"]))
        assert role_opponent[0]["role"] == "admin", "Role don't match with admin"
