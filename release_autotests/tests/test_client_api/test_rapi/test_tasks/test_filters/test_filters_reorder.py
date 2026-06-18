import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("27381")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Задачи")
@allure.feature("Фильтры задач")
@allure.label("layer", "api_layer")
@allure.title("Изменение порядка фильтров")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_task_filter_reorder(
    auth_account,
):
    with allure.step("Создаем фильтр"):
        filter_id = auth_account.add_task_filter(
            name="Filter",
            assignees=(auth_account.uin,),
            deadline=None,
        )

    with allure.step("Получаем текущий список фильтров"):
        filters_list = auth_account.tasks_filters_list()["results"]["filters"]

    with allure.step("Получаем позицию нового фильтра в общем списке"):
        filters_list_len = len(filters_list)

        filter_id_number = [x["id"] for x in filters_list].index(filter_id)

    with allure.step("Пытаемся поставить новый фильтр первым"):
        new_filter_position = 0 if filter_id_number else filters_list_len - 1

        auth_account.task_filters_reorder(
            filter_id=filter_id,
            order=new_filter_position,
        )

    with allure.step("Проверяем что порядок фильтров изменился"):
        filters_list = auth_account.tasks_filters_list()["results"]["filters"]

        old_filter_position = [x["id"] for x in filters_list].index(filter_id)

        assert old_filter_position == new_filter_position, (
            f"v{auth_account.api_ver}/tasks/filters/reorder:failed_to_change_filter_position"
        )

    with allure.step("Удаляем фильтр"):
        auth_account.tasks_filters_delete(
            filter_id=filter_id,
        )
