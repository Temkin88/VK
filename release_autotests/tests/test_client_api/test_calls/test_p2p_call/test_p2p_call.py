import allure
import pytest

from support.markers import SANDBOX
from imcommonsupplyclient import voip


@SANDBOX
@pytest.mark.HEALTHCHECK_VOIP
@allure.id("250084")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("P2P-звонки")
@allure.title("p2p звонок Desk + Desk")
def test_p2p_call(get_voip_bots):
    """
    P2P-звонок
    """
    with allure.step("Получение VoIP-ботов"):
        bot_a, bot_b = get_voip_bots(2)

    with allure.step("Позвонить с десктопного на десктопный клиент"):
        bot_a_call = bot_a.make_p2p_call(to=bot_b, with_video=False)
        bot_b_call = bot_b.wait_incoming_call(timeout=5)
        bot_b_call.accept(with_video=False)
        bot_a_call.check_participants(
            participants=bot_b,
            media_connected=True,
            microphone_on=True,
            camera_on=False,
            room_state=voip.RoomState.P2P_ONLY,
        )
        bot_b_call.check_participants(
            participants=bot_a,
            media_connected=True,
            microphone_on=True,
            camera_on=False,
            room_state=voip.RoomState.P2P_ONLY,
        )

    with allure.step("Включить видео с обеих сторон"):
        bot_a_call.unmute_camera()
        bot_b_call.unmute_camera()
        bot_a_call.check_participants(participants=bot_b, media_connected=True, camera_on=True)
        bot_b_call.check_participants(participants=bot_a, media_connected=True, camera_on=True)

    with allure.step("Завершить звонок на одной из сторон"):
        bot_a_call.hang_up()
