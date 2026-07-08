from loguru import logger

from app.bot.bot import qa_bot


logger.info("Starting bot")
qa_bot.start_poll()
