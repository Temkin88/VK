import inspect
import functools

from loguru import logger
from pydantic import ValidationError

from pyvkteamsbot.bot.bot import Bot
from pyvkteamsbot.bot.event import Event

from utils.model_validator import CustomBaseModel
from utils.context import ChatIdContextVar


def chat_id_context_wrapper():
    def _wrapped(func):
        @functools.wraps(func)
        def __wrapped(bot: Bot, event: Event):
            ChatIdContextVar.set(event.from_chat)
            return func(bot=bot, event=event)

        return __wrapped

    return _wrapped


def model_wrapper():
    def _wrapped(func):
        spec = inspect.getfullargspec(func).annotations
        pydantic_spec = {
            key: value
            for key, value in spec.items()
            if issubclass(value, CustomBaseModel)
        }

        logger.info(f"Computed pydantic_spec: {pydantic_spec}")

        @functools.wraps(func)
        def __wrapped(bot: Bot, event: Event):
            logger.debug(f"event: {event}")
            try:
                computed_kwargs = {
                    key: pydantic_spec[key].base64_validate(event.callback_query)
                    for key, value in pydantic_spec.items()
                }

                return func(bot=bot, event=event, **computed_kwargs)
            except (ValidationError, ValueError) as error:
                logger.warning(
                    f"Skipping call of function '{func.__name__}' because of error: {error}"
                )

        return __wrapped

    return _wrapped
