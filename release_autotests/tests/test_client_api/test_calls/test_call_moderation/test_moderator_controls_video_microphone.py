import allure
import pytest

from support.markers import SANDBOX
from imcommonsupplyclient import voip
from imcommonsupplyclient.voip import Permission


@SANDBOX
@allure.id("477684")
@allure.label("layer", "voip_layer")
@allure.title("Выключение/включение микрофона всем пользователям через управление звонком")
@allure.suite("Regression")
@allure.feature("Модерация звонков")
@pytest.mark.Regression
@pytest.mark.parametrize("participants_count", [3])
def test_mute_microphone_for_all_participant(get_voip_bots, participants_count):
    bots = get_voip_bots(participants_count)
    creator_bot, participant_bot1, participant_bot2 = bots

    with allure.step("1 Сгенерировать ссылку на звонок с любого из клиентов"):
        conference = creator_bot.create_conference(
            "Test conf",
            members={participant_bot1.uin: {"role": "speaker"}, participant_bot2.uin: {"role": "speaker"}},
            roles={
                "speaker": {"permissions": Permission.default()},
                "default": {"permissions": Permission.default()},
            },
        )
        call_link = conference.conferenceUrl

    with allure.step("2 Все пользователи заходят в конференцию с видео, среди них хотя бы 1 модератор."):
        call_creator = creator_bot.make_call_by_link(call_link=call_link, with_video=True)
        call_participant_bot1 = participant_bot1.make_call_by_link(call_link=call_link, with_video=True)
        call_participant_bot2 = participant_bot2.make_call_by_link(call_link=call_link, with_video=True)
        """
        Проверка медии
        """

        voip.cross_check_participants(
            calls=[call_creator, call_participant_bot1, call_participant_bot2],
            participants=bots,
            microphone_on=True,
            camera_on=True,
        )

    with allure.step('3 Модератор отключает микрофоны всем участникам звонка с помощью сайдбара "Управление звонком'):
        creator_bot.update_conference(
            conference.conferenceId,
            name="Test conf",
            members={participant_bot1.uin: {"role": "speaker"}, participant_bot2.uin: {"role": "speaker"}},
            roles={
                "speaker": {"permissions": Permission.default() & ~(Permission.send_audio)},
                "default": {"permissions": Permission.default()},
            },
        )
        """
        Проверка медии
        """
        call_creator.check_participants(
            participants=[participant_bot1, participant_bot2], camera_on=True, microphone_on=False
        )
        call_participant_bot1.check_participants(participants=participant_bot2, camera_on=True, microphone_on=False)
        call_participant_bot1.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)
        call_participant_bot2.check_participants(participants=participant_bot1, camera_on=True, microphone_on=False)
        call_participant_bot2.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)

    with allure.step('4 Модератор включает микрофоны всем участникам звонка с помощью сайдбара "Управление звонком'):
        creator_bot.update_conference(
            conference.conferenceId,
            name="Test conf",
            members={participant_bot1.uin: {"role": "speaker"}, participant_bot2.uin: {"role": "speaker"}},
            roles={
                "speaker": {"permissions": Permission.default()},
                "default": {"permissions": Permission.default()},
            },
        )
    with allure.step("5 Пользователи включают микрофоны"):
        call_creator.moderate_ask_unmute_mic([participant_bot1, participant_bot2])
        call_participant_bot1.unmute_microphone()
        call_participant_bot2.unmute_microphone()
        """
        Проверка медии
        """
        voip.cross_check_participants(
            calls=[call_creator, call_participant_bot1, call_participant_bot2],
            participants=bots,
            microphone_on=True,
            camera_on=True,
        )

    with allure.step("6 Завершить звонок для каждой стороны"):
        voip.bulk_hang_up([call_creator, call_participant_bot1, call_participant_bot2])


@SANDBOX
@allure.id("477687")
@allure.label("layer", "voip_layer")
@allure.title("Выключение/включение видео всем пользователям через управление звонком")
@allure.suite("Regression")
@allure.feature("Модерация звонков")
@pytest.mark.Regression
@pytest.mark.parametrize("participants_count", [3])
def test_mute_video_for_all_participant(get_voip_bots, participants_count):
    bots = get_voip_bots(participants_count)
    creator_bot, participant_bot1, participant_bot2 = bots

    with allure.step("1 Сгенерировать ссылку на звонок с любого из клиентов"):
        conference = creator_bot.create_conference(
            "Test conf",
            members={participant_bot1.uin: {"role": "speaker"}, participant_bot2.uin: {"role": "speaker"}},
            roles={
                "speaker": {"permissions": Permission.default()},
                "default": {"permissions": Permission.default()},
            },
        )
        call_link = conference.conferenceUrl

    with allure.step("2 Все пользователи заходят в конференцию с видео, среди них хотя бы 1 модератор."):
        call_creator = creator_bot.make_call_by_link(call_link=call_link, with_video=True)
        call_participant_bot1 = participant_bot1.make_call_by_link(call_link=call_link, with_video=True)
        call_participant_bot2 = participant_bot2.make_call_by_link(call_link=call_link, with_video=True)
        """
        Проверка медии
        """

        voip.cross_check_participants(
            calls=[call_creator, call_participant_bot1, call_participant_bot2],
            participants=bots,
            microphone_on=True,
            camera_on=True,
        )

    with allure.step('3 Модератор отключает видео всем участникам звонка с помощью сайдбара "Управление звонком'):
        creator_bot.update_conference(
            conference.conferenceId,
            name="Test conf",
            members={participant_bot1.uin: {"role": "speaker"}, participant_bot2.uin: {"role": "speaker"}},
            roles={
                "speaker": {"permissions": Permission.default() & ~(Permission.send_video)},
                "default": {"permissions": Permission.default()},
            },
        )
        """
        Проверка медии
        """
        call_creator.check_participants(
            participants=[participant_bot1, participant_bot2], camera_on=False, microphone_on=True
        )
        call_participant_bot1.check_participants(participants=participant_bot2, camera_on=False, microphone_on=True)
        call_participant_bot1.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)
        call_participant_bot2.check_participants(participants=participant_bot1, camera_on=False, microphone_on=True)
        call_participant_bot2.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)

    with allure.step('4 Модератор включает микрофоны всем участникам звонка с помощью сайдбара "Управление звонком'):
        creator_bot.update_conference(
            conference.conferenceId,
            name="Test conf",
            members={participant_bot1.uin: {"role": "speaker"}, participant_bot2.uin: {"role": "speaker"}},
            roles={
                "speaker": {"permissions": Permission.default()},
                "default": {"permissions": Permission.default()},
            },
        )
    with allure.step("5 Пользователи включают видео"):
        call_creator.moderate_ask_unmute_camera([participant_bot1, participant_bot2])
        call_participant_bot1.unmute_camera()
        call_participant_bot2.unmute_camera()
        """
        Проверка медии
        """
        voip.cross_check_participants(
            calls=[call_creator, call_participant_bot1, call_participant_bot2],
            participants=bots,
            microphone_on=True,
            camera_on=True,
        )

    with allure.step("6 Завершить звонок для каждой стороны"):
        voip.bulk_hang_up([call_creator, call_participant_bot1, call_participant_bot2])


@SANDBOX
@allure.id("477686")
@allure.label("layer", "voip_layer")
@allure.title("Выключение микрофона пользователю по ПКМ")
@allure.suite("Regression")
@allure.feature("Модерация звонков")
@pytest.mark.Regression
@pytest.mark.parametrize("participants_count", [3])
def test_turn_off_microphone_by_one_participant(get_voip_bots, participants_count):
    bots = get_voip_bots(participants_count)
    creator_bot, participant_bot_moderated, participant_bot = bots

    with allure.step("1 Сгенерировать ссылку на звонок с любого из клиентов"):
        call_link = creator_bot.create_conference().conferenceUrl

    with allure.step("2 Все пользователи заходят в конференцию с видео, среди них хотя бы 1 модератор."):
        call_creator = creator_bot.make_call_by_link(call_link=call_link, with_video=True)
        call_participant_bot_moderated = participant_bot_moderated.make_call_by_link(
            call_link=call_link, with_video=True
        )
        call_participant_bot = participant_bot.make_call_by_link(call_link=call_link, with_video=True)
        call_creator.check_participants(participants=bots, microphone_on=True, camera_on=True)

    with allure.step("3 Модератор отключает микрофон пользователю А"):
        call_creator.moderate_mute_microphone(participants=participant_bot_moderated)
        """
        Проверка медии всеми участниками
        """
        call_creator.check_participants(participants=participant_bot, camera_on=True, microphone_on=True)
        call_creator.check_participants(participants=participant_bot_moderated, camera_on=True, microphone_on=False)
        call_participant_bot_moderated.check_participants(
            participants=[participant_bot, creator_bot], camera_on=True, microphone_on=True
        )
        call_participant_bot.check_participants(
            participants=participant_bot_moderated, camera_on=True, microphone_on=False
        )
        call_participant_bot.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)

    with allure.step("4 Пользователь А самостоятельно включает себе микрофон"):
        call_participant_bot_moderated.unmute_microphone()
        """
        Проверка медии всеми участниками
        """
        voip.cross_check_participants(
            calls=[call_creator, call_participant_bot, call_participant_bot_moderated],
            participants=bots,
            microphone_on=True,
            camera_on=True,
        )

    with allure.step("5 Завершить звонок для каждой стороны"):
        voip.bulk_hang_up([call_creator, call_participant_bot_moderated, call_participant_bot])


@SANDBOX
@allure.id("477685")
@allure.label("layer", "voip_layer")
@allure.title("Выключение видео пользователю по ПКМ")
@allure.suite("Regression")
@allure.feature("Модерация звонков")
@pytest.mark.Regression
@pytest.mark.parametrize("participants_count", [3])
def test_turn_off_video_by_one_participant(get_voip_bots, participants_count):
    bots = get_voip_bots(participants_count)
    creator_bot, participant_bot_moderated, participant_bot = bots

    with allure.step("1 Сгенерировать ссылку на звонок с любого из клиентов"):
        call_link = creator_bot.create_conference().conferenceUrl

    with allure.step("2 Все пользователи заходят в конференцию с видео, среди них хотя бы 1 модератор."):
        call_creator = creator_bot.make_call_by_link(call_link=call_link, with_video=True)
        call_participant_bot_moderated = participant_bot_moderated.make_call_by_link(
            call_link=call_link, with_video=True
        )
        call_participant_bot = participant_bot.make_call_by_link(call_link=call_link, with_video=True)
        call_creator.check_participants(participants=bots, microphone_on=True, camera_on=True)

    with allure.step("3 Модератор отключает камеру пользователю А через контекстное меню по ПКМ"):
        call_creator.moderate_mute_camera(participants=participant_bot_moderated)
        """
        Проверка медии всеми участниками
        """
        call_creator.check_participants(participants=participant_bot, camera_on=True, microphone_on=True)
        call_creator.check_participants(participants=participant_bot_moderated, camera_on=False, microphone_on=True)
        call_participant_bot_moderated.check_participants(
            participants=[participant_bot, creator_bot], camera_on=True, microphone_on=True
        )
        call_participant_bot.check_participants(
            participants=participant_bot_moderated, camera_on=False, microphone_on=True
        )
        call_participant_bot.check_participants(participants=creator_bot, camera_on=True, microphone_on=True)

    with allure.step("4 Пользователь А самостоятельно включает себе микрофон"):
        call_participant_bot_moderated.unmute_camera()
        """
        Проверка медии всеми участниками
        """
        voip.cross_check_participants(
            calls=[call_creator, call_participant_bot, call_participant_bot_moderated],
            participants=bots,
            microphone_on=True,
            camera_on=True,
        )

    with allure.step("5 Завершить звонок для каждой стороны"):
        voip.bulk_hang_up([call_creator, call_participant_bot_moderated, call_participant_bot])
