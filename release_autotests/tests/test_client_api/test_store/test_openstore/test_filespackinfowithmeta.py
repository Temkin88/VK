import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("30145")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Стикеры")
@allure.feature("Информация о стикерах")
@allure.title("Метод store/openstore/filespackinfowithmeta")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_filespackinfowithmeta(
    auth_account,
):
    with allure.step("Получаем список стикер паков"):
        response = auth_account.store_showcase()

    with allure.step("Проверяем запрос мета инфы о паке"):
        for case in response["result"]["showcase"]:
            sticker_meta = auth_account.openstore_filespackinfowithmeta(
                pack_id=case["id"],
            )

            assert sticker_meta["data"]["store_id"] == case["store_id"], "Wrong store_id in meta"

            assert sticker_meta["data"]["price"] == 0, "Wrong price in meta"
