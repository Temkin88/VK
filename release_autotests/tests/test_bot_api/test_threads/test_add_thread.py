import allure
import pytest
import lorem
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("842935")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Создание треда к сообщению в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_add_thread(
    start_bot,
    auth_account,
    bot_class,
    chat_type,
    prepare_bot_test_chats,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем тестовое сообщение"):
        msg_response = bot_class.send_text(chat_id=chat, text=lorem.sentence()).json()

        msg_id = msg_response.get("msgId", None)

    with allure.step("Создаем тред"):
        response = bot_class.threads_add(chat_id=chat, msg_id=msg_id)
        auth_account.allure_attach(response)

        response.raise_for_status()

        response_json = response.json()

        assert response_json.get("ok", False), response_json.get("description")
