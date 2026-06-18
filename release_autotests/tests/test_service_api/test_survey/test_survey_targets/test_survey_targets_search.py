import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("511444")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Поиск среди целей")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
@SANDBOX
@pytest.mark.fierst
def test_internal_survey_targets_search(survey_miniapp, survey_id, survey_start):
    """
    Поиск среди целей (возможных респондентов) - осуществляет поиск keyword в sn-пользователя и friendly.

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    """
    with allure.step("Пробуем найти среди целе"):
        response = survey_miniapp.internal_survey_targets_search(
            sender_sn=survey_miniapp.account.uin, survey_id=survey_id, keyword=survey_miniapp.account.uin
        )
        results = response["results"]["targets"]
        responders = [target["responder"] for target in results]
        assert survey_miniapp.account.uin in responders, f"{survey_miniapp.account.uin} not in list: {responders}"
