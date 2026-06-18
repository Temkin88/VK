import time
import uuid

import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CONTACTS)]


@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.id("215633")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Чаты")
@allure.feature("Изменение отметки чата")
@allure.title("Отметки чата как непрочитанного")
@pytest.mark.parametrize("chat_type", ["group", "private", "favorite", "channel"])
def test_recently_set_attention_attribute(
    auth_account,
    opponent_account,
    prepare_test_chats,
    fetch_until_empty_answer,
    event_filter,
    chat_type,
):
    """
    Метод для отметки чата как непрочитанного
    :param prepare_test_chats: Фикстура котора создает чаты
    :param event_filter: Фикстура для фильтрации событий по типу
    :param chat_type: Тип созданного чата
    :param fetch_until_empty_answer: Фикстура предназначенная для выборки событий до пустого значения
    """
    event_filter.start_point()
    _, _, group, channel = prepare_test_chats

    if chat_type == "private":
        chat = auth_account.uin
    elif chat_type == "favorite":
        chat = opponent_account.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Пишем сообщение в чат"):
        auth_account.wim_im_sendIM(
            t=chat,
            message=f"Test message - {uuid.uuid4().hex}",
        )

    with allure.step("Помечаем чат как непрочитанный"):
        auth_account.wim_recently_setAttentionAttribute(sn=chat, value=1)

    with allure.step("Ищем событие attention"):
        attention_field = False

        for _ in range(3):
            fetch_until_empty_answer(auth_account)
            for event in event_filter(auth_account.events[::-1], "histDlgState"):
                event_data = event["eventData"]
                if "attention" in event_data:
                    attention_field = True
                    break
            if attention_field:
                break
            else:
                time.sleep(1)

        assert attention_field, "Attention field not found"
