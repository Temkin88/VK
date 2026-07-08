import requests
from loguru import logger


logger.remove()
logger.add(
    "logs/{time:YYYY-MM-DD}/tasks-check-{time:HH}.log",
    rotation="08:00",
    retention="10 days",
    level="DEBUG",
    format="<green>{time:HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{function: <40}</cyan>:<cyan>{line: <4}</cyan> - <level>{message}</level>",
    colorize=True,
    compression="zip"
)

def vkteams_log_sending(*msg):

    response = requests.get(
        'https://api.internal.myteam.mail.ru/bot/v1/messages/sendText',
        params={
            'token': '001.4004526681.4019241748:1000000649',
            'chatId': 'v.korobov@corp.mail.ru',
            'text': msg
        }
    )

    logger.debug(response.text)

logger.add(
    vkteams_log_sending, level='WARNING')
