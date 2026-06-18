from datetime import datetime

from pyvkteamsclient.client.exceptions import (
    BadRequestException,
)

import allure
import pytest


from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    failed_message,
    prepare_fwd_from_and_fwd_to_sns,
    send_msg_to_forward_it_later,
    send_msg_to_quote_it_later,
)


@allure.id("515295")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка ответа на сообщения при цитировании текстового и пересылаемого сообщения без ошибок в порядке")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["personal", "group", "channel"])
def test_quotes_and_forwards_simultaneous_correct_order(
    chat_type,
    prepare_test_chats_msg,
    prepare_public_and_private_test_chats_msg,
    third_account,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка функционала ответа на сообщения при цитировании текстового и пересылаемого сообщения

    Регулируется полем order в каждом part из массивов quoteParts и forwardParts.

    При одновременной отправке цитаты и пересылаемого сообщения добавляем в каждый из партов массивов
    quoteParts и forwardParts поле order c порядковым номером соответствующего парта.
    На основании значений в этих полях во front будут формироваться серверные парты в заданном порядке
    Поле order имеет тип int
    Order будет учитываться на сервере только при одновременном наличии элементов в quoteParts и forwardParts.

    При одновременном наличии элементов в quoteParts и forwardParts на сервере будут проверяться:
    1) Наличие поля order в каждом из партсов
    2) Корректность полученного порядка партсов, что значит уникальность элементов и отсутствие разрывов
        в упорядоченном списке номеров партсов, начало строго с нуля
    3) Значение параметра order должно строго монотонно увеличиваться внутри каждого массива партсов
        по мере продвижения по массиву.
    Это условие значит, что если в первом парте в массиве forwardParts параметр order = 2,
        то во втором элементе этого массива order > 2 (cтрого больше предыдущего) и аналогично далее

    В случае возникновения логических ошибок при построении упорядоченного списка партсов метод
        /rapi/message/send будет возвращать код ответа 40000

    Нумерация порядка будет начинаться с 0, те минимальное значение поля order равно 0
    """

    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    is_personal_chat, fwd_from, chat_fwd_to_and_quote_in = prepare_fwd_from_and_fwd_to_sns(
        opponent_acc, third_account, chats, chat_type
    )

    msg_to_fwd_author_sn, plain_to_forward, text_msg_id_for_fwd = send_msg_to_forward_it_later(
        opponent_acc, chat_type, {"sn": fwd_from, "public": True}
    )

    with allure.step("Пересылка текстового сообщения"):
        fwd_author_sn = main_acc.uin
        forward_msg_id = main_acc.forward_message_by_message_send(
            target=chat_fwd_to_and_quote_in,
            author_sn=msg_to_fwd_author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id_for_fwd,
            chat_sn_to_forward_from=None if is_personal_chat else fwd_from,
        )

    quote_author_sn, plain_to_quote, quote_msg_id = send_msg_to_quote_it_later(opponent_acc, chat_fwd_to_and_quote_in)

    with allure.step("Попытка отправки ответа на сообщение и пересылаемое сообщение одновременно"):
        response = main_acc.rapi_message_send(
            target=chat_fwd_to_and_quote_in,
            parts={
                "quoteParts": [
                    {
                        "text": {"plain": plain_to_quote},
                        "sn": quote_author_sn,
                        "msgId": quote_msg_id,
                        "time": int(datetime.now().timestamp()),
                        "order": 1,
                    },
                ],
                "forwardParts": [
                    {
                        "text": {"plain": plain_to_forward},
                        "sn": fwd_author_sn,
                        "msgId": forward_msg_id,
                        "time": int(datetime.now().timestamp()),
                        "order": 0,
                    },
                ],
                "mainPart": {
                    "text": {"plain": "Отвечаем на текстовое и пересылаемое сообщение"},
                },
            },
        )
    send_msg_id = response["results"]["msgId"]

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat_fwd_to_and_quote_in), (
            "Sended message not found in history"
        )
    opponent = opponent_acc
    if chat_type == "personal":
        opponent = third_account
    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        for account in [main_acc, opponent]:
            assert check_events_list_contains_event_with_msgId(account, send_msg_id), (
                f"Sended message not found in events of {account}"
            )


@allure.id("515303")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка ответа на сообщения при цитировании текстового и пересылаемого сообщения с ошибкой в порядке")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["personal", "group", "channel"])
def test_quotes_and_forwards_simultaneous_invalid_order(
    chat_type,
    prepare_test_chats_msg,
    prepare_public_and_private_test_chats_msg,
    third_account,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка функционала ответа на сообщения при цитировании текстового и пересылаемого сообщения с ошибкой в порядке

    Регулируется полем order в каждом part из массивов quoteParts и forwardParts.

    При одновременной отправке цитаты и пересылаемого сообщения добавляем в каждый из партов массивов
    quoteParts и forwardParts поле order c порядковым номером соответствующего парта.
    На основании значений в этих полях во front будут формироваться серверные парты в заданном порядке
    Поле order имеет тип int
    Order будет учитываться на сервере только при одновременном наличии элементов в quoteParts и forwardParts.

    При одновременном наличии элементов в quoteParts и forwardParts на сервере будут проверяться:
    1) Наличие поля order в каждом из партсов
    2) Корректность полученного порядка партсов, что значит уникальность элементов и отсутствие разрывов
        в упорядоченном списке номеров партсов, начало строго с нуля
    3) Значение параметра order должно строго монотонно увеличиваться внутри каждого массива партсов
        по мере продвижения по массиву.
    Это условие значит, что если в первом парте в массиве forwardParts параметр order = 2,
        то во втором элементе этого массива order > 2 (cтрого больше предыдущего) и аналогично далее

    В случае возникновения логических ошибок при построении упорядоченного списка партсов метод
        /rapi/message/send будет возвращать код ответа 40000

    Нумерация порядка будет начинаться с 0, те минимальное значение поля order равно 0
    """

    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    is_personal_chat, fwd_from, chat_fwd_to_and_quote_in = prepare_fwd_from_and_fwd_to_sns(
        opponent_acc, third_account, chats, chat_type
    )

    msg_to_fwd_author_sn, plain_to_forward, text_msg_id_for_fwd = send_msg_to_forward_it_later(
        opponent_acc, chat_type, {"sn": fwd_from, "public": True}
    )

    with allure.step("Пересылка текстового сообщения"):
        fwd_author_sn = main_acc.uin
        forward_msg_id = main_acc.forward_message_by_message_send(
            target=chat_fwd_to_and_quote_in,
            author_sn=msg_to_fwd_author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id_for_fwd,
            chat_sn_to_forward_from=None if is_personal_chat else fwd_from,
        )

    quote_author_sn, plain_to_quote, quote_msg_id = send_msg_to_quote_it_later(opponent_acc, chat_fwd_to_and_quote_in)

    with (
        allure.step(
            "Попытка отправки ответа на сообщение и пересылаемое сообщение "
            "одновременно. В одном из партов отсутсвует поле order"
        ),
        pytest.raises(BadRequestException),
    ):
        response = main_acc.rapi_message_send(
            target=chat_fwd_to_and_quote_in,
            parts={
                "quoteParts": [
                    {
                        "text": {"plain": plain_to_quote},
                        "sn": quote_author_sn,
                        "msgId": quote_msg_id,
                        "time": int(datetime.now().timestamp()),
                        "order": 0,
                    },
                ],
                "forwardParts": [
                    {
                        "text": {"plain": plain_to_forward},
                        "sn": fwd_author_sn,
                        "msgId": forward_msg_id,
                        "time": int(datetime.now().timestamp()),
                    },
                ],
                "mainPart": {
                    "text": {"plain": failed_message},
                },
            },
        )
        send_msg_id = response["results"]["msgId"]

        with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
            assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat_fwd_to_and_quote_in), (
                "Sended message not found in history"
            )

        with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
            for account in [main_acc, opponent_acc]:
                assert check_events_list_contains_event_with_msgId(account, send_msg_id), (
                    f"Sended message not found in events of {account}"
                )


# TODO(igor.kuleshov@vk.team): автотесты на порядок партсов в sendIM и message/send
