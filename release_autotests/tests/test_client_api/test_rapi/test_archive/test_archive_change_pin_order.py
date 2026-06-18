import allure

from support.markers import VKTI, PRE_VKTI, SANDBOX, SAAS, TARM, PRE_TARM, PRE_SAAS


@allure.id("205502")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Изменение порядка запиненных чатов (пинов) в архиве")
@allure.title("Изменение порядка запиненных чатов (пинов) в архиве")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_archive_change_pin_order(
    create_archive_chats,
):
    """
    Изменение порядка запиненных чатов (пинов) в архиве
    :param create_archive_chats: Фикстура которая создает 2 чата
    """
    account, chats = create_archive_chats

    with allure.step("Добавление чатов в архив"):
        account.rapi_archive_chatsModify(add_chats=chats)

    with allure.step("Получение чатов которые в архиве"):
        response = account.rapi_archive_getContent()
        chats_archive = response["results"]["chats"]

    with allure.step("Добавляем пины на чаты архива"):
        for chat in chats_archive:
            account.rapi_archive_chatPin(chat_id=chat)

    with allure.step("Проверяем что чаты в нужном порядке"):
        response = account.rapi_archive_getContent()
        before_pins = response["results"]["pins"]

        account.rapi_archive_changePinsOrder(before_pins)
        response = account.rapi_archive_getContent()
        after_pins = response["results"]["pins"]

        assert before_pins == after_pins, "Pins orders dont match"

    with allure.step("Проверяем что чаты в измененном порядке"):
        response = account.rapi_archive_getContent()
        before_pins_reverts = response["results"]["pins"][::-1]

        account.rapi_archive_changePinsOrder(before_pins_reverts)
        response = account.rapi_archive_getContent()
        after_pins_reverts = response["results"]["pins"]

        assert before_pins_reverts == after_pins_reverts, "Pins orders dont match"
