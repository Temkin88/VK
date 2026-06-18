import logging
import time

import allure

from concurrent.futures import ThreadPoolExecutor

from support.markers import SAAS, ISOLATION
from imcommonsupplyclient import voip

logger = logging.getLogger(__name__)


@ISOLATION
@SAAS
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Конференция")
@allure.title("[DESKTOP] Звонок по ссылке")
def test_link_call_isolation(get_voip_bots_isolation):
    """
    Подключение к звонку по ссылке
    """

    with allure.step("Получение VoIP-ботов"):
        bots = get_voip_bots_isolation(1)

        first_bot, *other_bots = bots

    with allure.step("Сгенерировать ссылку на звонок с любого из клиентов"):
        call_link = first_bot.create_conference().conferenceUrl

    def make_call(local_voip_bot: voip.VoIPBot):
        return local_voip_bot.make_call_by_link(call_link=call_link, with_video=False)

    with allure.step("Зайти по ссылке в звонок с любых клиентов количеством включительно"):
        calls = []

        with ThreadPoolExecutor(max_workers=voip.VOIP_WORKERS_COUNT) as executer:
            for result in executer.map(make_call, bots):
                calls.append(result)

        voip.cross_check_participants(calls=calls, participants=bots, microphone_on=True, camera_on=False)

    with allure.step("Все участники включают видео"):
        voip.bulk_unmute_camera(calls)
        voip.cross_check_participants(calls=calls, participants=bots, microphone_on=True, camera_on=True)

    with allure.step("Завершить звонок на каждой стороне"):
        voip.bulk_hang_up(calls)


@ISOLATION
@SAAS
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Конференция")
@allure.title("[DESKTOP] Звонок по ссылке пользователем не в тенанте")
def test_link_call_isolation_not_in_tenant(get_voip_bots_isolation):
    """
    Подключение к звонку по ссылке
    """

    with allure.step("Получение VoIP-ботов"):
        bots = get_voip_bots_isolation(1)

        first_bot, bot_b, bot_c = bots

    with allure.step("Сгенерировать ссылку на звонок с любого из клиентов"):
        call_link = first_bot.create_conference().conferenceUrl

    def make_call():
        return bot_c.make_call_by_link(call_link=call_link, with_video=False)

    with allure.step("Вход пользователя с десктопа в звонок"):
        first_bot_call = first_bot.make_call_by_link(call_link=call_link)

    with allure.step("Вход пользователя с десктопа в звонок"):
        bot_c_call = bot_c.make_call_by_link(call_link=call_link)

    with allure.step("Проверяем состояние участников"):
        guest_in_call = False
        guest_wait_timeout = 5
        for i in range(guest_wait_timeout):
            time.sleep(1)
            logger.info(f"Waiting for guest participant ({i} of {guest_wait_timeout} seconds)")
            participants = first_bot_call.get_participants()
            guest_in_call = any("@lalalalalalal.bizml.ru" in participant for participant in participants)
            if guest_in_call:
                break

        assert guest_in_call, "No guest in call party"

        first_bot_call.check_participants(
            participants=[participant for participant in participants if "@lalalalalalal.bizml.ru" in participant],
            camera_on=False,
        )
    with allure.step("Зайти по ссылке в звонок с любых клиентов количеством включительно"):
        calls = []

        with ThreadPoolExecutor(max_workers=voip.VOIP_WORKERS_COUNT) as executer:
            for result in executer.map(make_call, bots):
                calls.append(result)

        voip.cross_check_participants(calls=calls, participants=bots, microphone_on=True, camera_on=False)

    with allure.step("Завершить звонок на каждой стороне"):
        voip.bulk_hang_up(calls, bot_c_call, first_bot_call)
