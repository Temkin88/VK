import uuid
from datetime import datetime

import allure

from support.markers import VKTI, TARM, PRE_VKTI, PRE_TARM, SANDBOX, SAAS, PRE_SAAS


@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.id("530341")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Добавить новые события статистики/мониторинга")
@allure.title("Добавление нового события статистики/мониторинга")
def test_callevents_add_events(auth_account):
    """
    Добавление нового события статистики/мониторинга
    """
    conference_session_id = auth_account.getReqId()
    call_url = auth_account.api_url.replace("u-", "call-", 1)

    with allure.step("Проверяем добавить событие в конференцию"):
        response = auth_account.rapi_callevents_add_events(
            event="conference_started",
            time=int(datetime.now().timestamp() * 1000),
            type="focus",
            conference_url=f"{call_url}/{uuid.uuid4().hex}",
            room_name="Test room name",
            creator_uid=auth_account.uin,
            conference_session_id=conference_session_id,
        )
        assert response["status"]["code"] == 20000, "Response error code"
