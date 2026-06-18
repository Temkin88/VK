import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("79645")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Получение списка премодераци чата через Bot API")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_get_and_resolve_pending_users(
    bot_class,
    auth_account,
    opponent_account,
    chat_type,
):
    with allure.step("Создаем группу"):
        chat_id = auth_account.create_chat(
            name=f"[{auth_account.getReqId()}] Test group",
            members=[bot_class.uin],
            defaultRole="member" if chat_type == "group" else "readonly",
        )
        stamp = auth_account.get_chat_stamp(chat_id)

    with allure.step("Выдаем боту админские права"):
        auth_account.rapi_modChatMember(
            sn=chat_id,
            memberSn=bot_class.uin,
            role="moder",
        )

    with allure.step("Пробуем добавиться в чат"):
        opponent_account.rapi_joinChat(stamp)

    with allure.step("Проверяем что сотрудник попал в список премодерации и не добавился в чат"):
        response = auth_account.rapi_getChatInfo(sn=chat_id)
        assert opponent_account.uin not in [x["sn"] for x in response["results"]["members"]], (
            f'{auth_account.env}:User added by "rapi/joinChat" without premoderation'
        )

        response = bot_class.get_chat_pending_users(chat_id=chat_id).json()
        assert opponent_account.uin in [x["userId"] for x in response["users"]], (
            f"{auth_account.env}:User not mentioned as pending"
        )

    with allure.step("Подтверждаем добавление сотрудника в чат"):
        response = bot_class.chat_resolve_pending(chat_id=chat_id, user_id=opponent_account.uin).json()
        assert response["ok"], f"{auth_account.env}:{response['description']}"

    with allure.step("Проверяем что сотрудник добавился в чат"):
        response = bot_class.get_chat_pending_users(chat_id=chat_id).json()
        assert opponent_account.uin not in [x["userId"] for x in response["users"]], (
            f"{auth_account.env}:User mentioned as pending"
        )

        response = auth_account.rapi_getChatInfo(sn=chat_id)
        assert opponent_account.uin in [x["sn"] for x in response["results"]["members"]], (
            f"{auth_account.env}:User not added by resolving premoderation"
        )
