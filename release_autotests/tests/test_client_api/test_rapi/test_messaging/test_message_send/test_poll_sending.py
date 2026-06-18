import allure

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS


@allure.id("515285")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки опроса с одним вариатом ответа")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_polls_by_message_send_with_one_answer(
    auth_account,
    opponent_account,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки опроса с одним вариатом ответа
    """

    chat = opponent_account.uin
    with allure.step("Создаем опрос с одним вариантом ответа"):
        send_msg_id, existing_poll_id = auth_account.send_poll_by_message_send(
            target=chat, poll_title="Да?", poll_type="anon", responses=["Да"]
        )
        assert existing_poll_id, f"Failed to create poll with 1 response in chat ID {chat}"
    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(auth_account, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        for account in [auth_account, opponent_account]:
            assert check_events_list_contains_event_with_msgId(account, send_msg_id), (
                f"Sended message not found in events of {account}"
            )


@allure.id("515301")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки опроса с двумя вариатом ответа")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_polls_by_message_send_with_two_answer(
    auth_account,
    opponent_account,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки опроса с одним вариатом ответа
    """

    chat = opponent_account.uin
    with allure.step("Создаем опрос с двумя вариантами ответов"):
        send_msg_id, existing_poll_id = auth_account.send_poll_by_message_send(
            target=chat, poll_title="Да или нет?", poll_type="public", responses=["Да", "Нет"]
        )
        assert existing_poll_id, f"Failed to create poll with 2 responses in chat ID {chat}"
    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(auth_account, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        for account in [auth_account, opponent_account]:
            assert check_events_list_contains_event_with_msgId(account, send_msg_id), (
                f"Sended message not found in events of {account}"
            )


@allure.id("515284")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки существующего опроса")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_polls_by_message_send_regular_poll(
    auth_account,
    opponent_account,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки обычного опроса
    """

    chat = opponent_account.uin
    with allure.step("Создаем опрос с двумя вариантами ответов"):
        send_msg_id, existing_poll_id = auth_account.send_poll_by_message_send(
            target=chat, poll_title="Да или нет?", poll_type="public", responses=["Да", "Нет"]
        )
        assert existing_poll_id, f"Failed to create poll with 2 responses in chat ID {chat}"

    with allure.step("Создаем опрос с несколькими вариантами ответов"):
        send_msg_id, existing_poll_id = auth_account.send_poll_by_message_send(
            target=chat,
            poll_title="Выбери число от 1 до 7",
            poll_type="anon",
            responses=[str(i) for i in range(1, 8)],
        )
        assert existing_poll_id, f"Failed to create poll with many responses in chat ID {chat}"
    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(auth_account, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        for account in [auth_account, opponent_account]:
            assert check_events_list_contains_event_with_msgId(account, send_msg_id), (
                f"Sended message not found in events of {account}"
            )


@allure.id("515292")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала отправки опросов")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_polls_by_message_send_existing_poll(
    auth_account,
    opponent_account,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка функционала отправки опросов
    """

    chat = opponent_account.uin
    with allure.step("Создаем опрос с одним вариантом ответа"):
        send_msg_id, existing_poll_id = auth_account.send_poll_by_message_send(
            target=chat, poll_title="Да?", poll_type="anon", responses=["Да"]
        )
        assert existing_poll_id, f"Failed to create poll with 1 response in chat ID {chat}"

    with allure.step("Отправка существующего опроса без подписи"):
        existing_poll_id = auth_account.send_existing_poll_by_message_send(
            target=chat, poll_title="Да?", existing_poll_id=existing_poll_id
        )
        assert existing_poll_id, f"Failed to send existing poll with 1 response in chat ID {chat}"

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(auth_account, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        for account in [auth_account, opponent_account]:
            assert check_events_list_contains_event_with_msgId(account, send_msg_id), (
                f"Sended message not found in events of {account}"
            )
