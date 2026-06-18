import allure
import pytest

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("30338")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.suite("Опросы")
@allure.feature("Действия с опросами")
@allure.title("Остановка опроса")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_poll_stop(
    chat_type,
    prepare_test_chats,
):
    """
    Проверяем отправку опроса
    """
    main_acc, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем опрос"):
        poll_id = main_acc.send_poll(
            chat_id=chat,
            poll_title="test poll",
            poll_type="anon",
            responses=[f"variant_{i}" for i in range(1, 11)],
        )["response"]["data"]["pollId"]

    with allure.step("Останавливаем опрос"):
        main_acc.rapi_poll_stop(
            _id=poll_id,
        )

    with allure.step("Пробуем проголосовать в опросе"), pytest.raises(BadRequestException):
        main_acc.rapi_poll_vote(
            _id=poll_id,
            answerId="1",
        )
