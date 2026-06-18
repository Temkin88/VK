import allure
import pytest


@allure.title("Подготовка тестовых чатов")
@pytest.fixture(scope="session")
def prepare_bot_test_chats(
    request,
    opponent_account,
    auth_account,
    bot_class,
):
    with allure.step("Создаем тестовую группу"):
        group = auth_account.create_chat(
            f"Test group - {request.node.name}",
            members=[opponent_account, bot_class.uin],
        )

        auth_account.rapi_modChatMember(
            sn=group,
            memberSn=bot_class.uin,
        )

    with allure.step("Создаем тестовый канал"):
        channel = auth_account.create_chat(
            f"Test channel - {request.node.name}",
            defaultRole="readonly",
            members=[opponent_account, bot_class.uin],
        )

        auth_account.rapi_modChatMember(
            sn=channel,
            memberSn=bot_class.uin,
        )

    return auth_account, opponent_account, group, channel
