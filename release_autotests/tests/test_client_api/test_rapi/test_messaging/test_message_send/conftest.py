import logging
from time import sleep

import pytest
import allure
from pyvkteamsclient.client import DesktopClient

logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def run_before_tests(myteam_config):
    is_message_send_api_enabled = (
        "message-send-api-enabled" in myteam_config and myteam_config["message-send-api-enabled"]
    )
    is_api_version_high_enough = "api-version" not in myteam_config or myteam_config["api-version"] >= 129
    if not (is_message_send_api_enabled and is_api_version_high_enough):
        pytest.skip("Sending via message/send is disabled")


@allure.title("Подготовка публичных и частных тестовых чатов")
@pytest.fixture(scope="session")
def prepare_public_and_private_test_chats_msg(
    request, auth_account, opponent_account, third_account, fetch_until_empty_answer
):
    with allure.step("Создаем тестовую публичную группу"):
        public_group = auth_account.create_chat(
            f"Test public group - {request.node.name}",
            members=[opponent_account, third_account],
            public=True,
        )

    with allure.step("Создаем тестовый публичный канал"):
        public_channel = auth_account.create_chat(
            f"Test public channel - {request.node.name}",
            defaultRole="readonly",
            members=[opponent_account, third_account],
            public=True,
        )

    with allure.step("Создаем тестовую приватную группу"):
        private_group = auth_account.create_chat(
            f"Test group - {request.node.name}",
            members=[opponent_account],
        )

    with allure.step("Создаем тестовый приватный канал"):
        private_channel = auth_account.create_chat(
            f"Test channel - {request.node.name}",
            defaultRole="readonly",
            members=[opponent_account],
        )

    """
    Вычитываем системные сообщения о вступлении и добавлении в чаты
    Должно быть 4 штуки для opponent_account и 2 для third_account
    """
    fetch_until_empty_answer(opponent_account)
    fetch_until_empty_answer(third_account)

    return auth_account, opponent_account, [public_group, public_channel, private_group, private_channel]


@allure.title("Подготовка публичных и частных тестовых чатов")
@pytest.fixture(scope="session")
def process_chat_infos():
    def _process_chat_infos(main_acc, chat_type, chats_info):
        public_group, public_channel, private_group, private_channel = chats_info
        is_group = chat_type == "group"

        response = main_acc.rapi_getIdInfo(public_group if is_group else public_channel)
        public_info = response["results"]["chat"]
        assert public_info["public"] is True

        response = main_acc.rapi_getIdInfo(private_group if is_group else private_channel)
        private_info = response["results"]["chat"]
        assert "public" not in private_info or private_info["public"] is False

        return is_group, public_info, private_info

    return _process_chat_infos


@pytest.fixture
def check_history_contains_message_with_msgId():
    def func(account: DesktopClient, msg_id: int, chat_id: str):
        history = account.rapi_getHistory(sn=chat_id)
        msg_list = [msg["msgId"] for msg in history["results"]["messages"]]
        return str(msg_id) in msg_list

    return func


@pytest.fixture
def check_events_list_contains_event_with_msgId(fetch_until_empty_answer_with_filter):
    def func(account: DesktopClient, msgId: int):
        event_msg_ids = []
        for _ in range(5):
            for event in fetch_until_empty_answer_with_filter(account, "histDlgState"):
                event_msg_ids.extend([message["msgId"] for message in event["eventData"]["tail"]["messages"]])
            if msgId in event_msg_ids:
                return True
            else:
                sleep(1)
        return False

    return func
