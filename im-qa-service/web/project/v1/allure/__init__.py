import os

from fastapi import APIRouter, Path, Query

from web.project.v1.allure.dantic import AllureCloseResponseModel
from web.project.v1.allure.tasks import send_report_task
from web.project.logger import logger


allure_router = APIRouter(prefix='/allure', tags=["allure"])


@allure_router.get(
    path='/{launch_id}/close',
    responses={
        200: {
            "description": "Success",
            "model": AllureCloseResponseModel
        }
    }
)
async def launch_stats(
        launch_id: int = Path(..., description='ID лаунча в Allure TestOps'),
        send_to_chat: bool = Query(
            True,
            description="Отправлять ли отчет в чат",
            alias="with_report"
        ),
        with_chart: bool = Query(
            True,
            description="Добавить ли график в репорт в ICQ/VK Teams"
        ),
        chat_id: str = Query(
            os.getenv("JENKINS_CHAT"),
            description='Chat ID для отправки отчета'
        )
):
    """
    Запрос на закрытие лаунча в Allure TestOps и получения отчета в VK Teams
    """
    logger.info("Adding report task")
    task_id = send_report_task.delay(
        launch_id, send_to_chat, with_chart, chat_id).id
    return {
        "success": True,
        "task_id": task_id
    }
