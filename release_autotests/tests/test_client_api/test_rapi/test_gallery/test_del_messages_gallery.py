import time

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("215184")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Галерея чата")
@allure.feature("Удаление сообщений из галереи чата")
@allure.title("Запрос на удаление сообщений из галереи чата")
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
def test_del_messages_gallery(
    prepare_test_chats,
    chat_type,
    photo,
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

    url_type = ["image", "video"]

    with allure.step("Отправляем файл в чат"):
        msg_id = auth_account.send_basic_message(
            sn=chat_id,
            text=photo,
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
        msg_ids = [entry["id"]["mid"] for entries in gallery_subreqs for entry in entries["entries"]]

        assert msg_id in msg_ids, f"{msg_id} not found"

    with allure.step("Удаляем сообщение из галереи"):
        (
            auth_account.rapi_delMsgBatch(
                sn=chat_id,
                msgIds=msg_ids,
            ),
            "Failed to delete msgs",
        )

    with allure.step("Проверяем что сообщения удалились из галереи"):
        time.sleep(5)

        response = auth_account.rapi_getEntryGallery(
            sn=chat_id,
            urlType=url_type,
        )

        gallery_subreqs = response["results"]["subreqs"]

        assert msg_id not in [entry["id"]["mid"] for entries in gallery_subreqs for entry in entries["entries"]], (
            f"{msg_id} found"
        )
