import allure
import pytest

from support.markers import SANDBOX
from imcommonsupplyclient import voip


@SANDBOX
@allure.id("477679")
@allure.label("layer", "voip_layer")
@allure.title("Удаление пользователя из звонка модератором")
@allure.suite("Regression")
@allure.feature("Модерация звонков")
@pytest.mark.Regression
@pytest.mark.parametrize("participants_count", [3])
def test_kick_from_call(get_voip_bots, participants_count):
    bots = get_voip_bots(participants_count)
    creator_bot, participant_bot_moderated, participant_bot = bots

    with allure.step("1 Сгенерировать ссылку на звонок с любого из клиентов"):
        call_link = creator_bot.create_conference().conferenceUrl

    with allure.step("2 Все пользователи заходят в конференцию, включают видео, среди них хотя бы 1 модератор"):
        call_creator = creator_bot.make_call_by_link(call_link=call_link, with_video=True)
        call_participant_bot_moderated = participant_bot_moderated.make_call_by_link(
            call_link=call_link, with_video=True
        )
        call_participant_bot = participant_bot.make_call_by_link(call_link=call_link, with_video=True)
        """
        Проверка медии всеми участниками
        """
        call_creator.check_participants(participants=bots, microphone_on=True, camera_on=True)

    with allure.step("3 Модератор удаляет пользователя из звонка по контекстному меню ПКМ"):
        call_creator.moderate_kick(participants=participant_bot_moderated)
        """
        Звонок окончен для пользователя А
        """
        call_participant_bot_moderated.check_terminate_reason(terminate_reason=voip.TerminateReason.TR_KICKED)
        """
        Проверка медии всеми участниками
        """
        voip.cross_check_participants(
            calls=[call_creator, call_participant_bot], participants=bots, microphone_on=True, camera_on=True
        )

    with allure.step("4 Удаленный участник А заходит обратно в звонок"):
        call_participant_bot_moderated = participant_bot_moderated.make_call_by_link(
            call_link=call_link, with_video=True
        )
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
