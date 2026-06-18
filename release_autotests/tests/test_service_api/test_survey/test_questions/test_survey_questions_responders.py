import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88553")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Получение полного списка проголосовавших за вариант ответа по вопросу.")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
@SANDBOX
def test_internal_survey_questions_responders(
    survey_miniapp,
    question_id,
    survey_id,
    check_action,
):
    """
    Проверяем получение полного списка проголосовавших

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид созданного опроса в фикстуре
    :param question_id: ид созданного вопроса в фикстуре
    """
    with allure.step("Пробуем получить списка проголосовавших за вариант ответа по вопросу."):
        survey_miniapp.internal_survey_questions_responders(
            sender_sn=survey_miniapp.account.uin,
            question_id=question_id,
            survey_id=survey_id,
        )
