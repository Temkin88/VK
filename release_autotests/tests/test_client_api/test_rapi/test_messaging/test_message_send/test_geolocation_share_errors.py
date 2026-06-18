import allure
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
)

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS


@allure.id("515256")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка отправки геолокации c неправильной широтой")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_geo_sending_invalid_latitude(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Попытка отправки геолокации c неправильной широтой
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

    with allure.step("Попытка отправки геолокации с некорректной широтой"), pytest.raises(BadRequestException):
        main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "geo": {
                        "lat": -100,
                        "long": 19,
                    },
                },
            },
        )


@allure.id("515255")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка отправки геолокации c неправильной долготой")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_geo_sending_invalid_longitude(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Попытка отправки геолокации c неправильной долготой
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

    with allure.step("Попытка отправки геолокации с некорректной долготой"), pytest.raises(BadRequestException):
        main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "geo": {
                        "lat": 10,
                        "long": 197,
                    },
                },
            },
        )
