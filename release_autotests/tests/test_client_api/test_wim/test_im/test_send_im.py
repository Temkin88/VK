from typing import Optional

import allure
import lorem
import pytest

from support.cases.formatted_msgs import formatted_msgs
from support.cases.tasks import (
    TASK_TITLE_CASES,
    TASK_DURATION_CASES,
    TASK_ASSIGNEE_CASES,
    TASK_TAGS_CASES,
    TASK_PRIORITY_CASES,
    TASK_LABEL_CASES,
)
from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SLA, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import check_mentions_in_fetch_events
from tests.test_client_api.test_rapi.test_messaging.test_message_send.test_msg_quote import get_target_chat


@allure.id("26913")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений")
@allure.title("Отправка сообщений в чат")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_msg_sending(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Проверяем отправку сообщений
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправка тестового сообщения"):
        assert main_acc.send_basic_message(
            sn=chat,
            text=lorem.sentence(),
        ), f"Failed to send basic msg to chat ID {chat}"


@allure.id("26914")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений")
@allure.title("Отправка форматированного сообщения в чат")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
@pytest.mark.parametrize(
    "formatted_msg",
    formatted_msgs,
)
def test_formatted_msg_sending(
    chat_type,
    formatted_msg,
    prepare_test_chats_msg,
):
    """
    Проверяем отправку сообщений
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправка тестового сообщения"):
        assert main_acc.wim_im_sendIM(
            t=chat,
            parts=formatted_msg,
        ), f"Failed to send basic msg to chat ID {chat}"


@allure.id("26915")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Редактирование сообщения")
@allure.title("Редактирование сообщения в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_msg_edit(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Проверяем редактирование сообщений
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправка тестового сообщения"):
        msg_id = main_acc.send_basic_message(
            sn=chat,
            text="Test msg for edit",
        )

    with allure.step(f"Редактируем сообщение ID {msg_id}"):
        assert (
            main_acc.wim_im_sendIM(
                t=chat,
                updateMsgId=msg_id,
                message="Test",
            )["response"]["statusCode"]
            == 200
        )


@allure.id("26916")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка стикера")
@allure.title("Отправка стикера в чат")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_sticker_sending(
    chat_type,
    prepare_test_chats_msg,
    sticker,
):
    """
    Проверяем отправку стикера
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправка тестового сообщения"):
        assert main_acc.send_basic_message(
            sn=chat,
            text=sticker,
        )


@allure.id("26918")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка фото")
@allure.title("Отправка фото в чат")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_photo_sending(
    chat_type,
    prepare_test_chats_msg,
    photo,
):
    """
    Проверяем отправку фото
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем ссылку на файл"):
        assert main_acc.send_basic_message(
            sn=chat,
            text=photo,
        )


@allure.id("26919")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка фото с подписью")
@allure.title("Отправка фото с подписью в чат")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_photo_with_description_sending(
    chat_type,
    prepare_test_chats_msg,
    photo,
):
    """
    Проверяем отправку фото с подписью
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем ссылку на файл"):
        assert (
            main_acc.wim_im_sendIM(
                t=chat,
                parts=[
                    {
                        "mediaType": "text",
                        "text": "",
                        "captionedContent": {
                            "caption": "gwrgwrwger",
                            "url": photo,
                        },
                    }
                ],
            )["response"]["statusCode"]
            == 200
        )


@allure.id("26920")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка голосового")
@allure.title("Отправка голосового в чат")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_voice_record_sending(
    chat_type,
    prepare_test_chats_msg,
    voice,
):
    """
    Проверяем отправку голосового сообщения
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем ссылку на файл"):
        assert main_acc.send_basic_message(
            sn=chat,
            text=voice,
        )


@allure.id("26929")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Задачи")
@allure.feature("Создание задачи")
@allure.title("Создание задачи через /wim/sendIM")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("task_title", TASK_TITLE_CASES)
@pytest.mark.parametrize("task_duration", TASK_DURATION_CASES)
@pytest.mark.parametrize("task_assignee", TASK_ASSIGNEE_CASES)
@pytest.mark.parametrize("task_tags", TASK_TAGS_CASES)
@pytest.mark.parametrize("task_priority", TASK_PRIORITY_CASES)
@pytest.mark.parametrize("task_label", TASK_LABEL_CASES)
def test_task_add_by_sendIM(
    task_title,
    task_assignee,
    task_duration,
    task_tags,
    task_label,
    task_priority,
    opponent_account,
    auth_account,
):
    """
    Создание задачи
    """

    if task_assignee == "me":
        task_assignee = auth_account.uin
    elif task_assignee == "opponent":
        task_assignee = opponent_account.uin
    else:
        task_assignee = ""

    with allure.step("Отправляем запрос"):
        auth_account.task_add_by_sendIM(
            title=task_title,
            chat_id=opponent_account.uin,
            assignee=task_assignee,
            priority=task_priority,
            label=task_label,
            tags=task_tags,
        )


@allure.step("Подготовка: отправляем текстовое сообщение, чтобы потом использовать его для цитирования")
def send_msg_to_quote_it_later_via_sendIM(author_acc, target_chat, custom_plain_to_quote: Optional[str] = None):
    plain_to_quote = custom_plain_to_quote if custom_plain_to_quote else lorem.sentence()
    with allure.step(f"Отправка текстового сообщения в {target_chat} для последующего ответа на него"):
        author_sn = author_acc.uin
        text_msg_id = author_acc.send_basic_message(
            sn=target_chat,
            text=plain_to_quote,
        )
        assert text_msg_id, f"Failed to send basic msg to chat ID {target_chat}"
    return author_sn, plain_to_quote, text_msg_id


@allure.id("536187")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Проверка функционала ответа на сообщения")
@allure.title("Проверка появления меншенов в случае ответа в чате/ канале")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quote_with_quote_text_by_sendIM(chat_type, prepare_test_chats_msg):
    """
    Проверка появления меншенов в случае ответа в чате/ канале
    Является дублем теста для message/send allure.id("515286"), но только для sendIM
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    chat = get_target_chat(chat_type, opponent_acc.uin, group, channel)

    author_sn, plain_to_quote, text_msg_id = send_msg_to_quote_it_later_via_sendIM(opponent_acc, chat)

    with allure.step("Ответ на текстовое сообщение"):
        mentions_msg_id = main_acc.reply_message(
            sn=chat,
            author_sn=opponent_acc.uin,
            text=lorem.sentence(),
            quote=plain_to_quote,
            msg_id=text_msg_id,
        )

    """
    Меншн возникает только для чатов / каналов при ответе на сообщение
    """
    mention_occurs = chat_type != "private"
    check_mentions_in_fetch_events(
        mentions_msg_id,
        chat,
        opponent_acc,
        [opponent_acc.uin] if mention_occurs else [],
        mention_occurs,
    )
