from random import randint

import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88550")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Изменение номера вопроса")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
@SANDBOX
def test_internal_survey_questions_change(
    survey_miniapp,
    question_id,
    survey_id,
    check_action,
):
    """
    Проверяем изменение номера вопроса.
    Проверяем что данные полученные до и после изменения номера отличаются

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид созданного опроса в фикстуре
    :param question_id: ид созданного вопроса в фикстуре
    """
    with allure.step("Получаем номер вопроса"):
        response = survey_miniapp.internal_survey_get(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
        question_number = response["results"]["questions"][0]["number"]

    with allure.step("Пробуем изменить номер вопроса"):
        new_number = randint(2, 100)

        survey_miniapp.internal_survey_questions_change(
            sender_sn=survey_miniapp.account.uin,
            question_id=question_id,
            survey_id=survey_id,
            number=new_number,
        )

    with allure.step("Проверяем что номер вопроса вопроса изменен"):
        response = survey_miniapp.internal_survey_get(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
        question_list = response["results"]["questions"]

        assert any(new_number == x["number"] and question_number != x["number"] for x in question_list), (
            "Survey dont match"
        )
