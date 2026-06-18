import logging
import time
import allure
import pytest

from support.markers import SANDBOX
from imcommonsupplyclient import voip
from imcommonsupplyclient.voip.enums import RecordingCommand


logger = logging.getLogger(__name__)


@SANDBOX
@allure.id("391047")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Звонки")
@allure.feature("Запись звонка")
@allure.title("Запись звонка аудио")
@pytest.mark.parametrize("participants_count", [6])
def test_call_rec_audio(get_voip_bots, participants_count, check_recorded_call_video_file, get_bot_account):
    """
    Запись звонка на 6 участников без видео
    """

    with allure.step("Получение VoIP-ботов"):
        bots = get_voip_bots(participants_count)

        first_bot, *other_bots = bots

        bot_account = get_bot_account(first_bot)

    with allure.step("Очистка истории чата c RecorderBot"):
        bot_account.clean_user_chats_history(["70005"])

    with allure.step(f"Установить звонок в чат (любые клиенты, до  {participants_count} участников)."):
        first_call = first_bot.make_group_call(other_bots, with_video=False)
        calls = [first_call]

        for bot in other_bots:
            calls.append(bot.wait_call_and_accept(with_video=False))

        voip.cross_check_participants(calls=calls, participants=bots, microphone_on=True, camera_on=False)

    with allure.step("Стартовать запись звонка на одном из участников"):
        first_call.call_recording(RecordingCommand.START)

        for i in range(15):
            logger.info(f"Waiting for call to record ({i} of 15 seconds)")
            time.sleep(1)

    with allure.step("Остановить запись "):
        first_call.call_recording(RecordingCommand.STOP)

    with allure.step("Завершить звонок"):
        voip.bulk_hang_up(calls)

    check_recorded_call_video_file(bot_account=bot_account, recorder_bot_sn="70005", min_file_size_mb=0.3)
