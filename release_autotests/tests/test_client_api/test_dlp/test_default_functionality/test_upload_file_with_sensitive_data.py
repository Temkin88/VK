import allure
import pytest
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import (
    send_message_rapi,
    send_message_wim,
    upload_file_with_sensitive_data_to_block_by_fake_dlp,
)


@allure.id("862872")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Файлы")
@allure.title("Нарушение DLP. Чувствительные данные в файле. Отправка сообщения в личку/группу/канал/избранное")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@DLP
@pytest.mark.parametrize("send_func", [send_message_rapi, send_message_wim])
@pytest.mark.parametrize("chat_type", ["favorites", "private", "group", "channel", "thread"])
def test_upload_file_with_sensitive_data(
    chat_type,
    send_func,
    chat_entities,
    main_acc_second_instance,
    check_event_send_message_event_exist,
):
    upload_file_with_sensitive_data_to_block_by_fake_dlp(
        chat_type,
        send_func,
        chat_entities,
        check_event_send_message_event_exist,
        main_acc_second_instance,
    )
