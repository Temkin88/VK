import hashlib
import os
from typing import Optional

import allure
import lorem
import pytest

correct_message = "обычное сообщение"
failed_message = "Сообщение невалидно! НЕ ДОЛЖНО ПОЯИВТЬСЯ В ПЕРЕПИСКЕ!"
msg_too_long_len = 64000 + 1

formally_ok_but_invalid_user_sn = "123@invalid.com"
obviously_invalid_user_sn = "111e"


def correct_message_with_mentions(users_to_mention: list[str]):
    mentions_string = ", ".join(f"@[{user}]" for user in users_to_mention)
    return correct_message + mentions_string


@allure.step("Проверяем меншены во входящих событиях о сообщении")
def check_mentions_in_fetch_events(
    msg_id,
    receive_mention_from_chat,
    auth_account,
    mentioned_users: list,
    check_mention_me_event: bool = False,
    unread_mention_me_count: Optional[int] = None,
):
    auth_account.events = []
    for i in range(1, 6):
        auth_account.fetch(timeout=i * 100)

    success_checks = [False, False]
    histDlgStateSucessIdx = 0
    mentionMeSucessIdx = 1

    event_types_to_check = ["histDlgState"]
    if check_mention_me_event:
        event_types_to_check.append("mentionMeMessage")

    # TODO(@igor.kuleshov): Ловушка в том, что может прийти ивент mentionMeMessage,
    #   но в histDlgState поля mentions не будет, только "unreadMentionMeCount": 1,

    for event_type in event_types_to_check:
        for event in filter(
            lambda x: x["type"] == event_type and x["eventData"].get("sn") == receive_mention_from_chat,
            auth_account.events[::-1],
        ):
            is_cur_event_hist_dlg_state = event_type == "histDlgState"
            for cur_part in ("eventData", "tail", "intro"):
                event_data_to_check = event["eventData"]
                if cur_part != "eventData":
                    if event_type == "mentionMeMessage":
                        continue
                    elif cur_part in event_data_to_check:
                        event_data_to_check = event_data_to_check[cur_part]

                messages = (
                    event_data_to_check.get("messages", [])
                    if event_type == "histDlgState"
                    else [event_data_to_check.get("message", {})]
                )
                for message in messages:
                    if "msgId" in message and message["msgId"] == msg_id and "mentions" in message:
                        if len(mentioned_users) == 0:
                            pytest.fail("unexpected mentions in histDlgState")
                        mentions_list = message["mentions"]
                        if all(user in mentions_list for user in mentioned_users):
                            if is_cur_event_hist_dlg_state and unread_mention_me_count is not None:
                                parsed_unread_mention_me_count = event["eventData"].get("unreadMentionMeCount", -1)
                                if parsed_unread_mention_me_count != unread_mention_me_count:
                                    pytest.fail(
                                        f"In histDlgState event for msg_id {msg_id} "
                                        f"unexpected unreadMentionMeCount [{parsed_unread_mention_me_count}], "
                                        f"expected [{unread_mention_me_count}]"
                                    )
                            if not check_mention_me_event:
                                return
                            # if nothing was raised before this line then the check is passed
                            success_checks[
                                histDlgStateSucessIdx if is_cur_event_hist_dlg_state else mentionMeSucessIdx
                            ] = True

    if not all(success_checks) and len(mentioned_users) != 0:
        additional_check_log = "and mentionMeMessage " if check_mention_me_event else ""
        pytest.fail(f"failed to find mentions in histDlgState {additional_check_log}event for msg_id {msg_id}")


@allure.step("Проверяем сохранение черновика")
def set_draft_and_check_its_really_set(main_acc, chat):
    with allure.step("Сохраняем черновике"):
        response = main_acc.rapi_draft_set(
            sn=chat,
            parts=[{"mediaType": "text", "text": "Сообщение черновик"}],
        )
        assert response["status"]["code"] == 20000, "Failed to set draft"

    main_acc.events = []
    for i in range(1, 6):
        main_acc.fetch(timeout=i * 100)

    with allure.step("Проверяем что пришло событие черновика"):
        for event in filter(
            lambda x: x["type"] == "draft" and x["eventData"].get("sn") == chat,
            main_acc.events[::-1],
        ):
            if "parts" in event["eventData"] and len(event["eventData"]["parts"]) > 0:
                return
        else:
            pytest.fail("Failed to found draft event")


@allure.step("Проверяем что черновик сброшен")
def check_draft_is_reset(main_acc, chat):
    main_acc.events = []
    for i in range(1, 6):
        main_acc.fetch(timeout=i * 100)

    for event in filter(
        lambda x: x["type"] == "draft" and x["eventData"].get("sn") == chat,
        main_acc.events[::-1],
    ):
        if "parts" in event["eventData"] and len(event["eventData"]["parts"]) == 0:
            return
    else:
        pytest.fail("failed to found empty draft event")


@allure.step("Проверяем что черновик сохранился")
def check_draft_is_kept(main_acc, chat):
    main_acc.events = []
    for i in range(1, 6):
        main_acc.fetch(timeout=i * 100)

    for event in main_acc.events[::-1]:
        if event["type"] == "draft" and event["eventData"].get("sn") == chat and len(event["eventData"]["parts"]) == 0:
            pytest.fail("Invalid draft reset")


def prepare_fwd_from_and_fwd_to_sns(opponent_acc, third_acc, chats, chat_type):
    public_group, public_channel, private_group, private_channel = chats
    is_personal_chat = False
    if chat_type == "personal":
        is_personal_chat = True
        chat_fwd_from = opponent_acc.uin
        fwd_to = third_acc.uin
    elif chat_type == "group":
        chat_fwd_from = public_group
        fwd_to = private_group
    else:
        chat_fwd_from = public_channel
        fwd_to = private_channel

    return is_personal_chat, chat_fwd_from, fwd_to


@allure.step("Подготовка: отправляем текстовое сообщение, чтобы потом использовать его для пересылки")
def send_msg_to_forward_it_later(author_acc, chat_type, chat_info):
    is_personal = chat_type != "personal"
    is_public = not is_personal and "public" in chat_info and chat_info["public"] is True

    send_to = f"{' в ' if is_personal else (' в публичный ' if is_public else ' в частный ')} {chat_type}"
    forward_to = f"{' в ' if is_personal else (' в частный ' if is_public else ' в публичный ')} {chat_type}"

    plain_to_forward = lorem.sentence()
    with allure.step(f"Отправка текстового сообщения {send_to} для последующей его пересылки {forward_to}"):
        author_sn = author_acc.uin
        text_msg_id = author_acc.send_basic_message_by_message_send(
            target=chat_info["sn"],
            plain=plain_to_forward,
        )
        assert text_msg_id, f"Failed to send basic msg to chat ID {chat_info['sn']}"
    return author_sn, plain_to_forward, text_msg_id


@allure.step("Подготовка: отправляем текстовое сообщение, чтобы потом использовать его для цитирования")
def send_msg_to_quote_it_later(author_acc, target_chat, custom_plain_to_quote: Optional[str] = None):
    plain_to_quote = custom_plain_to_quote if custom_plain_to_quote else lorem.sentence()
    with allure.step(f"Отправка текстового сообщения в {target_chat} для последующего ответа на него"):
        author_sn = author_acc.uin
        text_msg_id = author_acc.send_basic_message_by_message_send(
            target=target_chat,
            plain=plain_to_quote,
        )
        assert text_msg_id, f"Failed to send basic msg to chat ID {target_chat}"
    return author_sn, plain_to_quote, text_msg_id


def check_forwarded_from_info_in_fetch_events(
    account_to_fetch,
    check_chat,
    msg_id,
    author_sn: Optional[str] = None,
    need_to_check_chat_info: bool = True,
    chat_sn: Optional[str] = None,
    chat_stamp: Optional[str] = None,
    chat_name: Optional[str] = None,
    chat_info: Optional[dict[str, str]] = None,
):
    """
    Проверка содержимого histDlgState ивента с указанным msg_id о пересылаемом сообщении
    Если какой-то из параметров chat_sn, chat_stamp или chat_name (которые могут быть получены и из chat_info)
        есть в вызове функции, но нет в ивенте, то ошибка,
        и если вызове функции нет параметро, но есть в ивенте, то тоже ошибка
    """
    if chat_info:
        chat_sn = chat_info["sn"]
        chat_stamp = chat_info.get("stamp", None)
        chat_name = chat_info.get("name", None)
    elif need_to_check_chat_info:
        assert chat_sn is not None, "chat_sn is None while need_to_check_chat_info==True"
    else:
        assert author_sn is not None, "author_sn is None"

    account_to_fetch.events = []
    for i in range(1, 6):
        account_to_fetch.fetch(timeout=i * 100)

    for event in filter(
        lambda x: x["type"] == "histDlgState" and x["eventData"].get("sn") == check_chat,
        account_to_fetch.events[::-1],
    ):
        for cur_part in ("eventData", "tail", "intro"):
            event_data_to_check = event["eventData"]
            if cur_part != "eventData" and cur_part in event_data_to_check:
                event_data_to_check = event_data_to_check[cur_part]
            for message in event_data_to_check.get("messages", []):
                if message["msgId"] != msg_id:
                    continue
                for part in message.get("parts", []):
                    if author_sn:
                        if "sn" in part and part["sn"] == author_sn:
                            if not need_to_check_chat_info:
                                return
                        else:
                            pytest.fail(f"failed to verify author_sn {author_sn} in histDlgState part {part}")

                    if "chat" in part:
                        chat_from_parts = part["chat"]
                        for var_name, expected_val in [("sn", chat_sn), ("name", chat_name), ("stamp", chat_stamp)]:
                            if expected_val:
                                if var_name not in chat_from_parts:
                                    pytest.fail(f"failed to find chat {var_name} in histDlgState")
                                elif chat_from_parts[var_name] != expected_val:
                                    pytest.fail(
                                        f"invalid chat {var_name} in histDlgState. Expected: [{expected_val}], "
                                        f"got: [{chat_from_parts[var_name]}]"
                                    )
                            elif var_name in chat_from_parts:
                                pytest.fail(f"failed to check chat {var_name} in histDlgState")
                        # if nothing was raised before this line then the check is passed
                        return
    else:
        pytest.fail(
            f"failed to find forwarded from info in histDlgState for msg_id: {msg_id}. "
            f"Events: {account_to_fetch.events}, check_chat: {check_chat}, "
            f"author_sn: {author_sn}, need_to_check_chat_info: {need_to_check_chat_info}"
        )


def get_new_stamp():
    # max stamp len is 30, so we generate len(stamp) = 21, must start with latin  letter
    return f"ik{str(hashlib.sha1(os.urandom(256)).hexdigest())[:20]}"
