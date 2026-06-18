from time import sleep

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS


@allure.id("513355")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверяем отправку контакта")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_contact(
    chat_type,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверяем отправку контакта
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

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
    send_msg_id = response["results"]["msgId"]

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    sleep(20)

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        assert check_events_list_contains_event_with_msgId(opponent, send_msg_id), "Sended message not found in events"


@allure.id("515247")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверяем отправку контакта с неправильным именем")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_contact_with_invalid_name(
    chat_type,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверяем отправку контакта с неправильным именем
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

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


@allure.id("515248")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверяем отправку контакта с неправильным именем, номером и без sn")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_contact_with_invalid_name_and_invalid_phone(chat_type, prepare_test_chats_msg):
    """
    Проверяем отправку контакта с неправильным именем, номером и без sn
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
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
