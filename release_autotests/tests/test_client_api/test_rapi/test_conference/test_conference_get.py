import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("83512")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Запросить параметры конференции")
@allure.title("Запрос параметров конференции")
def test_conference_get(
    auth_account,
    conference_id,
):
    with allure.step("Пробуем получить конференцию"):
        results = auth_account.rapi_conference_get(
            conference_id=conference_id,
        )["results"]

        conference_url = results.get("conferenceUrl")

    with allure.step("Проверяем ответ сервера"):
        assert "conferenceUrl" in results, f"Wrong conferenceUrl value: {conference_url}"
        assert conference_url, f"Wrong conferenceUrl value: {conference_url}"

        assert auth_account.uin == results["creator"], "Creator dont match"
        assert results["conferenceName"] == "Test conference", "Name dont match"
