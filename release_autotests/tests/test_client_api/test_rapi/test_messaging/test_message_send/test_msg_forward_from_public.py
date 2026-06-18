from datetime import datetime

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    send_msg_to_forward_it_later,
    get_new_stamp,
)
from tests.test_client_api.test_rapi.test_messaging.test_message_send.test_msg_forward import (
    check_forwarded_from_info_in_fetch_events,
)


@allure.id("515273")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title(
    "Проверка пересылки из публичного чата/канала без stamp, без name: "
    "в фетчи автоматически подкладываются данные (stamp и name)"
)
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_forwards_from_public_chats_and_channels_wo_stamp_and_wo_name(
    chat_type, prepare_public_and_private_test_chats_msg, process_chat_infos
):
    """
    Проверка пересылки из публичного чата/канала без stamp, без name:
        в фетчи автоматически подкладываются данные (stamp и name)
    """
    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    _, public_info, private_info = process_chat_infos(main_acc, chat_type, chats)

    fwd_from_info = public_info
    fwd_to_info = private_info

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(opponent_acc, chat_type, fwd_from_info)

    fwd_to_chat_sn = fwd_to_info["sn"]

    with allure.step(f"message/send: Пересылка текстового сообщения из публичного {chat_type} без stamp, без name"):
        msg_id_to_check = main_acc.forward_message_by_message_send(
            target=fwd_to_chat_sn,
            author_sn=author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id,
            chat_sn_to_forward_from=fwd_from_info["sn"],
            need_stamp=False,
        )
        assert msg_id_to_check

    with allure.step(
        f"message/send: "
        f"Проверяем, что при пересылке из публичного {chat_type} без stamp, без name "
        f"в фетчи автоматически подкладываются данные {chat_type} (stamp и name)"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=opponent_acc,
            check_chat=fwd_to_chat_sn,
            msg_id=msg_id_to_check,
            chat_info=fwd_from_info,
        )

    with allure.step(f"sendIM: Пересылка текстового сообщения из публичного {chat_type} без stamp, без name"):
        response = main_acc.wim_im_sendIM(
            t=fwd_to_chat_sn,
            parts=[
                {
                    "mediaType": "forward",
                    "text": plain_to_forward,
                    "sn": author_sn,
                    "msgId": text_msg_id,
                    "time": int(datetime.now().timestamp()),
                    "chat": {"sn": fwd_from_info["sn"]},
                }
            ],
        )
        msg_id_to_check = response["response"]["data"]["histMsgId"]
        assert msg_id_to_check

    with allure.step(
        f"sendIM: "
        f"Проверяем, что при пересылке из публичного {chat_type} без stamp, без name "
        f"в фетчи автоматически подкладываются данные {chat_type} (stamp и name)"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=opponent_acc,
            check_chat=fwd_to_chat_sn,
            msg_id=msg_id_to_check,
            chat_info=fwd_from_info,
        )


@allure.id("515280")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Пересылка текстового сообщения из публичного чата/канала без stamp, с некорректным name")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_forwards_from_public_chats_and_channels_wo_stamp_and_with_incorrect_name(
    chat_type, prepare_public_and_private_test_chats_msg, process_chat_infos
):
    """
    Пересылка текстового сообщения из публичного чата/канала без stamp, с некорректным name
    """
    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    _, public_info, private_info = process_chat_infos(main_acc, chat_type, chats)

    fwd_from_info = public_info
    fwd_to_info = private_info

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(opponent_acc, chat_type, fwd_from_info)

    fwd_to_chat_sn = fwd_to_info["sn"]

    # 4.15
    with allure.step(
        f"message/send: Пересылка текстового сообщения из публичного {chat_type} без stamp, с некорректным name"
    ):
        msg_id_to_check = main_acc.forward_message_by_message_send(
            target=fwd_to_chat_sn,
            author_sn=author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id,
            chat_sn_to_forward_from=fwd_from_info["sn"],
            chat_name="Invalid chat name",
        )
        assert msg_id_to_check

    with allure.step(
        f"message/send: "
        f"Проверяем, что при пересылке из публичного {chat_type} без stamp, с некорректным name "
        f"в фетчи автоматически подкладываются данные {chat_type} (stamp и корректный name)"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=opponent_acc,
            check_chat=fwd_to_chat_sn,
            msg_id=msg_id_to_check,
            chat_info=fwd_from_info,
        )

    with allure.step(
        f"sendIM: Пересылка текстового сообщения из публичного {chat_type} без stamp, с некорректным name"
    ):
        response = main_acc.wim_im_sendIM(
            t=fwd_to_chat_sn,
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

    with allure.step(
        f"sendIM: "
        f"Проверяем, что при пересылке из публичного {chat_type} без stamp, с некорректным name "
        f"в фетчи автоматически подкладываются данные {chat_type} (stamp и корректный name)"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=opponent_acc,
            check_chat=fwd_to_chat_sn,
            msg_id=msg_id_to_check,
            chat_info=fwd_from_info,
        )


@allure.id("515274")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Пересылка текстового сообщения из публичного чата/канала после смены stamp")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_forwards_from_public_chats_and_channels_after_stamp_update(
    chat_type, prepare_public_and_private_test_chats_msg, process_chat_infos
):
    """
    Пересылка текстового сообщения из публичного чата/канала после смены stamp
    """

    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    _, public_info, private_info = process_chat_infos(main_acc, chat_type, chats)

    fwd_from_info = public_info
    fwd_to_info = private_info

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(opponent_acc, chat_type, fwd_from_info)

    """
    4.17 для приватного чата: /api/v129/rapi/suggestPrivateGroupStamp
                                   sn: "26277@chat.agent"
         для публичного чата: /api/v129/rapi/checkGroupStamp
                                   stamp: "new_stamp"
                               + /api/v129/rapi/modChat
                                   public: true
                                   sn: "26277@chat.agent"
                                   stamp: "new_stamp"
    """

    with allure.step(f"Обновляем stamp для публичного {chat_type}"):
        is_new_stamp_ok = False
        while is_new_stamp_ok is not True:
            new_public_stamp = get_new_stamp()
            response = main_acc.rapi_checkGroupStamp(
                stamp=new_public_stamp,
            )
            is_new_stamp_ok = response["status"]["code"] == 20000

        response = main_acc.mod_chat(sn=fwd_from_info["sn"], public=True, stamp=new_public_stamp)
        assert response["status"]["code"] == 20000, "Failed to modify chat"
        fwd_from_info["stamp"] = new_public_stamp

    with allure.step(f"message/send: Пересылка текстового сообщения из публичного {chat_type} с обновленным stamp"):
        msg_id_to_check = main_acc.forward_message_by_message_send(
            target=fwd_to_info["sn"],
            author_sn=author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id,
            chat_sn_to_forward_from=fwd_from_info["sn"],
            chat_stamp=fwd_from_info["stamp"],
        )
        assert msg_id_to_check

    with allure.step(
        f"message/send: "
        f"Проверяем, что при пересылке из публичного {chat_type} с обновленным stamp "
        f"в фетчи автоматически подкладываются данные {chat_type} (stamp и корректный name)"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=opponent_acc,
            check_chat=fwd_to_info["sn"],
            msg_id=msg_id_to_check,
            chat_info=fwd_from_info,
        )

    with allure.step(f"sendIM: Пересылка текстового сообщения из публичного {chat_type} с обновленным stamp"):
        response = main_acc.wim_im_sendIM(
            t=fwd_to_info["sn"],
            parts=[
                {
                    "mediaType": "forward",
                    "text": plain_to_forward,
                    "sn": author_sn,
                    "msgId": text_msg_id,
                    "time": int(datetime.now().timestamp()),
                    "chat": {"sn": fwd_from_info["sn"], "stamp": fwd_from_info["stamp"]},
                }
            ],
        )
        msg_id_to_check = response["response"]["data"]["histMsgId"]
        assert msg_id_to_check

    with allure.step(
        f"sendIM: "
        f"Проверяем, что при пересылке из публичного {chat_type} с обновленным stamp "
        f"в фетчи автоматически подкладываются данные {chat_type} (stamp и корректный name)"
    ):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=opponent_acc,
            check_chat=fwd_to_info["sn"],
            msg_id=msg_id_to_check,
            chat_info=fwd_from_info,
        )
