import allure
import lorem
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("534959")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Черновик")
@allure.feature("Черновик в чате")
@allure.title("Сохранение черновика в чате с 2-я инстансами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "chat_type",
    ["private", "group", "channel"],
)
def test_save_draft_in_chat(chat_type, prepare_test_chats, second_auth_account, fetch_until_empty_answer_with_filter):
    """
    Проверяем сохранение черновика из под 2-х инстансов
    """

    auth_account, opponent, group, channel = prepare_test_chats

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Сохраняем черновик в чате от 1-го инстанса"):
        message_main = lorem.sentence()

        auth_account.rapi_draft_set(
            sn=chat,
            parts=[{"mediaType": "text", "text": message_main}],
        )

        main_acc_events = False

        for event in fetch_until_empty_answer_with_filter(auth_account, "draft"):
            event_data = event["eventData"]["parts"]

            if any(message["text"] == message_main for message in event_data):
                main_acc_events = True
                break

        assert main_acc_events, "Event 'draft' not found"

    with allure.step("Проверяем что на втором инстансе нет событий"):
        second_events = fetch_until_empty_answer_with_filter(second_auth_account, "draft")

        assert not second_events, f"Event not equal: {second_events}"

    with allure.step("Сохраняем черновик в чате из 2-го инстанса"):
        message_second = lorem.sentence()

        second_auth_account.rapi_draft_set(
            sn=chat,
            parts=[{"mediaType": "text", "text": message_second}],
        )

    with allure.step("Проверяем, что появились события 2-го инстанса у 1-го"):
        auth_account_events = False
        second_events = False

        for event in fetch_until_empty_answer_with_filter(auth_account, "draft"):
            event_data = event["eventData"]["parts"]

            if any(message["text"] == message_second for message in event_data):
                second_events = True
                continue
            elif any(message["text"] == message_main for message in event_data):
                auth_account_events = True
                continue

            if second_events and auth_account_events:
                break

        multi_instance_event = second_events and auth_account_events

        assert multi_instance_event, "Event 'draft' not found"
