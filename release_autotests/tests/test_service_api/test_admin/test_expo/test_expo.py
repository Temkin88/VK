import allure
import pytest

from support.markers import SANDBOX


@allure.id("79689")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление витриной чатов")
@allure.title(
    "Получение списка позиций витрины чатов",
)
@SANDBOX
def test_api_expo_get(admin_account):
    with allure.step("Пробуем выполнить запрос"):
        admin_account.api_expo_get("group")


@allure.id("79688")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление витриной чатов")
@allure.title(
    "Добавление публичных чата/канала/бота в витрину",
)
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_api_expo_post(
    admin_account,
    auth_account,
    chat_type,
):
    chat_id = auth_account.create_chat(
        name=f"[{auth_account.getReqId()}]",
        public=True,
        defaultRole="member" if chat_type == "group" else "readonly",
    )

    with allure.step("Пробуем выполнить запрос"):
        admin_account.api_expo_post(chat_id)
