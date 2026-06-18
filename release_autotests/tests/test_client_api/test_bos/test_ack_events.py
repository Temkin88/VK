from urllib.parse import urlparse

import allure
import pytest
from requests import Session

from pyvkteamsclient.client.base.client import BaseClient

from support.markers import SAAS, PRE_SAAS


@SAAS
@PRE_SAAS
@allure.id("88446")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("События")
@allure.feature("События на старте")
@allure.title("Получение события ackEvents")
@pytest.mark.skip("IMOPS-7544 Серверные ошибки при использовании eventsStream")
def test_bos_ack_events(
    account_with_event_stream,
):
    account = account_with_event_stream
    url = []

    account.send_basic_message(
        sn=account.uin,
        text="Test bot event",
    )

    with allure.step("Проверяем что пришло событие ackRequired от сервера"):
        account.fetch()

        for event in filter(lambda x: x["type"] == "ackRequired", account.events):
            url.append(event["eventData"]["ackURL"])
            assert isinstance(event["eventData"]["ackURL"], str), "ackURL has string type"
            assert event["eventData"]["ackURL"], "field ackURL has in event"

    url_set = set(url)

    with allure.step("Пробуем на клиенте перейти по ссылке от сервера"):
        session = Session()
        client = BaseClient(session=session)

        for url in url_set:
            response = client.request(
                method="GET",
                url=url,
                ignore_check=True,
                stream=True,
            )
            assert response["response"]["status"]["code"] == 200

    with allure.step("Пробуем отправить запрос"):
        for url in url_set:
            url_path = urlparse(url).path
            num = urlparse(url).query.split("&")[1].split("=")[1]
            account.bos_ackEvents(
                path=url_path,
                seqNum=num,
            )
