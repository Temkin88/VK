import time

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("67359")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений")
@allure.title("Отправка статуса тайпинга/лукинга")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("typing_status", ["typing", "none"])
@pytest.mark.parametrize("chat_type", ["private", "group"])
def test_set_typing_im(
    prepare_test_chats,
    typing_status,
    chat_type,
    fetch_until_empty_answer_with_filter,
    event_filter,
):
    """
    Проверяем добавление, наличие и удаление реакции к сообщению
    """

    main_acc, opponent, group, channel = prepare_test_chats

    if chat_type == "private":
        chat = opponent.uin
        event_chat = main_acc.uin
    else:
        chat = group
        event_chat = group

    with allure.step("Пытаемся изменить статус тайпинга/лукинга"):
        event_filter.start_point()

        response = main_acc.wim_im_setTyping(
            t=chat,
            typingStatus=typing_status,
        )
        assert response["response"]["statusCode"] == 200, "Response code error"

    with allure.step("Проверяем что пришло событие typing"):
        typing_event_found = False
        for _ in range(3):
            for event in fetch_until_empty_answer_with_filter(opponent, "typing")[::-1]:
                event_data = event["eventData"]

                if event_data["aimId"] == event_chat and event_data["typingStatus"] == typing_status:
                    typing_event_found = True
                    break
            if typing_event_found:
                break
            else:
                time.sleep(1)

        assert typing_event_found, "Event typing not found"
