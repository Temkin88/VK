import time

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("30204")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Боты")
@allure.feature("Stickers bot")
@allure.title("Импорт стикеров из Telegram")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.skip
def test_stickers_bot_import(
    auth_account,
    stickers_bot,
    event_filter,
    fetch_until_empty_answer_with_filter,
):
    with allure.step("Пишем боту /start"):
        auth_account.send_basic_message(
            sn=stickers_bot,
            text="/start",
        )

    with allure.step("Пробуем импортировать стикерпак из телеги"):
        auth_account.send_basic_message(
            sn=stickers_bot,
            text="https://t.me/addstickers/TimTheNerd",
        )

    with allure.step("Ждем"):
        time.sleep(20)

    with allure.step("Ищем ответ на импорт стикеров"):
        for _ in fetch_until_empty_answer_with_filter(auth_account, "apps"):
            return

        raise AssertionError('Failed to found "apps" events')
