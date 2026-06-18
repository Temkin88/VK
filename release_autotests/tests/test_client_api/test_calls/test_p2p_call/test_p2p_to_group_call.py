import allure

from support.markers import SANDBOX
from imcommonsupplyclient import voip


@SANDBOX
@allure.id("250085")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("P2P-звонки")
@allure.feature("Групповой звонок")
@allure.title("p2p Desk -> групповой")
def test_p2p_to_group_call(get_voip_bots):
    """
    P2P-звонок с переходом в групповой звонок через добавление участника
    """
    with allure.step("Получение VoIP-ботов"):
        bot_a, bot_b, bot_c = get_voip_bots(3)

    with allure.step("Позвонить с десктопного на десктопный клиент"):
        bot_a_out_call = bot_a.make_p2p_call(to=bot_b, with_video=False)
        bot_b_in_call = bot_b.wait_call_and_accept(with_video=False)
        voip.cross_check_participants(
            calls=[bot_a_out_call, bot_b_in_call], participants=[bot_a, bot_b], microphone_on=True, camera_on=False
        )

    with allure.step("Включить видео с обеих сторон"):
        voip.bulk_unmute_camera(calls=[bot_a_out_call, bot_b_in_call])
        voip.cross_check_participants(
            calls=[bot_a_out_call, bot_b_in_call], participants=[bot_a, bot_b], camera_on=True
        )

    with allure.step("На стороне любого из участников добавить в звонок еще одного участника"):
        bot_a_out_call.add_participants(bot_c)

    with allure.step("Вновь приглашенный участник отвечает на звонок и включает видео."):
        bot_c_in_call = bot_c.wait_call_and_accept()
        bot_c_in_call.unmute_camera()
        voip.cross_check_participants(
            calls=[bot_a_out_call, bot_b_in_call, bot_c_in_call],
            participants=[bot_a, bot_b, bot_c],
            microphone_on=True,
            camera_on=True,
        )

    with allure.step("Завершить звонок на каждой стороне."):
        voip.bulk_hang_up(calls=[bot_c_in_call, bot_b_in_call, bot_a_out_call])
