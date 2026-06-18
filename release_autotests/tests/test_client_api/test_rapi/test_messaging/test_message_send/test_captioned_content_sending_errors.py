import allure
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
    MessageIsTooBigException,
)

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    failed_message,
    msg_too_long_len,
)


@allure.id("515242")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка отправки файла с подписью, где вместо ссылки на фото обычный текст")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_captioned_content_sending_with_plain_text_as_url(chat_type, prepare_test_chats_msg, photo, third_account):
    """
    Попытка отправки файла с подписью, где вместо ссылки на фото обычный текст
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Пробуем отправить вместо ссылки на фото обычный текст"), pytest.raises(BadRequestException):
        main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "captionedContent": {
                        "url": "not a url text",
                        "caption": {"plain": failed_message},
                    },
                },
            },
        )


@allure.id("515241")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка отправки файла с подписью, где вместо ссылки на фото невалидная ссылка")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_captioned_content_sending_with_invalid_url(chat_type, prepare_test_chats_msg, photo, third_account):
    """
    Попытка отправки файла с подписью, где вместо ссылки на фото невалидная ссылка
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel
    with allure.step("Пробуем отправить вместо ссылки на фото невалидная ссылка"), pytest.raises(BadRequestException):
        main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "captionedContent": {
                        "url": photo.replace("devmail", "111"),
                        "caption": {"plain": failed_message},
                    },
                },
            },
        )


@allure.id("515243")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка отправки файла со слишком длинной подписью")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_captioned_content_sending_too_long_text(chat_type, prepare_test_chats_msg, photo, third_account):
    """
    Попытка отправки файла со слишком длинной подписью
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Пробуем отправить слишком длинную подпись к фото"), pytest.raises(MessageIsTooBigException):
        main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "captionedContent": {
                        "url": photo,
                        "caption": {"plain": failed_message + msg_too_long_len * "a"},
                    },
                },
            },
        )
