import allure
import pytest
from pyvkteamsclient.survey.exceptions import BadRequestException

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("511442")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Добавление пользователей в список целей (возможных респондентов)")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
@SANDBOX
def test_internal_survey_targets_add(
    survey_miniapp,
    opponent_survey_miniapp,
    survey_id,
    survey_start,
):
    """
    Добавление пользователей в список целей (возможных респондентов)

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param opponent_survey_miniapp: Второй клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    :param survey_start: фикстура предназначенная для старта опроса
    """
    with allure.step("Пробуем добавленить пользователей в список целей"):
        response = survey_miniapp.internal_survey_targets_add(
            sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_list=[opponent_survey_miniapp.account.uin]
        )
        results = response["results"]["targets"]

        assert results[0]["responder"] == opponent_survey_miniapp.account.uin, (
            f"{survey_miniapp.account.uin} dont matched"
        )


@allure.id("552564")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Добавление пользователей в список целей (возможных респондентов) для другого домена")
def test_internal_survey_targets_add_isolation(
    survey_miniapp, survey_id, survey_start, survey_miniapp_another_domain, opponent_survey_miniapp
):
    """
    Добавление пользователей в список целей (возможных респондентов)

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param opponent_survey_miniapp: Второй аккаунт для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    :param survey_start: фикстура предназначенная для старта опроса
    :param survey_miniapp_another_domain: Клиент для создания опросов с другим доменом
    """
    with allure.step("Пробуем добавленить пользователей из своего домена и из другого домена в список целей"):
        response = survey_miniapp.internal_survey_targets_add(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            sn_list=[opponent_survey_miniapp.account.uin, survey_miniapp_another_domain.account.uin],
        )
        targets = response["results"]["targets"]

        assert survey_miniapp_another_domain.account.uin not in targets, (
            f"{survey_miniapp_another_domain.account.uin} in targets"
        )

    with (
        allure.step("Пробуем добавить пользователей с другого домена в список целей"),
        pytest.raises(BadRequestException),
    ):
        survey_miniapp.internal_survey_targets_add(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            sn_list=[survey_miniapp_another_domain.account.uin],
        )
