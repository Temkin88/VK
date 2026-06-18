import string
from datetime import datetime
from contextlib import nullcontext as does_not_raise
import allure
import lorem
import pytest

from support.markers import SAAS, PRE_SAAS, ISOLATION
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    set_draft_and_check_its_really_set,
    correct_message,
    check_draft_is_reset,
)


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки текстового сообщения")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize(
    ("title", "sender_fixture_name", "prepared_chats_fixture_name", "exception_context"),
    [
        (
            "Пользователь внутри тенанта пишет сообщение в чаты пользователей внутри тенанта",
            "first_auth_account_in_tenant",
            "prepare_test_chats_msg_isolation",
            does_not_raise(),
        ),
        (
            "Пользователь извне тенанта пишет сообщение в чаты пользователей внутри тенанта",
            "first_auth_account_not_in_tenant",
            "prepare_test_chats_msg_isolation",
            pytest.raises(Exception),
        ),
        (
            "Пользователь извне тенанта пишет сообщение в чаты пользователей извне тенанта но в совем домене",
            "first_auth_account_not_in_tenant",
            "prepare_test_chats_not_in_tenant_msg_isolation",
            does_not_raise(),
        ),
    ],
)
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_text_sending_basic_message_isolation(
    request,
    title,
    sender_fixture_name,
    prepared_chats_fixture_name,
    exception_context,
    chat_type,
    check_message_in_history,
):
    """
    Проверка отправки текстового сообщения
    """
    main_acc = request.getfixturevalue(sender_fixture_name)
    _, opponent, group, channel = request.getfixturevalue(prepared_chats_fixture_name)

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel
    text = lorem.sentence()
    with allure.step(title), exception_context:
        msg_id = main_acc.send_basic_message_by_message_send(target=chat, plain=text)
        assert msg_id, f"Failed to send msg to  {chat}"

        chat = main_acc.uin if chat_type == "private" else chat
        assert check_message_in_history(
            acc=opponent,
            sn=chat,
            msg_id=msg_id,
        ), "Сообщение не найдено"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка редактирования текстового сообщения")
@ISOLATION
@SAAS
@PRE_SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "favorite"])
def test_text_sending_edit_message_isolation(chat_type, prepare_test_chats_msg_isolation):
    """
    Проверка редактирования текстового сообщения
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "favorite":
        chat = main_acc.uin
    else:
        chat = channel

    with allure.step("Отправка сообщения, чтобы потом отредактировать его"):
        msg_id = main_acc.send_basic_message_by_message_send(
            target=chat,
            plain="Test msg for edit",
        )
        assert msg_id, f"Failed to send msg to edit it to chat ID {chat}"

    with allure.step(f"Редактируем сообщение ID {msg_id}"):
        response = main_acc.rapi_message_send(
            target=chat,
            updateMsgId=msg_id,
            parts={"mainPart": {"text": {"plain": "Test"}}},
        )
        assert msg_id == response["results"]["msgId"], f"Got unexpected msg_id[{msg_id}]"
        assert "updatePatchVersion" in response["results"], f"No updatePatchVersion in msg id[{msg_id}]"

    if "favorite" not in chat_type:
        with (
            allure.step(f"Редактируем вторым пользователем из тенанта сообщение ID {msg_id}"),
            pytest.raises(Exception),
        ):
            response = opponent.rapi_message_send(
                target=chat,
                updateMsgId=msg_id,
                parts={"mainPart": {"text": {"plain": "Test opponent"}}},
            )
            assert msg_id == response["results"]["msgId"], f"Got unexpected msg_id[{msg_id}]"
            assert "updatePatchVersion" in response["results"], f"No updatePatchVersion in msg id[{msg_id}]"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки текстового сообщения, которое должно сбросить черновик")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "favorite"])
def test_text_sending_and_draft_reset_isolation(chat_type, prepare_test_chats_msg_isolation, is_draft_enabled):
    """
    Проверка отправки текстового сообщения, которое должно сбросить черновик
    """

    if not is_draft_enabled:
        pytest.skip("Drafts are disabled in myteam-config")

    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "favorite":
        chat = main_acc.uin
    else:
        chat = channel

    set_draft_and_check_its_really_set(main_acc, chat)

    # Enabling of draft reset after success message send is managed
    #   by compot variable front.message_send.draft_delete_time_enabled
    with allure.step("Отправка текстового сообщения, которое должно сбросить черновик"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={"mainPart": {"text": {"plain": correct_message}}},
            draftDeleteTime=int(datetime.now().timestamp()),
        )
        assert response["status"]["code"] == 20000, f"Failed to reset draft in chat ID {chat}"

    check_draft_is_reset(main_acc, chat)


@allure.step("Проверяем reqId во входящих событиях о сообщении")
def check_reqId_in_fetch_events(msg_id, chat, auth_account, req_id: string):
    auth_account.events = []
    for i in range(1, 6):
        auth_account.fetch(timeout=i * 100)

    for event in filter(
        lambda x: x["type"] == "histDlgState" and x["eventData"].get("sn") == chat,
        auth_account.events[::-1],
    ):
        for cur_part in ("eventData", "tail", "intro"):
            event_data_to_check = event["eventData"]
            if cur_part != "eventData" and cur_part in event_data_to_check:
                event_data_to_check = event_data_to_check[cur_part]
            for message in event_data_to_check.get("messages", []):
                if message["msgId"] == msg_id:
                    if "reqId" not in message or message["reqId"] != req_id:
                        pytest.fail("failed to find reqId in histDlgState for msg_id ", msg_id)
                    # if nothing was raised before this line then the check is passed
                    return


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка редактирования текстового сообщения")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "favorite"])
def test_text_sending_edit_message_isolation_not_in_tenant(
    chat_type, prepare_test_chats_msg_isolation, first_auth_account_not_in_tenant
):
    """
    Проверка редактирования текстового сообщения
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "favorite":
        chat = main_acc.uin
    else:
        chat = channel

    with allure.step("Отправка сообщения, чтобы потом отредактировать его"):
        msg_id = main_acc.send_basic_message_by_message_send(
            target=chat,
            plain="Test msg for edit",
        )
        assert msg_id, f"Failed to send msg to edit it to chat ID {chat}"

    with allure.step(f"Редактируем сообщение ID {msg_id} пользователем не из тенанта"), pytest.raises(Exception):
        first_auth_account_not_in_tenant.rapi_message_send(
            target=chat,
            updateMsgId=msg_id,
            parts={"mainPart": {"text": {"plain": "Test"}}},
        )


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки текстового сообщения, которое должно сбросить черновик")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "favorite"])
def test_text_sending_and_draft_reset_isolation_not_in_tenant(
    chat_type,
    prepare_test_chats_msg_isolation,
    is_draft_enabled,
    first_auth_account_not_in_tenant,
    check_message_in_history,
):
    """
    Проверка отправки текстового сообщения, которое должно сбросить черновик
    """

    if not is_draft_enabled:
        pytest.skip("Drafts are disabled in myteam-config")

    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    set_draft_and_check_its_really_set(main_acc, chat)

    with (
        allure.step("Отправка текстового сообщения, которое должно сбросить черновик пользователем не из тенанта"),
        pytest.raises(Exception),
    ):
        msg_id = first_auth_account_not_in_tenant.rapi_message_send(
            target=chat,
            parts={"mainPart": {"text": {"plain": correct_message}}},
            draftDeleteTime=int(datetime.now().timestamp()),
        )
        assert check_message_in_history(
            acc=main_acc,
            sn=chat,
            msg_id=msg_id,
        )
