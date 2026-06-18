import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CONTACTS)]


@allure.id("79673")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Участники чата")
@allure.title("Удаление собеседника из чата")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_group_members_add(
    chat_type,
    prepare_test_chats,
):
    """
    Проверяем Удаление пользователя из чат
    """

    auth_account, opponent_account, group, channel = prepare_test_chats

    with allure.step("Создаем тестовый чат"):
        chat_id = auth_account.create_chat(
            name="Test group for adding member",
            members=[opponent_account],
            defaultRole="member" if chat_type == "group" else "readonly",
        )

    with allure.step("Пробуем удалить пользователя из чат"):
        assert auth_account.rapi_group_members_delete(
            sn=chat_id,
            members=[opponent_account.uin],
        )

    with allure.step("Проверяем что пользователь удален"):
        response = auth_account.rapi_getChatInfo(
            sn=chat_id,
        )
        assert opponent_account.uin not in [x["sn"] for x in response["results"]["members"]], (
            f"{auth_account.env}:User mentioned as pending"
        )
