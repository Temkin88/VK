import time

import allure
from faker import Faker

from support.markers import SANDBOX

fake = Faker("en_US")
Faker.seed(0)


@allure.id("28529")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Biz")
@allure.title(
    "Методы /api/v1/biz/createUser, /api/v1/biz/changeUser, /api/v1/biz/deleteUser",
)
@SANDBOX
def test_create_user(
    stentor,
    auth_account,
    logger,
    stentor_account,
):
    stentor_account.update(
        {
            "title": "test_title",
            "department": "test_department",
        }
    )

    with allure.step("Проверяем пользователя"):
        response = auth_account.rapi_getUserInfo(
            sn=stentor_account["email"],
        )

        response = response["results"]

        assert response["firstName"] == stentor_account["firstName"], "Wrong firstName"
        assert response["middleName"] == stentor_account["middleName"], "Wrong middleName"
        assert response["lastName"] == stentor_account["lastName"], "Wrong lastName"
        assert response["userState"]["state"] == "absent", "Wrong user state"

    with allure.step("Пытаемся изменить пользователя"):
        new_account = stentor_account.copy()

        new_account["firstName"] = fake.first_name()
        new_account["middleName"] = fake.first_name()
        new_account["lastName"] = fake.last_name()
        new_account["phone"] = fake.phone_number()

        stentor.biz_changeUser(**new_account)

    with allure.step("Проверяем пользователя"):
        errors = []

        for i in range(7):
            time.sleep(i)

            try:
                response = auth_account.rapi_getUserInfo(
                    sn=new_account["email"],
                )

                response = response["results"]

                assert response["firstName"] == new_account["firstName"], "Wrong firstName"
                assert response["middleName"] == new_account["middleName"], "Wrong middleName"
                assert response["lastName"] == new_account["lastName"], "Wrong lastName"
                assert response["userState"]["state"] == "absent", "Wrong user state"

                break
            except AssertionError as error:
                errors.append(error)
                continue
        else:
            raise ExceptionGroup(
                __message="Errors in user info after biz/changeUser",
                exceptions=errors,
            )

    with allure.step("Пытаемся удалить пользователя"):
        stentor.biz_deleteUser(
            email=new_account["email"],
        )

    with allure.step("Проверяем пользователя"):
        response = auth_account.rapi_getUserInfo(
            sn=new_account["email"],
        )

        response = response["results"]

        assert response["firstName"] == new_account["firstName"], "Wrong firstName"
        assert response["middleName"] == new_account["middleName"], "Wrong middleName"
        assert response["lastName"] == new_account["lastName"], "Wrong lastName"
        assert response["userState"]["state"] == "blocked", "Wrong user state"
