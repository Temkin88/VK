import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("37332")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("События")
@allure.feature("События webapp")
@allure.title("Базовая проверка метода rapi/events/poll")
def test_events_poll(
    fetch_events_till_empty_queue,
    logger,
):
    for account in fetch_events_till_empty_queue:
        with allure.step(f"Проверяем rapi/events/poll у {account}"):
            account.rapi_events_poll(1)
