import allure
import pytest

from support.markers import SANDBOX
from imcommonsupplyclient import voip


@SANDBOX
@allure.id("250080")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Групповой звонок")
@allure.title("[DESKTOP] Групповой звонок через Звонки - Начать групповой звонок")
@pytest.mark.parametrize("participants_count", [6, 7, 10, 13])
def test_group_call_from_calls_tab(get_voip_bots, participants_count):
    """
    Сбор группового звонка через меню звонков
    """

    with allure.step("Получение VoIP-ботов"):
        bots = get_voip_bots(participants_count)

        first_bot, *other_bots = bots

    with allure.step(
        "На любом Desktop клиенте зайти в Звонки - Начать групповой звонок,"
        f" выбрать {participants_count} участников, стартовать звонок."
    ):
        calls = [first_bot.make_group_call(other_bots, with_video=False)]

    with allure.step("Все участники принимают вызов."):
        for bot in other_bots:
            calls.append(bot.wait_call_and_accept(with_video=False))

    with allure.step("Все участники включают видео"):
        voip.bulk_unmute_camera(calls)
        voip.cross_check_participants(calls=calls, participants=bots, microphone_on=True, camera_on=True)

    with allure.step("Завершить звонок на одной из сторон"):
        voip.bulk_hang_up(calls)


@allure.id("250082")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Групповой звонок")
@allure.title("[Desktop] Групповой звонок")
@SANDBOX
@pytest.mark.parametrize("participants_count", [13, 6, 7, 10])
def test_group_call_from_chat(get_voip_bots, participants_count):
    """
    Сбор группового звонка через звонок в чат
    """
    with allure.step("Получение VoIP-ботов"):
        bots = get_voip_bots(participants_count)

        first_bot, *other_bots = bots

    with allure.step("Создать чат до 6 участников включительно"):
        chat = first_bot.create_chat(members=bots)

    with allure.step("С десктопного клиента стартовать аудиозвонок в чат"):
        calls = [first_bot.make_chat_call(chat, other_bots, with_video=False)]

    with allure.step("Все участники принимают вызов"):
        for bot in other_bots:
            calls.append(bot.wait_call_and_accept(with_video=False))

        voip.cross_check_participants(calls=calls, participants=bots, microphone_on=True, camera_on=False)

    with allure.step("Все участники включают видео"):
        voip.bulk_unmute_camera(calls)
        voip.cross_check_participants(calls=calls, participants=bots, microphone_on=True, camera_on=True)

    with allure.step("Завершить звонок на каждой стороне"):
        voip.bulk_hang_up(calls)
