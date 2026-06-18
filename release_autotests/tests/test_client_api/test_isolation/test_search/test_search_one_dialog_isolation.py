import allure
import lorem
import pytest

from support.markers import SAAS, PRE_SAAS, ISOLATION


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по определенному чату")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_search_one_dialog_isolation(
    chat_type,
    prepare_test_chats_msg_isolation,
):
    """
    Проверяем поиск в определенном чате
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем тестовое сообщение"):
        text = lorem.sentence()

        msg_id = main_acc.send_basic_message(
            sn=chat,
            text=text,
        )
    if chat_type == "private":
        chat = main_acc.uin
    with allure.step("Ищем сообщение по определенному чату"):
        response = opponent.rapi_searchOneDialog(chat, text)

        assert response["status"]["code"] == 20000, "rapi_searchOneDialog - request failed"

        found = False

        for entry in response["results"]["entries"]:
            if entry["message"]["msgId"] == msg_id:
                found = True
                assert entry["message"]["text"] == text

        assert found, f"Failed to found msg ID {msg_id} in chat ID {chat}"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по треду")
@ISOLATION
@PRE_SAAS
@SAAS
def test_search_thread(
    prepared_thread_isolation,
):
    auth_account, opponent_account, target, msg_id, thread_id = prepared_thread_isolation

    text = "Text for [test_search_one_dialog]"

    with allure.step("Пишем сообщение в тред"):
        thread_msg_id = auth_account.send_basic_message(
            sn=thread_id,
            text=text,
        )

    with allure.step("Ищем сообщение в потоке тредов"):
        result = auth_account.rapi_searchOneDialog(
            chatId=thread_id,
            filter_keyword=text,
        )

        entry_found_and_checked = False

        for entry in result["results"]["entries"]:
            message = entry["message"]
            if message["msgId"] == thread_msg_id and message["text"] == text:
                entry_found_and_checked = True

        assert entry_found_and_checked, (
            f"/api/v{auth_account.api_ver}/rapi/searchOneDialog:msg_not_found:{thread_msg_id}"
        )

    with allure.step("Пишем сообщение в тред"):
        thread_msg_id = opponent_account.send_basic_message(
            sn=thread_id,
            text=text,
        )

    with allure.step("Ищем сообщение в потоке тредов"):
        result = opponent_account.rapi_searchOneDialog(
            chatId=thread_id,
            filter_keyword=text,
        )

        entry_found_and_checked = False

        for entry in result["results"]["entries"]:
            message = entry["message"]
            if message["msgId"] == thread_msg_id and message["text"] == text:
                entry_found_and_checked = True

        assert entry_found_and_checked, (
            f"/api/v{opponent_account.api_ver}/rapi/searchOneDialog:msg_not_found:{thread_msg_id}"
        )


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по определенному чату")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_search_one_dialog_isolation_not_in_tenant(
    chat_type,
    prepare_test_chats_msg_isolation,
    first_auth_account_not_in_tenant,
):
    """
    Проверяем поиск в определенном чате
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем тестовое сообщение"):
        text = lorem.sentence()

        main_acc.send_basic_message(
            sn=chat,
            text=text,
        )

    with allure.step("Ищем сообщение по определенному чату"), pytest.raises(Exception):
        first_auth_account_not_in_tenant.rapi_searchOneDialog(chat, text)
