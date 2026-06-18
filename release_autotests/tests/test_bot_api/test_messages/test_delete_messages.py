import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("27480")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Удаление отправленных сообщений")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_delete_msg(
    start_bot,
    auth_account,
    chat_type,
    prepare_bot_test_chats,
    bot_class,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Добавляем бота в чат"):
        auth_account.rapi_modChatMember(
            sn=chat,
            memberSn=bot_class.uin,
            role="admin",
        )

    with allure.step("Пробуем отправить тестовое сообщение"):
        response = bot_class.send_text(
            chat_id=chat,
            text="Test msg [test_bot_sendIM]",
        )

        auth_account.allure_attach(response)

        response_json = response.json()

        assert response_json.get("ok", False), response_json.get("description")

    with allure.step("Удаляем сообщение"):
        response = bot_class.delete_messages(
            chat_id=chat,
            msg_id=response_json["msgId"],
        )

        auth_account.allure_attach(response)

        response_json = response.json()

        assert response_json.get("ok", False), response_json.get("description")
