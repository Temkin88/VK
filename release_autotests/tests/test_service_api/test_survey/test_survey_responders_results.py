import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("511440")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Получение результатов прохождения опроса (ответы на вопросы) для пользователя")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_internal_survey_responders_results(survey_miniapp, survey_id, survey_start, get_survey_vote):
    """
    Получение результатов прохождения опроса (ответы на вопросы) для пользователя

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    :param survey_start: фикстура предназначенная для старта опроса
    """
    survey_id, question_id = get_survey_vote
    with allure.step("Пробуем получить результаты опроса"):
        response = survey_miniapp.internal_survey_responders_results(
            sender_sn=survey_miniapp.account.uin, survey_id=survey_id, responder=survey_miniapp.account.uin
        )
        results = response["results"]["questions"]
        question_ids = [question["questionId"] for question in results]

        assert response["status"]["code"] == 20000, "Response code error"
        assert question_id in question_ids, f"Question id: {question_id} not in {question_ids}"
