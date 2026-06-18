import allure

from support.markers import SAAS, ISOLATION
from imcommonsupplyclient import voip


@ISOLATION
@SAAS
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Конференция")
@allure.title("Повторное подключение к звонку по ссылке")
def test_repeated_link_call_isolation(get_voip_bots_isolation):
    """
    Переподключение к звонку по ссылке с уже подключенными участниками

    3 участник с Desktop-клиентом
    """

    with allure.step("Получение VoIP-ботов"):
        bot_a, bot_b, _ = get_voip_bots_isolation(1)

    with allure.step("Сгенерировать ссылку на звонок с любого из клиентов"):
        call_link = bot_a.create_conference().conferenceUrl

    with allure.step("Зайти в звонок по ссылке"):
        bot_a_call = bot_a.make_call_by_link(call_link=call_link, with_video=False)
        bot_b_call = bot_b.make_call_by_link(call_link=call_link, with_video=False)

        voip.cross_check_participants(
            calls=[bot_a_call, bot_b_call], participants=[bot_a, bot_b], microphone_on=True, camera_on=False
        )

    with allure.step("Все участники включают видео"):
        voip.bulk_unmute_camera([bot_a_call, bot_b_call])
        voip.cross_check_participants(
            calls=[bot_a_call, bot_b_call], participants=[bot_a, bot_b], microphone_on=True, camera_on=True
        )

    with allure.step("Один из участников завершает звонок"):
        bot_a_call.hang_up()

    with allure.step("Повторно зайти в этот же звонок по ссылке, включить видео"):
        bot_a_call = bot_a.make_call_by_link(call_link=call_link, with_video=False)
        bot_a_call.unmute_camera()
        voip.cross_check_participants(
            calls=[bot_a_call, bot_b_call], participants=[bot_a, bot_b], microphone_on=True, camera_on=True
        )

    with allure.step("Завершить звонок для каждой стороны"):
        voip.bulk_hang_up([bot_a_call, bot_b_call])


@ISOLATION
@SAAS
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Конференция")
@allure.title("Повторное подключение к звонку по ссылке пользователем не в тенанте")
def test_repeated_link_call_isolation_not_in_tenant(get_voip_bots_isolation):
    """
    Переподключение к звонку по ссылке с уже подключенными участниками

    3 участник с Desktop-клиентом
    """

    with allure.step("Получение VoIP-ботов"):
        bot_a, _, bot_c = get_voip_bots_isolation(1)

    with allure.step("Сгенерировать ссылку на звонок с любого из клиентов"):
        call_link = bot_a.create_conference().conferenceUrl

    with allure.step("Зайти в звонок по ссылке"):
        bot_a_call = bot_a.make_call_by_link(call_link=call_link, with_video=False)
        bot_c_call = bot_c.make_call_by_link(call_link=call_link, with_video=False)

        voip.cross_check_participants(
            calls=[bot_a_call, bot_c_call], participants=[bot_a, bot_c], microphone_on=True, camera_on=False
        )

    with allure.step("Все участники включают видео"):
        voip.bulk_unmute_camera([bot_a_call, bot_c_call])
        voip.cross_check_participants(
            calls=[bot_a_call, bot_c_call], participants=[bot_a, bot_c], microphone_on=True, camera_on=True
        )

    with allure.step("Один из участников завершает звонок"):
        bot_a_call.hang_up()

    with allure.step("Повторно зайти в этот же звонок по ссылке, включить видео"):
        bot_a_call = bot_a.make_call_by_link(call_link=call_link, with_video=False)
        bot_a_call.unmute_camera()
        voip.cross_check_participants(
            calls=[bot_a_call, bot_c_call], participants=[bot_a, bot_c], microphone_on=True, camera_on=True
        )

    with allure.step("Завершить звонок для каждой стороны"):
        voip.bulk_hang_up([bot_a_call, bot_c_call])
