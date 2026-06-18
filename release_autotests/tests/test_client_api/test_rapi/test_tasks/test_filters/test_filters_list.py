import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26935")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Задачи")
@allure.feature("Фильтры задач")
@allure.label("layer", "api_layer")
@allure.title("Получение списка фильтров задач")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_task_list_filters(
    auth_account,
):
    """
    Получение списка фильтров
    """

    with allure.step("Получение списка фильтров"):
        auth_account.tasks_filters_list()
