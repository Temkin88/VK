import allure
import pytest
from pyvkteamsclient.client import RequestException

from support.markers import SANDBOX


@allure.id("511446")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Проверить существование хэша для формирования временных url для скачивания iOS приложения")
@SANDBOX
def test_dl_veryfi_hash(
    auth_account,
):
    """
    Проверить существование хэша для формирования временных url для скачивания iOS приложения

    Используемые фикстуры:
    :param auth_account: Клиент
    """
    auth_account.rapi_dl_send(email=auth_account.uin)

    response = auth_account.rapi_dl_verify(email=auth_account.uin)

    with allure.step("Пробуем получить результаты опроса"):
        with pytest.raises(RequestException) as exeption:
            auth_account.rapi_internal_dl_verify_hash(transient_hash=response["results"]["hash"])

        assert exeption.value.response_status_code == 401, "Response code dont matched"
