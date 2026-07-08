import base64
import json

import httpx
from loguru import logger

from app.core.config import settings

ALERT_MSG_TEMPLATE = """
🔥⚡🔥 Внимание 🔥⚡🔥

По результатам обработки отчетов в проекте <a href=\"{gitlab_url}/{project}\">{project}</a> в <a href=\"{gitlab_url}/{project}/-/pipelines/{pipeline_id}\">pipeline</a>
в карантин улетело {count}

Просьба проверить работоспособность инфраструктуры и разрешить запрос на карантин!
"""


def encode_cmd(text: str) -> str:
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')


@logger.catch(message="Failed to sent alert msg", reraise=False)
async def send_quarantine_alert(
        chat_id: str,
        project: str,
        pipeline_id: int,
        ticket_id: str,
        count: int
) -> None:
    logger.info(f"Sending quarantine alert to {chat_id} about {count} tests => project={project} pipeline_id={pipeline_id} ticket_id={ticket_id}")

    approve_cmd = encode_cmd(
        f"quarantine:approve:{project}:{ticket_id}"
    )

    reject_cmd = encode_cmd(
        f"quarantine:reject:{project}:{ticket_id}"
    )

    inline_keyboard = [
        [
            {
                "text": "Approve",
                "callbackData": approve_cmd,
                "style": "primary",
            },
            {
                "text": "Decline",
                "callbackData": reject_cmd,
                "style": "attention",
            }
        ],
        [
            {
                "text": "Посмотреть в админке",
                "url": f"{settings.host_base_url}/admin/ticket/detail/{ticket_id}"
            }
        ]
    ]

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url="https://api.internal.myteam.mail.ru/bot/v1/messages/sendText",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "token": settings.bot_token,
                "parseMode": "HTML",
                "chatId": chat_id,
                "text": ALERT_MSG_TEMPLATE.format(
                    gitlab_url=settings.gitlab_url,
                    project=project,
                    pipeline_id=pipeline_id,
                    count=count,
                ),
                "inlineKeyboardMarkup": json.dumps(inline_keyboard),
            }
        )

    logger.info(f"Alert for pipeline_id={pipeline_id}  was sent, response: {response.status_code} {response.reason_phrase}")
    logger.debug(f"response text: {response.text}")
