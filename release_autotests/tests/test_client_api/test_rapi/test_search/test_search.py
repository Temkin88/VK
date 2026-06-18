import time

import allure
import lorem
import pytest

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26911")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по всем чатам")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_search_global(
    chat_type,
    prepare_test_chats,
):
    """
    Проверяем поиск сообщений по всем чатам
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

    with allure.step("Ищем сообщение по всем чатам"):
        response = main_acc.rapi_searchAllDialogs(text)

        assert response["status"]["code"] == 20000, "rapi_searchAllDialogs - request failed"

        found = False

        for dialog in filter(
            lambda x: x["sn"] == chat,
            response["results"]["dialogs"],
        ):
            for entry in filter(
                lambda x: x["message"]["msgId"] == msg_id,
                dialog["entries"],
            ):
                found = True
                assert entry["message"]["outgoing"]
                assert entry["message"]["text"] == text

        assert found, f"Failed to found msg ID {msg_id} in chat ID {chat}"


@allure.id("86572")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск чатов")
@allure.title("Поиск чатов")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_search(
    ENV_PLATFORM,
    auth_account,
    opponent_account,
):
    """
    Проверяем поиск чатов
    """
    text = f"Test chat [{auth_account.getReqId()}]"

    auth_account.create_chat(
        name=text,
        public=True,
    )

    time.sleep(15)

    with allure.step("Пробуем найти чаты"):
        response = opponent_account.rapi_search(
            keyword=text,
        )

        chats_list = [x["name"] for x in response["results"].get("chats", [])]

        assert response["status"]["code"] == 20000, "Response code error"
        assert text in chats_list, "Searching chat by full name failed"


@allure.id("571476")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск собщений по 2-м символам")
@allure.title("Поиск собщений по 2-м символам")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_search_two_symbol(
    chat_type,
    prepare_test_chats,
):
    """
    Проверяем поиск сообщений по всем чатам по 2м символам
    """
    main_acc, opponent, group, channel = prepare_test_chats

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем тестовое сообщение"):
        text = [lorem.sentence() for _ in range(2)]

        msg_id = [
            main_acc.send_basic_message(
                sn=chat,
                text=test_text,
            )
            for test_text in text
        ]

    with allure.step("Ищем сообщение по всем чатам"):
        response = main_acc.rapi_searchAllDialogs(text[0][:2])

        assert response["status"]["code"] == 20000, "rapi_searchAllDialogs - request failed"

        found = False
        found_text = False
        for dialog in filter(
            lambda x: x["sn"] == chat,
            response["results"]["dialogs"],
        ):
            for entry in filter(
                lambda x: x["message"]["msgId"] in msg_id,
                dialog["entries"],
            ):
                if entry["message"]["text"] == text[0] and entry["message"]["text"] != text[1]:
                    found_text = True
                    found = True
                    break
            if found_text and found:
                break

        assert found, f"Failed to found msg ID {msg_id} in chat ID {chat}"
        assert found_text, f"Failed to found text. Text: {found_text}"


@allure.id("86571")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск чатов")
@allure.title("Поиск чатов с невалидными параметрами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_param", [1234, [], {}, None])
def test_search_invalid_type(
    auth_account,
    invalid_param,
):
    """
    Проверяем невалидные типы в поиске чатов
    """
    with allure.step("Пробуем найти чаты с невалидными параметрами"), pytest.raises(BadRequestException):
        auth_account.rapi_search(
            keyword=invalid_param,
        )
