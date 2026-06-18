import allure

from support.markers import VKTI, PRE_VKTI, SANDBOX, SAAS, TARM, PRE_TARM, PRE_SAAS


@allure.id("191662")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Получить содержимое Архива")
@allure.title("Получить содержимое Архива")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_archive_get_content(
    create_archive_chats,
):
    """
    Проверяем получение списка Архива
    :param create_archive_chats: Фикстура которая создает 2 чата
    """
    auth_account, chats = create_archive_chats

    with allure.step("Добавляем чат в архив"):
        auth_account.rapi_archive_chatsModify(add_chats=chats)

    with allure.step("Проверяем, что чат добавился в архив"):
        response = auth_account.rapi_archive_getContent()
        chats_list = response["results"]["chats"]

        assert all(chat in chats_list for chat in chats), "Chat not in archive"
