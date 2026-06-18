import allure
import pytest

from concurrent.futures import ThreadPoolExecutor

from support.markers import SANDBOX
from imcommonsupplyclient import voip


@SANDBOX
@allure.id("250077")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Конференция")
@allure.title("[DESKTOP] Звонок по ссылке")
@pytest.mark.parametrize("participants_count", [13, 6, 7, 10])
def test_link_call(get_voip_bots, participants_count):
    """
    Подключение к звонку по ссылке
    """

    with allure.step("Получение VoIP-ботов"):
        bots = get_voip_bots(participants_count)

        first_bot, *other_bots = bots

    with allure.step("Сгенерировать ссылку на звонок с любого из клиентов"):
        call_link = first_bot.create_conference().conferenceUrl

    def make_call(local_voip_bot: voip.VoIPBot):
        return local_voip_bot.make_call_by_link(call_link=call_link, with_video=False)

    with allure.step(f"Зайти по ссылке в звонок с любых клиентов количеством {participants_count} включительно"):
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


@SANDBOX
@pytest.mark.HEALTHCHECK_VOIP
@allure.id("545912")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Конференция")
@allure.title("[DESKTOP] Звонок по ссылке")
@pytest.mark.parametrize("participants_count", [2])
def test_link_call_healthcheck(get_voip_bots, participants_count):
    """
    Подключение к звонку по ссылке
    """

    with allure.step("Получение VoIP-ботов"):
        bots = get_voip_bots(participants_count)

        first_bot, *other_bots = bots

    with allure.step("Сгенерировать ссылку на звонок с любого из клиентов"):
        call_link = first_bot.create_conference().conferenceUrl

    def make_call(local_voip_bot: voip.VoIPBot):
        return local_voip_bot.make_call_by_link(call_link=call_link, with_video=False)

    with allure.step(f"Зайти по ссылке в звонок с любых клиентов количеством {participants_count} включительно"):
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
