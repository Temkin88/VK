import allure
import pytest

from datetime import datetime, timedelta
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from support.cases.tasks import (
    TASK_ASSIGNEE_CASES,
)


@allure.id("557301")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Задачи")
@allure.title("Создание задачи с чувствительными данными через sendIM")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@DLP
@pytest.mark.parametrize("task_assignee", TASK_ASSIGNEE_CASES)
def test_create_task_with_sensitive_data_by_sendIM(task_assignee, main_acc, opponent_acc):
    """
    Создание задачи
    """

    if task_assignee == "me":
        task_assignee = main_acc.uin
    elif task_assignee == "opponent":
        task_assignee = opponent_acc.uin
    else:
        task_assignee = ""

    with allure.step("Отправляем запрос"):
        response = main_acc.wim_im_sendIM(
            t=opponent_acc.uin,
            parts=[
                {
                    "mediaType": "text",
                    "text": "block",
                    "task": {
                        "title": "block",
                        "assignee": task_assignee,
                        "endTime": (datetime.now() + timedelta(days=5)).timestamp(),
                        "creator": main_acc.uin,
                        "status": "new",
                        "priority": "critical",
                    },
                },
            ],
        )

        assert response["response"]["statusCode"] == 603, "Response code error"
