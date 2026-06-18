import allure
import pytest


@allure.title("Инфо о группах для теста biz/chats")
@pytest.fixture(scope="session", autouse=True)
def stentor_groups_info(request, opponent_account):
    return {
        "name": f"Test - {request.node.name}",
        "public": True,
        "defaultRole": "member",
        "members": [opponent_account],
    }
