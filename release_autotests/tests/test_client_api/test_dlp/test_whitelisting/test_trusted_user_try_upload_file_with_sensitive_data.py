import allure
import pytest
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import (
    send_message_rapi,
    send_message_wim,
    upload_file_with_sensitive_data_to_block_by_fake_dlp,
)


@allure.id("972725")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Файлы")
@allure.title(
    "Файл отправляется на проверку в DLP(при условии, что настроена и включена интеграция с DLP), если он не был"
    " заблокирован в security-функциях. Отправка сообщения в личку/группу/канал/избранное"
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
@pytest.mark.parametrize("chat_type", ["favorites", "private", "group", "channel", "thread"])
def test_trusted_user_try_upload_file_with_sensitive_data(
    chat_type,
    send_func,
    chat_entities,
    check_event_send_message_event_exist,
):
    upload_file_with_sensitive_data_to_block_by_fake_dlp(
        chat_type,
        send_func,
        chat_entities,
        check_event_send_message_event_exist,
    )
