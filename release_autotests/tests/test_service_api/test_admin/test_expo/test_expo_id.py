import allure
import pytest

from support.markers import SANDBOX


@allure.id("79691")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление витриной чатов")
@allure.title(
    "Удаление позиции из витрины",
)
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_api_expo_delete(admin_account, auth_account, chat_type):
    chat_id = auth_account.create_chat(
        name=f"[{auth_account.getReqId()}]",
        public=True,
        defaultRole="member" if chat_type == "group" else "readonly",
    )

    with allure.step("Пробуем выполнить запрос"):
        admin_account.api_expo_post(chat_id)

    with allure.step("Пробуем выполнить запрос"):
        admin_account.api_expo_delete(chat_id)


@allure.id("79692")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление витриной чатов")
@allure.title(
    "Обновление позиции чата в витрине",
)
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_api_expo_put(admin_account, auth_account, chat_type):
    chat_id = auth_account.create_chat(
        name=f"[{auth_account.getReqId()}]",
        public=True,
        defaultRole="member" if chat_type == "group" else "readonly",
    )

    with allure.step("Пробуем выполнить запрос"):
        admin_account.api_expo_post(chat_id)

    with allure.step("Пробуем выполнить запрос"):
        admin_account.api_expo_put(chat_id, 1)
