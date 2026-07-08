import peewee
from loguru import logger

from ...database import (
    ProductFunctionality,
    Team,
    TestResult,
    TestResultProductFunctionality,
    User,
)


def process_cases_by_team(cases_per_user: int):
    logger.info("[TEAM] Calculating assigns by team")

    for team_model in Team.select():
        try:
            pf_model = team_model.product_functionality.get()
        except peewee.DoesNotExist:
            pf_model = ProductFunctionality.get(name="Buff")

        logger.debug(f"[TEAM] Getting testresults for pf: {pf_model.name}")

        for testresult in (
            TestResult.select()
            .join(TestResultProductFunctionality)
            .join(ProductFunctionality)
            .where(ProductFunctionality.id == pf_model.id, TestResult.user.is_null())  # noqa
        ):
            for user in pf_model.team.users.order_by(User.assigned_by_team.asc()):
                if user.testresults.count() < cases_per_user:
                    testresult.user = user
                    testresult.reason = "Team"
                    testresult.save()

                    testresult.user.assigned_by_team += 1
                    testresult.user.save()

                    break
                else:
                    logger.debug(
                        f"[TEAM] User {user.email} exceeded cases limit: {user.testresults.count()} => {cases_per_user}"
                    )

            if testresult.user is not None:
                logger.debug(
                    f"[TEAM] Test result ID {testresult.testresult_id} assigned to {testresult.user.email} because of users team"
                )
                continue
