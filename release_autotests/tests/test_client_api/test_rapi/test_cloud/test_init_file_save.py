import time

import allure

from pyvkteamsclient.client.exceptions import ServerException
from support.markers import TARM, PRE_TARM, SANDBOX, VKTI, PRE_VKTI, SAAS, PRE_SAAS


@allure.id("31439")
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
@allure.title("Сохранение файлов в облако")
def test_init_file_save(
    opponent_account,
    photo_id,
    event_filter,
    fetch_until_empty_answer_with_filter,
):
    with allure.step("Запускаем сохранение файла в облаке"):
        opponent_account.rapi_cloud_initFileSave(
            file_id=photo_id,
            source="",
            folder="/",
        )

    with allure.step("Подписываемся на события сохранения в облаке"):
        event_filter.start_point()

        opponent_account.rapi_eventSubscribe(
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

        for _ in range(4):
            for event in fetch_until_empty_answer_with_filter(opponent_account, "cloudFileStatus"):
                data = event["eventData"]

                if data["fileHash"] == photo_id and data["status"] == "saved":
                    event_found = True
                    break
                elif data["fileHash"] == photo_id and data["status"] == "not_saved":
                    raise ServerException(
                        env=opponent_account.env,
                        path_url="cloudFileStatus: file saving failed",
                        response_status_code=f"{data['lastSaveFailed']['code']}",
                        response_status_text=f"{data['lastSaveFailed'].get('reason') or 'no_reason'}",
                        http_request_plain_text=None,
                    )
                else:
                    time.sleep(1)

        assert event_found, "'cloudFileStatus' event not found"
