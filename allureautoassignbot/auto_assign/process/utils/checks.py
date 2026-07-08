from loguru import logger

from ...database import TestResult


def check_if_unassigned_cases_left():
    unassigned_count = TestResult.select().where(TestResult.user.is_null()).count()

    logger.debug(f"[CHECK] Unassigned count: {unassigned_count}")

    try:
        assert not unassigned_count, "Not all cases assigned"
        logger.info("[CHECK] All cases assigned to users")
    except AssertionError as error:
        logger.error(error)
        for testresult in TestResult.select().where(TestResult.user.is_null()):
            logger.info(f"[CHECK] Test result ID {testresult.testresult_id}")

        raise error from error
