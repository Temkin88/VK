from project.logger import logger
from project.manual_updater import get_unassigned_tasks_from_db, rate_user
from project.Jira.JiraAccount import jira_account


def assign_tasks():
    """
    Пробуем назначить задачи на сотрудников согласно их загруженности
    :return:
    """
    for task in get_unassigned_tasks_from_db():
        rated_user = rate_user(task.platform)

        logger.info(
            f'task: {task.key}, task.status: {task.status.value}, target: {rated_user.uin}, rating: {rated_user.rating}')

        assign_result = jira_account.assign_issue(issue=task.key, assignee=rated_user.jira_name)

        if assign_result:
            task.assignee_id = rated_user.id
            task.save()

            logger.success(f'task {task.key} is assigned to {rated_user.uin}')
        else:
            logger.warning(f'task {task.key} is failed to assign')
