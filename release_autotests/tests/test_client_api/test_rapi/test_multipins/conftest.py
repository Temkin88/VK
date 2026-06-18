import logging

import pytest
import allure

from tests.test_client_api.test_rapi.test_multipins.common import (
    multipin_channel_limit,
    multipin_chat_limit,
    multipin_personal_limit,
    unpin_all_in_dialog,
    check_multipins,
    random_pin_in_dialog,
    random_pin_in_chat,
)

logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def run_before_tests(myteam_config):
    is_multipins_enabled = (
        "multi-pins" in myteam_config
        and "enabled" in myteam_config["multi-pins"]
        and myteam_config["multi-pins"]["enabled"]
    )
    is_api_version_high_enough = "api-version" not in myteam_config or myteam_config["api-version"] > 135
    if not (is_multipins_enabled and is_api_version_high_enough):
        pytest.skip("Multipins are disabled")


@allure.title("Наполнение лички сообщениями для проверки мультипинов")
@pytest.fixture(scope="session")
def prepare_personal_dialog(auth_account, opponent_account):
    def _prepare_personal_dialog():
        msgs = []
        with allure.step("Отправка сообщений, чтобы потом пинить эти сообщения"):
            for i in range(max(15, multipin_personal_limit)):
                msg_id = auth_account.send_basic_message(
                    sn=opponent_account.uin,
                    text="Auth to opponent " + str(i + 1),
                )
                assert msg_id, f"Auth failed to send msg to {opponent_account.uin}"
                msgs.append(msg_id)
                msg_id = opponent_account.send_basic_message(
                    sn=auth_account.uin,
                    text="Opponent to auth " + str(i + 1),
                )
                assert msg_id, f"Opponent failed to send msg to {auth_account.uin}"
                msgs.append(msg_id)

        """
        Убедимся, что пины действительно пустые
        """
        unpin_all_in_dialog([auth_account, opponent_account])
        check_multipins(
            auth_account,
            opponent_account.uin,
            [],
        )

        return [auth_account, opponent_account], msgs

    return _prepare_personal_dialog


@allure.title("Наполнение чата / канала сообщениями для проверки мультипинов")
@pytest.fixture(scope="session")
def prepare_chat(auth_account, opponent_account, third_account):
    def _prepare_chat(chat_type):
        is_channel = chat_type == "channel"
        with allure.step(
            "Создаем тестовый публичный " + ("канал" if is_channel else "чат"),
        ):
            chat = auth_account.create_chat(
                "Test public " + ("channel" if is_channel else "group"),
                defaultRole="readonly" if is_channel else "admin",
                members=[opponent_account, third_account],
                public=True,
            )
        msgs = []
        with allure.step("Отправка сообщений, чтобы потом пинить эти сообщения"):
            for i in range(max(15, max(multipin_chat_limit, multipin_channel_limit))):
                msg_id = auth_account.send_basic_message(
                    sn=chat,
                    text="Auth msg " + str(i + 1),
                )
                assert msg_id, f"Auth failed to send msg to {chat}"
                msgs.append(msg_id)
                if is_channel:
                    continue
                msg_id = opponent_account.send_basic_message(
                    sn=chat,
                    text="Opponent msg " + str(i + 1),
                )
                assert msg_id, f"Opponent failed to send msg to {chat}"
                msgs.append(msg_id)
                msg_id = third_account.send_basic_message(
                    sn=chat,
                    text="Third msg " + str(i + 1),
                )
                assert msg_id, f"Third failed to send msg to {chat}"
                msgs.append(msg_id)
        return is_channel, chat, [auth_account, opponent_account, third_account], msgs

    return _prepare_chat


@allure.title("Наполнение лички сообщениями и пин максимального числа сообщений")
@pytest.fixture(scope="session")
def prepare_private_dialog_with_pins(prepare_personal_dialog):
    def _prepare_private_dialog_with_pins():
        chat_type = "private"
        accounts, msgs_to_pin = prepare_personal_dialog()

        pinned_msgs = []
        with allure.step(f"Случайным образом закрепляем {multipin_personal_limit} сообщений в {chat_type}"):
            for _ in range(multipin_personal_limit):
                random_pin_in_dialog(accounts, msgs_to_pin, pinned_msgs)

        return accounts, pinned_msgs

    return _prepare_private_dialog_with_pins


@allure.title("Наполнение чата / канала сообщениями и пин максимального числа сообщений")
@pytest.fixture(scope="session")
def prepare_chat_with_pins(prepare_chat):
    def _prepare_chat_with_pins(chat_type):
        is_channel, chat, accounts, msgs_to_pin = prepare_chat(chat_type)

        cur_limit = multipin_channel_limit if is_channel else multipin_chat_limit
        pinned_msgs = []
        with allure.step(f"Случайным образом закрепляем {cur_limit} сообщений в {chat_type}"):
            for _ in range(cur_limit):
                random_pin_in_chat(accounts, chat, chat_type, msgs_to_pin, pinned_msgs)

        return is_channel, chat, accounts, pinned_msgs

    return _prepare_chat_with_pins
