import allure
import pytest

from support.markers import SAAS, PRE_SAAS


@allure.id("37345")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("События")
@allure.feature("События webapp")
@allure.title("Базовая проверка метода bos/eventsStream")
@SAAS
@PRE_SAAS
@pytest.mark.skip("IMOPS-7544 Серверные ошибки при использовании eventsStream")
def test_event_stream(
    account_with_event_stream,
):
    with allure.step("Пытаемся сделать запрос"):
        account_with_event_stream.fetch(timeout=300)

    with allure.step("Проверяем что пришли события"):
        assert account_with_event_stream.events, "eventsStream: empty_event_list"

    for event in filter(lambda x: x["type"] == "ackRequired", account_with_event_stream.events):
        assert isinstance(event["eventData"]["ackURL"], str), "ackURL has string type"
        assert event["eventData"]["ackURL"], "field ackURL has in event"
