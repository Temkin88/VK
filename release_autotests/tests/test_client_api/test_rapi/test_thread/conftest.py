import logging

import allure
import pytest

log = logging.getLogger(__name__)


@allure.title("Подготовка треда для тестов")
@pytest.fixture(scope="session", params=["group", "channel"])
def prepared_thread(request, auth_account, prepare_test_chats, ENV_PLATFORM):
    if ENV_PLATFORM == "TARM":
        pytest.skip("Отключается до устранения проблем по баге https://jira.vk.team/browse/IMSERVER-19077")

    _, _, group, channel = prepare_test_chats

    target = group if request.param == "group" else channel

    msg_id = auth_account.send_basic_message(
        sn=target,
        text="Message for threads test",
    )

    thread_id = auth_account.add_thread(chat_id=target, msg_id=msg_id)

    return target, msg_id, thread_id
