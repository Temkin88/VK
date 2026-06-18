import allure
import pytest

from pyvkteamsclient.client.exceptions import RequestException
from support.markers import VKTI, SAAS, TARM, SANDBOX, PRE_SAAS, PRE_VKTI, PRE_TARM


@allure.id("67229")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.suite("Чаты")
@allure.feature("Информация о чате")
@allure.title("Получение информации о чате не участником")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_get_chat_info_not_member(
    auth_account,
    opponent_account,
    prepare_test_chat_admin_only,
):
    """
    Readonly пользователя в чате
    """
    auth_account, opponent_account, group = prepare_test_chat_admin_only

    with pytest.raises(RequestException):
        opponent_account.rapi_getChatInfo(sn=group)
