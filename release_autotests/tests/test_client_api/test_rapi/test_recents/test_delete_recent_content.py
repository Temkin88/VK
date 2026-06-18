import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CONTACTS)]


@allure.id("37350")
@allure.label("layer", "api_layer")
@allure.label("jira", "IMQA-1101")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Инпут медиа")
@allure.feature("Инпут медиа")
@allure.title("Удаление emoji, стикеров и gif, отправленных пользователем")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.skip("IMQA-1101")
def test_delete_recent_content(
    auth_account,
):
    # TODO @v.korobov: Needs to investigate

    with allure.step("Пробуем отправить первичный запрос"):
        auth_account.rapi_deleteRecentContent(
            emoji=["😁"],
        )
