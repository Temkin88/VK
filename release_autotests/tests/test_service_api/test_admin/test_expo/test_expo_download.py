import allure

from support.markers import SANDBOX


@allure.id("79690")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление витриной чатов")
@allure.title(
    "Скачивание списка позиций витрины чатов",
)
@SANDBOX
def test_api_expo_download(admin_account):
    with allure.step("Пробуем выполнить запрос"):
        admin_account.api_expo_download("group")
