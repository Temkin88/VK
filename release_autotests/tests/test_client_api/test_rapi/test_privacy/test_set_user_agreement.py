import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26906")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Настройки приватности")
@allure.feature("Изменение настроек приватности")
@allure.title("Изменение пользовательского соглашения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("set_enable", [True, False], ids=["enable", "disable"])
def test_set_user_agreement(
    set_enable,
    auth_account,
):
    """
    Устанавливает или сбрасывает пользовательское соглашение.
    """
    with allure.step("Делаем запрос"):
        response = auth_account.rapi_setUserAgreement(
            name="gdpr_pp",
            enable=set_enable,
        )

        assert response["status"]["code"] == 20000, "Failed request"
