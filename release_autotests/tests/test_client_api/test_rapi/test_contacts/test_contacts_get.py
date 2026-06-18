import time

import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("31909")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Контакты")
@allure.feature("Получение списка контактов")
@allure.title("Получить список контактов")
def test_contact_get(
    setup_contact_add,
    auth_account,
    opponent_account,
    fetch_until_empty_answer,
    event_filter,
):
    event_filter.start_point()

    with allure.step("Добавляем в контакты"):
        auth_account.send_basic_message(opponent_account.uin, "pong")

    with allure.step("Проверяем что сообщение отправлено"):
        for _ in range(3):
            fetch_until_empty_answer(opponent_account)
            message_event_text = False

            for event in event_filter(opponent_account.events, "histDlgState"):
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

    with allure.step("Пробуем получить информацию"):
        response = auth_account.rapi_contacts_get()
        results = response["results"]
        assert "contacts" in results
        assert "persons" in results
        # persons сортируется по sn, собираем список всех и ищем в нем

        contacts_sns = [x["sn"] for x in results["contacts"]]

    with allure.step("Проверяем ответ сервера"):
        assert opponent_account.uin in contacts_sns
