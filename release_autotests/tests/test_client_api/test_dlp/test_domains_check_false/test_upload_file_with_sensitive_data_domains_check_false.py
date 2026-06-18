import pathlib

import allure
import pytest
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import send_message_rapi, send_message_wim, check_file_unavailability


@allure.id("901415")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Файлы")
@allure.title(
    "Домены настроены на дефолтный адатер. Если ответ от DLP по файлу запретить, система (Вахтёр) не"
    " должна давать доступ к файлу (чтение/скачивание) отправителю/получателю"
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
def test_upload_file_with_sensitive_data_domains_check_false(
    chat_type,
    send_func,
    chat_entities_multidomain,
    check_event_send_message_event_exist,
):
    main_acc, first_opponent_acc, second_opponent_acc, chats = chat_entities_multidomain

    chat = chats[chat_type]

    file = (
        pathlib.Path("support").joinpath("files").joinpath("dlp").joinpath("fake_file_with_sensitive_information.json")
    )

    with allure.step("Пытаемся загрузить файл"):
        file = main_acc.upload_file(file.absolute())

    file_id, file_url = file

    assert file_id is not None, "Идентификатор файла отстуствует"
    assert file_url is not None, "Ссылка на файл отстуствует"

    with allure.step("Отправляем файл получателю"):
        status_code, msg_id = send_func(main_acc, chat, None, file_url)

    assert msg_id is not None, "Идентификатор сообщения отстуствует"

    with allure.step("Первый оппонент пытается получить событие о сообщении"):
        assert check_event_send_message_event_exist(first_opponent_acc, msg_id=msg_id), (
            "Событие о новом сообщении не найдено"
        )
    with allure.step("Второй оппонент чата пытается получить событие о сообщении"):
        assert check_event_send_message_event_exist(second_opponent_acc, msg_id=msg_id), (
            "Событие о новом сообщении не найдено"
        )

    accounts = {
        "Отправитель": main_acc,
        "Первый оппонент": first_opponent_acc,
        "Второй оппонент": second_opponent_acc,
    }
    for friendly_name, acc in accounts.items():
        with allure.step(f"{friendly_name} пытается получить доступ к файлу"):
            assert check_file_unavailability(acc, file_id)
