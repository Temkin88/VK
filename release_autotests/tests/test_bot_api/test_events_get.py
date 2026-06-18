import allure

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("37492")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Получение событий через BotAPI")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_bot_events_get(
    bot_class,
    photo_id,
    auth_account,
):
    with allure.step("Пробуем получить события"):
        response = bot_class.events_get(poll_time_s=1)

        auth_account.allure_attach(response)

        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")
