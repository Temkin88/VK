import allure
import lorem

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.BASE_APP)]


@allure.id("26932")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Поддержка")
@allure.feature("Отправка отчета")
@allure.title("Отправка отчета ошибки об ошибке")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_send_report(auth_account, logs_file, photo_id):
    with allure.step("Отправляем тестовый отчет"):
        auth_account.rapi_misc_support(
            message=lorem.paragraph(),
            platform="web",
            appVersion=lorem.sentence(),
            osVersion="5.0 (Macintosh; "
            "Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            device="MacIntel",
            attachmentFileId=logs_file,
            screenshotFileIdList=[photo_id],
        )
