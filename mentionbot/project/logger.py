import sys
from datetime import timedelta

import requests
from loguru import logger

from project.constants import TOKEN, API_URL, LOG_FORMAT, LOG_LEVEL


logger.remove()


def vkteams_log_sending(*msg):

    response = requests.get(
        f'{API_URL}messages/sendText',
        params={
            'token': TOKEN,
            'chatId': 'v.korobov@corp.mail.ru',
            'text': msg,
            'parseMode': 'HTML'
        }
    )

    logger.debug(response.text)


logger.add(
    'logs/{time:YYYY-MM-DD}/{time:HH}.log',
    rotation=timedelta(hours=1),
    retention="10 days",
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    colorize=True,
    compression="zip"
)

# logger.add(sys.stdout, format=LOG_FORMAT, level=LOG_LEVEL)

logger.add(
    vkteams_log_sending,
    level='ERROR',
    format=LOG_FORMAT,
    diagnose=False,
    backtrace=False
)

logger._core.extra.setdefault('user_id', 'null')
logger._core.extra.setdefault('chat_id', 'null')
logger._core.extra.setdefault('cmd_text', 'null')
logger._core.extra.setdefault('event_type', 'null')
