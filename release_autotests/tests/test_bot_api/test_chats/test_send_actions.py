import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("79644")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Получение информации о чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
@pytest.mark.parametrize("action", ["looking", "typing", ""])
def test_bot_send_actions(
    bot_class,
    auth_account,
    prepare_bot_test_chats,
    chat_type,
    action,
    fetch_until_empty_answer_with_filter,
    event_filter,
):
    _, _, group, channel = prepare_bot_test_chats
    if chat_type == "private":
        user_target_chat = bot_class.uin
        bot_target_chat = auth_account.uin
    elif chat_type == "group":
        user_target_chat = group
        bot_target_chat = group
    else:
        user_target_chat = channel
        bot_target_chat = channel

    typing_status = action if action else "none"

    with allure.step("Пробуем отправить запрос"):
        response = bot_class.send_actions(
            chat_id=bot_target_chat,
            actions=action,
        ).json()
        assert response["ok"], f"{auth_account.env}:{response['description']}"

        if action == "looking" or chat_type == "channel":
            return

    with allure.step("Проверяем что пришло событие typing"):
        for event in fetch_until_empty_answer_with_filter(auth_account, "typing"):
            event_data = event["eventData"]
            if event_data["aimId"] == user_target_chat and event_data["typingStatus"] == typing_status:
                return
        else:
            raise Exception(f'{auth_account.env}:Failed to find event "typing"')
