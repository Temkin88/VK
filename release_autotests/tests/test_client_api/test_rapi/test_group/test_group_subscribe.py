import allure
import pytest_check as check
from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


def check_events(
    account,
    opponent,
    chat_id,
    event_filter,
    fetch_until_empty_answer,
):
    text = "Message for threads test"
    event_filter.start_point()

    msg_id_opponent = account.send_basic_message(
        sn=chat_id,
        text=text,
    )

    event_found_and_checked = None
    fetch_until_empty_answer(opponent)

    events = [event for event in opponent.events[::-1] if event["type"] == "histDlgState"]

    for event in events:
        if event["eventData"]["sn"] == chat_id and event["eventData"]["lastMsgId"] == msg_id_opponent:
            event_found_and_checked = text in [x["text"] for x in event["eventData"]["tail"]["messages"]]

        if event_found_and_checked:
            break
    return event_found_and_checked, "histDlgState event not found"


@allure.id("88065")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Чаты")
@allure.feature("Подписаться на сообщения из группы")
@allure.title("Подписаться на сообщения из группы, не вступая в неё.")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_rapi_group_subscribe_stamp(
    auth_account,
    opponent_account,
    event_filter,
    fetch_until_empty_answer,
    create_chat_with_public_join_moderation,
):
    chat_id, stamp = create_chat_with_public_join_moderation

    with allure.step("Пробуем подписаться на сообщение группы не вступая в нее"):
        for chat in create_chat_with_public_join_moderation:
            if "chat.agent" in chat:
                opponent_account.rapi_group_subscribe(chatId=chat_id)
                check.is_true(
                    check_events(
                        account=auth_account,
                        opponent=opponent_account,
                        chat_id=chat_id,
                        event_filter=event_filter,
                        fetch_until_empty_answer=fetch_until_empty_answer,
                    ),
                    "histDlgState event not found",
                )
            else:
                opponent_account.rapi_group_subscribe(stamp=stamp)
                check.is_true(
                    check_events(
                        account=auth_account,
                        opponent=opponent_account,
                        chat_id=chat_id,
                        event_filter=event_filter,
                        fetch_until_empty_answer=fetch_until_empty_answer,
                    ),
                    "histDlgState event not found",
                )
