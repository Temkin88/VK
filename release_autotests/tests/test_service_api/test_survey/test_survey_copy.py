import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88564")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Копировать опрос про")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_internal_survey_copy(
    survey_miniapp,
    survey_id,
):
    """
    Проверяем копирование опроса. Что после копирования получаем новые ид опроса

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид созданного опроса в фикстуре
    """
    with allure.step("Проверяем изменить опрос про"):
        response = survey_miniapp.internal_survey_copy(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )

        survey_id_copy = response["results"]["surveyId"]

        assert response["results"]["surveyId"], "Survey not found"
        assert survey_id != survey_id_copy, "ID of copied survey equels original survey ID"
