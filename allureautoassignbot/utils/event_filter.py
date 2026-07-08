import re

from loguru import logger
from pyvkteamsbot.bot.event import Event


class ButtonFilter:
    def __init__(self, button: str):
        self.button = button

    def __call__(self, event: Event) -> bool:
        logger.info(event.callback_query)
        return event.callback_query == self.button


class TextFilter:
    def __init__(self, regexp: str):
        self.regexp = regexp

    def __call__(self, event: Event) -> bool:
        try:
            logger.info(f"Text: {event.text}")
            result = re.findall(self.regexp, event.text)
            logger.debug(f"regexp result: {result}")
            return bool(result)
        except AttributeError:
            return False
