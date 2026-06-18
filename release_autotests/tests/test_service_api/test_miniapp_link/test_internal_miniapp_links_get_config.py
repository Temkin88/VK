import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("511447")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Получить ссылки для домена мини-аппа")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_internal_miniapp_links_get_сonfig(link_account):
    """
    Получить ссылки для домена мини-аппа

    Используемые фикстуры:
    :param link_account: Клиент для проверки ссылок
    """
    with allure.step("Пробуем получить ссылки для домена мини-аппа"):
        response = link_account.internal_miniapp_links_get_сonfig(sender_sn=link_account.account.uin)
        results = response["results"]["links"]

        assert response["status"]["code"] == 20000, "Response code error"
        assert results, "Empty list"
