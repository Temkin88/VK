import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26907")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Настройки приватности")
@allure.feature("Черный список")
@allure.title("Получение пустого черного списка")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_get_empty_invite_blacklist(auth_account):
    """
    Получение пустого черного списка
    """
    with allure.step("Делаем запрос"):
        response = auth_account.rapi_privacy_groups_inviteBlacklist_get(10)

        assert response["status"]["code"] == 20000, "Failed request"

    with allure.step("Проверяем что список пустой"):
        resp_results = response["results"]

        assert isinstance(resp_results["blacklist"], list)
        assert not resp_results["blacklist"], "Not empty blacklist"


@allure.id("28159")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Настройки приватности")
@allure.feature("Черный список")
@allure.title("Получение черного списка")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_get_invite_blacklist(
    auth_account,
    add_invite_blacklist,
):
    """
    Получение черного списка
    """

    uins_list = [
        "1000000001",
        "1000000002",
    ]

    with allure.step("Добавляем uin в черный список"):
        add_invite_blacklist(
            account=auth_account,
            users_list=uins_list,
        )

    with allure.step("Проверяем что uin появились в черном списке"):
        response = auth_account.rapi_privacy_groups_inviteBlacklist_get(10)

        assert response["status"]["code"] == 20000, "Failed request"
        assert all(uin in response["results"]["blacklist"] for uin in uins_list), "Uin not in blacklist"
