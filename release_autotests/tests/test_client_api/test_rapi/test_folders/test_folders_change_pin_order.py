import allure

from support.markers import VKTI, PRE_VKTI, SANDBOX, SAAS, TARM, PRE_TARM, PRE_SAAS


@allure.id("255566")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Изменение порядка запиненных чатов (пинов) в папке")
@allure.title("Изменение порядка запиненных чатов (пинов) в папке")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_archive_change_pin_order(
    auth_account,
    folder_id,
):
    """
    Изменение порядка запиненных чатов (пинов) в папке
    :param folder_id: Фикстура возвтращает folders_id созданной папки
    """

    with allure.step("Получение чатов которые в папке"):
        response = auth_account.rapi_folders_get_content(folder_id=folder_id)
        chats_folders = response["results"]["chats"]

    with allure.step("Добавляем пины на чаты папке"):
        for chat in chats_folders:
            auth_account.rapi_folders_chatPin(folder_id=folder_id, chat_id=chat, pin=True)

    with allure.step("Проверяем что чаты в нужном порядке"):
        response = auth_account.rapi_folders_get_content(folder_id=folder_id)
        before_pins = response["results"]["pins"]

        auth_account.rapi_folders_changePinsOrder(folder_id=folder_id, pins=before_pins)
        response = auth_account.rapi_folders_get_content(folder_id=folder_id)
        after_pins = response["results"]["pins"]

        assert before_pins == after_pins, "Pins orders dont match"

    with allure.step("Проверяем что чаты в измененном порядке"):
        response = auth_account.rapi_folders_get_content(folder_id=folder_id)
        before_pins_reverts = response["results"]["pins"][::-1]

        auth_account.rapi_folders_changePinsOrder(folder_id=folder_id, pins=before_pins_reverts)
        response = auth_account.rapi_folders_get_content(folder_id=folder_id)
        after_pins_reverts = response["results"]["pins"]

        assert before_pins_reverts == after_pins_reverts, "Pins orders dont match"
