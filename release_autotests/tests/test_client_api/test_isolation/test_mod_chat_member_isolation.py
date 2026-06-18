import allure
import pytest

from support.markers import SAAS, ISOLATION, PRE_SAAS
from contextlib import nullcontext as does_not_raise


@ISOLATION
@PRE_SAAS
@SAAS
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Администрирование чата")
@allure.feature("Роль пользователя в чате")
@allure.title("Смена роли пользователя в чате на админа")
@pytest.mark.parametrize(
    ("prepared_chats_fixture_name", "admin_fixture_name", "member_fixture_name", "exception_context"),
    [
        (
            "prepare_test_chats_msg_isolation",
            "first_auth_account_in_tenant",
            "second_auth_account_in_tenant",
            does_not_raise(),
        ),
        (
            "prepare_test_chats_msg_isolation",
            "first_auth_account_in_tenant",
            "first_auth_account_not_in_tenant",
            pytest.raises(Exception),
        ),
        (
            "prepare_test_chats_not_in_tenant_msg_isolation",
            "first_auth_account_not_in_tenant",
            "second_auth_account_not_in_tenant",
            does_not_raise(),
        ),
        (
            "prepare_test_chats_not_in_tenant_msg_isolation",
            "first_auth_account_not_in_tenant",
            "first_auth_account_in_tenant",
            pytest.raises(Exception),
        ),
        (
            "prepare_test_chats_not_in_tenant_msg_isolation",
            "first_auth_account_not_in_tenant",
            "second_auth_account_in_tenant",
            pytest.raises(Exception),
        ),
    ],
)
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_admin_in_chat_isolation(
    request, chat_type, admin_fixture_name, member_fixture_name, prepared_chats_fixture_name, exception_context
):
    """
    Readonly пользователя в чате
    """
    admin_acc = request.getfixturevalue(admin_fixture_name)
    member_acc = request.getfixturevalue(member_fixture_name)
    prepared_chats = request.getfixturevalue(prepared_chats_fixture_name)

    _, _, group, channel = prepared_chats

    if chat_type == "group":
        chat = group
        default_role = "member"
    else:
        chat = channel
        default_role = "readonly"

    with allure.step("Пробуем дать новую роль участнику чата"), exception_context:
        admin_acc.rapi_modChatMember(
            memberSn=member_acc.uin,
            sn=chat,
            role="moder",
        )

    if exception_context is not does_not_raise:
        return

    with allure.step("Проверяем что роль изменена"):
        response = admin_acc.rapi_getChatInfo(sn=chat)
        role_opponent = list(filter(lambda x: x["sn"] == member_acc.uin, response["results"]["members"]))
        assert role_opponent[0]["role"] == "moder", f"Role dont match with {'moder'}"

    with allure.step("Пробуем редактировать тестовый чат"):
        name = f"Modded {chat_type} - {request.node.name}"
        about = "Modded description"
        rules = "Modded rules"
        public = True
        join_moderation = False

        response = member_acc.mod_chat(
            sn=chat,
            name=name,
            about=about,
            rules=rules,
            public=public,
            joinModeration=join_moderation,
        )

        assert response["status"]["code"] == 20000, "Failed to edit chat text"

        response = admin_acc.rapi_getChatInfo(sn=chat)
        assert response["status"]["code"] == 20000, "Wrong status code"
        chat_info = response["results"]
        assert chat_info["creator"] == admin_acc.uin, f"Creator is'nt {admin_acc.uin}"
        assert chat_info["defaultRole"] == default_role
        assert chat_info["members"]
        assert chat_info.get("about", "") == about
        assert chat_info.get("rules", "") == rules

    with allure.step("Возвращаем старую роль"):
        admin_acc.rapi_modChatMember(
            memberSn=member_acc.uin,
            sn=chat,
            role="member" if chat_type == "group" else "readonly",
        )

    with allure.step("Проверяем что роль изменена"):
        response = admin_acc.rapi_getChatInfo(sn=chat)
        role_opponent = list(filter(lambda x: x["sn"] == member_acc.uin, response["results"]["members"]))
        defaul_role = "member" if chat_type == "group" else "readonly"
    assert role_opponent[0]["role"] == defaul_role, f"Default role dont match with {defaul_role}"
