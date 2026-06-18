import uuid

import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88557")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Обновить параметры опроса про")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_internal_survey_update(
    survey_miniapp,
    survey_id,
):
    """
    Проверяем обновление параметров опроса
    Задаем словарь параметров, пробуем изменить параметры опроса, после изменения получаем опрос и проверяем что
    параметры которые задавали совпадают с полученными

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    """
    params = {
        "creator": survey_miniapp.account.uin,
        "surveyId": survey_id,
        "name": f"Test update name {uuid.uuid4().hex}",
        "description": f"Test update description {uuid.uuid4().hex}",
        "thanks": f"Test update thanks {uuid.uuid4().hex}",
        "forwarding": False,
    }

    with allure.step("Проверяем изменить опрос про"):
        survey_miniapp.internal_survey_update(
            sender_sn=params["creator"],
            survey_id=params["surveyId"],
            name=params["name"],
            description=params["description"],
            thanks=params["thanks"],
            forwarding=params["forwarding"],
        )

    with allure.step("Проверяем что удалось изменить опрос про"):
        response = survey_miniapp.internal_survey_get(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )

        assert all(response["results"][key] == value for key, value in params.items()), "Survey dont match"


@allure.id("552561")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Обновить параметры опроса про для другого домена")
def test_internal_survey_update_isolation(
    survey_miniapp,
    survey_id,
    survey_miniapp_another_domain,
):
    """
    Проверяем обновление параметров опроса
    Задаем словарь параметров, пробуем изменить параметры опроса, после изменения получаем опрос и проверяем что
    параметры которые задавали совпадают с полученными

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    :param survey_miniapp_another_domain: Клиент для создания опросов с другим доменом
    """
    params = {
        "creator": survey_miniapp_another_domain.account.uin,
        "name": f"Test update name {uuid.uuid4().hex}",
        "description": f"Test update description {uuid.uuid4().hex}",
        "thanks": f"Test update thanks {uuid.uuid4().hex}",
    }

    with allure.step("Проверяем изменить опрос про"):
        survey_miniapp.internal_survey_update(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            name=f"Test update name {uuid.uuid4().hex}",
            description=f"Test update description {uuid.uuid4().hex}",
            thanks=f"Test update thanks {uuid.uuid4().hex}",
            forwarding=False,
        )

    with allure.step("Проверяем что удалось изменить опрос про"):
        response = survey_miniapp.internal_survey_get(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )

        assert all(response["results"][key] != value for key, value in params.items()), "Survey match"
