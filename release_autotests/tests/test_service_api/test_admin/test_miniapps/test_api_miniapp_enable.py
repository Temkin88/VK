import allure

from support.markers import SANDBOX


@allure.id("28792")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Миниаппы")
@allure.title(
    "Включение миниаппа",
)
@SANDBOX
def test_api_miniapp_enable(
    admin_account,
    miniapp_id,
):
    with allure.step("Включаем миниапп"):
        admin_account.api_miniapps_enable(
            miniapp_id=miniapp_id,
        )

    with allure.step("Получаем инфо о миниаппе"):
        response = admin_account.api_miniapps_get(miniapp_id)

    with allure.step("Проверяем статус миниаппа"):
        miniapp = response["result"]

        assert miniapp["enabled"], "MiniApp is disabled"
