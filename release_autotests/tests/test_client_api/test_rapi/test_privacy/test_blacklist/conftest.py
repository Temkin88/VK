import allure
import pytest

from pyvkteamsclient.client import DesktopClient


@pytest.fixture(scope="session")
def add_invite_blacklist():
    account_dict: dict[DesktopClient, list[str]] = {}

    def _add_black_list(account: DesktopClient, users_list: list[str]):
        nonlocal account_dict

        response = account.rapi_privacy_groups_inviteBlacklist_add(
            users=users_list,
        )
        assert response["status"]["code"] == 20000, "Response code error"

        if account in account_dict:
            account_dict[account].extend(users_list)
        else:
            account_dict[account] = users_list.copy()

    yield _add_black_list

    for account, users_list in account_dict.items():
        account.rapi_privacy_groups_inviteBlacklist_del(
            users=list(set(users_list)),
        )


@pytest.fixture(scope="session")
def clear_blacklist(
    auth_account,
):
    with allure.step("Очищаем черный список"):
        response = auth_account.rapi_privacy_groups_inviteBlacklist_get(10)
        if response["results"]["blacklist"]:
            auth_account.rapi_privacy_groups_inviteBlacklist_del(response["results"]["blacklist"])
