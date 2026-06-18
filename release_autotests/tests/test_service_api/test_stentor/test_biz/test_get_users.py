import pytest
import allure

import random
import string

from pyvkteamsclient.stentor.exceptions import HttpNotFoundException

from support.markers import SANDBOX


@allure.id("513332")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Biz")
@allure.title("Проверка получения списка пользователей /api/v1/biz/users")
@SANDBOX
def test_get_users(stentor, stentor_account):
    with allure.step(f"Ищем пользователя по email {stentor_account['email']}"):
        response = stentor.biz_getUsers(sn=stentor_account["email"])

        for user in response["results"]["users"]:
            if (
                user["username"] == stentor_account["email"]
                and user["firstName"] == stentor_account["firstName"]
                and user["lastName"] == stentor_account["lastName"]
            ):
                break
        else:
            pytest.fail(f"User {stentor_account['email']} not found")


@allure.id("513854")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Biz")
@allure.title("Поиск по email несуществующего пользователя /api/v1/biz/users")
@SANDBOX
def test_get_invalid_users(stentor):
    invalid_user_email = "".join(random.choices(string.ascii_letters + string.digits, k=11)) + "@autotest.clients"
    with allure.step(f"Проверяем, что пользователя {invalid_user_email} нет"), pytest.raises(HttpNotFoundException):
        stentor.biz_getUsers(sn=invalid_user_email)
