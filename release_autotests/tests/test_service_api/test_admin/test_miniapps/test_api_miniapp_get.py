import allure

from support.markers import SANDBOX


@allure.id("28788")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Миниаппы")
@allure.title(
    "Получение информации о миниаппе",
)
@SANDBOX
def test_api_miniapp_get(
    admin_account,
    miniapp_id,
):
    with allure.step("Пробуем получить информацию о миниаппе"):
        response = admin_account.api_miniapps_get(
            miniapp_id=miniapp_id,
        )

    with allure.step("Проверяем полученные данные"):
        miniapp = response["result"]

        assert miniapp["name"] == "Test miniapp autotest" or miniapp["name"] == "Updated test miniapp autotest", (
            "Wrong name"
        )
        assert miniapp["description"] == "Test description" or miniapp["description"] == "Updated test description", (
            "Wrong description"
        )
