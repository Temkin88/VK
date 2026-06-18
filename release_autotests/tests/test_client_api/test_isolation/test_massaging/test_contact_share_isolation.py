import allure
import pytest

from support.markers import SAAS, ISOLATION, PRE_SAAS


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверяем отправку контакта")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_contact_isolation(
    chat_type,
    prepare_test_chats_msg_isolation,
):
    """
    Проверяем отправку контакта
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем контакт"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "contact": {
                        "name": opponent.client_name,
                        "phone": opponent.phone if opponent.phone else "79150001122",
                        "sn": opponent.uin,
                    },
                },
            },
        )
        assert response["status"]["code"] == 20000, f"Failed to send contact in chat ID {chat}"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверяем отправку контакта с неправильным именем")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_contact_with_invalid_name_isolation(
    chat_type,
    prepare_test_chats_msg_isolation,
):
    """
    Проверяем отправку контакта с неправильным именем
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем контакт с неправильным именем"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "contact": {
                        "name": "Misleading name",
                        "phone": opponent.phone if opponent.phone else "79150001122",
                        "sn": opponent.uin,
                    },
                },
            },
        )
        assert response["status"]["code"] == 20000, f"Failed to send contact in chat ID {chat}"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверяем отправку контакта с неправильным именем, номером и без sn")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_contact_with_invalid_name_and_invalid_phone_isolation(
    chat_type,
    prepare_test_chats_msg_isolation,
):
    """
    Проверяем отправку контакта с неправильным именем, номером и без sn
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "favorite":
        chat = main_acc.uin
    else:
        chat = channel

    """
    Такой тест отрабатывает с кодом 20000
        и провоцирует бесконечные /files/avatar/get на веб-клиенте
    Воспроизводится и на sendIM и на message/send
    """

    with allure.step("message/send: Отправляем контакт с неправильным именем, номером и без sn"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "contact": {
                        "name": "Misleading name",
                        "phone": "Not a phone at all",
                    },
                },
            },
        )
        assert response["status"]["code"] == 20000, f"Failed to send INVALID contact in chat ID {chat}"
        msg_id = response["results"]["msgId"]
        response = main_acc.rapi_delMsgBatch(sn=chat, msgIds=[msg_id], shared=True)
        assert response["status"]["code"] == 20000, f"Failed to delete message with INVALID contact in chat ID {chat}"

    with allure.step("sendIM: Отправляем контакт с неправильным именем, номером и без sn"):
        response = main_acc.wim_im_sendIM(
            t=chat,
            parts=[
                {
                    "mediaType": "text",
                    "text": "",
                    "contact": {
                        "name": "Misleading name",
                        "phone": "Not a phone at all",
                    },
                }
            ],
        )
        assert response["response"]["statusCode"] == 200, f"Failed to send INVALID contact in chat ID {chat}"
        msg_id = response["response"]["data"]["histMsgId"]
        response = main_acc.rapi_delMsgBatch(sn=chat, msgIds=[msg_id], shared=True)
        assert response["status"]["code"] == 20000, f"Failed to delete message with INVALID contact in chat ID {chat}"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверяем отправку контакта")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_contact_isolation_not_in_tenant(
    chat_type, prepare_test_chats_msg_isolation, first_auth_account_not_in_tenant, check_message_in_history
):
    """
    Проверяем отправку контакта
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем контакт пользователем не из тенанта"), pytest.raises(Exception):
        msg_id = first_auth_account_not_in_tenant.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "contact": {
                        "name": opponent.client_name,
                        "phone": opponent.phone if opponent.phone else "79150001122",
                        "sn": opponent.uin,
                    },
                },
            },
        )
        assert check_message_in_history(
            acc=main_acc,
            sn=chat,
            msg_id=msg_id,
        )


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверяем отправку контакта с неправильным именем")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_contact_with_invalid_name_isolation_not_in_tenant(
    chat_type, prepare_test_chats_msg_isolation, first_auth_account_not_in_tenant, check_message_in_history
):
    """
    Проверяем отправку контакта с неправильным именем
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем контакт с неправильным именем пользователем не из тенанта"), pytest.raises(Exception):
        msg_id = first_auth_account_not_in_tenant.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "contact": {
                        "name": "Misleading name",
                        "phone": opponent.phone if opponent.phone else "79150001122",
                        "sn": opponent.uin,
                    },
                },
            },
        )
        assert check_message_in_history(
            acc=main_acc,
            sn=chat,
            msg_id=msg_id,
        )


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверяем отправку контакта с неправильным именем, номером и без sn")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_contact_with_invalid_name_and_invalid_phone_isolation_not_in_tenant(
    chat_type, prepare_test_chats_msg_isolation, first_auth_account_not_in_tenant, check_message_in_history
):
    """
    Проверяем отправку контакта с неправильным именем, номером и без sn
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "favorite":
        chat = main_acc.uin
    else:
        chat = channel

    """
    Такой тест отрабатывает с кодом 20000
        и провоцирует бесконечные /files/avatar/get на веб-клиенте
    Воспроизводится и на sendIM и на message/send
    """

    with (
        allure.step(
            "message/send: Отправляем контакт с неправильным именем, номером и без sn пользователем не из тенанта"
        ),
        pytest.raises(Exception),
    ):
        msg_id = first_auth_account_not_in_tenant.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "contact": {
                        "name": "Misleading name",
                        "phone": "Not a phone at all",
                    },
                },
            },
        )
        assert check_message_in_history(
            acc=main_acc,
            sn=chat,
            msg_id=msg_id,
        )
    with (
        allure.step("sendIM: Отправляем контакт с неправильным именем, номером и без sn пользователем не из тенанта"),
        pytest.raises(Exception),
    ):
        msg_id = first_auth_account_not_in_tenant.wim_im_sendIM(
            t=chat,
            parts=[
                {
                    "mediaType": "text",
                    "text": "",
                    "contact": {
                        "name": "Misleading name",
                        "phone": "Not a phone at all",
                    },
                }
            ],
        )
        assert check_message_in_history(
            acc=main_acc,
            sn=chat,
            msg_id=msg_id,
        )
