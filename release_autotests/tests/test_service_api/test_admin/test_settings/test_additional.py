import allure

from support.markers import SANDBOX


@allure.id("79657")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Настройки")
@allure.title(
    "Получение дополнительных настроек",
)
@SANDBOX
def test_get_additional_settings(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.get_api_settings_additional()


@allure.id("79656")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Настройки")
@allure.title(
    "Изменение дополнительных настроек",
)
@SANDBOX
def test_post_additional_settings(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.post_api_settings_additional(
            [
                "v.korobov@corp.mail.ru",
                "a.zakhtarenko@vk.team",
            ]
        )
