import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26925")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Саджесты")
@allure.feature("Саджест стикеров")
@allure.title("Саджест стикеров по тексту")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
@pytest.mark.parametrize("user_text", ["kek", "lol"])
def test_get_suggests(
    chat_type,
    user_text,
    prepare_test_chats,
):
    main_acc, opponent, group, channel = prepare_test_chats

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем запрос"):
        response = main_acc.rapi_getSuggests(
            sn=chat,
            suggestTypes=[
                {
                    "type": "sticker-by-text",
                    "text": user_text,
                }
            ],
        )

    with allure.step("Проверяем ответ"):
        assert response["status"]["code"] == 20000, "Failed request"

        assert response["results"].get("suggests") is not None, "Empty suggests"
