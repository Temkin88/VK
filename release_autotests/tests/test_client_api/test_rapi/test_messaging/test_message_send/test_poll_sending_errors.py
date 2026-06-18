import allure

import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
    SendImStateException,
    PollCreationErrorException,
)


from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    failed_message,
)


@allure.id("515302")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки опроса со слишком большим числом ответов")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_polls_by_message_send_too_many_answers(auth_account, opponent_account):
    """
    Проверка отправки опроса со слишком большим числом ответов
    """

    target = opponent_account.uin

    with (
        allure.step("Создаем опрос со слишком большим числом ответов"),
        pytest.raises(PollCreationErrorException),
    ):
        auth_account.send_poll_by_message_send(
            target=target,
            poll_title=failed_message,
            poll_type="anon",
            responses=[str(i) for i in range(50)],
        )

    with (
        allure.step(
            "Показываем консистентность message/send и sendIM"
            " при попытке создания опроса cо слишком большим числом ответов"
        ),
        pytest.raises(SendImStateException) as ex,
    ):
        auth_account.wim_im_sendIM(
            t=target,
            parts=[
                {
                    "mediaType": "text",
                    "text": failed_message,
                    "poll": {
                        "type": "anon",
                        "responses": [str(i) for i in range(50)],
                    },
                },
            ],
        )
        st_code = ex.value.response_status_code
        assert st_code == 400, f"Unexpected statusCode from sendIM: {st_code}"
        st_text = ex.value.response_status_text
        assert "statusDetailCode 21" in st_text, f"Unexpected statusDetailCode from sendIM: {st_text}"
        assert 'state: "failed"' in st_text, f"Unexpected msg state from sendIM: {st_text}"


@allure.id("515282")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки существующего опроса без подписи")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_polls_by_message_send_existing_poll_wo_text(auth_account, opponent_account):
    target = opponent_account.uin

    with allure.step("Создаем опрос с одним вариантом ответа"):
        _, existing_poll_id = auth_account.send_poll_by_message_send(
            target=target, poll_title="Да?", poll_type="anon", responses=["Да"]
        )
        assert existing_poll_id, f"Failed to create poll with 1 response in chat ID {target}"

    with (
        allure.step("Отправка существующеuо опроса без подписи"),
        pytest.raises(BadRequestException),
    ):
        auth_account.send_existing_poll_by_message_send(target=target, existing_poll_id=existing_poll_id)
