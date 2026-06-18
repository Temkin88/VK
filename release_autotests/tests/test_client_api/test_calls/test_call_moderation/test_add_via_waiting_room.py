import allure
import pytest

from support.markers import SANDBOX
from imcommonsupplyclient import voip
from imcommonsupplyclient.voip import Permission


@SANDBOX
@allure.id("477680")
@allure.label("layer", "voip_layer")
@allure.title("Впустить пользователей в звонок из комнаты ожидания")
@allure.suite("Regression")
@allure.feature("Модерация звонков")
@pytest.mark.Regression
@pytest.mark.parametrize("participants_count", [4])
def test_add_via_waiting_room(get_voip_bots, participants_count):
    bots = get_voip_bots(participants_count)
    creator_bot, participant_bot_moderated, participant_bot1, participant_bot2 = bots

    with allure.step("1 Создать конференцию (звонок по ссылке) с включенной комнатой ожидания"):
        call_link = creator_bot.create_conference(
            "Test conf",
            members={
                participant_bot_moderated.uin: {"role": "speaker"},
                participant_bot1.uin: {"role": "speaker"},
                participant_bot2.uin: {"role": "speaker"},
            },
            roles={
                "speaker": {
                    "permissions": Permission.send_audio
                    | Permission.send_video
                    | Permission.share_screen
                    | Permission.create_outgoing_media_connection
                },
                "default": {"permissions": Permission.all()},
            },
        ).conferenceUrl

    with allure.step("2 Каждый пользователь переходит по ссылке конференции"):
        call_creator = creator_bot.make_call_by_link(call_link=call_link)
        call_participant_bot_moderated = participant_bot_moderated.make_call_by_link(call_link=call_link)
        call_participant_bot1 = participant_bot1.make_call_by_link(call_link=call_link)
        call_participant_bot2 = participant_bot2.make_call_by_link(call_link=call_link)

    with allure.step("3  Модератор выбирает не впускать пользователя А, впускает В и С "):
        call_creator.moderate_reject(participants=participant_bot_moderated)
        call_creator.moderate_admit(participants=[participant_bot1, participant_bot2])
        """
        Звонок окончен для пользователя А
        """
        call_participant_bot_moderated.check_terminate_reason(terminate_reason=voip.TerminateReason.TR_REFUSED_TO_JOIN)

        """
        Пользователи В и С попадают в звонок, слышат друг друга и модератора
        """
        voip.cross_check_participants(
            calls=[call_participant_bot1, call_participant_bot1, call_creator],
            participants=[participant_bot1, participant_bot2, creator_bot],
            microphone_on=True,
            camera_on=False,
        )

    with allure.step("4 Завершить звонок для каждой стороны"):
        voip.bulk_hang_up([call_creator, call_participant_bot1, call_participant_bot2])
