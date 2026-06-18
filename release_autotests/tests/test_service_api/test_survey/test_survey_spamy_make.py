import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("190964")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Рассылка спама")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_internal_spamy_make(
    survey_miniapp,
    survey_id,
):
    """

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param chat: список пользователей
    """
    with allure.step("Пытаемся создать опрос"):
        response = survey_miniapp.internal_spamy_make(
            sender_sn=survey_miniapp.account.uin,
            chat=[survey_miniapp.account.uin],
        )

        assert response["results"]["id"], "Field id not found"
        assert survey_miniapp.account.uin in response["results"]["list"], "Account not in list"
