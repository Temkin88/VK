import time

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("38603")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений")
@allure.title("Закрепление сообщения в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["favorite", "private", "group", "channel"])
@pytest.mark.parametrize("who_pin", ["sender", "receiver"])
def test_rapi_pin_message(
    chat_type,
    who_pin,
    prepare_test_chats,
    fetch_until_empty_answer_with_filter,
):
    """
    Проверяем добавление, наличие и удаление реакции к сообщению
    """

    main_acc, opponent, group, channel = prepare_test_chats

    if chat_type in ["favorite", "private"] and who_pin == "receiver":
        pytest.skip("Для избранного и привата нельзя проверить с типом receiver")

    if chat_type == "favorite":
        chat = main_acc.uin
    elif chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем тестовое сообщение"):
        msg_id = (
            main_acc.send_basic_message(
                sn=chat,
                text="Test msg for reactions",
            )
            if who_pin == "sender"
            else opponent.send_basic_message(
                sn=chat,
                text="Test msg for reactions",
            )
        )

    with allure.step(f"Пытаемся закрепить сообщение ID {msg_id}"):
        main_acc.rapi_pinMessage(
            sn=chat,
            msgId=msg_id,
        )

    with allure.step("Проверяем что сообщение закреплено"):
        account = main_acc if who_pin == "sender" else opponent
        for _ in range(3):
            message_event_text = False

            for event in fetch_until_empty_answer_with_filter(account, "histDlgState"):
                messages = event["eventData"]["tail"]["messages"]
                for message in messages:
                    message_text = message.get("text", "")

                    if message_text == "Message was pinned":
                        message_event_text = True
                        break
                if message_event_text:
                    break
            if message_event_text:
                break
            else:
                time.sleep(1)

        assert message_event_text, 'Message text "pong" not found'

    with allure.step(f"Пытаемся открепить сообщение ID {msg_id}"):
        main_acc.rapi_pinMessage(
            sn=chat,
            msgId=msg_id,
            unpin=True,
        )
