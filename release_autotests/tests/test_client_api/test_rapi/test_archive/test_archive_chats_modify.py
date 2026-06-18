import allure

from support.markers import VKTI, PRE_VKTI, SANDBOX, SAAS, TARM, PRE_TARM, PRE_SAAS


@allure.id("191664")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Добавляет/удаляет чаты в Архиве")
@allure.title("Добавляет/удаляет чаты в Архиве")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_archive_chats_modify(
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

    event_filter.start_point()

    with allure.step("Добавляем чат в архив"):
        account.rapi_archive_chatsModify(add_chats=chats)

    with allure.step("Проверяем, что чат добавился в архив"):
        response = account.rapi_archive_getContent()
        chats_list = response["results"]["chats"]
        counter_version_get = response["results"]["contentVersion"]
        assert all(chat in chats_list for chat in chats), "Chat not in archive"

    with allure.step("Проверяем что пришло событие typing"):
        fetch_until_empty_answer(account)

        for event in event_filter(account.events[::-1], "archive"):
            fetch_counter_version = event["eventData"]["contentVersion"]
            break
        else:
            raise Exception(f'{account.env}:Failed to find event "archive"')

        assert fetch_counter_version == counter_version_get, "Archive counter version has not changed"
