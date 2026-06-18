import re
import time
import uuid

import allure
import pytest

from support.cases.metabot_keyboard import keyboard
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.BOT_API)]


def generate_random_bot_name():
    return "test_" + str(uuid.uuid1()).replace("-", "")[:21] + "_bot"


@allure.id("27469")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Боты")
@allure.feature("Metabot")
@allure.title("Написать Metabot /start")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.skip
def test_metabot_start(
    auth_account,
    metabot,
    event_filter,
    fetch_until_empty_answer_with_filter,
):
    with allure.step("Написать Metabot /start"):
        auth_account.send_basic_message(
            sn=metabot,
            text="/start",
        )

    with allure.step("Ждем и проверяем ответ"):
        answer_found_and_checked = False

        for _ in range(3):
            for event in fetch_until_empty_answer_with_filter(auth_account, "histDlgState"):
                data = event["eventData"]

                if data["sn"] == metabot:
                    for message in data["tail"]["messages"]:
                        bot_keyboard = message.get("inlineKeyboardMarkup")
                        if bot_keyboard == keyboard["ru"] or bot_keyboard == keyboard["en"]:
                            answer_found_and_checked = True
                            break
            if answer_found_and_checked:
                break
            else:
                time.sleep(1)

        assert answer_found_and_checked, "bots:metabot_not_answering_start"


@allure.id("27470")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Metabot")
@allure.title("Переключить язык Metabot")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "language",
    [
        "ru",
        "en",
    ],
    ids=lambda x: f"language:{x}",
)
@pytest.mark.skip
def test_metabot_callback_switch_language(
    auth_account,
    metabot,
    event_filter,
    start_metabot,
    language,
    fetch_until_empty_answer_with_filter,
):
    user_msg_id, bot_msg_id = start_metabot

    with allure.step(f"Переключить язык на {language}"):
        auth_account.rapi_getBotCallbackAnswer(
            chatId=metabot,
            msgId=bot_msg_id,
            callbackData=f"switch_lang_{language}",
        )

    with allure.step("Ждем и проверяем ответ"):
        answer_found_and_checked = False

        for _ in range(3):
            for _ in fetch_until_empty_answer_with_filter(auth_account, "histDlgState"):
                answer_found_and_checked = True

            if answer_found_and_checked:
                break
            else:
                time.sleep(1)

        assert answer_found_and_checked, "bots:metabot_not_answering_callback"

    with allure.step("Проверяем содержание ответа от бота"):
        msg_edited = False

        result = auth_account.rapi_getHistory(
            sn=metabot,
            count=1,
            fromMsgId=user_msg_id,
            patchVersion=str(bot_msg_id),
        )

        for message in result["results"]["messages"]:
            bot_keyboard = message.get("inlineKeyboardMarkup")
            if bot_keyboard == keyboard[language]:
                msg_edited = True

        assert msg_edited, "bots:metabot_msg_keyboard_not_edited"


@allure.id("27474")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Боты")
@allure.feature("Metabot")
@allure.title("Создание бота через Metabot")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.skip
def test_metabot_callback_create_bot(
    auth_account,
    metabot,
    start_metabot,
):
    user_msg_id, bot_msg_id = start_metabot

    with allure.step("Отправляем callback создания бота"):
        auth_account.rapi_getBotCallbackAnswer(
            chatId=metabot,
            msgId=bot_msg_id,
            callbackData="newbot",
        )

    with allure.step("Ждем ответ"):
        time.sleep(6)

        msg_edited = False

        result = auth_account.rapi_getHistory(
            sn=metabot,
            count=1,
            fromMsgId=user_msg_id,
            patchVersion=str(bot_msg_id),
        )

        for message in result["results"]["messages"]:
            bot_keyboard = message.get("inlineKeyboardMarkup")
            if bot_keyboard != keyboard["ru"] and bot_keyboard != keyboard["en"]:
                msg_edited = True

        assert msg_edited, "bots:metabot_msg_keyboard_not_edited"

    bot_name = generate_random_bot_name()

    with allure.step("Отправляем ник бота"):
        auth_account.send_basic_message(
            sn=metabot,
            text=bot_name,
        )

    with allure.step("Ждем ответа"):
        time.sleep(5)

    with allure.step("Проверяем ответ"):

        def get_bot_token(msg_text: str) -> str:
            for entry in re.findall(r"\d+\.\d+\.\d+\:\d+", msg_text):
                return entry

        result = auth_account.rapi_getHistory(
            sn=metabot,
            count=-1,
        )

        for message in result["results"]["messages"]:
            if get_bot_token(message["text"]):
                return
        else:
            pytest.fail("metabot:failed_to_create_bot")
