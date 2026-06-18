import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("27479")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Редактирование отправленных сообщений")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_edit_basic_msg(
    start_bot,
    chat_type,
    auth_account,
    prepare_bot_test_chats,
    bot_class,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Пробуем отправить тестовое сообщение"):
        response = bot_class.send_text(
            chat_id=chat,
            text="Test msg [test_bot_sendIM]",
        )

        auth_account.allure_attach(response)

        response_json = response.json()

        assert response_json.get("ok", False), response_json.get("description")

    with allure.step("Пытаемся его отредактировать"):
        response = bot_class.edit_text(
            chat_id=chat,
            msg_id=response_json["msgId"],
            text="Test msg [test_bot_sendIM] edited",
        )

        auth_account.allure_attach(response)

        response_json = response.json()

        assert response_json.get("ok", False), response_json.get("description")


@allure.id("79700")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Редактирование отправленных сообщений c добавлением форматирования")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_edit_msg_with_format(
    start_bot,
    auth_account,
    chat_type,
    prepare_bot_test_chats,
    bot_class,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Пробуем отправить тестовое сообщение"):
        response = bot_class.send_text(
            chat_id=chat,
            text="Test msg [test_bot_sendIM]",
        )

        auth_account.allure_attach(response)

        response_json = response.json()

        assert response_json.get("ok", False), response_json.get("description")

    with allure.step("Пытаемся его отредактировать"):
        response = bot_class.edit_text(
            chat_id=chat,
            msg_id=response_json["msgId"],
            text='<a href="https://yandex.ru">Test msg [test_bot_sendIM]</a>',
            parse_mode="HTML",
        )

        auth_account.allure_attach(response)

        response_json = response.json()

        assert response_json.get("ok", False), response_json.get("description")
