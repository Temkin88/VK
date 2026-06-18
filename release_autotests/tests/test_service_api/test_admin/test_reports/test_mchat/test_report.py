import time

import allure

from support.markers import SANDBOX
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.MINIAPPS)]


@allure.id("79655")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Настройки")
@allure.title(
    "Выгрузка участников групп и каналов",
)
@SANDBOX
def test_get_mchat_report(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.api_mchat_report("GET")


@allure.id("79659")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Настройки")
@allure.title(
    "Запрос на создание списка участников групп и каналов",
)
@SANDBOX
def test_post_mchat_report(admin_account):
    with allure.step("Запрашиваем создание отчета"):
        response = admin_account.api_mchat_report("POST")

    with allure.step("Пробуем скачать отчет"):
        time.sleep(3)
        admin_account.api_mchat_report_download(
            uuid=response["result"]["last_report"]["UUID"],
        )
