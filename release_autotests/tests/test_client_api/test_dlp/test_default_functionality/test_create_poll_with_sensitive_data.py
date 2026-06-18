import allure
import pytest


from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM


@allure.id("557304")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Опросы")
@allure.title("Создание опроса с чувствительными данными через message/send")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@DLP
@pytest.mark.parametrize(
    "parts",
    [{"plain": "block?", "responses": ["yes", "no"]}, {"plain": "what to do?", "responses": ["block", "nothing"]}],
)
def test_create_poll_with_sensitive_data(main_acc, opponent_acc, parts):
    """
    Проверка отправки опроса с чувствительными данными
    """

    target = opponent_acc.uin
    with allure.step("Создаем опрос с чувствительными данными"):
        response = main_acc.rapi_message_send(
            target=target,
            parts={
                "mainPart": {
                    "text": {"plain": parts["plain"]},
                    "poll": {"type": "anon", "responses": parts["responses"]},
                }
            },
        )

        assert response["status"]["code"] == 40607, "Response code error"
