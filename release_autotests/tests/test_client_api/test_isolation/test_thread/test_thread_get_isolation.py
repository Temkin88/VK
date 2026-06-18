import allure

from support.markers import SAAS, ISOLATION, PRE_SAAS


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Треды")
@allure.feature("Информация о треде")
@allure.title("Информация о треде в чате")
@ISOLATION
@PRE_SAAS
@SAAS
def test_thread_get_isolation(prepared_thread_isolation):
    """
    Проверяем создание тредов
    """
    auth_account, opponent, chat, msg_id, threadId = prepared_thread_isolation
    with allure.step("Пытаемся получить информацию о треде"):
        response = auth_account.rapi_thread_get(
            threadId=threadId,
        )

        assert response["status"]["code"] == 20000, f"Failed to get thread info from msgId {msg_id} in chat {chat}"

        assert response["results"]["threadId"] == threadId, "Wrong threadId in thread info"

        assert response["results"]["parentTopic"]["chatId"] == chat, "Wrong parent topic in thread info"

        assert response["results"]["parentTopic"]["messageId"] == msg_id, "Wrong parent msgId in thread info"

    with allure.step("Пытаемся получить информацию о треде оппонентом"):
        response = opponent.rapi_thread_get(
            threadId=threadId,
        )

        assert response["status"]["code"] == 20000, f"Failed to get thread info from msgId {msg_id} in chat {chat}"

        assert response["results"]["threadId"] == threadId, "Wrong threadId in thread info"

        assert response["results"]["parentTopic"]["chatId"] == chat, "Wrong parent topic in thread info"

        assert response["results"]["parentTopic"]["messageId"] == msg_id, "Wrong parent msgId in thread info"
