import time

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS


@allure.id("523301")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Отправка текстового сообщения на 15000 символов с пробелами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_text_sending_with_long_message(chat_type, bot_class, prepare_test_chats_msg):
    """
    Отправка текстового сообщения на 15000 символов с пробелами
    """
    message_len = 15000
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "bot":
        chat = bot_class.uin
    else:
        chat = channel

    lorem_100 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore."

    start = time.time()
    with allure.step(f"Отправка текстового сообщения на {message_len} символов с пробелами"):
        assert main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=lorem_100 * int(message_len / 100),
        ), f"Failed to send msg of {message_len} chars to chat ID {chat}"
    time_used = time.time() - start
    assert time_used < 1, f"Sending of {message_len} chars to chat ID {chat} message takes too long"


@allure.id("523298")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Отправка текстового сообщения на 15000 символов БЕЗ пробелов")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_text_sending_with_long_message_wo_spaces(chat_type, prepare_test_chats_msg):
    """
    Отправка текстового сообщения на 15000 символов БЕЗ пробелов
    https://jira.vk.team/browse/IMSERVER-19423
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    start = time.time()
    with allure.step("Отправка текстового сообщения на 15000 символов БЕЗ пробелов"):
        assert main_acc.send_basic_message_by_message_send(target=chat, plain="0123456789" * 1500), (
            f"Failed to send msg of 15000 chars wo spaces to chat ID {chat}"
        )
    time_used = time.time() - start
    assert time_used > 4, f"Sending of 15000 chars wo spaces to chat ID {chat} message is too fast"
