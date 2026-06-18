import uuid

import allure
import pytest

from pyvkteamsclient.survey.exceptions import RequestException
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88552")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Удалить опрос про")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_internal_survey_delete(
    survey_miniapp,
    photo_id,
):
    """
    Проверяем удаление опроса.
    Проверяем что опрос создался, получаем его ид опроса, удаляем опрос и проверяем что опрос удалился

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param photo_id: ид аватарки
    """

    with allure.step("Создаем опрос"):
        response = survey_miniapp.internal_survey_create(
            sender_sn=survey_miniapp.account.uin,
            name=f"Test survey {uuid.uuid4().hex}",
            image=photo_id,
            flags=["anonymous"],
        )
        survey_id = response["results"]["surveyId"]

    with allure.step("Проверяем что опрос есть"):
        survey_miniapp.internal_survey_get(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )

    with allure.step("Пробуем удалить опрос"):
        survey_miniapp.internal_survey_delete(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )

    with allure.step("Проверяем что опрос удален"), pytest.raises(RequestException):
        survey_miniapp.internal_survey_get(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
