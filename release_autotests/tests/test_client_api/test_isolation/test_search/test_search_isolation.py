import random

import allure
import lorem
import pytest

from support.markers import SAAS, PRE_SAAS, ISOLATION


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по всем чатам")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_search_global_isolation(
    chat_type,
    prepare_test_chats_msg_isolation,
):
    """
    Проверяем поиск сообщений по всем чатам
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

    with allure.step("Ищем сообщение по всем чатам"):
        response = opponent.rapi_searchAllDialogs(text)

        assert response["status"]["code"] == 20000, "rapi_searchAllDialogs - request failed"

        found = False

        chat_for_find = chat
        if chat_type == "private":
            chat_for_find = main_acc.uin
        for dialog in filter(
            lambda x: x["sn"] == chat_for_find,
            response["results"]["dialogs"],
        ):
            for entry in filter(
                lambda x: x["message"]["msgId"] == msg_id,
                dialog["entries"],
            ):
                found = True
                assert entry["message"]["text"] == text

        assert found, f"Failed to found msg ID {msg_id} in chat ID {chat}"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск чатов")
@allure.title("Поиск чатов")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize(
    ("title", "chat_creator_fixture_name", "finder_fixture_name", "chats_key", "result"),
    [
        (
            "Ищем внутренний чат изнутри тенанта и находим",
            "first_auth_account_in_tenant",
            "second_auth_account_in_tenant",
            "public_groups",
            True,
        ),
        (
            "Ищем внутренний чат снаружи тенанта и не находим",
            "first_auth_account_in_tenant",
            "first_auth_account_not_in_tenant",
            "public_groups",
            False,
        ),
        (
            "Ищем внешний чат снаружи тенанта но в одном домене и находим",
            "first_auth_account_not_in_tenant",
            "second_auth_account_not_in_tenant",
            "public_groups_not_in_tenant",
            True,
        ),
        (
            "Ищем внешний чат изнутри тенанта и ненаходим",
            "first_auth_account_not_in_tenant",
            "first_auth_account_in_tenant",
            "public_groups_not_in_tenant",
            False,
        ),
    ],
)
def test_search_chat_isolation(
    ENV_PLATFORM, request, title, chat_creator_fixture_name, finder_fixture_name, chats_key, result
):
    """
    Проверяем поиск чатов
    """

    finder = request.getfixturevalue(finder_fixture_name)
    if ENV_PLATFORM == "PRE_SAAS":
        isolation_prepared_data = request.getfixturevalue("isolation_prepared_data")
        prepared_chats = isolation_prepared_data[chats_key]
        chat_sn = random.choice(list(prepared_chats.keys()))
        text = prepared_chats[chat_sn]["name"]
    else:
        chat_creator = request.getfixturevalue(chat_creator_fixture_name)
        text = f"Test chat [{chat_creator.getReqId()}]"
        chat_sn = chat_creator.create_chat(
            name=text,
            public=True,
        )

    with allure.step("Пробуем найти чаты"):
        response = finder.rapi_search(
            keyword=text,
        )

        chats_list = [x["sn"] for x in response["results"].get("chats", [])]

        assert response["status"]["code"] == 20000, "Response code error"
        assert (chat_sn in chats_list) == result, "Searching chat by full name failed"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск собщений по 3-м символам")
@allure.title("Поиск собщений по 3-м символам")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_search_two_symbol_isolation(
    chat_type,
    prepare_test_chats_msg_isolation,
):
    """
    Проверяем поиск сообщений по всем чатам по 3м символам
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

    with allure.step("Ищем сообщение по всем чатам"):
        response = opponent.rapi_searchAllDialogs(text[:2])

        assert response["status"]["code"] == 20000, "rapi_searchAllDialogs - request failed"
        if chat_type == "private":
            chat = main_acc.uin
        found = False
        for dialog in filter(
            lambda x: x["sn"] == chat,
            response["results"]["dialogs"],
        ):
            for entry in filter(
                lambda x: x["message"]["msgId"] == msg_id,
                dialog["entries"],
            ):
                if entry["message"]["text"] == text:
                    found = True
                    break

        assert found, f"Failed to found text. Text: {text}"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск чатов")
@allure.title("Поиск чатов с невалидными параметрами")
@ISOLATION
@PRE_SAAS
@SAAS
def test_search_isolation_not_in_tenant(
    prepare_test_chats_msg_isolation,
    first_auth_account_not_in_tenant,
):
    """
    Проверяем невалидные типы в поиске чатов
    """
    sender, _, group, _ = prepare_test_chats_msg_isolation
    response = sender.rapi_getChatInfo(sn=group)
    assert response["status"]["code"] == 20000, "Response code error"
    group_name = response["results"]["name"]
    with allure.step("Пробуем найти чаты пользователем не из тенанта"):
        response = first_auth_account_not_in_tenant.rapi_search(
            keyword=group_name,
        )
    assert response["status"]["code"] == 20000, "Response code error"
    chats_list = [x["sn"] for x in response["results"].get("chats", [])]
    assert group not in chats_list, "Success search"
