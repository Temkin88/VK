from loguru import logger

from ...database import (
    ProductFunctionality,
    TestResult,
    TestResultProductFunctionality,
    User,
)


def process_cases_by_pf(cases_per_user: int):
    logger.info("[PF] Calculating assigns by Product Functionality")

    for pf_model in ProductFunctionality.select():
        logger.debug(f"[PF] Getting testresults for pf: {pf_model.name}")

        for testresult in (
            TestResult.select()
            .join(TestResultProductFunctionality)
            .join(ProductFunctionality)
            .where(ProductFunctionality.id == pf_model.id, TestResult.user.is_null())  # noqa
        ):
            for user in pf_model.users.order_by(User.assigned_by_pf.asc()):
                if user.testresults.count() < cases_per_user:
                    testresult.user = user
                    testresult.reason = "Product Functionality"
                    testresult.save()

                    testresult.user.assigned_by_pf += 1
                    testresult.user.save()

                    break
                else:
                    logger.debug(
                        f"[PF] User {user.email} exceeded cases limit: {user.testresults.count()} => {cases_per_user}"
                    )

            if testresult.user is not None:
                logger.debug(
                    f"[PF] Test result ID {testresult.testresult_id} assigned to {testresult.user.email} because of users pf"
                )
                continue
