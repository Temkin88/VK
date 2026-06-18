import allure
import lorem
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("37475")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Закрепление/открепление сообщения в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_pin_message(
    bot_class,
    prepare_bot_test_chats,
    chat_type,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем тестовое сообщение"):
        msg_id = (
            bot_class.send_text(
                chat_id=chat,
                text=lorem.sentence(),
            )
            .json()
            .get("msgId")
        )

    with allure.step("Пробуем закрепить сообщение в чате"):
        response = bot_class.pin_message(
            chat_id=chat,
            msg_id=msg_id,
        )

    with allure.step("Проверяем ответ"):
        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")

    with allure.step("Пробуем закрепить сообщение в чате"):
        response = bot_class.unpin_message(
            chat_id=chat,
            msg_id=msg_id,
        )

    with allure.step("Проверяем ответ"):
        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")
