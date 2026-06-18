import json
import random
from pathlib import Path

import allure
import pytest

from tests.test_client_api.test_isolation.common import cleanup_chat, restore_prepared_chats


@pytest.fixture(scope="session", autouse=True)
def skip_test_isolations(request):
    env = request.config.getoption("-m")
    if "ISOLATION" not in env:
        pytest.skip("Tests skip: ISOLATION marker is not set")
    if "PRE_SAAS" in env and request.config.getoption("--isolation-prepared-data") is None:
        pytest.skip("Не загружены предварительно подготовленные данные")


@allure.title("Подготовка тестовых чатов")
@pytest.fixture(scope="session")
def prepare_test_chats_msg_isolation(
    ENV_PLATFORM,
    request,
    worker_index,
    first_auth_account_in_tenant,
    second_auth_account_in_tenant,
    isolation_prepared_data,
    uncleanable_messages_isolation,
):
    sender = first_auth_account_in_tenant
    recipient = second_auth_account_in_tenant
    if ENV_PLATFORM == "PRE_SAAS":
        with allure.step("На стейдже саас берем предзаготовленные группу и чат"):
            stage_records = isolation_prepared_data["prepare_test_chats_msg_isolation"]
            stage_chats = stage_records[worker_index]
            group = stage_chats[2]
            channel = stage_chats[3]
        with allure.step("Восстанавливаем исходное состояние предзаготовленных чатов"):
            restore_prepared_chats(
                sender=sender,
                recipient=recipient,
                group_sn=group,
                channel_sn=channel,
                uncleanable_messages=uncleanable_messages_isolation,
            )
    else:
        with allure.step("Создаем тестовую группу"):
            group = sender.create_chat(
                f"Test group - {request.node.name}",
                members=[recipient],
            )

        with allure.step("Создаем тестовый канал"):
            channel = sender.create_chat(
                f"Test channel - {request.node.name}",
                defaultRole="readonly",
                members=[recipient],
            )
    return sender, recipient, group, channel


@allure.title("Подготовка тестовых чатов")
@pytest.fixture(scope="session")
def prepare_test_chats_not_in_tenant_msg_isolation(
    ENV_PLATFORM,
    request,
    worker_index,
    first_auth_account_not_in_tenant,
    second_auth_account_not_in_tenant,
    isolation_prepared_data,
    uncleanable_messages_isolation,
):
    sender = first_auth_account_not_in_tenant
    recipient = second_auth_account_not_in_tenant
    if ENV_PLATFORM == "PRE_SAAS":
        with allure.step("На стейдже саас берем предзаготовленные группу и чат"):
            stage_records = isolation_prepared_data["prepare_test_chats_not_in_tenant_msg_isolation"]
            stage_chats = stage_records[worker_index]
            group = stage_chats[2]
            channel = stage_chats[3]
        with allure.step("Восстанавливаем исходное состояние предзаготовленных чатов"):
            restore_prepared_chats(
                sender=sender,
                recipient=recipient,
                group_sn=group,
                channel_sn=channel,
                uncleanable_messages=uncleanable_messages_isolation,
            )
    else:
        with allure.step("Создаем тестовую группу"):
            group = sender.create_chat(
                f"Test group - {request.node.name}",
                members=[recipient],
            )

        with allure.step("Создаем тестовый канал"):
            channel = sender.create_chat(
                f"Test channel - {request.node.name}",
                defaultRole="readonly",
                members=[recipient],
            )

    return sender, recipient, group, channel


@pytest.fixture(scope="session")
def uncleanable_messages_isolation(isolation_prepared_data):
    return isolation_prepared_data["static_messages"]


@allure.title("Подготовка тестовых чатов для администрирования")
@pytest.fixture(scope="session")
def prepare_test_chats_admin_readonly_isolation(
    ENV_PLATFORM,
    worker_index,
    request,
    prepare_test_chats_msg_isolation,
    isolation_prepared_data,
    uncleanable_messages_isolation,
):
    sender, recipient, _, _ = prepare_test_chats_msg_isolation
    group = None
    channel = None
    if ENV_PLATFORM == "PRE_SAAS":
        stage_records = isolation_prepared_data["prepare_test_chats_admin_readonly_isolation"]
        stage_chats = stage_records[worker_index]
        if stage_chats[0] == sender.uin and stage_chats[1] == recipient.uin:
            group = stage_chats[2]
            channel = stage_chats[3]
        else:
            raise Exception("Нарушен порядок предзаготовленных чатов для стейджа. Тестовые пользователи не совпадают")
        with allure.step("Восстанавливаем исходное состояние предзаготовленных чатов"):
            restore_prepared_chats(
                sender=sender,
                recipient=recipient,
                group_sn=group,
                channel_sn=channel,
                uncleanable_messages=uncleanable_messages_isolation,
            )
    else:
        with allure.step("Создаем тестовую группу"):
            group = sender.create_chat(
                f"Test group - {request.node.name}",
                members=[recipient],
                public=True,
            )

        with allure.step("Создаем тестовый канал"):
            channel = sender.create_chat(
                f"Test channel - {request.node.name}",
                defaultRole="readonly",
                members=[recipient],
                public=True,
            )
    assert channel is not None, "Тестовый канал отсутствует"
    assert group is not None, "Тестовая группа отсутствует"

    return group, channel


@allure.title("Считываем предзаготовленные данные")
@pytest.fixture(scope="session")
def isolation_prepared_data(request, ENV_PLATFORM):
    if ENV_PLATFORM != "PRE_SAAS":
        return None
    file_path = request.config.getoption("--isolation-prepared-data")
    if file_path is not None:
        with Path.open(file_path, "r", encoding="utf-8") as f:
            isolation_prepared_data = json.load(f)
    if isolation_prepared_data is not None:
        return isolation_prepared_data
    else:
        raise Exception("Не удалось прочитать файл предзаготовленных данных")


@allure.title("Получение первого пользователя в тенанте ")
@pytest.fixture(scope="session")
def first_auth_account_in_tenant(ENV_PLATFORM, worker_index, account_fabric, isolation_prepared_data):
    if ENV_PLATFORM == "PRE_SAAS":
        keys = list(isolation_prepared_data["in_tenant_accounts"].keys())
        key = keys[2 * worker_index]
        account_dict = isolation_prepared_data["in_tenant_accounts"][key]
        main_account = account_fabric(account_dict=account_dict)
    else:
        domain = "testb1iz.bizml.ru"
        main_account = account_fabric(domain=domain)
    return main_account


@allure.title("Получение второго пользователя в тенанте ")
@pytest.fixture(scope="session")
def second_auth_account_in_tenant(ENV_PLATFORM, worker_index, account_fabric, isolation_prepared_data):
    if ENV_PLATFORM == "PRE_SAAS":
        keys = list(isolation_prepared_data["in_tenant_accounts"].keys())
        key = keys[2 * worker_index + 1]
        account_dict = isolation_prepared_data["in_tenant_accounts"][key]
        main_account = account_fabric(account_dict=account_dict)
    else:
        domain = "test-testbiz-vkteams-qa-02.bizml.ru"
        main_account = account_fabric(domain=domain)
    return main_account


@allure.title("Получение второго пользователя в тенанте ")
@pytest.fixture(scope="session")
def third_auth_account_in_tenant(ENV_PLATFORM, worker_index, account_fabric, isolation_prepared_data):
    if ENV_PLATFORM == "PRE_SAAS":
        keys = list(isolation_prepared_data["in_tenant_accounts"].keys())
        keys.remove(keys[2 * worker_index])
        keys.remove(keys[2 * worker_index + 1])
        account_dict = isolation_prepared_data["in_tenant_accounts"][random.choice(keys)]
        main_account = account_fabric(account_dict=account_dict)
    else:
        domain = random.choice(["test-testbiz-vkteams-qa-02.bizml.ru", "testb1iz.bizml.ru"])
        main_account = account_fabric(domain=domain)
    return main_account


@allure.title("Получение пользователя не в тенанте ")
@pytest.fixture(scope="session")
def first_auth_account_not_in_tenant(ENV_PLATFORM, worker_index, account_fabric, isolation_prepared_data):
    domain = "lalalalalalal.bizml.ru"
    if ENV_PLATFORM == "PRE_SAAS":
        keys = list(isolation_prepared_data["not_in_tenant_accounts"].keys())
        key = keys[2 * worker_index]
        account_dict = isolation_prepared_data["not_in_tenant_accounts"][key]
        main_account = account_fabric(account_dict=account_dict)
    else:
        main_account = account_fabric(domain=domain)
    return main_account


@allure.title("Получение пользователя не в тенанте ")
@pytest.fixture(scope="session")
def second_auth_account_not_in_tenant(ENV_PLATFORM, worker_index, account_fabric, isolation_prepared_data):
    domain = "lalalalalalal.bizml.ru"
    if ENV_PLATFORM == "PRE_SAAS":
        keys = list(isolation_prepared_data["not_in_tenant_accounts"].keys())
        key = keys[2 * worker_index + 1]
        account_dict = isolation_prepared_data["not_in_tenant_accounts"][key]
        main_account = account_fabric(account_dict=account_dict)
    else:
        main_account = account_fabric(domain=domain)
    return main_account


@allure.title("Подготавливаем чаты для проверки пересылки сообщений")
@pytest.fixture(scope="session")
def prepare_public_and_private_test_chats_msg_isolation(
    prepare_test_chats_msg_isolation, prepare_test_chats_admin_readonly_isolation
):
    main_acc, opponent_acc, private_group, private_channel = prepare_test_chats_msg_isolation
    public_group, public_channel = prepare_test_chats_admin_readonly_isolation
    chats = [private_group, private_channel, public_group, public_channel]
    return main_acc, opponent_acc, chats


@allure.title("Подготовка треда для тестов")
@pytest.fixture(scope="session", params=["group", "channel"])
def prepared_thread_isolation(
    request,
    prepare_test_chats_msg_isolation,
    ENV_PLATFORM,
    isolation_prepared_data,
    worker_index,
    uncleanable_messages_isolation,
):
    auth_account, opponent_account, group, channel = prepare_test_chats_msg_isolation

    if ENV_PLATFORM == "PRE_SAAS":
        key = "prepared_thread_isolation_" + request.param
        sender, reader, target, msg_id, thread_id = isolation_prepared_data[key][worker_index]
        if auth_account.uin != sender and opponent_account.uin != reader:
            raise Exception("Uses wrong accounts")

        for actor in [auth_account, opponent_account]:
            cleanup_chat(acc=actor, chat_sn=thread_id, uncleanable_messages=uncleanable_messages_isolation)
    else:
        target = group if request.param == "group" else channel
        msg_id = auth_account.send_basic_message(
            sn=target,
            text="Message for threads test",
        )
        thread_id = auth_account.add_thread(chat_id=target, msg_id=msg_id)

    return auth_account, opponent_account, target, msg_id, thread_id
