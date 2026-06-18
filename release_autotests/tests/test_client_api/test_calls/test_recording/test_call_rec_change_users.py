import logging
import allure
import time

from support.markers import SANDBOX
from imcommonsupplyclient import voip
from imcommonsupplyclient.voip.enums import RecordingCommand


logger = logging.getLogger(__name__)


@SANDBOX
@allure.id("391048")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Звонки")
@allure.feature("Запись в звонке со сменой участников звонка во время записи")
@allure.title("Запись звонка со сменой участников")
def test_call_rec_change_users(get_voip_bots, check_recorded_call_video_file, get_bot_account):
    """
    Запись в звонке со сменой участников звонка во время записи
    """
    with allure.step("Получение VoIP-ботов"):
        bot_a, bot_b, bot_c, bot_d = get_voip_bots(4)

        bot_account = get_bot_account(bot_a)

    with allure.step("Очистка истории чата c RecorderBot"):
        bot_account.clean_user_chats_history(["70005"])

    with allure.step("Установить п2п видеозвонок между пользователями А и В"):
        bot_a_out_call = bot_a.make_p2p_call(to=bot_b, with_video=True)
        bot_b_in_call = bot_b.wait_call_and_accept(with_video=True)
        voip.cross_check_participants(
            calls=[bot_a_out_call, bot_b_in_call], participants=[bot_a, bot_b], camera_on=True
        )

    with allure.step("Стартовать запись на стороне одного участника А"):
        bot_a_out_call.call_recording(RecordingCommand.START)

        for i in range(15):
            logger.info(f"Waiting for call to record ({i} of 15 seconds)")
            time.sleep(1)

    with allure.step("Добавить в звонок несколько пользователей (минимум 2) - С и D"):
        bot_a_out_call.add_participants([bot_c, bot_d])
        bot_c_in_call = bot_c.wait_call_and_accept(with_video=True)
        bot_d_in_call = bot_d.wait_call_and_accept(with_video=True)

    with allure.step("Выйти из звонка пользователем B"):
        bot_b_in_call.hang_up()

        voip.cross_check_participants(
            calls=[bot_c_in_call, bot_d_in_call],
            participants=[bot_d, bot_c],
            microphone_on=True,
            camera_on=True,
        )

    with allure.step("Пользователь А добавляет обратно пользователя B"):
        bot_a_out_call.add_participants(bot_b)
        bot_b_in_call = bot_b.wait_call_and_accept(with_video=True)

        voip.cross_check_participants(
            calls=[bot_a_out_call, bot_b_in_call],
            participants=[bot_a, bot_b],
            microphone_on=True,
            camera_on=True,
        )

    with allure.step("Завершить звонок"):
        voip.bulk_hang_up(calls=[bot_c_in_call, bot_b_in_call, bot_a_out_call, bot_d_in_call])

    check_recorded_call_video_file(bot_account=bot_account, recorder_bot_sn="70005")
