import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88556")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Получение информации об опросах, созданным пользователем")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_internal_survey_list(
    survey_miniapp,
    survey_id,
):
    """
    Проверяем получение информации об опросах по созданному пользователю
    Проверяем что созданный ид опроса есть в списке

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    """
    with allure.step("Пробуем получить информацию об опросах"):
        response = survey_miniapp.internal_survey_list(
            sender_sn=survey_miniapp.account.uin,
        )

        assert [survey for survey in response["results"]["surveys"] if survey_id == survey["surveyId"]], (
            "Survey not found"
        )
