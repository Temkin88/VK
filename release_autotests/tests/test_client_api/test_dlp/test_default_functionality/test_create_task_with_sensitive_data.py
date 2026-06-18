import allure

from datetime import datetime, timedelta
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM


@allure.id("557306")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Задачи")
@allure.title("Создание задачи с чувствительными данными через message/send")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@DLP
def test_create_task_with_sensitive_data(main_acc, opponent_acc):
    """
    Проверка функционала создания задач
    """

    target = opponent_acc.uin

    with allure.step("Отправляем задачу"):
        response = main_acc.rapi_message_send(
            target=target,
            parts={
                "mainPart": {
                    "task": {
                        "title": "block title",
                        "assignee": target,
                        "endTime": int((datetime.now() + timedelta(days=5)).timestamp()),
                        "priority": "medium",
                    }
                }
            },
        )

        assert response["status"]["code"] == 40607, "Response code error"
