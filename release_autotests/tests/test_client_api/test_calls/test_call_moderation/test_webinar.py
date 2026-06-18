import allure
import pytest

from support.markers import SANDBOX
from imcommonsupplyclient import voip
from imcommonsupplyclient.voip import Permission, ConferenceType


@SANDBOX
@allure.id("477678")
@allure.label("layer", "voip_layer")
@allure.title("Обычный звонок становится вебинаром")
@allure.suite("Regression")
@allure.feature("Модерация звонков")
@pytest.mark.Regression
@pytest.mark.parametrize("participants_count", [5])
def test_call_becomes_webinar(get_voip_bots, participants_count):
    bots = get_voip_bots(participants_count)
    creator_bot, participant_bot1, participant_bot2, participant_bot3, participant_bot4 = bots

    with allure.step("1 Создать ссылку на звонок"):
        conference = creator_bot.create_conference(
            "Test conf",
            members={participant_bot1.uin: {"role": "speaker"}, participant_bot2.uin: {"role": "speaker"}},
            roles={
                "speaker": {"permissions": Permission.default()},
                "default": {"permissions": Permission.default()},
            },
            conf_type=ConferenceType.EQUITABLE,
        )
        call_link = conference.conferenceUrl

    with allure.step("2 Зайти по ссылке создателем"):
        call_creator = creator_bot.make_call_by_link(call_link=call_link, with_video=True)

    with allure.step("3 Участники заходят в звонок"):
        call_participant_bot1 = participant_bot1.make_call_by_link(call_link=call_link, with_video=True)
        call_participant_bot2 = participant_bot2.make_call_by_link(call_link=call_link, with_video=True)
        """
        Проверка медии
        """
        voip.cross_check_participants(
            calls=[call_creator, call_participant_bot1, call_participant_bot2],
            participants=[creator_bot, participant_bot1, participant_bot2],
            microphone_on=True,
            camera_on=True,
        )

    with allure.step("4 Включить вебинар"):
        creator_bot.update_conference(
            conference.conferenceId,
            name="Test conf",
            members={participant_bot1.uin: {"role": "listener"}, participant_bot2.uin: {"role": "listener"}},
            roles={
                "listener": {"permissions": Permission.listener()},
                "default": {"permissions": Permission.listener()},
            },
            conf_type=ConferenceType.WEBINAR,
        )
        """
        Проверка медии
        """
        call_creator.check_participants(
            participants=[participant_bot1, participant_bot2], camera_on=False, microphone_on=False
        )
        call_participant_bot1.check_participants(participants=participant_bot2, camera_on=False, microphone_on=False)
        call_participant_bot1.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)
        call_participant_bot2.check_participants(participants=participant_bot1, camera_on=False, microphone_on=False)
        call_participant_bot2.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)

    with allure.step("5 Другие участники заходят в звонок-вебинар"):
        call_participant_bot3 = participant_bot3.make_call_by_link(call_link=call_link)
        call_participant_bot4 = participant_bot4.make_call_by_link(call_link=call_link)
        """
        Проверка медии
        """
        voip.cross_check_participants(
            participants=[participant_bot1, participant_bot2, participant_bot3, participant_bot4],
            calls=[
                call_creator,
                call_participant_bot1,
                call_participant_bot2,
                call_participant_bot3,
                call_participant_bot4,
            ],
            camera_on=False,
            microphone_on=False,
        )
        voip.cross_check_participants(
            participants=creator_bot,
            calls=[call_participant_bot1, call_participant_bot2, call_participant_bot3, call_participant_bot4],
            camera_on=True,
            microphone_on=True,
        )

    with allure.step("6 Завершить звонок для каждой стороны"):
        voip.bulk_hang_up(
            [call_creator, call_participant_bot1, call_participant_bot2, call_participant_bot3, call_participant_bot4]
        )


@SANDBOX
@allure.id("477681")
@allure.label("layer", "voip_layer")
@allure.title("Вход в вебинар")
@allure.suite("Regression")
@allure.feature("Модерация звонков")
@pytest.mark.Regression
@pytest.mark.parametrize("participants_count", [3])
def test_enter_webinar(get_voip_bots, participants_count):
    bots = get_voip_bots(participants_count)
    creator_bot, participant_bot1, participant_bot2 = bots

    with allure.step("1 Создать ссылку на звонок, зайти в звонок создателем и сделать ее вебинаром"):
        call_link = creator_bot.create_conference(
            "Test conf",
            members={participant_bot1.uin: {"role": "listener"}, participant_bot2.uin: {"role": "listener"}},
            roles={
                "listener": {"permissions": Permission.listener()},
                "default": {"permissions": Permission.listener()},
            },
        ).conferenceUrl

    with allure.step("2 Участники заходят в звонок"):
        call_creator = creator_bot.make_call_by_link(call_link=call_link, with_video=True)
        call_participant_bot1 = participant_bot1.make_call_by_link(call_link=call_link)
        call_participant_bot2 = participant_bot2.make_call_by_link(call_link=call_link)
        """
        У каждого из участников не передается в звонок видео и звук.
        Каждый из участников слышит и видит создателя звонка;
        """
        call_creator.check_participants(
            participants=[participant_bot1, participant_bot2], camera_on=False, microphone_on=False
        )
        call_participant_bot1.check_participants(participants=participant_bot2, camera_on=False, microphone_on=False)
        call_participant_bot1.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)
        call_participant_bot2.check_participants(participants=participant_bot1, camera_on=False, microphone_on=False)
        call_participant_bot2.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)

    with allure.step("3 Завершить звонок для каждой стороны"):
        voip.bulk_hang_up([call_creator, call_participant_bot1, call_participant_bot2])


@SANDBOX
@allure.id("477683")
@allure.label("layer", "voip_layer")
@allure.title("Назначение докладчиком в вебинаре")
@allure.suite("Regression")
@allure.feature("Модерация звонков")
@pytest.mark.Regression
@pytest.mark.parametrize("participants_count", [3])
def test_assign_speaker_in_webinar(get_voip_bots, participants_count):
    bots = get_voip_bots(participants_count)
    creator_bot, participant_bot1, participant_bot2 = bots

    with allure.step("1 Создать ссылку на звонок, зайти создателем и сделать ее вебинаром"):
        conference = creator_bot.create_conference(
            "Test conf",
            members={participant_bot1.uin: {"role": "listener"}, participant_bot2.uin: {"role": "listener"}},
            roles={
                "listener": {"permissions": Permission.listener()},
                "default": {"permissions": Permission.listener()},
            },
        )
        call_link = conference.conferenceUrl
        call_creator = creator_bot.make_call_by_link(call_link=call_link, with_video=True)

    with allure.step("2 Участники заходят в звонок"):
        call_participant_bot1 = participant_bot1.make_call_by_link(call_link=call_link)
        call_participant_bot2 = participant_bot2.make_call_by_link(call_link=call_link)
        """
        Проверка медии
        """
        call_creator.check_participants(
            participants=[participant_bot1, participant_bot2], camera_on=False, microphone_on=False
        )
        call_participant_bot1.check_participants(participants=participant_bot2, camera_on=False, microphone_on=False)
        call_participant_bot1.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)
        call_participant_bot2.check_participants(participants=participant_bot1, camera_on=False, microphone_on=False)
        call_participant_bot2.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)

    with allure.step("3 Создатель назначает участника докладчиком"):
        creator_bot.update_conference(
            conference.conferenceId,
            name="Test conf",
            members={participant_bot1.uin: {"role": "speaker"}, participant_bot2.uin: {"role": "listener"}},
            roles={
                "listener": {"permissions": Permission.listener()},
                "speaker": {"permissions": Permission.default()},
                "default": {"permissions": Permission.listener()},
            },
        )

    with allure.step("4 Докладчик включает видео и микрофон"):
        call_participant_bot1.unmute_microphone()
        call_participant_bot1.unmute_camera()
        """
        Проверка медии
        """
        call_creator.check_participants(participants=participant_bot2, camera_on=False, microphone_on=False)
        call_creator.check_participants(participants=participant_bot1, camera_on=True, microphone_on=True)
        call_participant_bot1.check_participants(participants=participant_bot2, camera_on=False, microphone_on=False)
        call_participant_bot1.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)
        call_participant_bot2.check_participants(
            participants=[participant_bot1, creator_bot], camera_on=True, microphone_on=True
        )

    with allure.step("5 Завершить звонок для каждой стороны"):
        voip.bulk_hang_up([call_creator, call_participant_bot1, call_participant_bot2])
