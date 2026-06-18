import time
import logging

import allure

from support.markers import SANDBOX
from imcommonsupplyclient import voip

logger = logging.getLogger(__name__)


@SANDBOX
@allure.id("389342")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Конференция")
@allure.title("[DESKTOP + Guest] Звонок по ссылке")
def test_guest_call(get_voip_bots, get_guest_bots):
    """
    Подключение к звонку по ссылке
    """

    with allure.step("Получение VoIP-ботов"):
        first_bot = get_voip_bots(1)

    with allure.step("Сгенерировать ссылку на звонок с любого из клиентов"):
        call_link = first_bot.create_conference().conferenceUrl

    with allure.step("Получаем гостевого бота"):
        guest_bot = get_guest_bots(call_link=call_link, count=1)

    with allure.step("Вход пользователя с десктопа в звонок"):
        first_bot_call = first_bot.make_call_by_link(call_link=call_link)

    with allure.step("Вход гостевого пользователя в звонок"):
        # TODO (v.korobov@corp.mail.ru): FIX with_video flag for guest type of bot
        guest_call = guest_bot.wait_call_and_accept()

    with allure.step("Проверяем состояние участников"):
        guest_in_call = False
        guest_wait_timeout = 5
        for i in range(guest_wait_timeout):
            time.sleep(1)
            logger.info(f"Waiting for guest participant ({i} of {guest_wait_timeout} seconds)")
            participants = first_bot_call.get_participants()
            guest_in_call = any("@guest" in participant for participant in participants)
            if guest_in_call:
                break

        assert guest_in_call, "No guest in call party"

        first_bot_call.check_participants(
            participants=[participant for participant in participants if "@guest" in participant], camera_on=False
        )

    with allure.step("Завершить звонок на каждой стороне"):
        voip.bulk_hang_up([first_bot_call, guest_call])
