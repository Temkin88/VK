import logging

from database import ProductFunctionality, TestResult, TestResultProductFunctionality

logger = logging.getLogger(__name__)


def process_cases_by_team(cases_per_user: int):
    logger.info("[TEAM] Calculating assigns by team")

    for pf_model in ProductFunctionality.select():
        logger.debug(f"[TEAM] Getting testresults for pf: {pf_model.name}")

        for testresult in (
            TestResult.select()
            .join(TestResultProductFunctionality)
            .join(ProductFunctionality)
            .where(ProductFunctionality.id == pf_model.id, TestResult.user.is_null())
        ):
            for user in pf_model.team.users:
                if user.testresults.count() < cases_per_user:
                    testresult.user = user
                    testresult.reason = "Team"
                    testresult.save()
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
