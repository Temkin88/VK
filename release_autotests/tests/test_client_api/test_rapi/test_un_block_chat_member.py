import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CONTACTS)]


@allure.id("26892")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Администрирование чата")
@allure.feature("Блокирование пользователя в чате")
@allure.title("Блокирование и разблокировка пользователя в чате")
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.parametrize("with_del_last_msgs", [True, False], ids=["with_delete", "without_delete"])
def test_block_user_in_chat(
    chat_type,
    with_del_last_msgs,
    auth_account,
    opponent_account,
    prepare_test_chats_admin,
):
    """
    Блокирование и разблокирование пользователя в чате
    """
    group, channel = prepare_test_chats_admin

    chat = group if chat_type == "group" else channel

    with allure.step("Пробуем заблокировать пользователя в чате"):
        auth_account.rapi_blockChatMember(
            sn=chat,
            members=[opponent_account.uin],
            deleteLastMessages=with_del_last_msgs,
        )

    with allure.step("Пробуем разблокировать пользователя в чате"):
        auth_account.rapi_unblockChatMembers(
            sn=chat,
            members=[opponent_account.uin],
        )
