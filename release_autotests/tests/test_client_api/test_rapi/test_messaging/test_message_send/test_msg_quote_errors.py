from datetime import datetime

import allure
import lorem
import pytest

from pyvkteamsclient.client.exceptions import (
    BadRequestException,
    MessageIsTooBigException,
)

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    obviously_invalid_user_sn,
    send_msg_to_quote_it_later,
)
from tests.test_client_api.test_rapi.test_messaging.test_message_send.test_msg_quote import get_target_chat


@allure.id("515281")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала ответа на сообщения: очевидно невалидный sn автора пересылаемого сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quotes_with_obviously_invalid_quote_author_sn(chat_type, prepare_test_chats_msg):
    """
    Проверка функционала ответа на сообщения: очевидно невалидный sn автора пересылаемого сообщения
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    chat = get_target_chat(chat_type, opponent_acc.uin, group, channel)

    author_sn, plain_to_quote, text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat)

    with (
        allure.step("Ответ на текстовое сообщение очевидно невалидного юзеру"),
        pytest.raises(BadRequestException),
    ):
        main_acc.quote_message_by_message_send(
            target=chat,
            author_sn=obviously_invalid_user_sn,
            plain_text=lorem.sentence(),
            plain_to_quote=plain_to_quote,
            msg_id=text_msg_id,
        )


@allure.id("522848")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка ответа на сообщения на английском, суммарный размер которых слишком велик (лимит в front)")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_quotes_eng_text_with_resulting_parts_too_big(chat_type, bot_class, prepare_test_chats_msg):
    """
    Попытка ответа на сообщения на английском, суммарный размер которых слишком велик
    В этом тесте проверяет лимит на размер строкового представления parts_json в 64k во front,
        а не аналогичный лимит размера всего payload запроса в boss
    Текст на английском языке занимает меньше места, чем на русском,
        поэтому в этом тесте проверим, что ответ на 8 сообщений по 9000 английских букв
        НЕ пройдут лимит общей длины сторокого представления parts_json во front
        (грепать в imagine по "size limit in tlv16n_sl implementation")
    На английском нужно 8 сообщений по 9000
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    chat = get_target_chat(chat_type, opponent_acc.uin, group, channel)
    quote_parts = []
    with allure.step("Отправляем 8 сообщений по 9000 английских букв для последующей пересылки"):
        for i in range(1, 9):
            # len(tmp_plain_to_quote) = 9'000 потому что обычно на клиентах лимит на одно сообщение около 10'000
            tmp_plain_to_quote = (str(i) + "abcdefg ") * 1000
            assert len(tmp_plain_to_quote) == 9000, "Plain to quote len must be equal to 9'000"
            author_sn, _, tmp_text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat, tmp_plain_to_quote)
            quote_parts.append(
                {
                    "text": {"plain": tmp_plain_to_quote},
                    "sn": author_sn,
                    "time": int(datetime.now().timestamp()),
                    "msgId": tmp_text_msg_id,
                }
            )

    with (
        allure.step(
            "Ответ на 8 текстовых сообщений на английском языке, "
            "для которых общая длина строкового представления parts_json выше лимита в 64kb во front"
        ),
        pytest.raises(MessageIsTooBigException),
    ):
        main_acc.quote_message_by_message_send(target=chat, plain_text=lorem.sentence(), quote_parts=quote_parts)


@allure.id("823197")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка ответа на сообщения на английском, суммарный размер которых слишком велик (лимит в boss)")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_quotes_eng_text_with_resulting_payload_too_big(chat_type, bot_class, prepare_test_chats_msg):
    """
    Попытка ответа на сообщения на английском,
        суммарный размер которых слишком велик для лимита размера всего payload запроса в boss (~64kB),
        но проходит лимит на строковое представление parts_json во front

    После фикса бага IMSERVER-20468 в payload запроса в boss помимо parts_json кладется еще строка для поля im->message
        => отличине от теста выше в том, что ошибка messageTooBig появится именно из-за лимита в босе
            уже после 5 сообщений (там 8 сообщений не пройдут из-за лимита во front, те до боса запрос не дойдет)

    Текст на английском языке занимает меньше места, чем на русском,
    поэтому в этом тесте:
        1) Покажем, что 4 сообщений по 9000 английских букв пройдут по лимиту общего размера payload запроса в boss
        2) Проверим, что 5 сообщения по 9000 английских букв НЕ пройдут по лимиту общего размера payload запроса в boss
    На русском нужно 3 сообщения по 9000
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    chat = get_target_chat(chat_type, opponent_acc.uin, group, channel)
    quote_parts = []
    with allure.step("Отправляем 4 сообщения по 9000 английских букв для последующей пересылки"):
        for i in range(1, 5):
            # len(tmp_plain_to_quote) = 9'000 потому что обычно на клиентах лимит на одно сообщение около 10'000
            tmp_plain_to_quote = (str(i) + "abcdefg ") * 1000
            assert len(tmp_plain_to_quote) == 9000, "Plain to quote len must be equal to 9'000"
            author_sn, _, tmp_text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat, tmp_plain_to_quote)
            quote_parts.append(
                {
                    "text": {"plain": tmp_plain_to_quote},
                    "sn": author_sn,
                    "time": int(datetime.now().timestamp()),
                    "msgId": tmp_text_msg_id,
                }
            )

    with allure.step(
        "Ответ на 4 текстовых сообщений на английском языке, "
        "для которых общая длина строкового представления parts_json ниже лимита в 64kb"
    ):
        assert main_acc.quote_message_by_message_send(target=chat, plain_text=lorem.sentence(), quote_parts=quote_parts)

    with allure.step("Отправляем пятое сообщение длиной 9000 английских букв для последующей пересылки"):
        # len(tmp_plain_to_quote) = 9'000 потому что обычно на клиентах лимит на одно сообщение около 10'000
        tmp_plain_to_quote = (str(5) + "abcdefg ") * 1000
        assert len(tmp_plain_to_quote) == 9000, "Plain to quote len must be equal to 9'000"
        author_sn, _, tmp_text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat, tmp_plain_to_quote)
        quote_parts.append(
            {
                "text": {"plain": tmp_plain_to_quote},
                "sn": author_sn,
                "time": int(datetime.now().timestamp()),
                "msgId": tmp_text_msg_id,
            }
        )

    with (
        allure.step(
            "Ответ на 5 текстовых сообщений на английском языке, "
            "для которых общая длина строкового представления parts_json выше лимита в 64kb"
        ),
        pytest.raises(MessageIsTooBigException),
    ):
        main_acc.quote_message_by_message_send(target=chat, plain_text=lorem.sentence(), quote_parts=quote_parts)


@allure.id("522849")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка ответа на сообщения на русском, суммарный размер которых слишком велик (лимит в front)")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_quotes_rus_text_with_resulting_parts_too_big(chat_type, bot_class, prepare_test_chats_msg):
    """
    Попытка ответа на сообщения на русском, суммарный размер которых слишком велик
    В этом тесте проверяет лимит на размер строкового представления parts_json в 64k во front,
        а не аналогичный лимит размера всего payload запроса в boss
    Текст на русском языке занимает больше места (примерно в 2 раза, но будут использовать еще и пробелы),
        поэтому в этом тесте проверим, что ответ на 5 сообщений по 9000 русских букв
        НЕ пройдут лимит общей длины сторокого представления parts_json во front
        (грепать в imagine по "size limit in tlv16n_sl implementation")
    На английском нужно 8 сообщений по 9000
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    chat = get_target_chat(chat_type, opponent_acc.uin, group, channel)
    quote_parts = []
    with allure.step("Отправляем 5 сообщений по 9000 русских букв для последующей пересылки"):
        for i in range(1, 6):
            # len(tmp_plain_to_quote) = 9'000 потому что обычно на клиентах лимит на одно сообщение около 10'000
            tmp_plain_to_quote = (str(i) + "абвгдеж ") * 1000
            assert len(tmp_plain_to_quote) == 9000, "Plain to quote len must be equal to 9'000"
            author_sn, _, tmp_text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat, tmp_plain_to_quote)
            quote_parts.append(
                {
                    "text": {"plain": tmp_plain_to_quote},
                    "sn": author_sn,
                    "time": int(datetime.now().timestamp()),
                    "msgId": tmp_text_msg_id,
                }
            )

    with (
        allure.step(
            "Ответ на 5 текстовых сообщений на русском языке, "
            "для которых общая длина строкового представления parts_json выше лимита в 64kb во front"
        ),
        pytest.raises(MessageIsTooBigException),
    ):
        main_acc.quote_message_by_message_send(target=chat, plain_text=lorem.sentence(), quote_parts=quote_parts)


@allure.id("823198")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка ответа на сообщения на русском, суммарный размер которых слишком велик (лимит в boss)")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_quotes_rus_text_with_resulting_payload_too_big(chat_type, bot_class, prepare_test_chats_msg):
    """
    Попытка ответа на сообщения на русском,
        суммарный размер которых слишком велик для лимита размера всего payload запроса в boss (~64kB),
        но проходит лимит на строковое представление parts_json во front

    После фикса бага IMSERVER-20468 в payload запроса в boss помимо parts_json кладется еще строка для поля im->message
        => отличине от теста выше в том, что ошибка messageTooBig появится именно из-за лимита в босе
            уже после 3 сообщений (там 5 сообщений не пройдут из-за лимита во front, те до боса запрос не дойдет)

    Текст на русском языке занимает больше места (примерно в 2 раза, но будут использовать еще и пробелы),
    поэтому в этом тесте:
        1) Покажем, что 2 сообщений по 9000 русских букв пройдут по лимиту общего размера payload запроса в boss
        2) Проверим, что 3 сообщения по 9000 русских букв НЕ пройдут по лимиту общего размера payload запроса в boss
    На английском нужно 5 сообщений по 9000
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    chat = get_target_chat(chat_type, opponent_acc.uin, group, channel)
    quote_parts = []
    with allure.step("Отправляем 2 сообщений по 9000 русских букв для последующей пересылки"):
        for i in range(1, 3):
            # len(tmp_plain_to_quote) = 9'000 потому что обычно на клиентах лимит на одно сообщение около 10'000
            tmp_plain_to_quote = (str(i) + "абвгдеж ") * 1000
            assert len(tmp_plain_to_quote) == 9000, "Plain to quote len must be equal to 9'000"
            author_sn, _, tmp_text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat, tmp_plain_to_quote)
            quote_parts.append(
                {
                    "text": {"plain": tmp_plain_to_quote},
                    "sn": author_sn,
                    "time": int(datetime.now().timestamp()),
                    "msgId": tmp_text_msg_id,
                }
            )

    with allure.step(
        "Ответ на 2 текстовых сообщений на русском языке, "
        "для которых общий объем payload запроса в boss ниже лимита в 64kb"
    ):
        assert main_acc.quote_message_by_message_send(target=chat, plain_text=lorem.sentence(), quote_parts=quote_parts)

    with allure.step("Отправляем третье сообщение длиной 9000 русских букв для последующей пересылки"):
        # len(tmp_plain_to_quote) = 9'000 потому что обычно на клиентах лимит на одно сообщение около 10'000
        tmp_plain_to_quote = (str(3) + "абвгдеж ") * 1000
        assert len(tmp_plain_to_quote) == 9000, "Plain to quote len must be equal to 9'000"
        author_sn, _, tmp_text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat, tmp_plain_to_quote)
        quote_parts.append(
            {
                "text": {"plain": tmp_plain_to_quote},
                "sn": author_sn,
                "time": int(datetime.now().timestamp()),
                "msgId": tmp_text_msg_id,
            }
        )

    with (
        allure.step(
            "Ответ на 3 текстовых сообщения на русском языке, "
            "для которых общий объем payload запроса в boss выше лимита в 64kb"
        ),
        pytest.raises(MessageIsTooBigException),
    ):
        main_acc.quote_message_by_message_send(target=chat, plain_text=lorem.sentence(), quote_parts=quote_parts)
