import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26921")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.suite("Опросы")
@allure.feature("Отправка опроса")
@allure.title("Отправка опроса в чат")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_poll_send(
    chat_type,
    prepare_test_chats,
):
    """
    Проверяем отправку опроса
    """
    main_acc, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем опрос"):
        response = main_acc.send_poll(
            chat_id=chat,
            poll_title="test poll",
            poll_type="anon",
            responses=[f"variant_{i}" for i in range(1, 11)],
        )

        assert response["response"]["statusCode"] == 200, "Failed to send test poll"

        assert response["response"]["data"]["pollId"], "pollId is not received in response"
