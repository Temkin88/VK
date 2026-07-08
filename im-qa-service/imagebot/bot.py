import asyncio
import os

import aiohttp
import sentry_sdk
from async_icq.bot import AsyncBot
from async_icq.events import Event


sentry_sdk.init(
    "http://a147a3cbf86546fc8680ad931995d8bb@100.99.5.41:8000/3",
    traces_sample_rate=1.0,
)


# Creating bot
imagerbot = AsyncBot(
    token=os.getenv('BOT_TOKEN', '001.2702945158.3738676396:1000000111'),
    url=os.getenv('BOT_API_URL', 'https://api.internal.myteam.mail.ru'),
    log_level='DEBUG'
)


@imagerbot.message_handler()
async def hello(event: Event):
    await event.answer(
        text=f'Hi, {event.from_.userId}'
    )

    await event.log(
        f'Answered to {event.chat.chatId} to {event.from_.userId}')


@imagerbot.callback()
async def callback(event: Event):
    if event.callbackData.startswith('replace'):
        screen_name = event.callbackData.split('|')[-1]
        with open(f'Origins/{screen_name}.png', 'wb') as w_file:
            with open(f'Attention/{screen_name}.png', 'rb') as r_file:
                w_file.write(
                    r_file.read()
                )
        await event.bot.edit_text(
            chatId=event.data['message']['chat']['chatId'],
            msgId=event.data['message']['msgId'],
            text=f'Exchanged image Attention/{screen_name} and Origins/{screen_name}'
        )
    elif event.callbackData.startswith('leave'):
        screen_name = event.callbackData.split('|')[-1]
        os.remove(f'Attention/{screen_name}.png')
        await event.bot.edit_text(
            chatId=event.data['message']['chat']['chatId'],
            msgId=event.data['message']['msgId'],
            text=f'Deleted image Attention/{screen_name}'
        )
    elif event.callbackData.startswith('restart_launch'):
        launch_id = event.callbackData.split('|')[-1]
        async with aiohttp.ClientSession(
            base_url=os.getenv("ALLURE_ENDPOINT"),
            headers={
                'Authorization': f'Api-Token {os.getenv("ALLURE_TOKEN")}'
            }
        ) as client:
            try:
                response = await client.post(
                    url=f'/api/rs/launch/{launch_id}/reopen'
                )
                await event.log(await response.text())
                response.raise_for_status()

                response = await (await client.get(
                    url=f'/api/rs/launch/{launch_id}'
                )).json()

                await event.log(response)

                while response['closed']:
                    await asyncio.sleep(1)
                    response = await (await client.get(
                        url=f'/api/rs/launch/{launch_id}'
                    )).json()
                    await event.log(response)

                response = await client.get(
                    url=f'/api/rs/launch/{launch_id}/job'
                )
                await event.log(await response.text())
                response.raise_for_status()
                response = await response.json()

                for job_run in response:
                    job_run_id = job_run.get('id')

                    response = await client.post(
                        url=f'/api/rs/jobrun/{job_run_id}/rerun',
                        json={
                            'rql': 'status in ["failed", "broken", "unknown"] '
                                   'OR cfv in ["Установка", "Удаление"]'
                        }
                    )
                    await event.log(await response.text())
                    response.raise_for_status()
            except Exception as error:
                await event.log(await response.text())
                await event.answer_callback(await response.text())
                raise error
        await event.answer_callback('Launch restarted for failed/broken tests')

    else:
        await event.answer(f'Unknown query: {event.callbackData}')


imagerbot.start_poll()