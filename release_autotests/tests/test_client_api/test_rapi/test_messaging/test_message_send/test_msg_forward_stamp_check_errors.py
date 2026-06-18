from datetime import datetime

import allure
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
    MissingParameterException,
)

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    send_msg_to_forward_it_later,
    get_new_stamp,
)


@allure.id("515276")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Пересылка текстового сообщения из публичного чата/канала с некорректным stamp")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_forwards_from_public_chats_and_channels_with_incorrect_stamp(
    chat_type, prepare_public_and_private_test_chats_msg, process_chat_infos
):
    """
    Пересылка текстового сообщения из публичного чата/канала с некорректным stamp
    """

    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    _, public_info, private_info = process_chat_infos(main_acc, chat_type, chats)

    fwd_from_info = public_info
    fwd_to_info = private_info

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(opponent_acc, chat_type, fwd_from_info)

    with (
        allure.step(f"message/send: Пересылка текстового сообщения из публичного {chat_type} с некорректным stamp"),
        pytest.raises(BadRequestException),
    ):
        main_acc.forward_message_by_message_send(
            target=fwd_to_info["sn"],
            author_sn=author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id,
            chat_sn_to_forward_from=fwd_from_info["sn"],
            chat_stamp="Invalid stamp!",
        )

    with (
        allure.step(f"sendIM: Пересылка текстового сообщения из публичного {chat_type} с некорректным stamp"),
        pytest.raises(MissingParameterException),
    ):
        main_acc.wim_im_sendIM(
            t=fwd_to_info["sn"],
            parts=[
                {
                    "mediaType": "forward",
                    "text": plain_to_forward,
                    "sn": author_sn,
                    "msgId": text_msg_id,
                    "time": int(datetime.now().timestamp()),
                    "chat": {"sn": fwd_from_info["sn"], "stamp": "Invalid stamp!"},
                }
            ],
        )


@allure.id("515277")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка пересылки текстового сообщения из публичного чата/канала с устаревшим stamp после смены stamp")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_forwards_from_public_chats_and_channels_with_old_stamp_after_change(
    chat_type, prepare_public_and_private_test_chats_msg, process_chat_infos
):
    """
    Попытка пересылки текстового сообщения из публичного чата/канала с устаревшим stamp после смены stamp
    """

    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    _, public_info, private_info = process_chat_infos(main_acc, chat_type, chats)

    fwd_from_info = public_info
    fwd_to_info = private_info

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(opponent_acc, chat_type, fwd_from_info)

    old_public_stamp = fwd_from_info["stamp"]
    with allure.step(f"Обновляем stamp для публичного {chat_type}"):
        is_new_stamp_ok = False
        while is_new_stamp_ok is not True:
            new_public_stamp = get_new_stamp()
            response = main_acc.rapi_checkGroupStamp(
                stamp=new_public_stamp,
            )

            is_new_stamp_ok = response["status"]["code"] == 20000

        response = main_acc.mod_chat(sn=fwd_from_info["sn"], public=True, stamp=new_public_stamp)["status"]["code"]
        assert response == 20000, "Failed to modify chat"
        fwd_from_info["stamp"] = new_public_stamp

    with (
        allure.step(
            f"message/send: "
            f"Пересылка текстового сообщения из публичного {chat_type} с устаревшим stamp после смены stamp"
        ),
        pytest.raises(BadRequestException),
    ):
        main_acc.forward_message_by_message_send(
            target=fwd_to_info["sn"],
            author_sn=author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id,
            chat_sn_to_forward_from=fwd_from_info["sn"],
            chat_stamp=old_public_stamp,
        )


@allure.id("515279")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка пересылки текстового сообщения из частного чата/канала с некорректным stamp")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_forwards_from_private_chats_and_channels_with_invalid_stamp(
    chat_type, prepare_public_and_private_test_chats_msg, process_chat_infos
):
    """
    Попытка пересылки текстового сообщения из частного чата/канала с некорректным stamp
    """

    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    _, public_info, private_info = process_chat_infos(main_acc, chat_type, chats)

    fwd_from_info = private_info
    fwd_to_info = public_info

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(opponent_acc, chat_type, fwd_from_info)

    # Testing forward from private chat: sending to private chat and forward it to public chat
    with (
        allure.step(f"message/send: Пересылка текстового сообщения из частного {chat_type} с некорректным stamp"),
        pytest.raises(BadRequestException),
    ):
        main_acc.forward_message_by_message_send(
            target=fwd_to_info["sn"],
            author_sn=author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id,
            chat_sn_to_forward_from=fwd_from_info["sn"],
            chat_stamp="Invalid stamp!",
        )

    with (
        allure.step(f"sendIM: Пересылка текстового сообщения из частного {chat_type} с некорректным stamp"),
        pytest.raises(MissingParameterException),
    ):
        main_acc.wim_im_sendIM(
            t=fwd_to_info["sn"],
            parts=[
                {
                    "mediaType": "forward",
                    "text": plain_to_forward,
                    "sn": author_sn,
                    "msgId": text_msg_id,
                    "time": int(datetime.now().timestamp()),
                    "chat": {"sn": fwd_from_info["sn"], "stamp": "Invalid stamp!"},
                }
            ],
        )
