from typing import Literal

import pytest
import allure
from _pytest.config import Config
from pyvkteamsclient.client import DesktopClient
from tests.test_client_api.test_federation.common import (
    get_remote_sn_from_buddylist_event,
    get_remote_sn_from_histDlgState_events,
    find_chat_by_some_criterion,
    generate_uniq_chat_name,
)


@pytest.fixture(scope="session", autouse=True)
def check_federation_config(pytestconfig: Config):
    """
    В качестве значения аргумента --federation-config должна быть передана матрица вида:
        +-------+----------+----------+
        |       | Host1    | Host2    |
        +-------+----------+----------+
        | Host1 | domain11 | domain12 |
        +-------+----------+----------+
        | Host2 | domain21 | domain22 |
        +-------+----------+----------+
    В главной диагонали будут находится домены, не являющиеся федеративными. На пересечении строк и столбцов
    указывается домен в котором находятся пользователи которые являются федератиными и их надо
    использовать на хосте-строки, чтобы отправлять соодщения на хост-столбца.
    Если нет связи между хостами указываем None.

    Матрица записывается построчно, символом конца строки является ";" а разделителем столбцов ",".
    Хост строки отделяется символом:"

    Шаблон для записи матрицы выше выглядит так:
    Host1:domain11,domain22;Host2:domain21,domain22;

    Пример боевой записи:
    --federation-config="fed1auto-1-25-4.im-sandbox.devmail.ru:autotest.clients,autotest-01.clients;
    fed1auto-2-25-4.im-sandbox.devmail.ru:autotest-02.clients,autotest.clients"
    """
    if pytestconfig.getoption("--federation-config") is None or federation_config == {}:
        pytest.skip()


@pytest.fixture(scope="session")
def federation_config(pytestconfig: Config):
    config_as_string = pytestconfig.getoption("--federation-config")
    federation_config = {}
    options = config_as_string.split(";")
    hosts = [option.split(":")[0] for option in options]
    domains_all = [option.split(":")[1] for option in options]
    for i, host_i in enumerate(hosts):
        domains = domains_all[i].split(",")
        domains_map = {}
        for j, host_j in enumerate(hosts):
            domains[j] = None if domains[j] == "None" else domains[j]
            domains_map[host_j] = domains[j]
        federation_config[host_i] = domains_map
    return federation_config


@pytest.fixture(scope="session")
def main_acc_on_host1(account_fabric, get_supply_session, federation_config):
    hosts = list(federation_config.keys())
    host = hosts[0]
    domain = federation_config[host][host]
    if domain is None:
        pytest.skip("Domain not described")
    return account_fabric(domain=domain, supply_session=get_supply_session(host))


@pytest.fixture(scope="session")
def opponent_acc_on_host1(account_fabric, get_supply_session, federation_config):
    hosts = list(federation_config.keys())
    host = hosts[0]
    domain = federation_config[host][host]
    if domain is None:
        pytest.skip("Domain not described")
    return account_fabric(domain=domain, supply_session=get_supply_session(host))


@pytest.fixture(scope="session")
def main_acc_on_host2(account_fabric, get_supply_session, federation_config):
    hosts = list(federation_config.keys())
    host = hosts[1]
    domain = federation_config[host][host]
    if domain is None:
        pytest.skip("Domain not described")
    return account_fabric(domain=domain, supply_session=get_supply_session(host))


@pytest.fixture(scope="session")
def opponent_acc_on_host2(account_fabric, get_supply_session, federation_config):
    hosts = list(federation_config.keys())
    host = hosts[1]
    domain = federation_config[host][host]
    if domain is None:
        pytest.skip("Domain not described")
    return account_fabric(domain=domain, supply_session=get_supply_session(host))


@pytest.fixture(scope="session")
def fed_acc_on_host1_host2(account_fabric, get_supply_session, federation_config):
    hosts = list(federation_config.keys())
    host1 = hosts[0]
    host2 = hosts[1]
    domain = federation_config[host1][host2]
    if domain is None:
        pytest.skip("Domain not described")
    return account_fabric(domain=domain, supply_session=get_supply_session(host1))


@pytest.fixture(scope="session")
def fed_acc2_on_host1_host2(account_fabric, get_supply_session, federation_config):
    hosts = list(federation_config.keys())
    host1 = hosts[0]
    host2 = hosts[1]
    domain = federation_config[host1][host2]
    if domain is None:
        pytest.skip("Domain not described")
    return account_fabric(domain=domain, supply_session=get_supply_session(host1))


@pytest.fixture(scope="session")
def fed_acc3_on_host1_host2(account_fabric, get_supply_session, federation_config):
    hosts = list(federation_config.keys())
    host1 = hosts[0]
    host2 = hosts[1]
    domain = federation_config[host1][host2]
    if domain is None:
        pytest.skip("Domain not described")
    return account_fabric(domain=domain, supply_session=get_supply_session(host1))


@pytest.fixture(scope="session")
def fed_acc_on_host2_host1(account_fabric, get_supply_session, federation_config):
    hosts = list(federation_config.keys())
    host1 = hosts[1]
    host2 = hosts[0]
    domain = federation_config[host1][host2]
    if domain is None:
        pytest.skip("Domain not described")

    return account_fabric(domain=domain, supply_session=get_supply_session(host1))


@pytest.fixture(scope="session")
def fed_acc2_on_host2_host1(account_fabric, get_supply_session, federation_config):
    hosts = list(federation_config.keys())
    host1 = hosts[1]
    host2 = hosts[0]
    domain = federation_config[host1][host2]
    if domain is None:
        pytest.skip("Domain not described")
    return account_fabric(domain=domain, supply_session=get_supply_session(host1))


@pytest.fixture(scope="session")
def fed_acc3_on_host2_host1(account_fabric, get_supply_session, federation_config):
    hosts = list(federation_config.keys())
    host1 = hosts[1]
    host2 = hosts[0]
    domain = federation_config[host1][host2]
    if domain is None:
        pytest.skip("Domain not described")
    return account_fabric(domain=domain, supply_session=get_supply_session(host1))


@pytest.fixture
def get_chat_sn_from_event(fetch_until_empty_answer_with_filter):
    def func(acc, chat_name):
        remote_sn = find_chat_by_some_criterion(acc, chat_name)
        if remote_sn is None:
            events_hist_dlg_state = fetch_until_empty_answer_with_filter(acc, "histDlgState")
            remote_sn = get_remote_sn_from_histDlgState_events(events_hist_dlg_state, chat_name)
        if remote_sn is None:
            events_buddy_list = fetch_until_empty_answer_with_filter(acc, "buddylist")
            remote_sn = get_remote_sn_from_buddylist_event(events_buddy_list, chat_name)
        return remote_sn

    return func


@pytest.fixture
def create_group_or_channel(get_chat_sn_from_event):
    def func(
        defaultRole: Literal["member", "admin", "readonly"],
        creator: DesktopClient,
        members: list[DesktopClient],
        friendly_name: str,
        public: bool,
    ):
        local_chat_sn = None
        remote_chat_sn = None
        chat_name = generate_uniq_chat_name(friendly_name)
        with allure.step(f"Создаем чат {friendly_name}"):
            response = creator.rapi_createChat(
                name=chat_name, joinModeration=False, defaultRole=defaultRole, public=public
            )
            local_chat_sn = response["results"]["sn"]
            assert response["status"]["code"] == 20000, "Не удалось создать чат"
            if members:
                remote_clients = [acc for acc in members if acc.api_url != creator.api_url]
                remote_client = remote_clients[0] if remote_clients else None
                members_uins = [acc.uin for acc in members]
                with allure.step(f"Добавляем в чат {friendly_name} федеративных пользователей {members}"):
                    response = creator.rapi_group_members_add(sn=local_chat_sn, members=members_uins)
                    assert response["status"]["code"] == 20000, "Не удалось добавить в чат пользователей"
                    if remote_client:
                        remote_chat_sn = get_chat_sn_from_event(remote_client, chat_name)
        return chat_name, local_chat_sn, remote_chat_sn

    return func


@pytest.fixture
def group_GA1(create_group_or_channel, fed_acc3_on_host1_host2, fed_acc_on_host1_host2):
    return create_group_or_channel(
        defaultRole="member",
        creator=fed_acc3_on_host1_host2,
        members=[fed_acc_on_host1_host2],
        friendly_name="Группа_ГА1",
        public=True,
    )


@pytest.fixture
def channel_GA1(create_group_or_channel, fed_acc3_on_host1_host2, fed_acc_on_host1_host2):
    return create_group_or_channel(
        defaultRole="readonly",
        creator=fed_acc3_on_host1_host2,
        members=[fed_acc_on_host1_host2],
        friendly_name="Канал_ГА1",
        public=True,
    )


@pytest.fixture
def group_GA2(create_group_or_channel, fed_acc3_on_host1_host2, fed_acc3_on_host2_host1):
    return create_group_or_channel(
        defaultRole="member",
        creator=fed_acc3_on_host1_host2,
        members=[fed_acc3_on_host2_host1],
        friendly_name="Группа_ГА2",
        public=True,
    )


@pytest.fixture
def channel_GA2(create_group_or_channel, fed_acc3_on_host1_host2, fed_acc3_on_host2_host1):
    return create_group_or_channel(
        defaultRole="readonly",
        creator=fed_acc3_on_host1_host2,
        members=[fed_acc3_on_host2_host1],
        friendly_name="Канал_ГА2",
        public=True,
    )


@pytest.fixture
def group_GA3(create_group_or_channel, fed_acc3_on_host1_host2, fed_acc2_on_host1_host2):
    return create_group_or_channel(
        defaultRole="member",
        creator=fed_acc3_on_host1_host2,
        members=[fed_acc2_on_host1_host2],
        friendly_name="Группа_ГА3",
        public=False,
    )


@pytest.fixture
def channel_GA3(create_group_or_channel, fed_acc3_on_host1_host2, fed_acc2_on_host1_host2):
    return create_group_or_channel(
        defaultRole="readonly",
        creator=fed_acc3_on_host1_host2,
        members=[fed_acc2_on_host1_host2],
        friendly_name="Канал_ГА3",
        public=False,
    )


@pytest.fixture
def group_GA4(create_group_or_channel, fed_acc3_on_host1_host2, fed_acc2_on_host1_host2, fed_acc2_on_host2_host1):
    return create_group_or_channel(
        defaultRole="member",
        creator=fed_acc3_on_host1_host2,
        members=[fed_acc2_on_host1_host2, fed_acc2_on_host2_host1],
        friendly_name="Группа_ГА4",
        public=False,
    )


@pytest.fixture
def channel_GA4(create_group_or_channel, fed_acc3_on_host1_host2, fed_acc2_on_host1_host2, fed_acc2_on_host2_host1):
    return create_group_or_channel(
        defaultRole="readonly",
        creator=fed_acc3_on_host1_host2,
        members=[fed_acc2_on_host1_host2, fed_acc2_on_host2_host1],
        friendly_name="Канал_ГА4",
        public=False,
    )


@pytest.fixture
def group_GA5(create_group_or_channel, fed_acc3_on_host1_host2, fed_acc2_on_host1_host2, main_acc_on_host1):
    return create_group_or_channel(
        defaultRole="member",
        creator=fed_acc3_on_host1_host2,
        members=[fed_acc2_on_host1_host2, main_acc_on_host1],
        friendly_name="Группа_ГА3",
        public=False,
    )


@pytest.fixture
def channel_GA5(create_group_or_channel, fed_acc3_on_host1_host2, fed_acc2_on_host1_host2, main_acc_on_host1):
    return create_group_or_channel(
        defaultRole="readonly",
        creator=fed_acc3_on_host1_host2,
        members=[fed_acc2_on_host1_host2, main_acc_on_host1],
        friendly_name="Канал_ГА3",
        public=False,
    )
