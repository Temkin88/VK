import allure
import pytest

from pyvkteamsclient.client.exceptions import HttpNotFoundException, AccessDeniedException

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88551")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Начать прохождение/пройти еще раз")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
@SANDBOX
@pytest.mark.fierst
def test_rapi_survey_begin(survey_miniapp, create_questions_all_types):
    """
    Проверяем что можем начать прохождение либо пройти еще раз, со стороны клиента

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param create_questions_all_types: ид созданного опроса в фикстуре и словарь типов и их ид вопросов
    """
    survey_id, _ = create_questions_all_types

    with allure.step("Стартуем опрос"):
        survey_miniapp.internal_survey_targets_add(
            sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_list=[survey_miniapp.account.uin]
        )
        survey_miniapp.internal_survey_start(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            targets=[survey_miniapp.account.uin],
        )

    with allure.step("Пробуем начать прохождение"):
        survey_miniapp.account.rapi_survey_begin(
            survey_id=survey_id,
        )


@allure.id("552536")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Начать прохождение/пройти еще раз для другого домена")
def test_rapi_survey_begin_isolation(
    survey_miniapp,
    create_questions_all_types,
    survey_miniapp_another_domain,
):
    """
    Проверяем что можем начать прохождение либо пройти еще раз, со стороны клиента

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param create_questions_all_types: ид созданного опроса в фикстуре и словарь типов и их ид вопросов
    :param survey_miniapp_another_domain: Клиент для создания опросов с другим доменом
    """
    survey_id, _ = create_questions_all_types

    with allure.step("Стартуем опрос"):
        survey_miniapp.internal_survey_targets_add(
            sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_list=[survey_miniapp.account.uin]
        )
        survey_miniapp.internal_survey_start(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            targets=[survey_miniapp.account.uin],
        )

    with allure.step("Проверяем что нельзя начать прохождение с другим доменом"):
        with pytest.raises((HttpNotFoundException, AccessDeniedException)) as exeption:
            survey_miniapp_another_domain.account.rapi_survey_begin(
                survey_id=survey_id,
            )

        assert exeption.value.response_status_code in [40400, 40300], "Response code is not matched"
