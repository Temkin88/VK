import logging

from database import User

logger = logging.getLogger(__name__)


def stat_user_assigned_testresult_count():
    for user in User.select():
        logger.debug(f"[STAT] {user.email}: {user.testresults.count()}")
