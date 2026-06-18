import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("31907")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Контакты")
@allure.feature("Удаление контакта")
@allure.title("Удалить контакт")
def test_contact_delete(
    setup_contact_add,
    auth_account,
    opponent_account,
):
    with allure.step("Пробуем удалить контакт"):
        auth_account.rapi_contacts_delete([opponent_account.uin])

    with allure.step("Проверяем что удалили оппонента"):
        response = auth_account.rapi_contacts_get()

        # persons сортируется по sn, собираем список всех и ищем в нем
        sns = [x["sn"] for x in response["results"]["contacts"]]

        assert opponent_account.uin not in sns, "contacts/delete - fail, contact still in list"
