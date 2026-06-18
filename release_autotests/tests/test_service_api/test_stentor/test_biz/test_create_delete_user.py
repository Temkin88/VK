import allure
from faker import Faker

from support.markers import SANDBOX

fake = Faker("en_US")
Faker.seed(0)


@allure.id("28531")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Biz")
@allure.title(
    "Методы /api/v1/biz/createUser, /api/v1/biz/deleteUser",
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
        )["results"]

        assert response["firstName"] == stentor_account["firstName"], "Wrong firstName"
        assert response["middleName"] == stentor_account["middleName"], "Wrong middleName"
        assert response["lastName"] == stentor_account["lastName"], "Wrong lastName"
        assert response["userState"]["state"] == "absent", "Wrong user state"

    with allure.step("Пытаемся удалить пользователя"):
        stentor.biz_deleteUser(
            email=stentor_account["email"],
        )

    with allure.step("Проверяем пользователя"):
        response = auth_account.rapi_getUserInfo(
            sn=stentor_account["email"],
        )["results"]

        assert response["firstName"] == stentor_account["firstName"], "Wrong firstName"
        assert response["middleName"] == stentor_account["middleName"], "Wrong middleName"
        assert response["lastName"] == stentor_account["lastName"], "Wrong lastName"
        assert response["userState"]["state"] == "blocked", "Wrong user state"
