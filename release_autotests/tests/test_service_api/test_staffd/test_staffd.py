import random

import allure

from support.markers import SANDBOX


@SANDBOX
def test_users(
    staffd,
    auth_account,
):
    group_id = str(random.randint(1, 100))

    with allure.step("Пытаемся добавить пользователя"):
        response = staffd.create_user(
            [
                {
                    "id": auth_account.uin,
                    "firstName": auth_account.uin.split("@")[0],
                    "lastName": auth_account.uin.split("@")[-1],
                    "groupID": group_id,
                }
            ]
        )

        results = response["users"][0]
        assert results["id"] == auth_account.uin, "Id dont match"
        assert results["status"] in ["updated", "created"], f"status not in list {['updated', 'created']}"

    with allure.step("Проверяем что пользователь создался"):
        response = staffd.get_user_by_id(
            user_id=auth_account.uin,
        )

        assert response["id"] == auth_account.uin, "Id dont match"
        assert response["firstName"] == auth_account.uin.split("@")[0], "first name dont match"
        assert response["lastName"] == auth_account.uin.split("@")[-1], "last name dont match"

    with allure.step("Пробуем удалить пользователя"):
        staffd.remove_user(
            user_id=auth_account.uin,
        )

    with allure.step("Проверяем что пользователь удалился"):
        staffd.get_user_by_id(
            user_id=auth_account.uin,
        )

    staffd.sync_users()


@SANDBOX
def test_users_in_group(
    staffd,
    auth_account,
    opponent_account,
    third_account,
    create_users,
):
    with allure.step("Проверяем что пользователи добавились в группу"):
        for results, user in zip(
            create_users["users"],
            (auth_account, opponent_account, third_account),
            strict=False,
        ):
            assert results["id"] == user.uin, "Id dont match"
            assert results["status"] in ["updated", "created"], f"status not in list {['updated', 'created']}"

    with allure.step("Проверяем что группа создалась"):
        response = staffd.get_group_by_id(group_id="4")
        assert response["id"] == "4", "Id dont match"
        assert response["name"] == "Test-head-1-1", "name dont match"
        assert response["parentName"] == "Test-head-1-1", "parent name dont match"
        assert response["parentID"] == "4", "parent id dont match"

    with allure.step("Проверяем получение списка групп"):
        response = staffd.get_groups_list()
        assert "4" in response["groups"], 'group id "4" not in groups'

    with allure.step("Проверяем получение пользователя группы"):
        response = staffd.get_group_users(group_id="4")
        results = response["users"]
        assert results["id"] == auth_account.uin, "Id dont match"
        assert results["firstName"] == auth_account.uin.split("@")[0], "first name dont match"
        assert results["lastName"] == auth_account.uin.split("@")[-1], "last name dont match"
        assert results["groupID"] == "4", "group id dont match"
        assert results["groupName"] == "Test-head-1-1", "group name dont match"


@SANDBOX
def test_etc_config_group(
    staffd,
    auth_account,
    opponent_account,
    third_account,
    etcd,
    create_group,
):
    with allure.step("Проверяем что данные добавились в конфиг"):
        response = etcd.get(
            "/vars/services/staffd/development/public/service/auto_add/auto_add_json_config",
            create_group,
        )

        for results, user in zip(
            response,
            (auth_account, opponent_account, third_account),
            strict=False,
        ):
            assert user.uin in results, f"{user.uin} not in {results}"


@SANDBOX
def test_etc_config_manual(
    staffd,
    auth_account,
    opponent_account,
    third_account,
    etcd,
    create_group,
):
    with allure.step("Проверяем что данные добавились в конфиг"):
        params = {
            create_group: [
                {
                    "name": "IMSERVER: Autotest",
                    "rid": "",
                    "admins": [auth_account.uin, opponent_account.uin, third_account.uin],
                },
            ],
        }

        etcd.put("/vars/services/staffd/development/public/service/auto_add/auto_add_json_config", params)

        response = etcd.get(
            "/vars/services/staffd/development/public/service/auto_add/auto_add_json_config",
            create_group,
        )
        assert response == params


@SANDBOX
def test_add_group(
    staffd,
):
    group_id = str(random.randint(1, 100))
    with allure.step("Пытаемся добавить группу"):
        response = staffd.add_group(group_id=group_id, name="Test-head-1-1", parent_id="4")
        assert response["isCreated"]

    staffd.sync_users()

    with allure.step("Проверяем что группа создалась"):
        response = staffd.get_group_by_id(group_id="4")
        assert response["id"] == group_id, "Id dont match"
        assert response["name"] == "Test-head-1-1", "name dont match"
        assert response["parentName"] == "Test-head-1-1", "parent name dont match"
        assert response["parentID"] == "4", "parent id dont match"


@SANDBOX
def test_remove_group(
    staffd,
):
    group_id = str(random.randint(1, 100))

    with allure.step("Пытаемся добавить группу"):
        response = staffd.add_group(group_id=group_id, name="Test-head-1-1", parent_id="4")
        assert response["isCreated"]

    staffd.sync_users()

    with allure.step("Пробуем удалить группу"):
        staffd.remove_group(group_id=group_id)

    with allure.step("Проверяем что группа удалилась"):
        response = staffd.get_group_users(group_id=group_id)
        assert not response["users"], "users field not empty"
