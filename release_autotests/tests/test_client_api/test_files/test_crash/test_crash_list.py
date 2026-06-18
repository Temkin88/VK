import allure
import pytest

from support.markers import VKTI, SAAS, TARM, SANDBOX, PRE_SAAS, PRE_VKTI, PRE_TARM

from pyvkteamsclient.client.exceptions import RequestException, AccessDeniedException


@allure.id("37357")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Крэши")
@allure.feature("Загрузка крэш дампа")
@allure.title("Получение списка крэшей на сервере")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("platform_name", ["desktop", "ios", "android"])
def test_crash_list(
    auth_account,
    platform_name,
):
    """
    Проверяем список крашей
    :param auth_account: Основной аккаунт
    :param platform_name: Параметризация с видами платформ
    """
    with allure.step("Получаем список крэшей"), pytest.raises((RequestException, AccessDeniedException)):
        auth_account.files_crash_list(
            platform=platform_name,
        )
