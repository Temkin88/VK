import json

import pytest
from filelock import FileLock


@pytest.fixture(scope="session")
def filled_icon_id(auth_account):
    filled_icon_id, _ = auth_account.upload_file("support/files/for_miniapps_tests/filled_icon.svg")

    return filled_icon_id


@pytest.fixture(scope="session")
def outlined_icon_id(auth_account):
    outlined_icon_id, _ = auth_account.upload_file("support/files/for_miniapps_tests/outlined_icon.svg")

    return outlined_icon_id


@pytest.fixture(scope="session")
def showcase_icon_id(auth_account):
    showcase_icon_id, _ = auth_account.upload_file("support/files/for_miniapps_tests/showcase_icon.png")

    return showcase_icon_id


@pytest.fixture(scope="session")
def miniapp_id(
    admin_account,
    outlined_icon_id,
    filled_icon_id,
    showcase_icon_id,
    tmp_path_factory,
    worker_id,
):
    def get_or_create_miniapp():
        try:
            miniapps_list_response = admin_account.api_miniapps_list()
            miniapps_list = miniapps_list_response["result"]["miniapps"]

            app = [miniapp for miniapp in miniapps_list if "Test miniapp autotest" in miniapp["name"]]
            app_id = app[0]["miniappId"]
        except (TypeError, IndexError):
            create_miniapp_response = admin_account.api_miniapps_create(
                name="Test miniapp autotest",
                description="Test description",
                filled_icon_id=filled_icon_id,
                outlined_icon_id=outlined_icon_id,
                showcase_icon_id=showcase_icon_id,
            )
            app_id = create_miniapp_response["result"]["miniappId"]

        response = admin_account.api_miniapps_get(
            miniapp_id=app_id,
        )
        assert response["result"]["miniappId"] == app_id, f"{app_id} dont match"

        return app_id

    if worker_id == "master":
        appId = get_or_create_miniapp()
    else:
        root_tmp_dir = tmp_path_factory.getbasetemp().parent

        fn = root_tmp_dir / "data.json"
        with FileLock(str(fn) + ".lock"):
            if fn.is_file():
                appId = json.loads(fn.read_text())["miniappId"]
            else:
                appId = get_or_create_miniapp()
                fn.write_text(
                    json.dumps(
                        {
                            "miniappId": appId,
                        }
                    )
                )

    return appId


@pytest.fixture(scope="session")
def miniapp_id_backend(
    admin_account,
    outlined_icon_id,
    filled_icon_id,
    showcase_icon_id,
):
    return admin_account.api_miniapps_create(
        name="Test miniapp autotest",
        description="Test description",
        filled_icon_id=filled_icon_id,
        outlined_icon_id=outlined_icon_id,
        showcase_icon_id=showcase_icon_id,
    )["result"]["miniappId"]


@pytest.fixture(scope="session")
def miniapp_id_for_delete(
    admin_account,
    outlined_icon_id,
    filled_icon_id,
    showcase_icon_id,
):
    response = admin_account.api_miniapps_create(
        name="Test miniapp autotest",
        description="Test description",
        filled_icon_id=filled_icon_id,
        outlined_icon_id=outlined_icon_id,
        showcase_icon_id=showcase_icon_id,
    )

    return response["result"]["miniappId"]


@pytest.fixture(scope="session", autouse=True)
def clean_miniapps(admin_account, logger):
    yield

    miniapps_list = admin_account.api_miniapps_list()["result"]["miniapps"]

    for miniapp in miniapps_list:
        if "autotest" in miniapp["name"]:
            try:
                admin_account.api_miniapps_disable(
                    miniapp_id=miniapp["miniappId"],
                )
                admin_account.api_miniapps_delete(
                    miniapp_id=miniapp["miniappId"],
                )
            except Exception as error:
                logger.error(error)
