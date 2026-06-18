from random import randint

import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88554")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Удалить вопрос из опроса")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
@SANDBOX
def test_internal_survey_questions_delete(
    survey_miniapp,
    survey_id,
    check_action,
):
    """
    Проверяем удаление вопроса из опроса.
    Сначала создаем вопрос который необходимо удалить и его удаляем

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид созданного опроса в фикстуре
    """
    with allure.step("Создаем вопрос"):
        response = survey_miniapp.internal_survey_questions_create(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            name="Какой язык программирования?",
            number=randint(1, 100),
            typeQuestion="single",
            flags=["require", "many", "own_version"],
            values=[
                "C++1",
                "Java1",
                "Golang1",
                "Python1",
            ],
        )
        question_id = response["results"]["questionId"]

    with allure.step("Пробуем удалить вопрос"):
        survey_miniapp.internal_survey_questions_delete(
            sender_sn=survey_miniapp.account.uin,
            question_id=question_id,
            survey_id=survey_id,
        )
