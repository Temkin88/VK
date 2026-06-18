import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CONTACTS)]


@allure.id("26900")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Участники чата")
@allure.title("Добавление собеседника в чат")
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
    Проверяем добавление пользователя в чат
    """

    main_acc, opponent, group, channel = prepare_test_chats

    with allure.step("Создаем тестовый чат"):
        if chat_type == "group":
            chat = main_acc.create_chat(
                name="Test group for adding member",
            )
        else:
            chat = main_acc.create_chat(
                name="Test group for adding member",
                defaultRole="readonly",
            )

    with allure.step("2. Пробуем добавить пользователя в чат"):
        assert main_acc.rapi_group_members_add(
            sn=chat,
            members=[opponent.uin],
            confirmUnblock=True,
        )
