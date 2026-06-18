import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("31911")
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
@allure.feature("Запрос информации id")
@allure.title("Запрос информации id чата")
def test_contacts_get_id_info_chat(
    prepare_test_chats,
):
    main_acc, opponent, group, channel = prepare_test_chats

    with allure.step("Пробуем получить информацию"):
        response = main_acc.rapi_getIdInfo(_id=group)
        chat = response["results"].get("chat")

    with allure.step("Проверяем ответ сервера"):
        assert "sn" in chat, "Failed to get sn"
        assert "memberCount" in chat, "Failed to get memberCount"
        assert "name" in chat, "Failed to get name"
        assert "about" in chat, "Failed to get about"
        assert "stamp" in chat, "Failed to get stamp"
