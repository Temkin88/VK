import peewee as pw
from loguru import logger

from ...database import TestResult, User


def process_all_lefted_cases():
    logger.info("[Leftovers] Calculating assigns for all lefted cases")

    while TestResult.select().where(TestResult.user.is_null()).count() != 0:
        for user in (
            User.select(
                User.id,
                User.email,
                pw.fn.COUNT(TestResult.testresult_id).alias("testresult_count"),
            )
            .join(TestResult, pw.JOIN.LEFT_OUTER)
            .group_by(User.email)
            .order_by(
                pw.fn.COUNT(TestResult.testresult_id).alias("testresult_count").asc()
            )
        ):
            logger.debug(f"[Leftovers] {user.email}")
            for testresult in TestResult.select().where(TestResult.user.is_null()):
                user = User.get_by_id(user.id)
                logger.debug(
                    f"[Leftovers] Testresult ID {testresult.testresult_id} assigned to {user.email}, count: {user.testresults.count()}"
                )
                testresult.user = user
                testresult.reason = "left after all other reasons"
                testresult.save()

                testresult.user.assigned_by_left_cases += 1
                testresult.user.save()

                break
            break
