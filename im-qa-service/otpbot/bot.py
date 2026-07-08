import os

import sentry_sdk
from async_icq.bot import AsyncBot
from async_icq.events import Event

from db import OTP_Token, init_db

sentry_sdk.init(
    "http://a147a3cbf86546fc8680ad931995d8bb@100.99.5.41:8000/3",
    traces_sample_rate=1.0,
)


# Creating bot
otpbot = AsyncBot(
    token=os.getenv('OTP_BOT_TOKEN'),
    url=os.getenv('BOT_API_URL', 'https://api.internal.myteam.mail.ru'),
    log_level='DEBUG'
)

is_db_inited = False


@otpbot.message_handler()
async def otp_receive(event: Event):

    global is_db_inited

    if not is_db_inited:
        try:
            await init_db()
            is_db_inited = True
        except Exception as error:
            await event.log(error)

    await event.log(str(event))

    text_lines = event.text.splitlines()

    await OTP_Token.create(
        uin=text_lines[0].split(' ')[-1],
        token=text_lines[1]
    )


otpbot.start_poll()
