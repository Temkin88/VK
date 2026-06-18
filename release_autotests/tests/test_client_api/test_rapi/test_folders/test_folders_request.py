import allure

from support.markers import SANDBOX, PRE_TARM, TARM, PRE_VKTI, VKTI, SAAS, PRE_SAAS


@allure.id("83370")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Запросить папки")
@allure.title("Запросить папки")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_folders_request(
    auth_account,
    fetch_until_empty_answer_with_filter,
    event_filter,
    folder_id,
):
    with allure.step("Запросить папки"):
        assert auth_account.rapi_request_folders()

    with allure.step("Проверяем что папка появилась в событиях"):
        event_found_folder_id = False

        for event in fetch_until_empty_answer_with_filter(auth_account, "folders"):
            data = event["eventData"]["folders"]
            for folders_id in data:
                if folder_id == folders_id["id"]:
                    event_found_folder_id = True
                    break

            if event_found_folder_id:
                break

        assert event_found_folder_id, 'Event "Folders" not found'
