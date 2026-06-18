import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("511443")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Получение списка целей (возможных респондентов).")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
@SANDBOX
def test_internal_survey_targets(
    survey_miniapp,
    survey_id,
    survey_start,
):
    """
    Получение списка целей (возможных респондентов).

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    :param survey_start: фикстура предназначенная для старта опроса
    """
    with allure.step("Пробуем получить результаты опроса"):
        response = survey_miniapp.internal_survey_targets(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
        results = response["results"]["targets"]
        responders = [target["responder"] for target in results]
        assert survey_miniapp.account.uin in responders, f"{survey_miniapp.account.uin} not in list: {responders}"
