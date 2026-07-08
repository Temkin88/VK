import logging

from database import ProductFunctionality, TestResult, TestResultProductFunctionality


logger = logging.getLogger(__name__)


def process_cases_by_direction(cases_per_user: int):
    logger.info("[Direction] Calculating assigns by Direction")

    for pf_model in ProductFunctionality.select():
        logger.debug(f"[Direction] Getting testresults for pf: {pf_model.name}")

        for testresult in (
            TestResult.select()
            .join(TestResultProductFunctionality)
            .join(ProductFunctionality)
            .where(ProductFunctionality.id == pf_model.id, TestResult.user.is_null())
        ):
            for user in pf_model.direction.users:
                if user.testresults.count() < cases_per_user:
                    testresult.user = user
                    testresult.reason = "Direction"
                    testresult.save()
                    logger.debug(
                        f"[Direction] Test result ID {testresult.testresult_id} assigned to {testresult.user.email} because of users direction"
                    )
                    break
                else:
                    logger.debug(
                        f"[Direction] User {user.email} exceeded cases limit: {user.testresults.count()} => {cases_per_user}"
                    )
