import allure

from support.markers import SANDBOX


@allure.id("28789")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Миниаппы")
@allure.title(
    "Получение списка миниаппов",
)
@SANDBOX
def test_api_miniapp_list(
    admin_account,
    miniapp_id,
    outlined_icon_id,
    filled_icon_id,
    showcase_icon_id,
):
    with allure.step("Пробуем получить список миниаппов"):
        response = admin_account.api_miniapps_list()

    with allure.step("Проверяем что свеже созданный миниапп есть в списке"):
        miniapp_index = [x["miniappId"] for x in response["result"]["miniapps"]].index(miniapp_id)

        miniapp = response["result"]["miniapps"][miniapp_index]

        assert miniapp["name"] == "Test miniapp autotest" or miniapp["name"] == "Updated test miniapp autotest", (
            "Wrong name"
        )
        assert miniapp["description"] == "Test description" or miniapp["description"] == "Updated test description", (
            "Wrong description"
        )
