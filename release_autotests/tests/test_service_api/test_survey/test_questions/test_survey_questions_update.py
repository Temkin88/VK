from __future__ import annotations

import uuid

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88566")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Обновить вопрос")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
@SANDBOX
@pytest.mark.parametrize("type_question", ["pleasure", "scale", "single", "open", "yesNo"])
def test_internal_survey_questions_update(
    survey_miniapp,
    question_id,
    survey_id,
    type_question,
    check_action,
):
    """
    Проверяем обновление вопроса
    Проверяем что все изменяемые данные полученные до и после отличаются

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид созданного опроса в фикстуре
    :param question_id: ид созданного вопроса в фикстуре
    """
    with allure.step("Проверяем что вопрос создался"):
        response = survey_miniapp.internal_survey_get(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
        question_list = response["results"]["questions"]

        assert question_list, "Question list empty"

    with allure.step("Пытаемся изменить вопрос"):
        params: dict[str, list[str] | int | str | dict[str, [int, str]]] = {
            "name": f"Какой обновленный язык программирования? {uuid.uuid4().hex}",
            "typeQuestion": type_question,
        }

        if type_question == "single":
            params["values"] = [
                "C",
                "JS",
                "React",
                "Rudy",
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
                "!-_-! Очень хорошо",
                "!-_-! Хорошо",
                "!-_-! Может быть",
                "!-_-! Удовлетворен",
                "!-_-! Не удовлетворен",
            ]
        else:
            raise ValueError(f"Unknown survey question type: {type_question}")

        survey_miniapp.internal_survey_questions_update(
            sender_sn=survey_miniapp.account.uin,
            question_id=question_id,
            survey_id=survey_id,
            **params,
        )

    with allure.step("Проверяем что вопрос изменился"):
        response = survey_miniapp.internal_survey_get(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
        question_list = response["results"]["questions"]

        assert question_list, "Questions list empty"

        for question in question_list:
            if question["name"] == params["name"]:
                assert all(question[key] == value for key, value in params.items()), "Question not found"
