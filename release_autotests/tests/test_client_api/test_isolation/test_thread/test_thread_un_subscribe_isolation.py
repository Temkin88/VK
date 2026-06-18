import allure

from support.markers import SAAS, ISOLATION, PRE_SAAS


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Подписка на тред")
@allure.title("Подписка и отписка от треда в чате")
@ISOLATION
@PRE_SAAS
@SAAS
def test_subscribe_thread_isolation(
    prepared_thread_isolation,
):
    """
    Проверяем создание тредов
    """
    auth_account, opponent_account, chat, msg_id, thread_id = prepared_thread_isolation
    auth_account.send_basic_message(
        sn=thread_id,
        text="test",
    )

    with allure.step("Пытаемся отписаться от треда"):
        response = auth_account.rapi_thread_unsubscribe(
            threadId=thread_id,
        )

        assert response["status"]["code"] == 20000, (
            f"Failed to unsubscribe from thread from msgId {msg_id} in chat {chat}"
        )

    with allure.step("Пытаемся отписаться от треда оппонентом"):
        response = opponent_account.rapi_thread_unsubscribe(
            threadId=thread_id,
        )

        assert response["status"]["code"] == 20000, (
            f"Failed to unsubscribe from thread from msgId {msg_id} in chat {chat}"
        )

    with allure.step("Пытаемся подписаться на треда "):
        response = auth_account.rapi_thread_subscribe(
            threadId=thread_id,
        )

        assert response["status"]["code"] == 20000, f"Failed to subscribe to thread from msgId {msg_id} in chat {chat}"

    with allure.step("Пытаемся подписаться на треда оппонентом"):
        response = opponent_account.rapi_thread_subscribe(
            threadId=thread_id,
        )

        assert response["status"]["code"] == 20000, f"Failed to subscribe to thread from msgId {msg_id} in chat {chat}"
