import re
import uuid
import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality

pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.BOT_API)]


def generate_random_bot_name():
    return "test_" + str(uuid.uuid1()).replace("-", "")[:21] + "_bot"


def extract_bot_token(text):
    match = re.search(r"(\d+\.\d+\.\d+\:\w+)", text)
    return match.group(1) if match else None


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Боты")
@allure.feature("Metabot")
@allure.title("Создание через Metabot и проверка видимости бота в домене 3")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_domain3_bot_visibility(
    auth_account_with_domain_testbiz,
    auth_account_with_domain_testb1iz,
    auth_account_with_domain_lalalalalalal,
    metabot,
    start_metabot_domain3,
):
    user_msg_id, bot_msg_id = start_metabot_domain3
    bot_token = None

    with allure.step("Создаем бота в домене 3"):
        auth_account_with_domain_lalalalalalal.rapi_getBotCallbackAnswer(
            chatId=metabot,
            msgId=bot_msg_id,
            callbackData="newbot",
        )

        bot_name = generate_random_bot_name()
        auth_account_with_domain_lalalalalalal.send_basic_message(
            sn=metabot,
            text=bot_name,
        )

        history = auth_account_with_domain_lalalalalalal.rapi_getHistory(
            sn=metabot,
            count=-1,
        )
        for message in history["results"]["messages"]:
            token = extract_bot_token(message["text"])
            if token:
                bot_token = token
                break

        assert bot_token, "Failed to get bot token in domain 3"

    with allure.step("Проверяем, что бот недоступен в домене 1"), pytest.raises(Exception):
        auth_account_with_domain_testbiz.rapi_getBotInfo(
            botToken=bot_token,
        )

    with allure.step("Проверяем, что бот недоступен в домене 2"), pytest.raises(Exception):
        auth_account_with_domain_testb1iz.rapi_getBotInfo(
            botToken=bot_token,
        )

    with allure.step("Проверяем, что бот доступен в домене 3"):
        info = auth_account_with_domain_lalalalalalal.rapi_getBotInfo(
            botToken=bot_token,
        )
        assert info, "The bot must be available on its domain 3"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Боты")
@allure.feature("Metabot")
@allure.title("Создание через Metabot и проверка видимости бота в домене 2")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_domain2_bot_visibility(
    auth_account_with_domain_testbiz,
    auth_account_with_domain_testb1iz,
    auth_account_with_domain_lalalalalalal,
    metabot,
    start_metabot_domain2,
):
    user_msg_id, bot_msg_id = start_metabot_domain2
    bot_token = None

    with allure.step("Создаем бота в домене 2"):
        auth_account_with_domain_testb1iz.rapi_getBotCallbackAnswer(
            chatId=metabot,
            msgId=bot_msg_id,
            callbackData="newbot",
        )

        bot_name = generate_random_bot_name()
        auth_account_with_domain_testb1iz.send_basic_message(
            sn=metabot,
            text=bot_name,
        )

        history = auth_account_with_domain_testb1iz.rapi_getHistory(
            sn=metabot,
            count=-1,
        )

        for message in history["results"]["messages"]:
            token = extract_bot_token(message["text"])
            if token:
                bot_token = token
                break

        assert bot_token, "Failed to get bot token in domain 2"

    with allure.step("Проверяем, что бот доступен в домене 2"):
        info = auth_account_with_domain_testb1iz.rapi_getBotInfo(
            botToken=bot_token,
        )
        assert info, "The bot must be available on its domain 2"

    with allure.step("Проверяем, что бот доступен в домене 1"):
        info = auth_account_with_domain_testbiz.rapi_getBotInfo(
            botToken=bot_token,
        )
        assert info, "Bot from domain 1 should be available in domain 1"

    with allure.step("Проверяем, что бот недоступен в домене 3"), pytest.raises(Exception):
        auth_account_with_domain_lalalalalalal.rapi_getBotInfo(
            botToken=bot_token,
        )


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Боты")
@allure.feature("Metabot")
@allure.title("Создание через Metabot и проверка видимости бота в домене 1")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_domain1_bot_visibility(
    auth_account_with_domain_testbiz,
    auth_account_with_domain_testb1iz,
    auth_account_with_domain_lalalalalalal,
    metabot,
    start_metabot_domain1,
):
    user_msg_id, bot_msg_id = start_metabot_domain1
    bot_token = None

    with allure.step("Создаем бота в домене 1"):
        auth_account_with_domain_testbiz.rapi_getBotCallbackAnswer(
            chatId=metabot,
            msgId=bot_msg_id,
            callbackData="newbot",
        )

        bot_name = generate_random_bot_name()
        auth_account_with_domain_testbiz.send_basic_message(
            sn=metabot,
            text=bot_name,
        )

        history = auth_account_with_domain_testbiz.rapi_getHistory(
            sn=metabot,
            count=-1,
        )
        for message in history["results"]["messages"]:
            token = extract_bot_token(message["text"])
            if token:
                bot_token = token
                break

        assert bot_token, "Failed to get bot token in domain 1"

        with allure.step("Проверяем, что бот доступен в домене 1"):
            info = auth_account_with_domain_testbiz.rapi_getBotInfo(
                botToken=bot_token,
            )
            assert info, "The bot must be available on its domain 1"

        with allure.step("Проверяем, что бот доступен в домене 2"):
            info = auth_account_with_domain_testb1iz.rapi_getBotInfo(
                botToken=bot_token,
            )
            assert info, "Bot from domain 1 should be available in domain 2"

        with allure.step("Проверяем, что бот недоступен в домене 3"), pytest.raises(Exception):
            auth_account_with_domain_lalalalalalal.rapi_getBotInfo(
                botToken=bot_token,
            )
