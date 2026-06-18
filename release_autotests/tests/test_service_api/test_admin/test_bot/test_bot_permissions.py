import allure
import pytest

from support.markers import SANDBOX


@allure.id("28693")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Боты")
@allure.title(
    "Изменение прав ботов",
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
    with allure.step("Пробуем изменить permissions бота"):
        admin_account.patch_api_bot_id(bot_id, [])

    with allure.step("Пробуем вернуть permissions бота"):
        admin_account.patch_api_bot_id(
            bot_id,
            [
                "can_create_chats",
                "can_write_first",
            ],
        )
