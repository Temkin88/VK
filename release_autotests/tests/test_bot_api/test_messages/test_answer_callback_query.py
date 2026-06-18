import allure
import pytest

from pyvkteamsbot.bot.types import InlineKeyboardMarkup, KeyboardButton
from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("79646")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Ответ на callback через Bot API")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
@pytest.mark.parametrize("callback_show_alert", [True, False], ids=lambda x: f"showAlert:{x}")
@pytest.mark.parametrize(
    "callback_url", [None, "https://mail.ru"], ids=lambda x: "without_url" if x is None else "with_url"
)
def test_bot_answer_callback_query(
    bot_class,
    auth_account,
    opponent_account,
    prepare_bot_test_chats,
    chat_type,
    callback_show_alert,
    callback_url,
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

    callback_data = f"[{auth_account.getReqId()}][test]"
    bot_class.events_get(poll_time_s=2)

    with allure.step("Отправляем сообщение с кнопками"):
        markup = InlineKeyboardMarkup()
        markup.row(
            KeyboardButton(
                text=callback_data,
                callbackData=callback_data,
            ),
        )

        msg_id = (
            bot_class.send_text(
                chat_id=bot_target_chat,
                text=f"Test message [{auth_account.getReqId()}]",
                inline_keyboard_markup=markup,
            )
            .json()
            .get("msgId", -1)
        )

    with allure.step("Пробуем вызвать callback через клиентское API"):
        auth_account.rapi_getBotCallbackAnswer(
            chatId=user_target_chat,
            msgId=msg_id,
            callbackData=callback_data,
        )

    with allure.step("Отправляем ответ на запрос клиента"):
        event_filter.start_point()

        for event in filter(
            lambda x: x["type"] == "callbackQuery" and x["payload"]["callbackData"] == callback_data,
            bot_class.events_get(poll_time_s=5).json()["events"],
        ):
            response = bot_class.answer_callback_query(
                query_id=event["payload"]["queryId"],
                text=callback_data,
                show_alert=callback_show_alert,
                url=callback_url,
            ).json()
            assert response["ok"], f"{auth_account.env}:{response['description']}"
            break
        else:
            raise Exception(f"{auth_account.env}:Failed to find event callbackQuery")

    with allure.step("Проверяем что ответ пришел на сторону клиента"):
        for event in fetch_until_empty_answer_with_filter(auth_account, "asyncResponse"):
            event_data = event["eventData"]["payload"]
            if (
                event_data["text"] == callback_data
                and event_data.get("url") == callback_url
                and event_data["showAlert"] == callback_show_alert
            ):
                return
        else:
            raise Exception(f'{auth_account.env}:Failed to find event "asyncResponse"')
