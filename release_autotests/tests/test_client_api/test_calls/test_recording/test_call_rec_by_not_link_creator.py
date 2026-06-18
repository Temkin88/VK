import logging
import time
import allure
import pytest

from concurrent.futures import ThreadPoolExecutor
from support.markers import SANDBOX
from imcommonsupplyclient import voip
from imcommonsupplyclient.voip.enums import RecordingCommand


logger = logging.getLogger(__name__)


@SANDBOX
@allure.id("391045")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Звонки")
@allure.feature("Запись звонка не создателем ссылки")
@allure.title("Старт записи звонка не создателем ссылки")
@pytest.mark.parametrize("participants_count", [3])
def test_call_rec_by_not_link_creator(
    get_voip_bots, participants_count, check_recorded_call_video_file, get_bot_account
):
    """
    Запись в звонке по ссылке, инициатором записи является не создатель ссылки
    """

    with allure.step("Получение VoIP-ботов"):
        bots = get_voip_bots(participants_count)

        first_bot, *other_bots = bots

        bot_account = get_bot_account(bots[1])

    with allure.step("Очистка истории чата c RecorderBot"):
        bot_account.clean_user_chats_history(["70005"])

    with allure.step("Создать ссылку на звонок"):
        call_link = first_bot.create_conference().conferenceUrl

    def make_call(local_voip_bot: voip.VoIPBot):
        return local_voip_bot.make_call_by_link(call_link=call_link, with_video=False)

    with allure.step("Несколько участников заходят в звонок, включают видео"):
        calls = []

        with ThreadPoolExecutor(max_workers=voip.VOIP_WORKERS_COUNT) as executer:
            for result in executer.map(make_call, bots):
                calls.append(result)

        voip.cross_check_participants(calls=calls, participants=bots, microphone_on=True, camera_on=False)
        voip.bulk_unmute_camera(calls)
        voip.cross_check_participants(calls=calls, participants=bots, microphone_on=True, camera_on=True)

    with allure.step("Не создатель ссылки на звонок стартует запись звонка"):
        calls[1].call_recording(RecordingCommand.START)

        for i in range(15):
            logger.info(f"Waiting for call to record ({i} of 15 seconds)")
            time.sleep(1)

    with allure.step("Остановить запись, выйти из звонка"):
        calls[1].call_recording(RecordingCommand.STOP)
        voip.bulk_hang_up(calls)

    check_recorded_call_video_file(bot_account=bot_account, recorder_bot_sn="70005")
