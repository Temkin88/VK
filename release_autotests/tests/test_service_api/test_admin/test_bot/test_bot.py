import allure
import pytest

from support.markers import SANDBOX


@allure.id("28694")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Боты")
@allure.title(
    "Получение списка ботов",
)
@pytest.mark.parametrize(
    "permissions",
    [
        None,
        ("can_write_first", "can_create_chats"),
    ],
)
@SANDBOX
def test_bot(admin_account, permissions):
    with allure.step("Пробуем получить список ботов"):
        admin_account.api_bot(permissions)
