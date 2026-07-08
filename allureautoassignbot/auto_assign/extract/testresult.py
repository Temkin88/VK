import openapi_client as allure

from ..database import users_config, Team, Direction, ProductFunctionality, TestResult


def extract_testresults_without_pf(
    testresult_tree_ctlr: allure.TestResultTreeControllerApi,
    launch_id: int,
):
    testresults = testresult_tree_ctlr.get_leafs(launch_id=launch_id, size=5000)

    for testresult in filter(lambda x: x.assignee is None, testresults.content):
        test_result_model, _ = TestResult.get_or_create(testresult_id=testresult.id)


def extract_testresults_with_pf(
    testresult_tree_ctlr: allure.TestResultTreeControllerApi,
    launch_id: int,
    tree_id: int,
):
    root_groups = testresult_tree_ctlr.get_groups(
        launch_id=launch_id, tree_id=tree_id, size=5000
    )

    for func_group in root_groups.content:
        testresults = testresult_tree_ctlr.get_leafs(
            launch_id=launch_id,
            tree_id=tree_id,
            path=[func_group.id],
            size=5000,
        )

        for testresult in filter(lambda x: x.assignee is None, testresults.content):
            team_model, _ = Team.get_or_create(
                name=users_config["product_functionality"]
                .get(func_group.name, {})
                .get("team", "Buff")
            )
            direction_model, _ = Direction.get_or_create(
                name=users_config["product_functionality"]
                .get(func_group.name, {})
                .get("direction", "Buff")
            )

            pf_model, _ = ProductFunctionality.get_or_create(
                name=func_group.name, direction=direction_model, team=team_model
            )

            test_result_model, _ = TestResult.get_or_create(testresult_id=testresult.id)

            test_result_model.product_functionality.add(pf_model)
