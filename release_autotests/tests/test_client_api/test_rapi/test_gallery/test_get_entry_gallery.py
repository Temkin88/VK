import time

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("30197")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Галерея чата")
@allure.feature("Просмотр галереи чата")
@allure.title("Запрос элементов галереи чата")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "chat_type",
    [
        "favorite",
        "private",
        "group",
        "channel",
    ],
)
def test_get_gallery_entries(
    prepare_test_chats,
    chat_type,
    common_file,
    uploaded_common_file_url,
    ENV_PLATFORM,
):
    auth_account, opponent_account, group, channel = prepare_test_chats

    if chat_type == "favorite":
        chat_id = auth_account.uin
    elif chat_type == "private":
        chat_id = opponent_account.uin
    elif chat_type == "group":
        chat_id = group
    elif chat_type == "channel":
        chat_id = channel
    else:
        raise ValueError(f"Unknown chat_type value: {chat_type}")

    if common_file.suffix in [
        ".jpeg",
        ".jpg",
        ".png",
        ".webp",
        ".gif",
        ".webm",
        ".avi",
        ".mov",
        ".wmv",
        ".mp4",
    ]:
        url_type = ["image", "video"]
    elif common_file.suffix in [
        ".zip",
        ".odp",
        ".xml",
        ".pdf",
        ".ppt",
        ".csv",
        ".xls",
        ".doc",
        ".odt",
        ".rtf",
        ".ods",
        ".txt",
        ".json",
        ".svg",
        ".tiff",
        ".ico",
    ]:
        url_type = ["file"]
    elif common_file.suffix in [
        ".aac",
        ".mp3",
        ".ogg",
        ".wav",
    ]:
        url_type = ["audio"]
    else:
        url_type = ["ptt", "link"]

    with allure.step("Отправляем файл в чат"):
        msg_id = auth_account.send_basic_message(
            sn=chat_id,
            text=uploaded_common_file_url,
        )

    with allure.step("Пробуем получить элементы галереи"):
        if ENV_PLATFORM == "SANDBOX":
            time.sleep(5)
        else:
            time.sleep(2)

        response = auth_account.rapi_getEntryGallery(
            sn=chat_id,
            urlType=url_type,
        )

        for key in ("galleryState", "subreqs", "persons"):
            assert key in response["results"], f'"{key}" not found in response'

        gallery_subreqs = response["results"]["subreqs"]

        assert msg_id in [entry["id"]["mid"] for entries in gallery_subreqs for entry in entries["entries"]], (
            f"{auth_account.env}:rapi/getEntryGallery:file {common_file.name} not found:{msg_id}"
        )
