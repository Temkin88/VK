import pathlib
import allure
import pytest
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import send_message_rapi, send_message_wim


@allure.id("901416")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("DLP")
@allure.feature("Файлы")
@allure.title(
    "Домены настроены на дефолтный адатер. Если ответ от DLP по тексту запретить,"
    " система (Вахтёр) должна заблокировать отправку сообщения в группу/канал"
)
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@DLP
@pytest.mark.parametrize("send_func", [send_message_rapi, send_message_wim])
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_upload_file_without_sensitive_data_and_blocked_text_domains_check_false(
    chat_type, chat_entities_multidomain, dlp_block_text, send_func, check_event_send_message_event_exist
):
    main_acc, first_opponent_acc, second_opponent_acc, chats = chat_entities_multidomain
    chat = chats[chat_type]

    text = dlp_block_text

    file = (
        pathlib.Path("support")
        .joinpath("files")
        .joinpath("dlp")
        .joinpath("fake_file_without_sensitive_information.json")
    )

    with allure.step("Пытаемся загрузить файл"):
        file = main_acc.upload_file(file.absolute())

    file_id, file_url = file

    assert file_id is not None, "Идентификатор файла отстуствует"
    assert file_url is not None, "Ссылка на файл отстуствует"

    with allure.step("Отправляем файл получателю"):
        status_code, msg_id = send_func(main_acc, chat, text, file_url)

    assert msg_id is None, "Идентификатор сообщения присутствует"

    assert not check_event_send_message_event_exist(first_opponent_acc, msg_text=text), (
        "Событие о новом сообщении найдено"
    )

    assert not check_event_send_message_event_exist(second_opponent_acc, msg_text=text), (
        "Событие о новом сообщении найдено"
    )
