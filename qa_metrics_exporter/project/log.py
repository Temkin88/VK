import logging


logging.basicConfig(
    format='%(levelname)s | %(asctime)s | '
           '%(funcName)s:%(lineno)d | %(message)s',
)

logger = logging.getLogger(__name__)
logger.handlers = []
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
