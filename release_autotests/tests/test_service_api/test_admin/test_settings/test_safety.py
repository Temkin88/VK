import allure

from support.markers import SANDBOX


@allure.id("79662")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Настройки")
@allure.title(
    "Получение информации по активности антивируса",
)
@SANDBOX
def test_get_safety(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.get_api_settings_safety()


@allure.id("79665")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Настройки")
@allure.title(
    "Изменение информации по активности антивируса",
)
@SANDBOX
def test_post_safety(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.post_api_settings_safety(
            antivirus_enabled=True,
            work_mode="async",
            kspd_work_mode="test",
            dmz_work_mode="test",
            key_name="test",
            pin_enabled=False,
        )
