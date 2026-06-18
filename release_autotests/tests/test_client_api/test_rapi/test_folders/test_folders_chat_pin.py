import allure

from support.markers import VKTI, PRE_VKTI, SANDBOX, SAAS, TARM, PRE_TARM, PRE_SAAS


@allure.id("255562")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Добавляем или снимаем пин с чата в папке")
@allure.title("Добавляем или снимаем пин с чата в папке")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_folders_chat_pin(
    auth_account,
    fetch_until_empty_answer,
    event_filter,
    folder_id,
):
    """
    Проверяем дабавление / снятие пина чата в папке
    :param folder_id: Фикстура возвтращает folders_id созданной папки
    :param fetch_until_empty_answer: Фикстура для поиска всех событий
    :param event_filter: Фикстура для фильтрации событий
    """

    event_filter.start_point()

    with allure.step("Проверяем что пришло событие folders"):
        fetch_until_empty_answer(auth_account)

        for event in event_filter(auth_account.events[::-1], "folders"):
            before_counter_version_fetch = event["eventData"]["folders"][::-1][0]["contentVersion"]
            break
        else:
            raise Exception(f'{auth_account.env}:Failed to find event "folders"')

    with allure.step("Проверяем добавление пина на чат"):
        chat_folders = auth_account.rapi_folders_get_content(folder_id=folder_id)
        chat_pin = chat_folders["results"]["chats"][0]
        auth_account.rapi_folders_chatPin(folder_id=folder_id, chat_id=chat_pin, pin=True)

    with allure.step("Проверяем что пришло событие folders"):
        fetch_until_empty_answer(auth_account)

        for event in event_filter(auth_account.events[::-1], "folders"):
            after_counter_version_fetch = event["eventData"]["folders"][::-1][0]["contentVersion"]
            break
        else:
            raise Exception(f'{auth_account.env}:Failed to find event "folders"')

    with allure.step("Проверяем, что пин добавлен на чат"):
        response = auth_account.rapi_folders_get_content(folder_id=folder_id)
        chats_pins_list = response["results"]["pins"]
        before_counter_version_get = response["results"]["contentVersion"]

        assert chat_pin in chats_pins_list, f"Archive {chat_pin} not in pin chat list"

        assert before_counter_version_fetch < before_counter_version_get, "Content version event up get version"
        assert after_counter_version_fetch == before_counter_version_get, "Content version event up get version"

    with allure.step("Проверяем снятие пина с чата"):
        auth_account.rapi_folders_chatPin(folder_id=folder_id, chat_id=chat_pin, pin=False)

    with allure.step("Проверяем, что пин снят с чата"):
        response = auth_account.rapi_folders_get_content(folder_id=folder_id)
        after_counter_version_get = response["results"]["contentVersion"]

        if "pins" in response["results"]:
            chats_pins_list = response["results"]["pins"]
            assert chat_pin not in chats_pins_list, f"Chat {chat_pin} in pin chat list"

        assert before_counter_version_get < after_counter_version_get, "Content version get before up get after version"
