import allure
import pytest

from support.markers import SANDBOX


@allure.id("79647")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Добавления сотрудника в чат через Bot API")
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_members_add(
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

    with allure.step("Выдаем боту админские права"):
        auth_account.rapi_modChatMember(
            sn=chat_id,
            memberSn=bot_class.uin,
            role="moder",
        )

    with allure.step("Пробуем добавить второго сотрудника через Bot API"):
        response = bot_class.add_chat_members(
            chat_id=chat_id,
            members=[opponent_account.uin],
        ).json()

        assert response["ok"], f"{auth_account.env}:{response['description']}"

    with allure.step("Пишем сообщение в чат от имени добавленного пользователя"):
        opponent_account.wim_im_sendIM(
            t=chat_id,
            message="text",
        )

    with allure.step("Проверяем что сотрудник добавился"):
        response = auth_account.rapi_getChatInfo(sn=chat_id)
        result_member = response["results"]["members"]

        assert opponent_account.uin in [x["sn"] for x in result_member], (
            f"{auth_account.env}:Failed to add user to group with Bot API"
        )
        assert all(lastseen["userState"]["lastseen"] >= 0 for lastseen in result_member), "Lastseen invalid"
