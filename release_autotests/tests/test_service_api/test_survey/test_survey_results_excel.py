import time

import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88555")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Получение excel файла с результатом опроса.")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_internal_survey_results_excel(
    survey_miniapp,
    create_questions_all_types,
):
    """
    Проверяем получение excel файла с результатами опроса

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param create_questions_all_types: ид созданного опроса в фикстуре и словарь типов и их ид вопросов
    """
    survey_id, _ = create_questions_all_types

    survey_action = False

    for t in range(6):
        with allure.step("Стартуем опрос"):
            survey_miniapp.internal_survey_start(
                sender_sn=survey_miniapp.account.uin,
                survey_id=survey_id,
                targets=[survey_miniapp.account.uin],
            )

        with allure.step("Получаем информацию об опросах"):
            response = survey_miniapp.internal_survey_list(
                sender_sn=survey_miniapp.account.uin,
            )
            for survey in list(filter(lambda x: x["surveyId"] == survey_id, response["results"]["surveys"])):
                if not survey["active"]:
                    time.sleep(t)
                else:
                    survey_action = True
                    break

            if survey_action:
                break

    with allure.step("Пробуем изменить номер вопроса"):
        survey_miniapp.internal_survey_results_excel(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
