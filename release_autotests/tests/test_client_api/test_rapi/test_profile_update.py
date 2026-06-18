import allure
import pytest
import requests

from pyvkteamsclient.client.exceptions import RequestException
from support.markers import VKTI, TARM, PRE_VKTI, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.PROFILE)]


@allure.id("66429")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Профиль")
@allure.feature("Изменение профиля")
@allure.title("Ошибка запроса на изменение профиля")
def test_profile_update_error(
    auth_account,
    get_myteam_config,
    ENV_PLATFORM,
):
    with allure.step("Получаем allow-self-info-change"):
        if ENV_PLATFORM in ["TARM", "SAAS"]:
            get_myteam_config = requests.get(get_myteam_config["myteam-config.json.url"]).json()

        if get_myteam_config["allow-self-info-change"]:
            pytest.skip('Значение "allow-self-info-change" в статусе True')

        else:
            with pytest.raises(RequestException):
                auth_account.rapi_profile_update(
                    first_name="Test first_name",
                    last_name="Test last_name",
                    middle_name="Test middle_name",
                    about="Test about",
                )


@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.id("66428")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Профиль")
@allure.feature("Изменение профиля")
@allure.title("Запроса на изменение профиля")
def test_profile_update(auth_account, get_myteam_config, ENV_PLATFORM):
    with allure.step("Получаем allow-self-info-change"):
        if ENV_PLATFORM in ["TARM", "SAAS"]:
            get_myteam_config = requests.get(get_myteam_config["myteam-config.json.url"]).json()

        if get_myteam_config["allow-self-info-change"]:
            response = auth_account.rapi_profile_update(
                first_name="Test first_name",
                last_name="Test last_name",
                middle_name="Test middle_name",
                about="Test about",
            )
            assert response["status"]["code"] == 20000

        else:
            pytest.skip("Значение allow-self-info-change в статусе True")
