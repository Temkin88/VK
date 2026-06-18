import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("30133")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Опросы")
@allure.feature("Действия с опросами")
@allure.title("Получение данных опроса")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.parametrize("subscribe", [True, False])
def test_poll_get(
    chat_type,
    subscribe,
    prepare_test_chats,
):
    """
    Проверяем отправку опроса
    """
    main_acc, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем опрос"):
        response = main_acc.wim_im_sendIM(
            t=chat,
            parts=[
                {
                    "mediaType": "text",
                    "text": "test poll",
                    "poll": {
                        "type": "anon",
                        "responses": [f"variant_{i}" for i in range(1, 11)],
                    },
                },
            ],
        )

        assert response["response"]["statusCode"] == 200, "Failed to send test poll"

        assert response["response"]["data"]["pollId"], "pollId is not received in response"

        poll_id = response["response"]["data"]["pollId"]

    with allure.step("Голосуем"):
        for i in range(1, 11):
            assert main_acc.rapi_poll_vote(
                _id=poll_id,
                answerId=str(i),
            )["status"]["code"], f"Failed to vote in poll ID: {poll_id}"

            votes_response = main_acc.rapi_poll_get(
                _id=poll_id,
                subscribe=subscribe,
            )

            assert votes_response["status"]["code"] == 20000, f"Failed to get votes from poll ID: {poll_id}"

            assert votes_response["results"]["myAnswerId"] == str(i), f"Failed to get votes from poll ID: {poll_id}"
