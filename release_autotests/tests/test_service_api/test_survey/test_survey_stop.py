import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("88565")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Завершить опрос про")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_internal_survey_stop(
    survey_miniapp,
    survey_id,
    survey_start,
):
    """
    Проверяем остановку опроса.
    Проверяем что в поле active стоит значение False

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    :param survey_start: запускаем опрос
    """
    with allure.step("Проверяем то не активен опрос"):
        response = survey_miniapp.account.rapi_survey_get(
            survey_id=survey_id,
        )

        if not response["results"]["active"]:
            survey_miniapp.internal_survey_targets_add(
                sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_list=[survey_miniapp.account.uin]
            )
            survey_miniapp.internal_survey_start(
                sender_sn=survey_miniapp.account.uin,
                survey_id=survey_id,
                targets=[survey_miniapp.account.uin],
            )

    with allure.step("Пробуем завершить опрос"):
        response = survey_miniapp.internal_survey_stop(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )

        assert not response["results"]["active"], "Field active True"
