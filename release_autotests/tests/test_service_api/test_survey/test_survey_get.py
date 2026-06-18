import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88561")
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
def test_internal_survey_get(
    survey_miniapp,
    survey_id,
):
    """
    Проверяем получение результатов опроса, что ид опроса созданного и полученного совпадают

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    """
    with allure.step("Пробуем получать результаты опроса"):
        response = survey_miniapp.internal_survey_get(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )

        assert response["results"]["surveyId"] == survey_id, "Survey dont match"
