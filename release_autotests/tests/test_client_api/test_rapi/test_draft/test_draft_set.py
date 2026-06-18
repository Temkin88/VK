import datetime

import allure
import pytest

from support.cases.drafts import draft_parts
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26903")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Черновик")
@allure.feature("Черновик в чате")
@allure.title("Сохранение и удаление черновика в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "chat_type",
    ["private", "group", "channel"],
)
@pytest.mark.parametrize(
    "draft_part",
    draft_parts,
    ids=[
        "text",
        "text_with_quote",
        "formatted_text",
        "formatted_text_with_quote",
    ],
)
def test_save_and_delete_draft_in_chat(
    chat_type,
    draft_part,
    prepare_test_chats,
):
    """
    Проверяем сохранеие разных видов черновика и его удаление
    """

    main_acc, opponent, group, channel = prepare_test_chats

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Сохраняем черновик в чате"):
        assert (
            main_acc.rapi_draft_set(
                sn=chat,
                parts=draft_part,
            )["status"]["code"]
            == 20000
        )

    with allure.step("Удаляем черновик в чате"):
        assert (
            main_acc.rapi_draft_set(
                sn=chat,
                parts=[],
            )["status"]["code"]
            == 20000
        )

    with allure.step("Удаляем черновик в чате со семи параметрами"):
        assert (
            main_acc.rapi_draft_set(
                sn=chat,
                parts=[],
                mentions=["123"],
            )["status"]["code"]
            == 20000
        )


@allure.id("216506")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Черновик")
@allure.feature("Черновик в чате")
@allure.title("Сохранение черновика и отправка сообщения в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "chat_type",
    ["private", "group", "channel"],
)
def test_save_and_send_message_draft_in_chat(
    chat_type,
    prepare_test_chats,
    fetch_until_empty_answer_with_filter,
    event_filter,
    second_auth_account,
    is_draft_enabled,
):
    """
    Проверяем что приходят события при создании черновика и при его удалении
    """
    if not is_draft_enabled:
        pytest.skip("Drafts are disabled in myteam-config")

    message = [{"mediaType": "text", "text": "test111"}]
    main_acc, opponent, group, channel = prepare_test_chats

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    event_filter.start_point()

    with allure.step("Сохраняем черновик в чате"):
        assert (
            main_acc.rapi_draft_set(
                sn=chat,
                parts=message,
            )["status"]["code"]
            == 20000
        )

    with allure.step("Отправляем такое же сообщение как и в черновике"):
        main_acc.wim_im_sendIM(
            t=chat,
            parts=message,
            draftDeleteTime=datetime.datetime.now().timestamp(),
        )

    with allure.step(f"Проверяем что черновик пуст под инстансом {main_acc}"):
        for event in fetch_until_empty_answer_with_filter(main_acc, "draft")[::-1]:
            event_data = event["eventData"]
            if event_data["sn"] == chat:
                assert not event_data["parts"], "Parts field not empty"
                break
        else:
            raise Exception(f'{main_acc.env}:Failed to find event "draft"')

    with allure.step(f"Проверяем что черновик пуст под инстансом {second_auth_account}"):
        for event in fetch_until_empty_answer_with_filter(second_auth_account, "draft")[::-1]:
            event_data = event["eventData"]
            if event_data["sn"] == chat:
                assert not event_data["parts"], "Parts field not empty"
                break
        else:
            raise Exception(f'{main_acc.env}:Failed to find event "draft"')
