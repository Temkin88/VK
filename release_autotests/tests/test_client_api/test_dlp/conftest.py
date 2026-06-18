import pytest

from pathlib import Path
import json


@pytest.fixture(scope="session")
def dlp_config(request, ENV_PLATFORM):
    dlp_config_file_path = request.config.getoption("--dlp-config-file")
    dlp_config_default = {
        "_comment": "Ключи начинающиеся с символа _ являются коментариями и будут пропущены тестами. "
        "Для сохранения структуры файла конфигурации рекомендуется использовать данный способ"
        "коментирования строк в место удаления",
        "SANDBOX": {
            "adapters": {
                "default": {
                    "_comment": "Эти тесты можно запускать в общей пачке тестов на дефолтном конфиге"
                    "_регрессионного стенда. Важно не забыть в админке supply-server выставить атрибут vip_type"
                    "_в соответствующее значение для пользователей из списка исключенных в конфиге вахтера",
                    "vip_type": "VIP1",
                    "domain": "autotest.clients",
                },
                "strategy_on_fail_block": {
                    "_comment": "Эти тесты можно запускать в общей пачке тестов на дефолтном конфиге "
                    "регрессионного стенда",
                    "domain": "autotest.clients",
                },
                "strategy_on_fail_ok": {
                    "_comment": "Эти тесты можно запускать в общей пачке тестов на дефолтном конфиге "
                    "регрессионного стенда",
                    "domain": "autotest-01.clients",
                },
                "external_files": {
                    "_comment": "Эти тесты можно запускать в общей пачке тестов на дефолтном конфиге"
                    "_регрессионного стенда",
                    "domain": "autotest-02.clients",
                },
                "internal_files": {
                    "_comment": "Эти тесты можно запускать в общей пачке тестов на дефолтном конфиге "
                    "регрессионного стенда",
                    "domain": "autotest.clients",
                },
                "debug_mode_true": {
                    "_comment": "Эти тесты можно запускать в общей пачке тестов на дефолтном конфиге "
                    "регрессионного стенда",
                    "domain": "autotest-04.clients",
                },
                "excluded_users": {
                    "_comment": "Эти тесты можно запускать в общей пачке тестов на дефолтном конфиге"
                    "_регрессионного стенда. Важно не забыть в админке supply-server выставить атрибут vip_type"
                    "_в соответствующее значение для пользователей из списка исключенных в конфиге вахтера",
                    "vip_type": "VIP1",
                    "domain": "autotest-03.clients",
                },
                "_file_attributes_blocking": {
                    "_comment": "Эти тесты требуют переопределения конфига вахтера или файлзов для рассмотрения"
                    " каждого тестового случая и не подходят для проверки на дефолтном конфиге регрессионного стенда",
                    "domain": "autotest-03.clients",
                    "file_limits": {"image/png": "200KiB", "image/jpeg": "0", "others": "1MiB"},
                },
                "_whitelisting": {
                    "_comment": "Эти тесты требуют переопределения конфига вахтера или файлзов для рассмотрения"
                    " каждого тестового случая и не подходят для проверки на дефолтном конфиге регрессионного стенда",
                    "domain": "autotest.clients",
                    "_trusted_subnets": ["1.1.1.1/24"],
                    "trusted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                    " (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36",
                    "_untrusted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                    " (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                },
                "_domains_check_false": {
                    "_comment": "Эти тесты требуют переопределения конфига вахтера",
                    "domain": "autotest.clients",
                    "domains": ["autotest-01.clients", "autotest-02.clients"],
                },
                "domains_check_true": {
                    "_comment": "Эти тесты можно запускать в общей пачке тестов на дефолтном конфиге регрессионного"
                    "_стенда",
                    "domain": "autotest.clients",
                    "domains": ["autotest-01.clients", "autotest-02.clients"],
                },
            },
            "headers": {
                "_comment1": "При проверке на регрессионом стенде с использованием adapter_chooser и включенной опцией "
                "check_access_level, тут нужно указать user-aget для internal сессии",
                "internal": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36",
                "_comment2": "При проверке на регрессионом стенде с использованием adapter_chooser и включенной опцией "
                "check_access_level, тут нужно указать user-aget для external сессии. "
                "Eсли браузер chrome не входит internal, то эту опцию можно не указывать",
                "external": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            },
        },
        "SAAS": {
            "adapters": {
                "_default": {
                    "domain": "dlpautotest.bizml.ru",
                    "vip_type": "VIP1",
                },
                "excluded_users": {
                    "domain": "dlpautotest.bizml.ru",
                    "vip_type": "VIP1",
                },
                "_strategy_on_fail_block": {"domain": "dlpautotest.bizml.ru"},
                "_whitelisting": {
                    "_comment": "Эти тесты требуют переопределения конфига вахтера или файлзов для рассмотрения"
                    " каждого тестового случая и не подходят для проверки на дефолтном конфиге регрессионного стенда",
                    "domain": "dlpautotest.bizml.ru",
                    "_trusted_subnets": ["1.1.1.1/24"],
                    "trusted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                    " (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36",
                    "_untrusted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                    " (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                },
                "file_attributes_blocking": {
                    "_comment": "Эти тесты требуют переопределения конфига вахтера или файлзов для рассмотрения"
                    " каждого тестового случая и не подходят для проверки на дефолтном конфиге регрессионного стенда",
                    "domain": "dlpautotest.bizml.ru",
                    "file_limits": {"image/png": "200KiB", "image/jpeg": "0", "others": "1MiB"},
                },
            },
            "headers": {
                "internal": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36",
                "external": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            },
        },
        "PRE_SAAS": {
            "adapters": {
                "_default": {
                    "domain": "dlpautotest.bizml.ru",
                    "vip_type": "VIP1",
                },
                "excluded_users": {
                    "domain": "dlpautotest.bizml.ru",
                    "vip_type": "VIP1",
                },
                "_strategy_on_fail_block": {"domain": "dlpautotest.bizml.ru"},
                "_whitelisting": {
                    "_comment": "Эти тесты требуют переопределения конфига вахтера или файлзов для рассмотрения"
                    " каждого тестового случая и не подходят для проверки на дефолтном конфиге регрессионного стенда",
                    "domain": "dlpautotest.bizml.ru",
                    "_trusted_subnets": ["1.1.1.1/24"],
                    "trusted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                    " (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36",
                    "_untrusted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                    " (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                },
                "file_attributes_blocking": {
                    "_comment": "Эти тесты требуют переопределения конфига вахтера или файлзов для рассмотрения"
                    " каждого тестового случая и не подходят для проверки на дефолтном конфиге регрессионного стенда",
                    "domain": "dlpautotest.bizml.ru",
                    "file_limits": {"image/png": "200KiB", "image/jpeg": "0", "others": "1MiB"},
                },
            },
            "headers": {
                "internal": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36",
                "external": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            },
        },
        "PRE_TARM": {
            "adapters": {
                "default": {
                    "domain": "dlpautotest-01.tppr.vmailru.net",
                },
            },
            "headers": {
                "internal": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36",
                "external": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            },
        },
    }

    with Path.open("dlp-domain-config.template.json", "w", encoding="utf-8") as json_file:
        json.dump(dlp_config_default, json_file, indent=4, ensure_ascii=False)
    dlp_config = dlp_config_default
    dlp_config_from_file = None
    if dlp_config_file_path is not None:
        with Path.open(dlp_config_file_path, "r", encoding="utf-8") as f:
            dlp_config_from_file = json.load(f)
    if dlp_config_from_file is not None:
        dlp_config = dlp_config_from_file
    if ENV_PLATFORM not in dlp_config:
        pytest.skip("DLP domains not configured for this environment")
    return dlp_config[ENV_PLATFORM]


@pytest.fixture(scope="session")
def external_header(dlp_config):
    if "headers" in dlp_config and "external" in dlp_config["headers"]:
        return dlp_config["headers"]["external"]
    else:
        return None


@pytest.fixture(scope="session")
def internal_header(dlp_config):
    if "headers" in dlp_config and "internal" in dlp_config["headers"]:
        return dlp_config["headers"]["internal"]
    else:
        return None


@pytest.fixture(scope="session", autouse=True)
def skip_tests_dlp(request):
    env = request.config.getoption("-m")
    if "DLP" not in env:
        pytest.skip("Tests skip: DLP marker is not set")


@pytest.fixture(scope="session")
def dlp_block_text():
    return "block"


@pytest.fixture(scope="session")
def dlp_noblock_text(dlp_block_text):
    dlp_noblock_text = "blokc"

    assert dlp_block_text.lower() not in dlp_noblock_text.lower(), (
        "Noblock word contains block word. Please change one of them"
    )
    return dlp_noblock_text


@pytest.fixture(scope="session")
def check_text_warn_timeout():
    return 1


@pytest.fixture(scope="session")
def check_text_disconnect_timeout():
    return 3


@pytest.fixture(scope="session")
def check_file_warn_timeout():
    return 2


@pytest.fixture(scope="session")
def check_file_disconnect_timeout():
    return 4


@pytest.fixture(scope="session")
def dlp_system(request):
    return request.config.getoption("--dlp-system")


@pytest.fixture(scope="session")
def default_main_acc(account_fabric, dlp_config, internal_header):
    if "default" not in dlp_config["adapters"]:
        return None
    domain = dlp_config["adapters"]["default"]["domain"]
    header = {"User-Agent": internal_header} if internal_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )


@pytest.fixture(scope="session")
def default_main_acc_second_instance(account_fabric, default_main_acc, internal_header):
    if default_main_acc is None:
        return None
    domain = default_main_acc.uin.split("@")[1]
    header = {"User-Agent": internal_header} if internal_header is not None else {}
    return account_fabric(
        header=header,
        account_uin=default_main_acc.uin,
        domain=domain,
    )


@pytest.fixture(scope="session")
def default_opponent_acc(account_fabric, dlp_config, internal_header):
    if "default" not in dlp_config["adapters"]:
        return None
    domain = dlp_config["adapters"]["default"]["domain"]
    header = {"User-Agent": internal_header} if internal_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )
