import allure
import pytest
from pyvkteamsclient.client.exceptions import HttpNotFoundException, AccessDeniedException

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88560")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Проголосовать/переголосовать")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
@SANDBOX
@pytest.mark.parametrize("type_question", ["single", "scale", "open", "yesNo", "pleasure"])
def test_rapi_survey_vote(
    survey_miniapp,
    create_questions_all_types,
    type_question,
):
    """
    Проверяем что можем проголосовать с разными параметрами, со стороны клиента

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param create_questions_all_types: ид созданного опроса в фикстуре и словарь типов и их ид вопросов
    """
    survey_id, questions_all = create_questions_all_types

    response_active = survey_miniapp.account.rapi_survey_get(
        survey_id=survey_id,
    )["results"]["active"]

    if not response_active:
        survey_miniapp.internal_survey_targets_add(
            sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_list=[survey_miniapp.account.uin]
        )
        survey_miniapp.internal_survey_start(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            forwarding=True,
            targets=[survey_miniapp.account.uin],
        )

    if type_question == "single":
        value = [1, 2, 3, "Your personal variant"]
        question_id = questions_all[type_question]
    elif type_question == "scale":
        value = 5
        question_id = questions_all[type_question]
    elif type_question == "open":
        value = "GO"
        question_id = questions_all[type_question]
    elif type_question == "yesNo":
        value = True
        question_id = questions_all[type_question]
    elif type_question == "pleasure":
        value = 3
        question_id = questions_all[type_question]
    else:
        raise ValueError(f"Unknown survey question type: {type_question}")

    with allure.step("Пробуем проголосовать"):
        survey_miniapp.account.rapi_survey_vote(
            survey_id=survey_id,
            question_id=question_id,
            value=value,
        )


@allure.id("552538")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Проголосовать/переголосовать для другого домена")
def test_rapi_survey_vote_isolation(
    survey_miniapp,
    opponent_account,
    create_questions_all_types,
    survey_miniapp_another_domain,
):
    """
    Проверяем что можем проголосовать с разными параметрами, со стороны клиента

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param opponent_account: Второй аккаунт
    :param create_questions_all_types: ид созданного опроса в фикстуре и словарь типов и их ид вопросов
    :param survey_miniapp_another_domain: Клиент для создания опросов с другим доменом
    """
    survey_id, questions_all = create_questions_all_types
    survey_miniapp.internal_survey_targets_add(
        sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_list=[survey_miniapp.account.uin]
    )
    survey_miniapp.internal_survey_start(
        sender_sn=survey_miniapp.account.uin,
        survey_id=survey_id,
        forwarding=True,
        targets=[survey_miniapp.account.uin],
    )

    with allure.step("Пробуем проголосовать из другого домена"):
        with pytest.raises((HttpNotFoundException, AccessDeniedException)) as exeption:
            survey_miniapp_another_domain.account.rapi_survey_vote(
                survey_id=survey_id,
                question_id=questions_all["single"],
                value=[1, 2, 3, "Your personal variant"],
            )

        assert exeption.value.response_status_code in [40400, 40300], "Response code is not matched"
