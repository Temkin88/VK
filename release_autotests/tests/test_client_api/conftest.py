import pytest
import allure


@pytest.fixture(scope="session")
def miniapp_id(myteam_config):
    if myteam_config.get("custom-miniapps"):
        yield myteam_config["custom-miniapps"][0]["id"]

    else:
        pytest.skip("No custom miniapps in myteam-config.json")


@pytest.fixture(scope="session")
def is_draft_enabled(myteam_config):
    draft_enabled = ("draft-enabled" not in myteam_config) or (
        "draft-enabled" in myteam_config and myteam_config["draft-enabled"]
    )
    return draft_enabled


@allure.title("Подготовка тестовых чатов")
@pytest.fixture(scope="session")
def prepare_test_chats_msg(
    request,
    opponent_account,
    auth_account,
):
    with allure.step("Создаем тестовую группу"):
        group = auth_account.create_chat(
            f"Test group - {request.node.name}",
            members=[opponent_account],
        )

    with allure.step("Создаем тестовый канал"):
        channel = auth_account.create_chat(
            f"Test channel - {request.node.name}",
            defaultRole="readonly",
            members=[opponent_account],
        )

    return auth_account, opponent_account, group, channel


@allure.title("Подготовка тестовых чатов")
@pytest.fixture(scope="session")
def prepare_test_chats_msg_isolation(
    request,
    auth_account_with_domain_testbiz,
    auth_account_with_domain_testb1iz,
):
    with allure.step("Создаем тестовую группу"):
        group = auth_account_with_domain_testbiz.create_chat(
            f"Test group - {request.node.name}",
            members=[auth_account_with_domain_testb1iz],
        )

    with allure.step("Создаем тестовый канал"):
        channel = auth_account_with_domain_testbiz.create_chat(
            f"Test channel - {request.node.name}",
            defaultRole="readonly",
            members=[auth_account_with_domain_testb1iz],
        )

    return auth_account_with_domain_testbiz, auth_account_with_domain_testb1iz, group, channel
