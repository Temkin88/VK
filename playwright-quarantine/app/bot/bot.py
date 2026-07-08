import json

import httpx
from async_icq.bot import AsyncBot
from async_icq.events import Event
from loguru import logger

from app.bot.utils import decode_cmd
from app.core.config import settings



qa_bot = AsyncBot(
  token=settings.bot_token,
  url='https://api.internal.myteam.mail.ru',
)


@qa_bot.callback()
async def process_callback(event: Event):
    logger.info(f"event: {event}")
    cmd = decode_cmd(event.callbackData)
    chat_id = event.data["message"]["chat"]["chatId"]
    msg_id = event.data["message"]["msgId"]
    text = event.data["message"]["text"]
    logger.info(f"cmd: {cmd}")
    if cmd is None:
        await event.answer_callback(f'Unknown command: {event.callbackData}')
        return
    try:
        *_, cmd_type, project_name, ticket_id = cmd.split(":")

        logger.info(f"request => cmd_type: {cmd_type} project_name: {project_name} ticket_id: {ticket_id}")

        async with httpx.AsyncClient(base_url=settings.api_host_base_url) as client:
            if cmd_type == 'approve':

                response = await client.post(
                    url="api/v1/tickets/resolve",
                    json={
                        "project": project_name,
                        "ticket_id": ticket_id,
                        "decision": "active",
                    }
                )

                response.raise_for_status()

                await event.answer_callback(f'Success: approved ticket ID: {ticket_id}')

                await qa_bot.edit_text(
                    chatId=chat_id,
                    msgId=msg_id,  # noqa
                    text=f"✅📝 Запрос ID {ticket_id} решен, тесты отправлены в карантин",
                    inlineKeyboardMarkup=[[
                        {
                            "text": "Посмотреть в админке",
                            "url": f"{settings.host_base_url}/admin/ticket/detail/{ticket_id}"
                        }
                    ]]
                )
            elif cmd_type == 'reject':

                response = await client.post(
                    url="api/v1/tickets/resolve",
                    json={
                        "project": project_name,
                        "ticket_id": ticket_id,
                        "decision": "inactive",
                    }
                )

                response.raise_for_status()

                await event.answer_callback(f'Success: rejected ticket ID: {ticket_id}')

                await qa_bot.edit_text(
                    chatId=chat_id,
                    msgId=msg_id,  # noqa
                    text=f"⛔📝 Запрос ID {ticket_id} решен, карантин отменен",
                    inlineKeyboardMarkup=[[
                        {
                            "text": "Посмотреть в админке",
                            "url": f"{settings.host_base_url}/admin/ticket/detail/{ticket_id}"
                        }
                    ]]
                )

            else:
                raise Exception(f'Unknown command: {cmd_type}')
    except httpx.HTTPError:
        if response.status_code == 409:
            await event.answer_callback(f"Запрос уже разрешен, смотреть ticket ID: {ticket_id}")
            await qa_bot.edit_text(
                chatId=chat_id,
                msgId=msg_id,  # noqa
                text=f"✅📝 Запрос ID {ticket_id} уже решен",
                inlineKeyboardMarkup=[[
                    {
                        "text": "Посмотреть в админке",
                        "url": f"{settings.host_base_url}/admin/ticket/detail/{ticket_id}"
                    }
                ]]
            )
        else:
            raise
    except Exception as exc:
        logger.error(exc)
        await event.answer_callback(f'Error: {exc}')
