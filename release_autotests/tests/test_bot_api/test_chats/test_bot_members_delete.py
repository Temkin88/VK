import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("79648")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Удаление сотрудника в чате через Bot API")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_members_delete(
    bot_class,
    auth_account,
    opponent_account,
    chat_type,
):
    with allure.step("Создаем группу"):
        chat_id = auth_account.create_chat(
            name=f"[{auth_account.getReqId()}] Test group",
            members=[bot_class.uin, opponent_account],
            defaultRole="member" if chat_type == "group" else "readonly",
        )

    with allure.step("Выдаем боту админские права"):
        auth_account.rapi_modChatMember(
            sn=chat_id,
            memberSn=bot_class.uin,
            role="moder",
        )

    with allure.step("Пробуем добавить второго сотрудника через Bot API"):
        response = bot_class.delete_chat_members(
            chat_id=chat_id,
            members=[opponent_account.uin],
        ).json()

        assert response["ok"], f"{auth_account.env}:{response['description']}"

    with allure.step("Проверяем что сотрудник добавился"):
        response = auth_account.rapi_getChatInfo(sn=chat_id)

        assert opponent_account.uin not in [x["sn"] for x in response["results"]["members"]], (
            f"{auth_account.env}:Failed to delete user to group with Bot API"
        )
