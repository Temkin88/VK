from loguru import logger

from ...database import User


def stat_user_assigned_testresult_count():
    for user in User.select():
        logger.debug(f"[STAT] {user.email}: {user.testresults.count()}")
