import allure
import pytest

from support.markers import SANDBOX


@allure.id("79676")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление группами и каналами")
@allure.title(
    "Поиск по группам и каналам",
)
@SANDBOX
@pytest.mark.parametrize(
    "chat_type",
    [
        # 'private',
        # 'bot',
        "group",
        "channel",
    ],
)
@pytest.mark.parametrize("is_chat_public", [True, False])
def test_api_chats_search(
    admin_account,
    auth_account,
    chat_type,
    is_chat_public,
):
    with allure.step("Создаем чат"):
        chat_title = f"[{auth_account.getReqId()}]"
        chat_id = auth_account.create_chat(
            name=chat_title,
            public=is_chat_public,
            defaultRole="member" if chat_type == "group" else "readonly",
        )

    with allure.step("Пробуем найти его в списке"):
        response = admin_account.api_chats_search(
            filter_q=chat_title,
            filter_public=is_chat_public,
        )

        assert chat_id in [x["id"] for x in response["result"]["chats"]], f"Chat_id {chat_id} not found"
