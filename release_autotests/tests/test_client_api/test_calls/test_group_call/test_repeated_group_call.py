import allure

from support.markers import SANDBOX
from imcommonsupplyclient import voip


@SANDBOX
@allure.id("250083")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Групповой звонок")
@allure.title("Повторное подключение к звонку из профиля")
def test_repeated_group_call(get_voip_bots):
    """
    Переподключение к групповому звонку через добавление участника

    3 участника с Desktop-клиентом
    """
    with allure.step("Получение VoIP-ботов"):
        bot_a, bot_b, bot_c = get_voip_bots(3)

    with allure.step("Зайти в таб 'Звонки - Начать групповой звонок'. выбрать несколько участников, стартовать звонок"):
        bot_a_call = bot_a.make_group_call([bot_b, bot_c], with_video=True)

    with allure.step("Участники отвечают на звонок с видео"):
        bot_b_call = bot_b.wait_call_and_accept(with_video=True)
        bot_c_call = bot_c.wait_call_and_accept(with_video=True)

        voip.cross_check_participants(
            calls=[bot_a_call, bot_b_call, bot_c_call],
            participants=[bot_a, bot_b, bot_c],
            microphone_on=True,
            camera_on=True,
        )

    with allure.step("Один из участников завершает звонок"):
        bot_b_call.hang_up()

    with allure.step(
        "Участник в звонке добавляет вышедшего из звонка пользователя по кнопке 'Пригласить' в списке участников"
    ):
        bot_c_call.add_participants(bot_b)

    with allure.step("Ответить на звонок, включить камеру, микрофон"):
        bot_b_call = bot_b.wait_call_and_accept(with_video=True)

        voip.cross_check_participants(
            calls=[bot_a_call, bot_b_call, bot_c_call],
            participants=[bot_a, bot_b, bot_c],
            microphone_on=True,
            camera_on=True,
        )

    with allure.step("Завершить звонок для каждой стороны"):
        voip.bulk_hang_up([bot_a_call, bot_b_call, bot_c_call])
