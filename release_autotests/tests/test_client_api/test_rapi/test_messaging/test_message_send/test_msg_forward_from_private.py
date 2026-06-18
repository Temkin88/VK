from datetime import datetime

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    send_msg_to_forward_it_later,
)
from tests.test_client_api.test_rapi.test_messaging.test_message_send.test_msg_forward import (
    check_forwarded_from_info_in_fetch_events,
)


@allure.id("515275")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Пересылка текстового сообщения из частного чата/канала с корректным stamp и без name")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_forwards_from_private_chats_and_channels_with_correct_stamp(
    chat_type, prepare_public_and_private_test_chats_msg, third_account, process_chat_infos
):
    """
    Пересылка текстового сообщения из частного чата/канала с корректным stamp и без name
    """

    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    _, public_info, private_info = process_chat_infos(main_acc, chat_type, chats)

    fwd_from_info = private_info
    fwd_to_info = public_info

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(opponent_acc, chat_type, fwd_from_info)

    # Enabling of stamp check is managed by compot variable front.message_send.check_stamp
    with allure.step(
        f"message/send: Пересылка текстового сообщения из частного {chat_type} с корректным stamp и без name"
    ):
        msg_id_to_check = main_acc.forward_message_by_message_send(
            target=fwd_to_info["sn"],
            author_sn=author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id,
            chat_sn_to_forward_from=fwd_from_info["sn"],
            chat_stamp=fwd_from_info["stamp"],
        )
        assert msg_id_to_check

    """
    # opponent_acc СОСТОИТ в приватной группе/ канале, откуда пересылали => ему придет name
    # Смотри prepare_public_and_private_test_chats_msg
    """
    with allure.step(
        f"message/send: "
        f"Проверяем, что при пересылке из частного {chat_type} автоматически "
        f"удаляется stamp и добавляется name, если получатель сообщения СОСТОИТ в частном {chat_type}"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=opponent_acc,
            check_chat=fwd_to_info["sn"],
            msg_id=msg_id_to_check,
            chat_sn=private_info["sn"],
            chat_name=private_info["name"],
        )

    """
    # third_account НЕ СОСТОИТ в приватной группе/ канале, откуда пересылали => ему НЕ придет name
    # Смотри prepare_public_and_private_test_chats_msg
    """
    with allure.step(
        f"message/send: "
        f"Проверяем, что при пересылке из частного {chat_type} автоматически "
        f"удаляется stamp и НЕ добавляется name, если получатель сообщения НЕ состоит в частном {chat_type}"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=third_account,
            check_chat=fwd_to_info["sn"],
            msg_id=msg_id_to_check,
            chat_sn=private_info["sn"],
        )

    with allure.step(f"sendIM: Пересылка текстового сообщения из частного {chat_type} с корректным stamp и без name"):
        msg_id_to_check = main_acc.forward_message(
            sn=fwd_to_info["sn"],
            author_sn=opponent_acc.uin,
            quote=plain_to_forward,
            msg_id=text_msg_id,
            old_sn=private_info["sn"],
        )
        assert msg_id_to_check

    """
    # opponent_acc СОСТОИТ в приватной группе/ канале, откуда пересылали => ему придет name
    # Смотри prepare_public_and_private_test_chats_msg
    """
    with allure.step(
        f"sendIM: "
        f"Проверяем, что при пересылке из частного {chat_type} автоматически "
        f"удаляется stamp и добавляется name, если получатель сообщения СОСТОИТ в частном {chat_type}"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=opponent_acc,
            check_chat=fwd_to_info["sn"],
            msg_id=msg_id_to_check,
            chat_sn=private_info["sn"],
            chat_name=private_info["name"],
        )

    """
    # third_account НЕ СОСТОИТ в приватной группе/ канале, откуда пересылали => ему НЕ придет name
    # Смотри prepare_public_and_private_test_chats_msg
    """
    with allure.step(
        f"sendIM: "
        f"Проверяем, что при пересылке из частного {chat_type} автоматически "
        f"удаляется stamp и НЕ добавляется name, если получатель сообщения НЕ состоит в частном {chat_type}"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=third_account,
            check_chat=fwd_to_info["sn"],
            msg_id=msg_id_to_check,
            chat_sn=private_info["sn"],
        )


@allure.id("515290")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Пересылка текстового сообщения из частного чата/канала без stamp и с некорректным name")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_forwards_from_private_chats_and_channels_wo_stamp_and_invalid_name(
    chat_type, prepare_public_and_private_test_chats_msg, third_account, process_chat_infos
):
    """
    Пересылка текстового сообщения из частного чата/канала без stamp и с некорректным name
    """

    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    _, public_info, private_info = process_chat_infos(main_acc, chat_type, chats)

    fwd_from_info = private_info
    fwd_to_info = public_info

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(opponent_acc, chat_type, fwd_from_info)

    with allure.step(
        f"message/send: Пересылка текстового сообщения из частного {chat_type} без stamp с некорректным name"
    ):
        msg_id_to_check = main_acc.forward_message_by_message_send(
            target=fwd_to_info["sn"],
            author_sn=author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id,
            chat_sn_to_forward_from=fwd_from_info["sn"],
            chat_name="Invalid chat name",
        )
        assert msg_id_to_check

    """
    # opponent_acc СОСТОИТ в приватной группе/ канале, откуда пересылали => ему придет name
    # Смотри prepare_public_and_private_test_chats_msg
    """
    with allure.step(
        f"message/send: "
        f"Проверяем, что при пересылке из частного {chat_type} "
        f"некорректное имя {chat_type} автоматически заменяется на корректное, "
        f"если получатель сообщения СОСТОИТ в частном {chat_type}"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=opponent_acc,
            check_chat=fwd_to_info["sn"],
            msg_id=msg_id_to_check,
            chat_sn=fwd_from_info["sn"],
            chat_name=fwd_from_info["name"],
        )

    """
    # third_account НЕ состоит в приватной группе/ канале, откуда пересылали => ему НЕ придет name
    # Смотри prepare_public_and_private_test_chats_msg
    """
    with allure.step(
        f"message/send: "
        f"Проверяем, что при пересылке из частного {chat_type} "
        f"некорректное имя {chat_type} автоматически УДАЛЯЕТСЯ, "
        f"если получатель сообщения НЕ состоит в частном {chat_type}"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=third_account,
            check_chat=fwd_to_info["sn"],
            msg_id=msg_id_to_check,
            chat_sn=fwd_from_info["sn"],
        )

    with allure.step(f"sendIM: Пересылка текстового сообщения из частного {chat_type} без stamp с некорректным name"):
        response = main_acc.wim_im_sendIM(
            t=fwd_to_info["sn"],
            parts=[
                {
                    "mediaType": "forward",
                    "text": plain_to_forward,
                    "sn": author_sn,
                    "msgId": text_msg_id,
                    "time": int(datetime.now().timestamp()),
                    "chat": {"sn": fwd_from_info["sn"], "name": "Invalid chat name"},
                }
            ],
        )
        msg_id_to_check = response["response"]["data"]["histMsgId"]
        assert msg_id_to_check

    """
    # opponent_acc СОСТОИТ в приватной группе/ канале, откуда пересылали => ему придет name
    # Смотри prepare_public_and_private_test_chats_msg
    """
    with allure.step(
        f"sendIM: "
        f"Проверяем, что при пересылке из частного {chat_type} "
        f"некорректное имя {chat_type} автоматически заменяется на корректное, "
        f"если получатель сообщения СОСТОИТ в частном {chat_type}"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=opponent_acc,
            check_chat=fwd_to_info["sn"],
            msg_id=msg_id_to_check,
            chat_sn=fwd_from_info["sn"],
            chat_name=fwd_from_info["name"],
        )

    """
    # third_account НЕ СОСТОИТ в приватной группе/ канале, откуда пересылали => ему НЕ придет name
    # Смотри prepare_public_and_private_test_chats_msg
    """
    with allure.step(
        f"sendIM: "
        f"Проверяем, что при пересылке из частного {chat_type} "
        f"некорректное имя {chat_type} автоматически УДАЛЯЕТСЯ, "
        f"если получатель сообщения НЕ состоит в частном {chat_type}"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=third_account,
            check_chat=fwd_to_info["sn"],
            msg_id=msg_id_to_check,
            chat_sn=fwd_from_info["sn"],
        )
