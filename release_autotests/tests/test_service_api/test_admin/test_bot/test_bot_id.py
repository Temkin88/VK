import allure
import pytest

from support.markers import SANDBOX


@allure.id("28691")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Боты")
@allure.title(
    "Получение информации о боте по ID",
)
@pytest.mark.parametrize(
    "bot_id",
    [
        "70001",
        "100500",
        "100000",
    ],
    ids=[
        "metabot",
        "stickers_bot",
        "task_bot",
    ],
)
@SANDBOX
def test_bot(admin_account, bot_id):
    with allure.step("Пробуем получить информацию о боте"):
        admin_account.api_bot_id(bot_id)
