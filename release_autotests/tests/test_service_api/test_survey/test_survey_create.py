import uuid

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("27483")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Создания опроса про")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("flags", [["anonymous"], ["nonanonymous"]])
def test_internal_survey_create(
    survey_miniapp,
    photo_id,
    flags,
):
    """
    Проверяем создание опроса с разными параметрами аннонимности.
    Проверяем что опрос создался и ид опроса совпадает с полученным

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param photo_id: ид аватарки
    """
    with allure.step("Пытаемся создать опрос"):
        response = survey_miniapp.internal_survey_create(
            sender_sn=survey_miniapp.account.uin,
            name=f"Test survey {uuid.uuid4().hex}",
            image=photo_id,
            flags=flags,
        )

        survey_id = response["results"]["surveyId"]

        assert response["results"]["surveyId"], "Survey id not found"

    with allure.step("Проверяем что опрос про создался"):
        response = survey_miniapp.internal_survey_get(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )

        survey_id_get = response["results"]["surveyId"]

        assert survey_id == survey_id_get, "Survey dont match"
