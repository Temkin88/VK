import random

import allure
import etcd3

import pytest
import requests

from pyvkteamsclient.staffd import StaffdClient


@pytest.fixture(scope="session")
def staffd(ENV_PLATFORM, PROXY, swagger_http_spy, web_url):
    pytest.skip("staffD: Test run only on sandbox host machine locally")

    session = requests.Session()
    session.headers = {
        "X-Token": "X-Tests",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/113.0.0.0 Safari/537.36",
        "Referer": web_url,
        "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "macOS",
    }
    session.verify = False

    if PROXY is not None:
        session.proxies = {
            "http": PROXY,
            "https": PROXY,
        }

    if swagger_http_spy is not None:
        swagger_http_spy.register_as_hook(session)

    return StaffdClient(
        session=session,
        env=ENV_PLATFORM,
    )


@pytest.fixture(scope="session")
def etcd():
    return etcd3.client(host="etcd.im-etcd.svc.cluster.local", port=2379, grpc_options="--endpoints")


@pytest.fixture(scope="session")
def create_group(
    staffd,
):
    group_id = str(random.randint(1, 100))
    with allure.step("Пытаемся добавить группу"):
        response = staffd.add_group(group_id=group_id, name="Test-head-1-1", parent_id=group_id)
        assert response["isCreated"], "Group not created"

    return group_id


@pytest.fixture(scope="session")
def create_users(
    staffd,
    auth_account,
    opponent_account,
    third_account,
    create_group,
):
    with allure.step("Пытаемся добавить пользователей"):
        response = staffd.create_user(
            [
                {
                    "id": auth_account.uin,
                    "firstName": auth_account.uin.split("@")[0],
                    "lastName": auth_account.uin.split("@")[-1],
                    "groupID": create_group,
                },
                {
                    "id": opponent_account.uin,
                    "firstName": opponent_account.uin.split("@")[0],
                    "lastName": opponent_account.uin.split("@")[-1],
                    "groupID": create_group,
                },
                {
                    "id": third_account.uin,
                    "firstName": third_account.uin.split("@")[0],
                    "lastName": third_account.uin.split("@")[-1],
                    "groupID": create_group,
                },
            ]
        )
        staffd.sync_users()

    return response


@pytest.fixture(scope="session", autouse=True)
def remote_users_groups(
    staffd,
    auth_account,
    opponent_account,
    third_account,
    create_group,
):
    with allure.step("Пробуем удалить пользователя"):
        staffd.remove_user(
            user_id=auth_account.uin,
        )
        staffd.remove_user(
            user_id=opponent_account.uin,
        )
        staffd.remove_user(
            user_id=third_account.uin,
        )

    with allure.step("Пробуем удалить группу"):
        staffd.remove_group(group_id=create_group)
