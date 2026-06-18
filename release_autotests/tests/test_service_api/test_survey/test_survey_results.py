import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88549")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Получение результатов опроса")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_internal_survey_results(
    survey_miniapp,
    survey_id,
    survey_start,
):
    """
    Проверяем получение результаты опроса
    Проверяем что созданный ид опроса есть в результатах

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    :param survey_start: фикстура предназначенная для старта опроса
    """
    with allure.step("Пробуем получить результаты опроса"):
        response = survey_miniapp.internal_survey_results(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )

        assert response["results"]["surveyId"] == survey_id, "Survey dont match"
