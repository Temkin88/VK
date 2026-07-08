import sys

from loguru import logger


logger_format = (
    "<level>{level: <8}</level> - <level>{message}</level>"
)
logger.remove()
logger.add(sys.stdout, format=logger_format)
