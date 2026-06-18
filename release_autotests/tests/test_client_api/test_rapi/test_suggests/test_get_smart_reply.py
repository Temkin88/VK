import allure
import pytest

from support.markers import VKTI, SAAS, PRE_VKTI, PRE_SAAS, TARM, PRE_TARM


@allure.id("26926")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Саджесты")
@allure.feature("Смартреплаи")
@allure.title("Саджест смартреплеев по сообщению")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
@pytest.mark.parametrize("user_text", ["kek", "lol", "i tried", "mm?"])
def test_get_smart_reply(
    chat_type,
    user_text,
    prepare_test_chats,
):
    main_acc, opponent, group, channel = prepare_test_chats

    if chat_type == "private":
        chat = main_acc.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем тестовое сообщение"):
        msg_id = opponent.send_basic_message(
            sn=chat,
            text=user_text,
        )

    with allure.step("Отправляем запрос"):
        response = main_acc.rapi_getSmartReply(
            sn=chat,
            msgId=msg_id,
            suggestTypes=[
                "sticker-smartreply",
                "text-smartreply",
                "smart-hello",
            ],
        )

    with allure.step("Проверяем ответ"):
        assert response["status"]["code"] == 20000, "Failed request"
