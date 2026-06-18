import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("31910")
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
@allure.title("Запрос групповой информации id")
def test_contacts_get_id_info_batch(
    prepare_test_chats,
):
    main_acc, opponent, group, channel = prepare_test_chats

    with allure.step("Пробуем получить информацию"):
        response = main_acc.rapi_getIdInfoBatch(ids=[group, main_acc.uin, opponent.uin])
        results = response["results"]

    with allure.step("Проверяем ответ сервера"):
        assert len(results.keys()) == 3
        for _id in results:
            if "chat" in results[_id]:
                assert "sn" in results[_id]["chat"], "Failed to get sn"
                assert "memberCount" in results[_id]["chat"], "Failed to get memberCount"
                assert "name" in results[_id]["chat"], "Failed to get name"
                assert "about" in results[_id]["chat"], "Failed to get about"
                assert "stamp" in results[_id]["chat"], "Failed to get stamp"
            elif "user" in results[_id]:
                assert "sn" in results[_id]["user"], "Failed to get sn"
                assert "firstName" in results[_id]["user"], "Failed to get firstName"
                assert "lastName" in results[_id]["user"], "Failed to get lastName"
