import allure

from support.markers import VKTI, PRE_VKTI, SANDBOX, SAAS, TARM, PRE_TARM, PRE_SAAS


@allure.id("191663")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Добавляем или снимаем пин с чата в архиве")
@allure.title("Добавляем или снимаем пин с чата в архиве")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_archive_chat_pin(
    fetch_until_empty_answer,
    event_filter,
    create_archive_chats,
):
    """
    Проверяем дабавление / снятие пина чата в архиве
    :param create_archive_chats: Фикстура которая создает 2 чата
    :param fetch_until_empty_answer: Фикстура для поиска всех событий
    :param event_filter: Фикстура для фильтрации событий
    """
    account, chats = create_archive_chats

    account.rapi_archive_chatsModify(add_chats=chats)

    response = account.rapi_archive_getContent()
    chat_archive = response["results"]["chats"][0]

    event_filter.start_point()

    with allure.step("Проверяем что пришло событие typing"):
        fetch_until_empty_answer(account)

        for event in event_filter(account.events, "archive"):
            before_counter_version_fetch = event["eventData"]["contentVersion"]
            break
        else:
            raise Exception(f'{account.env}:Failed to find event "archive"')

    with allure.step("Проверяем добавление пина на чат"):
        account.rapi_archive_chatPin(chat_id=chat_archive)

    with allure.step("Проверяем что пришло событие typing"):
        fetch_until_empty_answer(account)

        for event in event_filter(account.events[::-1], "archive"):
            after_counter_version_fetch = event["eventData"]["contentVersion"]
            break
        else:
            raise Exception(f'{account.env}:Failed to find event "archive"')

    with allure.step("Проверяем, что пин добавлен на чат"):
        response = account.rapi_archive_getContent()
        chats_pins_list = response["results"]["pins"]
        before_counter_version_get = response["results"]["contentVersion"]

        assert chat_archive in chats_pins_list, f"Archive {chat_archive} not in pin chat list"

        assert before_counter_version_fetch < before_counter_version_get, "Content version event up get version"
        assert after_counter_version_fetch == before_counter_version_get, "Content version event up get version"

    with allure.step("Проверяем снятие пина с чата"):
        account.rapi_archive_chatPin(chat_id=chat_archive, pin=False)

    with allure.step("Проверяем, что пин снят с чата"):
        response = account.rapi_archive_getContent()
        after_counter_version_get = response["results"]["contentVersion"]

        if "pins" in response["results"]:
            chats_pins_list = response["results"]["pins"]
            assert chat_archive not in chats_pins_list, f"Chat {chat_archive} in pin chat list"

        assert before_counter_version_get < after_counter_version_get, "Content version get before up get after version"
