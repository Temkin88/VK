import uuid

import allure

from support.markers import SAAS, ISOLATION
from tests.test_client_api.test_isolation.common import subscribe_thread_if_not_subscribed


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Проверка прочитанности сообщения")
@allure.title("Проверка прочитанности сообщения")
@ISOLATION
@SAAS
def test_thread_check_opponent_isolation(
    prepared_thread_isolation,
    fetch_until_empty_answer_with_filter,
):
    """
    Проверяем изменение порядка тредов
    """

    auth_account, opponent_account, chat, msg_id, thread_id = prepared_thread_isolation

    [subscribe_thread_if_not_subscribed(acc=acc, thread_id=thread_id) for acc in (auth_account, opponent_account)]

    with allure.step("Пишем сообщение в тред"):
        msg_id = opponent_account.send_basic_message(
            sn=thread_id,
            text=f"Test text-{uuid.uuid4().hex}",
        )
    with allure.step("Пытаемся изменить состояние диалога"):
        opponent_account.rapi_setDlgState(
            sn=chat,
            stranger=True,
            exclude=[],
            lastRead=msg_id,
        )

        auth_account.wim_im_setTyping(
            t=chat,
        )

    with allure.step("Ишем событие chatHeadsUpdate"):
        event_found = False
        for _ in range(3):
            for event in fetch_until_empty_answer_with_filter(auth_account, "chatHeadsUpdate"):
                event_data = event["eventData"]
                if chat == event_data["sn"]:
                    event_found = True
                    break
            if event_found:
                break
        assert event_found, "Event chatHeadsUpdate not found"
