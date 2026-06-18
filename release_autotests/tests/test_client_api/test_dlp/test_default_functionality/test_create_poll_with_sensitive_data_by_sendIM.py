import allure

from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM


@allure.id("557302")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Опросы")
@allure.title("Создание опроса с чувствительными данными через sendIM")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@DLP
def test_create_poll_with_sensitive_data_by_sendIM(main_acc, opponent_acc):
    """
    Создание опроса
    """

    with allure.step("Отправляем запрос"):
        response = main_acc.wim_im_sendIM(
            t=opponent_acc.uin,
            parts=[
                {
                    "mediaType": "text",
                    "text": "block",
                    "poll": {
                        "type": "anon",
                        "responses": ["block"],
                    },
                },
            ],
        )

        assert response["response"]["statusCode"] == 603, "Response code error"
