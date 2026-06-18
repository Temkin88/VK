import datetime

import allure

from support.markers import SANDBOX


@allure.id("206057")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Чаты")
@allure.feature("Получение истории")
@allure.title("Получение истории")
@SANDBOX
def test_borrow_history(
    create_chat_id,
    auth_account,
    opponent_account,
):
    data_now = datetime.datetime.now()
    data_delta = data_now + datetime.timedelta(minutes=10)

    with allure.step("Отправляем тестовое сообщение"):
        msg_id = auth_account.send_basic_message(
            sn=create_chat_id,
            text="Test msg for auth_account",
        )

    with allure.step("Добавляемся в чат"):
        chat_info = auth_account.rapi_getChatInfo(sn=create_chat_id)

        opponent_account.rapi_joinChat(
            stamp=chat_info["results"]["stamp"],
        )

    with allure.step("Пробуем получить историю чата"):
        response = auth_account.rapi_borrowHistory(
            sender_sn=opponent_account.uin, sn=create_chat_id, time_range_from=data_now, time_range_to=data_delta
        )
        results = response["results"]["messages"]

        for message in filter(lambda x: x["msgId"] == msg_id, results):
            assert message["chat"]["sender"] == auth_account.uin, f"Sender {auth_account.uin} not dont match"
