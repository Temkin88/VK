import allure
import pytest
import lorem
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("842936")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Получение подписчиков треда")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.parametrize("page_size", [1, 2, 5])
def test_bot_get_threads_subscribers(
    start_bot,
    auth_account,
    bot_class,
    chat_type,
    page_size,
    prepare_bot_test_chats,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем тестовое сообщение"):
        msg_response = bot_class.send_text(chat_id=chat, text=lorem.sentence()).json()

        msg_id = msg_response.get("msgId", None)

    with allure.step("Создаем тред"):
        thread_response = bot_class.threads_add(
            chat_id=chat,
            msg_id=msg_id,
        ).json()

        thread_id = thread_response.get("threadId", None)

    with allure.step(f"Получаем подписчиков треда с page_size={page_size} и cursor=None"):
        response = bot_class.threads_get_subscribers(thread_id=thread_id, page_size=page_size, cursor=None)

        auth_account.allure_attach(response)

        response.raise_for_status()

        response_json = response.json()

        assert response_json.get("ok", False), response_json.get("description")

        cursor = response_json.get("cursor")

    with allure.step(f"Получаем следующую страницу подписчиков с cursor={cursor}"):
        response_paginated = bot_class.threads_get_subscribers(thread_id=thread_id, page_size=page_size, cursor=cursor)
        auth_account.allure_attach(response_paginated)

        response_paginated.raise_for_status()

        response_paginated_json = response_paginated.json()

        assert response_paginated_json.get("ok", False), response_paginated_json.get("description")
