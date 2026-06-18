import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("79712")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Отправка обычных сообщений пользователю")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_sendIM_without_parse_mode(
    start_bot,
    auth_account,
    bot_class,
    chat_type,
    prepare_bot_test_chats,
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


@allure.id("27472")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Отправка форматированных сообщений пользователю с parseMode HTML")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_sendIM_parse_mode_HTML(
    start_bot,
    auth_account,
    bot_class,
    chat_type,
    prepare_bot_test_chats,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Пробуем отправить тестовое сообщение"):
        response = bot_class.send_text(
            chat_id=chat,
            text='<a href="https://yandex.ru">Test msg [test_bot_sendIM]</a>',
            parse_mode="HTML",
        )

        auth_account.allure_attach(response)

        response_json = response.json()

        assert response_json.get("ok", False), response_json.get("description")


@allure.id("79703")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Отправка форматированных сообщений пользователю с parseMode MarkdownV2")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_sendIM_parse_mode_Markdown(
    start_bot,
    auth_account,
    bot_class,
    chat_type,
    prepare_bot_test_chats,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Пробуем отправить тестовое сообщение"):
        response = bot_class.send_text(
            chat_id=chat,
            text="[Test msg](https://yandex.ru/)",
            parse_mode="MarkdownV2",
        )

        auth_account.allure_attach(response)

        response.raise_for_status()

        response_json = response.json()

        assert response_json.get("ok", False), response_json.get("description")
