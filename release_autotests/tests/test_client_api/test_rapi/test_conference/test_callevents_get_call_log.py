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
@allure.id("530342")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Получить данные по звонкам, в которых участвовал конкретный пользователь")
@allure.title("Получение данных по звонкам, в которых участвовал конкретный пользователь")
def test_callevents_get_call_log(auth_account):
    """
    Получение данных по звонкам, в которых участвовал конкретный пользователь
    """

    conference_session_id = auth_account.getReqId()
    call_url = auth_account.api_url.replace("u-", "call-", 1)
    session_guid = uuid.uuid4().hex

    auth_account.rapi_callevents_add_events(
        event="conference_started",
        time=int(datetime.now().timestamp() * 1000),
        type="focus",
        conference_url=f"{call_url}/{uuid.uuid4().hex}",
        room_name="Test room name",
        creator_uid=auth_account.uin,
        conference_session_id=conference_session_id,
    )

    auth_account.rapi_callevents_add_events(
        event="participant_joined",
        dir="out",
        instance="qweqwe",
        session_guid=session_guid,
        time=int(datetime.now().timestamp() * 1000),
        type="focus",
        uid=auth_account.uin,
        conference_session_id=conference_session_id,
    )

    auth_account.rapi_callevents_add_events(
        event="participant_leaved",
        hangup_reason="hangup",
        instance="qweqwe",
        session_guid=session_guid,
        time=int(datetime.now().timestamp() * 1000),
        type="focus",
        uid=auth_account.uin,
        conference_session_id=conference_session_id,
    )

    auth_account.rapi_callevents_add_events(
        conference_session_id=conference_session_id,
        event="conference_ended",
        time=int(datetime.now().timestamp() * 1000),
        type="focus",
    )

    with allure.step("Проверяем ответ сервера"):
        response = auth_account.rapi_callevents_get_call_log(
            start=str(int((datetime.now().timestamp() - 60))), end=str(int(datetime.now().timestamp()))
        )
        results = response["results"]

        assert response["status"]["code"] == 20000, "Response error code"
        assert results["count"] > 0, "Zero conference session"
        assert all(sn["uid"] == auth_account.uin for sn in results["results"]), f"{auth_account.uin} not equal"
        assert any(session_id["conferenceSessionId"] == conference_session_id for session_id in results["results"]), (
            f"{conference_session_id} not equal"
        )
        assert any(guid["guid"] == session_guid for guid in results["results"]), f"{session_guid} not equal"
