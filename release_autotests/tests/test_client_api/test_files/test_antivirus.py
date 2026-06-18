import pathlib
import time

import allure
import pytest

from support.markers import SANDBOX


@pytest.fixture(scope="session", autouse=True)
def need_ignore_antivirus_tests(
    pytestconfig: pytest.Config,
    myteam_config: dict,
):
    if (
        pytestconfig.getoption("--ignore-antivirus")
        or myteam_config.get("ignore-antivirus", False)
        or not myteam_config.get("antivirus-check-enabled", False)
    ):
        pytest.skip("Skipping antivirus tests")


@allure.id("79714")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("Загрузка файлов")
@allure.title("Проверка файлов антивирусом")
@SANDBOX
@pytest.mark.Antivirus
def test_file_antivirus_success_detect(
    auth_account,
    fetch_until_empty_answer_with_filter,
    event_filter,
):
    file_detect = pathlib.Path("support").joinpath("files").joinpath("antivirus").joinpath("detect.json")

    with allure.step("Пытаемся загрузить файл"):
        event_filter.start_point()

        fileId, _ = auth_account.upload_file(
            file_detect.absolute(),
        )

        auth_account.rapi_eventSubscribe(
            subscriptions=[
                {
                    "type": "antivirus",
                    "data": {
                        "fileHashes": [fileId],
                    },
                }
            ],
        )

    with allure.step("Ищем события проверки антивирусом"):
        event_unchecked_found = False
        event_found = False
        for _ in range(3):
            for event in fetch_until_empty_answer_with_filter(auth_account, "antivirus"):
                data = event["eventData"]
                if data["fileHash"] == fileId:
                    if data["fileState"] in ("safe", "unsafe"):
                        event_found = True
                    if data["fileState"] == "unchecked":
                        event_unchecked_found = True
            time.sleep(10)

        assert event_unchecked_found, f"{auth_account.env}:Antivirus first event not found for {file_detect.name}"
        assert event_found, f"{auth_account.env}:Antivirus event not found for {file_detect.name}"

    with allure.step("Проверчем статус файла"):
        response = auth_account.get_file_info(fileId)

        file_status_antivirus = response["info"]["antivirus"]["check_result"]
        file_status_cloud = response["info"]["cloud"]["status"]

        assert file_status_antivirus == "unsafe"
        assert file_status_cloud == "not_saved"


@allure.id("161353")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("Загрузка файлов")
@allure.title("Проверка файлов антивирусом")
@SANDBOX
@pytest.mark.Antivirus
def test_file_antivirus_success_error(
    auth_account,
    fetch_until_empty_answer_with_filter,
    event_filter,
):
    file_error = pathlib.Path("support").joinpath("files").joinpath("antivirus").joinpath("error.json")
    with allure.step("Пытаемся загрузить файл"):
        event_filter.start_point()

        fileId, _ = auth_account.upload_file(
            file_error.absolute(),
        )

        auth_account.rapi_eventSubscribe(
            subscriptions=[
                {
                    "type": "antivirus",
                    "data": {
                        "fileHashes": [fileId],
                    },
                }
            ],
        )

    with allure.step("Ищем события проверки антивирусом"):
        event_unchecked_found = False
        event_found = False
        for _ in range(3):
            for event in fetch_until_empty_answer_with_filter(auth_account, "antivirus"):
                data = event["eventData"]
                if data["fileHash"] == fileId:
                    if data["fileState"] in ("safe", "unsafe"):
                        event_found = True
                    if data["fileState"] == "unchecked":
                        event_unchecked_found = True
            time.sleep(10)

        assert event_unchecked_found, f"{auth_account.env}:Antivirus first event not found for {file_error.name}"
        assert event_found, f"{auth_account.env}:Antivirus event not found for {file_error.name}"

    with allure.step("Проверчем статус файла"):
        response = auth_account.get_file_info(fileId)

        file_status_antivirus = response["info"]["antivirus"]["check_result"]
        file_status_cloud = response["info"]["cloud"]["status"]

        assert file_status_antivirus == "unchecked"
        assert file_status_cloud == "not_saved"


@allure.id("161351")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("Загрузка файлов")
@allure.title("Проверка файлов антивирусом")
@SANDBOX
@pytest.mark.Antivirus
def test_file_antivirus_success_not_detected(
    auth_account,
    fetch_until_empty_answer_with_filter,
    event_filter,
):
    file_not_detected = pathlib.Path("support").joinpath("files").joinpath("antivirus").joinpath("not_detected.json")
    with allure.step("Пытаемся загрузить файл"):
        event_filter.start_point()

        fileId, _ = auth_account.upload_file(
            file_not_detected.absolute(),
        )

        auth_account.rapi_eventSubscribe(
            subscriptions=[
                {
                    "type": "antivirus",
                    "data": {
                        "fileHashes": [fileId],
                    },
                }
            ],
        )

    with allure.step("Ищем события проверки антивирусом"):
        event_unchecked_found = False
        event_found = False

        for _ in range(3):
            for event in fetch_until_empty_answer_with_filter(auth_account, "antivirus"):
                data = event["eventData"]
                if data["fileHash"] == fileId:
                    if data["fileState"] in ("safe", "unsafe"):
                        event_found = True
                    if data["fileState"] == "unchecked":
                        event_unchecked_found = True
            time.sleep(10)

        assert event_unchecked_found, f"{auth_account.env}:Antivirus first event not found for {file_not_detected.name}"
        assert event_found, f"{auth_account.env}:Antivirus event not found for {file_not_detected.name}"

    with allure.step("Проверчем статус файла"):
        response = auth_account.get_file_info(fileId)

        file_status_antivirus = response["info"]["antivirus"]["check_result"]
        file_status_cloud = response["info"]["cloud"]["status"]

        assert file_status_antivirus == "safe"
        assert file_status_cloud == "not_saved"


@allure.id("161352")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("Загрузка файлов")
@allure.title("Проверка файлов антивирусом")
@SANDBOX
@pytest.mark.Antivirus
def test_file_antivirus_success_timeout(
    auth_account,
    fetch_until_empty_answer_with_filter,
    event_filter,
):
    file_timeout = pathlib.Path("support").joinpath("files").joinpath("antivirus").joinpath("timeout.json")
    with allure.step("Пытаемся загрузить файл"):
        event_filter.start_point()

        fileId, _ = auth_account.upload_file(
            file_timeout.absolute(),
        )

        auth_account.rapi_eventSubscribe(
            subscriptions=[
                {
                    "type": "antivirus",
                    "data": {
                        "fileHashes": [fileId],
                    },
                }
            ],
        )

    with allure.step("Ищем события проверки антивирусом"):
        event_unchecked_found = False
        event_found = False
        for _ in range(3):
            for event in fetch_until_empty_answer_with_filter(auth_account, "antivirus"):
                data = event["eventData"]
                if data["fileHash"] == fileId:
                    if data["fileState"] in ("safe", "unsafe"):
                        event_found = True
                    if data["fileState"] == "unchecked":
                        event_unchecked_found = True
            time.sleep(10)

        assert event_unchecked_found, f"{auth_account.env}:Antivirus first event not found for {file_timeout.name}"
        assert event_found, f"{auth_account.env}:Antivirus event not found for {file_timeout.name}"

    with allure.step("Проверчем статус файла"):
        response = auth_account.get_file_info(fileId)

        file_status_antivirus = response["info"]["antivirus"]["check_result"]
        file_status_cloud = response["info"]["cloud"]["status"]

        assert file_status_antivirus == "unchecked"
        assert file_status_cloud == "not_saved"


@allure.id("30783")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("Загрузка файлов")
@allure.title("Ошибки проверки антивирусом")
@SANDBOX
@pytest.mark.Antivirus
def test_file_antivirus_error(
    auth_account,
    fetch_until_empty_answer_with_filter,
    event_filter,
    antivirus_file,
):
    with allure.step("Пытаемся загрузить файл"):
        event_filter.start_point()

        fileId, _ = auth_account.upload_file(
            antivirus_file.absolute(),
        )

        auth_account.rapi_eventSubscribe(
            subscriptions=[
                {
                    "type": "antivirus",
                    "data": {
                        "fileHashes": [fileId],
                    },
                }
            ],
        )
    with allure.step("Ищем события проверки антивирусом"):
        event_unchecked_found = False
        event_found = False

        for event in fetch_until_empty_answer_with_filter(auth_account, "antivirus"):
            data = event["eventData"]
            if data["fileHash"] == fileId:
                if data["fileState"] in ("safe", "unsafe"):
                    event_found = True
                if data["fileState"] == "unchecked":
                    event_unchecked_found = True
        assert event_unchecked_found, f"{auth_account.env}: Antivirus first event not found for {antivirus_file.name}"
        assert not event_found, f"{auth_account.env}: Antivirus event found for {antivirus_file.name}"
