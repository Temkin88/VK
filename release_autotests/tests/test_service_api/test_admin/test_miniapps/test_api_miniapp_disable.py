import allure

from support.markers import SANDBOX


@allure.id("28791")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Миниаппы")
@allure.title(
    "Отключение миниаппа",
)
@SANDBOX
def test_api_miniapp_disable(
    admin_account,
    miniapp_id,
):
    with allure.step("Отключаем миниапп"):
        admin_account.api_miniapps_disable(
            miniapp_id=miniapp_id,
        )

    with allure.step("Пробуем получить информацию о миниаппе"):
        response = admin_account.api_miniapps_get(
            miniapp_id=miniapp_id,
        )

    with allure.step("Проверяем полученные данные"):
        miniapp = response["result"]

        assert not miniapp["enabled"], "MiniApp is enabled"

    with allure.step("Включаем миниапп"):
        admin_account.api_miniapps_enable(
            miniapp_id=miniapp_id,
        )
