import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("30138")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Опросы")
@allure.feature("Действия с опросами")
@allure.title("Голосуем в опросе")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_poll_vote(
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

        poll_id = response["response"]["data"]["pollId"]

    with allure.step("Голосуем"):
        assert main_acc.rapi_poll_vote(
            _id=poll_id,
            answerId="1",
        )["status"]["code"], f"Failed to vote in poll ID: {poll_id}"
