import allure
import lorem
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
)

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    obviously_invalid_user_sn,
    prepare_fwd_from_and_fwd_to_sns,
    send_msg_to_forward_it_later,
)


@allure.id("513352")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка пересылки сообщения от очевидно невалидного юзера")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["personal", "group", "channel"])
def test_forwards_invalid_requests(chat_type, prepare_public_and_private_test_chats_msg, process_chat_infos):
    """
    Попытка пересылки сообщения от очевидно невалидного юзера
    """
    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    _, public_info, private_info = process_chat_infos(main_acc, chat_type, chats)

    fwd_from_info = private_info
    fwd_to_info = public_info

    is_personal_chat, fwd_from, fwd_to = prepare_fwd_from_and_fwd_to_sns(main_acc, opponent_acc, chats, chat_type)

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(
        opponent_acc, chat_type, {"sn": fwd_from, "public": True}
    )

    with (
        allure.step("Пересылка текстового сообщения очевидно невалидного юзера"),
        pytest.raises(BadRequestException),
    ):
        main_acc.forward_message_by_message_send(
            target=fwd_to_info["sn"],
            author_sn=obviously_invalid_user_sn,
            plain_to_forward=lorem.sentence(),
            msg_id=text_msg_id,
            chat_sn_to_forward_from=None if is_personal_chat else fwd_from_info["sn"],
        )
