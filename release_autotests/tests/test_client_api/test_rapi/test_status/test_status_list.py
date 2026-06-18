import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26923")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Статусы")
@allure.feature("Список готовых статусов")
@allure.title("Получение списка статусов без хэша")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_status_list(auth_account, ENV_PLATFORM):
    """
    Получение списка статусов
    """

    with allure.step("Получение списка статусов без хэша"):
        response = auth_account.rapi_status_list(
            _hash=None,
            lang="RU",
        )

        assert response["status"]["code"] == 20000, "Failed to get statuses list"

        list_hash = response["results"]["hash"]
        statuses_list = response["results"]["statuses"]

        assert not statuses_list if ENV_PLATFORM in ["ICQ", "SAAS"] else statuses_list, "Received empty statuses list"

    with allure.step("Получение списка статусов по хэшу"):
        response = auth_account.rapi_status_list(
            _hash=list_hash,
            lang="RU",
        )

        assert response["status"]["code"] == 30400, "Received code not equal 30400"
