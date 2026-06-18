import allure
import pytest
from pyvkteamsclient.client.exceptions import HttpNotFoundException, AccessDeniedException

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88558")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Получение всей имеющейся информации об опросе")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
@SANDBOX
def test_rapi_survey_get(
    survey_miniapp,
    survey_id,
):
    """
    Проверяем что получаем всю имеющуюся информацию об опросе и ид опроса созданный есть в полученных данных,
    со стороны клиента

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид созданного опроса в фикстуре
    """
    with allure.step("Проверяем получить опрос"):
        response = survey_miniapp.account.rapi_survey_get(
            survey_id=survey_id,
        )

        assert response["results"]["surveyId"] == survey_id, "Survey dont match"


@allure.id("552537")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Получение всей имеющейся информации об опросе для другого домена")
def test_rapi_survey_get_isolation(
    survey_miniapp,
    survey_id,
    survey_miniapp_another_domain,
):
    """
    Проверяем что получаем всю имеющуюся информацию об опросе и ид опроса созданный есть в полученных данных,
    со стороны клиента

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид созданного опроса в фикстуре
    :param survey_miniapp_another_domain: Клиент для создания опросов с другим доменом
    """
    with allure.step("Проверяем получить опрос с другого домена"):
        with pytest.raises((HttpNotFoundException, AccessDeniedException)) as exeption:
            survey_miniapp_another_domain.account.rapi_survey_get(
                survey_id=survey_id,
            )

        assert exeption.value.response_status_code in [40400, 40300], "Response code is not matched"
