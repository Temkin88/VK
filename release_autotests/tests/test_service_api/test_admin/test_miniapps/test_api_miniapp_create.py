import allure

from support.markers import SANDBOX


@allure.id("28785")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Миниаппы")
@allure.title(
    "Создание миниаппа",
)
@SANDBOX
def test_api_miniapp_create(
    admin_account,
    outlined_icon_id,
    filled_icon_id,
    showcase_icon_id,
):
    with allure.step("Пробуем создать миниапп"):
        response = admin_account.api_miniapps_create(
            name="Test miniapp autotest",
            description="Test description",
            filled_icon_id=filled_icon_id,
            outlined_icon_id=outlined_icon_id,
            showcase_icon_id=showcase_icon_id,
            allowed_cross_origin_api_hosts=("cdn.jsdelivr.net",),
        )
        app_id = response["result"]["miniappId"]

    with allure.step("Проверяем что мипиапп создался"):
        response = admin_account.api_miniapps_get(
            miniapp_id=app_id,
        )
        assert response["result"]["miniappId"] == app_id, f"{app_id} dont match"
