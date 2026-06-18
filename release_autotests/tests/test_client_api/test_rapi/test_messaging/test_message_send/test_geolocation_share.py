import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS


@allure.id("515251")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки геолокации: отправляем корректную геолокацию c положительными величинами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_geo_sending_with_positive_values(
    chat_type,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки геолокации: отправляем корректную геолокацию c положительными величинами
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    """
    Latitude: -90 <= lat <= 90
    Longitude: -180 <= long <= 180
    """

    with allure.step("Отправляем корректную геолокацию c положительными величинами"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "geo": {
                        "lat": 55.75222,
                        "long": 37.61556,
                    },
                },
            },
        )
        assert response["status"]["code"] == 20000, f"Failed to send geo with positive values in chat ID {chat}"
    send_msg_id = response["results"]["msgId"]

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        assert check_events_list_contains_event_with_msgId(opponent, send_msg_id), "Sended message not found in events"


@allure.id("515252")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки геолокации: отправляем корректную геолокацию c отрициательными величинами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_geo_sending_with_negative_values(
    chat_type,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки геолокации: отправляем корректную геолокацию c отрициательными величинами
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    """
    Latitude: -90 <= lat <= 90
    Longitude: -180 <= long <= 180
    """

    with allure.step("Отправляем корректную геолокацию c отрицательными величинами"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "geo": {
                        "lat": -31.250470394027978,
                        "long": -97.40810027899616,
                    },
                },
            },
        )
        assert response["status"]["code"] == 20000, f"Failed to send geo with negative values in chat ID {chat}"
    send_msg_id = response["results"]["msgId"]

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        assert check_events_list_contains_event_with_msgId(opponent, send_msg_id), "Sended message not found in events"


@allure.id("515250")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала отправки геолокации с экстремальными положительными значениями долготы и широты")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_geo_sending_with_extreme_positive_values(
    chat_type,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка функционала отправки геолокации с экстремальными положительными значениями долготы и широты
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    """
    Latitude: -90 <= lat <= 90
    Longitude: -180 <= long <= 180
    """

    with allure.step("Отправляем корректную геолокацию c максимальными положительными величинами"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "geo": {
                        "lat": 90,
                        "long": 180,
                    },
                },
            },
        )
        assert response["status"]["code"] == 20000, f"Failed to send geo with positive max values in chat ID {chat}"
    send_msg_id = response["results"]["msgId"]

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        assert check_events_list_contains_event_with_msgId(opponent, send_msg_id), "Sended message not found in events"


@allure.id("515254")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала отправки геолокации с экстремальными отрицательными значениями долготы и широты")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_geo_sending_with_extreme_negative_values(
    chat_type,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка функционала отправки геолокации с экстремальными отрицательными значениями долготы и широты
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    """
    Latitude: -90 <= lat <= 90
    Longitude: -180 <= long <= 180
    """

    with allure.step("Отправляем корректную геолокацию c максимальными отрицательными величинами"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "geo": {
                        "lat": -90,
                        "long": -180,
                    },
                },
            },
        )
        assert response["status"]["code"] == 20000, f"Failed to send geo with negative max values in chat ID {chat}"
    send_msg_id = response["results"]["msgId"]

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        assert check_events_list_contains_event_with_msgId(opponent, send_msg_id), "Sended message not found in events"
