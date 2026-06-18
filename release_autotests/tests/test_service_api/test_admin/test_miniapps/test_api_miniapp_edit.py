import allure

from support.markers import SANDBOX


@allure.id("28784")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Миниаппы")
@allure.title(
    "Редактирование миниаппа",
)
@SANDBOX
def test_api_miniapp_edit(
    admin_account,
    outlined_icon_id,
    filled_icon_id,
    showcase_icon_id,
    miniapp_id,
):
    with allure.step("Пробуем отредактировать миниапп"):
        admin_account.api_miniapps_edit(
            miniapp_id=miniapp_id,
            name="Updated test miniapp autotest",
            description="Updated test description",
            filled_icon_id=filled_icon_id,
            outlined_icon_id=outlined_icon_id,
            showcase_icon_id=showcase_icon_id,
            allowed_cross_origin_api_hosts=("cdn.jsdelivr.net",),
        )
