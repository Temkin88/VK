import uuid

import allure
import pytest
from pyvkteamsclient.survey.exceptions import BadRequestException

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88562")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Запустить опрос про")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
def test_internal_survey_start(
    survey_miniapp,
    survey_id,
):
    """
    Проверяем запуск опроса для другого пользователя

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    :param opponent_account: аккаунт другого клиента
    """
    survey_miniapp.internal_survey_targets_add(
        sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_list=[survey_miniapp.account.uin]
    )
    with allure.step("Пробуем запустить опрос"):
        response = survey_miniapp.internal_survey_start(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            targets=[survey_miniapp.account.uin],
        )

        assert response["results"]["active"], "Field active False"
        assert response["results"]["targets"][0] == survey_miniapp.account.uin, "Target dont match"


@allure.id("552544")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Запустить опрос про для другого домена")
def test_internal_survey_start_isolation(
    survey_miniapp,
    photo_id,
    survey_miniapp_another_domain,
):
    """
    Проверяем запуск опроса для другого пользователя

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param opponent_account: аккаунт другого клиента
    :param photo_id: Ид аватарки
    :param survey_miniapp_another_domain: Клиент для создания опросов с другим доменом
    """
    with allure.step("Стартуем опрос"):
        response = survey_miniapp.internal_survey_create(
            sender_sn=survey_miniapp.account.uin,
            name=f"Test survey {uuid.uuid4().hex}",
            image=photo_id,
            flags=["nonanonymous"],
        )
        survey_id = response["results"]["surveyId"]

    with allure.step("Пробуем запустить опрос"):
        survey_miniapp.internal_survey_targets_add(
            sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_list=[survey_miniapp.account.uin]
        )
        response = survey_miniapp.internal_survey_start(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            targets=[survey_miniapp.account.uin, survey_miniapp_another_domain.account.uin],
        )
        targets = response["results"]["targets"]

        assert survey_miniapp_another_domain.account.uin not in targets, (
            f"{survey_miniapp_another_domain.account.uin} in targets"
        )

    with (
        allure.step("Пробуем добавленить пользователей с другого домена в список целей"),
        pytest.raises(BadRequestException),
    ):
        survey_miniapp.internal_survey_start(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            targets=[survey_miniapp_another_domain.account.uin],
        )

    with allure.step("Останавливаем опрос"):
        survey_miniapp.internal_survey_stop(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
