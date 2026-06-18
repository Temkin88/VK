import logging
import time
import allure
import pytest

from support.markers import SANDBOX
from imcommonsupplyclient import voip
from imcommonsupplyclient.voip.enums import RecordingCommand


logger = logging.getLogger(__name__)


@SANDBOX
@pytest.mark.HEALTHCHECK_VOIP
@allure.id("391049")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Звонки")
@allure.feature("Запись звонка")
@allure.title("Запись звонка видео")
def test_call_rec_video(get_voip_bots, get_bot_account, check_recorded_call_video_file):
    """
    Запись звонка с видео в п2п
    """

    with allure.step("Получение VoIP-ботов"):
        bot_a, bot_b = get_voip_bots(2)

        bot_account = get_bot_account(bot_a)

    with allure.step("Очистка истории чата c RecorderBot"):
        bot_account.clean_user_chats_history(["70005"])

    with allure.step("Установить p2p звонок, выключить микрофоны "):
        bot_a_out_call = bot_a.make_p2p_call(to=bot_b, with_video=True)
        bot_b_in_call = bot_b.wait_call_and_accept(with_video=True)
        voip.bulk_mute_microphone(calls=[bot_a_out_call, bot_b_in_call])
        voip.cross_check_participants(
            calls=[bot_a_out_call, bot_b_in_call], participants=[bot_a, bot_b], microphone_on=False, camera_on=True
        )

    with allure.step("Стартовать запись звонка на одном из участников"):
        bot_a_out_call.call_recording(RecordingCommand.START)

        for i in range(10):
            logger.info(f"Waiting for call to record ({i} of 10 seconds)")
            time.sleep(1)

    with allure.step("Поставить запись на паузу"):
        bot_a_out_call.call_recording(RecordingCommand.PAUSE)
        for i in range(5):
            logger.info(f"Waiting for call to pause the recording ({i} of 5 seconds)")
            time.sleep(1)

    with allure.step("Остановить запись"):
        bot_a_out_call.call_recording(RecordingCommand.STOP)

    with allure.step("Завершить звонок"):
        voip.bulk_hang_up(calls=[bot_a_out_call, bot_b_in_call])

    check_recorded_call_video_file(bot_account=bot_account, recorder_bot_sn="70005")
