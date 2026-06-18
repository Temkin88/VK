import allure

from support.markers import SANDBOX


@allure.id("28786")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Миниаппы")
@allure.title(
    "Удаление миниаппа",
)
@SANDBOX
def test_api_miniapp_delete(
    admin_account,
    miniapp_id_for_delete,
):
    with allure.step("Пробуем удалить миниапп"):
        admin_account.api_miniapps_delete(
            miniapp_id=miniapp_id_for_delete,
        )
