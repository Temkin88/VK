from __future__ import annotations

from random import randint

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88559")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Cоздать вопрос")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
@SANDBOX
@pytest.mark.parametrize("type_question", ["single", "scale", "open", "yesNo", "pleasure"])
@pytest.mark.parametrize("flag", ["require", "many", "own_version"])
def test_internal_survey_questions_create(
    survey_miniapp,
    survey_id,
    type_question,
    flag,
    check_action,
):
    """
    Проверяем создание вопроса. с различными параметрами и типами
    Проверяем что после создания вопсроса его ид присутствует в полученных результатах

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид созданного опроса в фикстуре
    """
    with allure.step("Пытаемся создать вопрос"):
        params: dict[str, list[str] | int | str | dict[str, [int, str]]] = {
            "number": randint(1, 100),
            "typeQuestion": type_question,
            "flags": [flag],
        }

        if type_question == "single":
            params["values"] = [
                "C++",
                "Java",
                "Golang",
                "Python",
            ]
        elif type_question == "scale":
            params["values"] = {
                "min": [1, "Не нравится!"],
                "max": [10, "Обожаю!"],
            }
        elif type_question == "open":
            params["values"] = "Your personal variant"
        elif type_question == "yesNo":
            params["values"] = False
        elif type_question == "pleasure":
            params["values"] = [
                "!-_-! Совершенно удовлетворен",
                "!-_-! Удовлетворен",
                "!-_-! Не знаю",
                "!-_-!  Не удовлетворен",
                "!-_-! Абсолютно не удовлетворен",
            ]
        else:
            raise ValueError(f"Unknown survey question type: {type_question}")

        response = survey_miniapp.internal_survey_questions_create(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            name="Какой язык программирования вы предпочитаете?",
            **params,
        )

        assert response["results"]["questionId"], "Question id id not found"

    with allure.step("Проверяем что вопрос создался"):
        response = survey_miniapp.internal_survey_get(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
        question_list = response["results"]["questions"]

        assert question_list, "Question list empty"
