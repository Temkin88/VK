import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26905")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Настройки приватности")
@allure.feature("Изменение настроек приватности")
@allure.title("Изменение настроек приватности")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("calls", ["nobody", "myContacts", "everybody"])
@pytest.mark.parametrize("groups", ["nobody", "myContacts", "everybody"])
def test_update_privacy_settings(
    calls,
    groups,
    auth_account,
):
    """
    Проверяем изменение настроек приватности
    """
    with allure.step("Изменяем настройки приватности"):
        auth_account.rapi_updatePrivacySettings("calls", calls)
        auth_account.rapi_updatePrivacySettings("groups", groups)

    with allure.step("Проверяем что настройки сохранились"):
        response = auth_account.rapi_getPrivacySetting()

        assert response["status"]["code"] == 20000, "Failed request"

        assert response["results"]["calls"]["allowTo"] == calls, "Calls settings not changed"
        assert response["results"]["groups"]["allowTo"] == groups, "Groups settings not changed"
