import allure
import lorem
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26912")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по определенному чату")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_search_one_dialog(
    chat_type,
    prepare_test_chats,
):
    """
    Проверяем поиск в определенном чате
    """
    main_acc, opponent, group, channel = prepare_test_chats

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

    with allure.step("Ищем сообщение по определенному чату"):
        response = main_acc.rapi_searchOneDialog(chat, text)

        assert response["status"]["code"] == 20000, "rapi_searchOneDialog - request failed"

        found = False

        for entry in response["results"]["entries"]:
            if entry["message"]["msgId"] == msg_id:
                found = True
                assert entry["message"]["outgoing"]
                assert entry["message"]["text"] == text

        assert found, f"Failed to found msg ID {msg_id} in chat ID {chat}"


@allure.id("28134")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по треду")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_search_thread(
    prepared_thread,
    auth_account,
):
    target, msg_id, thread_id = prepared_thread

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
