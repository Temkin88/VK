import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("511441")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Получение списка респондентов и статуса прохождения Опроса")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_internal_survey_responders(
    survey_miniapp,
    survey_id,
    survey_start,
    get_survey_vote,
):
    """
    Получение списка респондентов и статуса прохождения Опроса, в списке только начавшие прохождение и прошедшие.

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    :param survey_start: фикстура предназначенная для старта опроса
    """
    survey_id, _ = get_survey_vote
    with allure.step("Пробуем получить результаты опроса"):
        response = survey_miniapp.internal_survey_responders(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
        results = response["results"]["responders"]
        responders_users = [responder["responder"] for responder in results]

        assert response["status"]["code"] == 20000, "Response code error"
        assert survey_miniapp.account.uin in responders_users, (
            f"Account: {survey_miniapp.account.uin} not in {responders_users}"
        )
