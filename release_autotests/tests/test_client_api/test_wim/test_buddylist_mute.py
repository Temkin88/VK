import time

import allure

from support.markers import SAAS, PRE_SAAS, VKTI, PRE_VKTI, TARM, PRE_TARM
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CONTACTS)]


@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@allure.id("66468")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Контакты")
@allure.feature("Изменение контакта")
@allure.title("Отключение уведомлений")
def test_buddylist_mute(
    auth_account,
    opponent_account,
    fetch_until_empty_answer_with_filter,
    event_filter,
):
    event_filter.start_point()

    with allure.step("Добавляем в контакты"):
        auth_account.send_basic_message(opponent_account.uin, "pong")

    with allure.step("Проверяем что сообщение отправлено"):
        for _ in range(3):
            message_event_text = False

            for event in fetch_until_empty_answer_with_filter(opponent_account, "histDlgState"):
                messages = event["eventData"]["tail"]["messages"]
                for message in messages:
                    message_text = message.get("text", "")
                    if message_text == "pong":
                        message_event_text = True
                        break
                if message_event_text:
                    break
            if message_event_text:
                break
            else:
                time.sleep(1)

        assert message_event_text, 'Message text "pong" not found'

    def ensure_correct_diff_found() -> None:
        time.sleep(3)
        RETRIES = 5
        for _ in range(RETRIES):
            for event in fetch_until_empty_answer_with_filter(opponent_account, "diff"):
                for data in event["eventData"]:
                    for entry in data["data"]:
                        for buddy in filter(
                            lambda y: auth_account.uin == y["aimId"],
                            entry["buddies"],
                        ):
                            if ("mute" in buddy) == eternal:
                                return

        raise Exception(f"diff event not found for eternal={eternal}")

    # Сначало мьютим, потом размьючиваем.
    for eternal in [True, False]:
        with allure.step(f"Пробуем сделать запрос с eternal={eternal}"):
            response = opponent_account.wim_buddyList_Mute(
                buddy=auth_account.uin,
                eternal=eternal,
            )
            data = response["response"]["data"]

            assert response["response"]["statusCode"] == 200
            assert response["response"]["data"]["result"] == "OK"
            assert opponent_account.uin == data["target"]
            assert auth_account.uin == data["buddy"]

        with allure.step(f"Проверям пришел ли правильный дифф после запроса с eternal={eternal}"):
            ensure_correct_diff_found()
