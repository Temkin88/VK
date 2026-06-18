import allure

from support.markers import TARM, PRE_TARM, SANDBOX, VKTI, PRE_VKTI, SAAS, PRE_SAAS


@allure.id("31437")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("jira", "IMQA-974")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Файлы")
@allure.feature("Загрузка файлов")
@allure.title("Отмена сохранения файлов в облако")
def test_cancel_file_save(
    auth_account,
    photo_id,
    event_filter,
    fetch_until_empty_answer_with_filter,
):
    with allure.step("Запускаем сохранение файла в облаке"):
        auth_account.rapi_cloud_initFileSave(
            file_id=photo_id,
            source="",
            folder="/",
        )

        auth_account.rapi_cloud_cancelSave(
            file_id=photo_id,
            source="",
        )

    with allure.step("Подписываемся на события сохранения в облаке"):
        event_filter.start_point()

        auth_account.rapi_eventSubscribe(
            subscriptions=[
                {
                    "type": "cloudFileStatus",
                    "data": {
                        "fileHashes": [photo_id],
                    },
                }
            ],
        )

    with allure.step("Ищем события сохранения в облаке"):
        event_found = False

        for event in fetch_until_empty_answer_with_filter(auth_account, "cloudFileStatus"):
            data = event["eventData"]

            if data["fileHash"] == photo_id and data["status"] == "not_saved":
                event_found = True

        assert event_found, "'cloudFileStatus' event not found"
