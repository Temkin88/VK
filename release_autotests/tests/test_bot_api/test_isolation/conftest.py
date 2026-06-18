import allure
import pytest
import time


@pytest.fixture(scope="session", autouse=True)
def skip_test_isolations():
    pytest.skip("Нет окружения где это настроено")


@allure.title("Написать из 3 домена Metabot /start")
@pytest.fixture(scope="session")
def start_metabot_domain3(auth_account_with_domain_lalalalalalal, metabot):
    with allure.step("Написать Metabot /start"):
        msg_id = auth_account_with_domain_lalalalalalal.send_basic_message(
            sn=metabot,
            text="/start",
        )

    with allure.step("Ждем ответа"):
        time.sleep(6)

    with allure.step("Получаем ID ответа бота"):
        result = auth_account_with_domain_lalalalalalal.rapi_getHistory(
            sn=metabot,
            count=-1,
            fromMsgId=msg_id,
            patchVersion="init",
        )

    return msg_id, result["results"]["lastMsgId"]


@allure.title("Написать из 2 домена Metabot /start")
@pytest.fixture(scope="session")
def start_metabot_domain2(auth_account_with_domain_testb1iz, metabot):
    with allure.step("Написать Metabot /start"):
        msg_id = auth_account_with_domain_testb1iz.send_basic_message(
            sn=metabot,
            text="/start",
        )

    with allure.step("Ждем ответа"):
        time.sleep(6)

    with allure.step("Получаем ID ответа бота"):
        result = auth_account_with_domain_testb1iz.rapi_getHistory(
            sn=metabot,
            count=-1,
            fromMsgId=msg_id,
            patchVersion="init",
        )

    return msg_id, result["results"]["lastMsgId"]


@allure.title("Написать из 1 домена Metabot /start")
@pytest.fixture(scope="session")
def start_metabot_domain1(auth_account_with_domain_testbiz, metabot):
    with allure.step("Написать Metabot /start"):
        msg_id = auth_account_with_domain_testbiz.send_basic_message(
            sn=metabot,
            text="/start",
        )

    with allure.step("Ждем ответа"):
        time.sleep(6)

    with allure.step("Получаем ID ответа бота"):
        result = auth_account_with_domain_testbiz.rapi_getHistory(
            sn=metabot,
            count=-1,
            fromMsgId=msg_id,
            patchVersion="init",
        )

    return msg_id, result["results"]["lastMsgId"]
