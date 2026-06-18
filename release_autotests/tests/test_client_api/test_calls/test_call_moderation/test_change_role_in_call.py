import allure
import pytest

from support.markers import SANDBOX
from imcommonsupplyclient import voip
from imcommonsupplyclient.voip import Permission


@SANDBOX
@allure.id("477682")
@allure.label("layer", "voip_layer")
@allure.title("Изменение роли участника в обычном звонке")
@allure.suite("Regression")
@allure.feature("Модерация звонков")
@pytest.mark.Regression
@pytest.mark.parametrize("participants_count", [3])
def test_change_role_in_call(get_voip_bots, participants_count):
    bots = get_voip_bots(participants_count)
    creator_bot, participant_bot1, participant_bot2 = bots

    with allure.step("1 Создать ссылку на звонок, зайти создателем"):
        conference = creator_bot.create_conference(
            "Test conf",
            type="equitable",
            pinRequired=True,
            members={participant_bot1.uin: {"role": "speaker"}, participant_bot2.uin: {"role": "speaker"}},
            roles={
                "speaker": {"permissions": Permission.default()},
                "moderator": {"permissions": Permission.all()},
                "default": {"permissions": Permission.default()},
            },
        )
        call_link = conference.conferenceUrl
        call_creator = creator_bot.make_call_by_link(call_link=call_link, with_video=True)

    with allure.step("2 Участники заходят в звонок и включают видео"):
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

    with allure.step("3 Создатель делает одного из участника модератором"):
        creator_bot.update_conference(
            conference.conferenceId,
            name="Test conf",
            members={participant_bot1.uin: {"role": "moderator"}, participant_bot2.uin: {"role": "speaker"}},
        )
    with allure.step("4 Модератор пытается сделать создателя обычным участником"):
        """
        Модератор не может сделать создателя обычным участником
        """
        try:
            participant_bot1.update_conference(
                conference.conferenceId,
                name="Test conf",
                members={creator_bot.uin: {"role": "speaker"}, participant_bot2.uin: {"role": "speaker"}},
            )
            pytest.fail("Executed despite permission")
        except Exception:
            pass

    with allure.step("5 Создатель звонка делает модератора обычным участником"):
        creator_bot.update_conference(
            conference.conferenceId,
            name="Test conf",
            members={participant_bot1.uin: {"role": "speaker"}, participant_bot2.uin: {"role": "speaker"}},
        )

        call_participant_bot1.check_role(role_name="speaker", permissions=Permission.default())

    with allure.step("6 Завершить звонок для каждой стороны"):
        voip.bulk_hang_up([call_creator, call_participant_bot1, call_participant_bot2])
