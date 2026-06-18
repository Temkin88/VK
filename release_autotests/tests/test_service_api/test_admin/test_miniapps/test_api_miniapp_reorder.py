import allure

from support.markers import SANDBOX


@allure.id("28787")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Миниаппы")
@allure.title(
    "Изменения порядка миниаппов в списке",
)
@SANDBOX
def test_api_miniapp_reorder(
    admin_account,
    filled_icon_id,
    outlined_icon_id,
    showcase_icon_id,
):
    with allure.step("Создаем миниапп"):
        admin_account.api_miniapps_create(
            name="Test miniapp autotest",
            description="Test description",
            filled_icon_id=filled_icon_id,
            outlined_icon_id=outlined_icon_id,
            showcase_icon_id=showcase_icon_id,
        )["result"]["miniappId"]

    with allure.step("Получаем список миниаппов"):
        miniapps_list = admin_account.api_miniapps_list()["result"]["miniapps"]

        if len(miniapps_list) <= 1:
            return

        list_before_test = [x["miniappId"] for x in miniapps_list]

    with allure.step("Переставляем миниаппы местами"):
        reordered_list = list_before_test[1:] + list_before_test[:1]

    with allure.step("Отправляем запрос на смену порядка"):
        admin_account.api_miniapps_reorder(
            miniapp_ids=reordered_list,
        )

    with allure.step("Получаем список миниаппов"):
        response = admin_account.api_miniapps_list()
        list_after_test = [x["miniappId"] for x in response["result"]["miniapps"]]

    with allure.step("Сверяем порядок миниаппов"):
        assert list_after_test == reordered_list, "Wrong miniapps order"
