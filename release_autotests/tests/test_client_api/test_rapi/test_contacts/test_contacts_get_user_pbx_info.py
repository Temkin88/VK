import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("86223")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Контакты")
@allure.feature("Получить информацию")
@allure.title("Получить информацию о PBX-биндингах пользователя")
@pytest.mark.skip("Нет на песке state_stage и нет песка где эта функциональность раскатана")
def test_contacts_get_user_pbx_info(
    auth_account,
):
    with allure.step("Пробуем получить информацию"):
        auth_account.rapi_getUserPbxInfo(
            sn=auth_account.uin,
        )
