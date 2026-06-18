from random import randint

import pytest


@pytest.fixture(scope="session", autouse=True)
def is_folders_enabled(
    myteam_config,
):
    if myteam_config.get("folders-enabled"):
        return True

    else:
        pytest.skip("Folder is disabled")


@pytest.fixture(scope="session")
def folders_create(prepare_test_chats):
    auth_account, _, group, channel = prepare_test_chats

    response = auth_account.rapi_folders_create(
        title=f"Test folders {randint(0, 99)}",
        chats=[group, channel],
    )
    return response


@pytest.fixture(scope="session")
def folder_id(folders_create):
    return folders_create["results"]["folderId"]


@pytest.fixture(scope="session")
def second_folders_create(prepare_test_chats):
    auth_account, _, group, channel = prepare_test_chats

    response = auth_account.rapi_folders_create(
        title=f"Test folders {randint(0, 99)}",
        chats=[group, channel],
    )
    return response


@pytest.fixture(scope="session")
def second_folder_id(second_folders_create):
    return second_folders_create["results"]["folderId"]


@pytest.fixture(scope="session", autouse=True)
def after_test_folders(
    is_folders_enabled,
    auth_account,
    opponent_account,
    fetch_until_empty_answer,
):
    yield
    if is_folders_enabled:
        for account in (auth_account, opponent_account):
            account.rapi_request_folders()

            fetch_until_empty_answer(auth_account)

            for event in filter(lambda x: x["type"] == "folders", account.events[::-1]):
                folders = [folder["id"] for folder in event["eventData"]["folders"]]
                for folder_id in filter(lambda x: x != 0, folders):
                    try:
                        account.rapi_folders_delete(
                            folder_id=folder_id,
                        )
                    except Exception as error:
                        account.logger.exception(error)
                        break
                break
