import typing

import peewee
from project.logger import logger

from typing import Iterable

from project.db.models import assignees, Project, Issue, IssueStatus, User
from project.Jira.JiraAccount import jira_account, JIRA_JQL_SEARCH_MAX_RESULTS
from project.Jira.JiraPipeline import get_all_tasks_by_assignee, \
    get_unassigned_issues, map_customfields, map_priority, JIRA_EXPAND_FIELDS
from project.db.sql_functions import sql_get_users_rating_table_from_db, \
    sql_get_tasks_for_assign, sql_get_all_users


def get_jql_for_tasks_update_in_db() -> str:
    """
    Получаем JQL выражение для получения по API инфы о всех тасках,
    уже сохраненных в DB
    :return: JQL-выражение
    """

    JIRA_ISSUE_LIST = [x.key for x in Issue.select(Issue.key)]

    JIRA_ISSUE_LIST_LEN = len(JIRA_ISSUE_LIST)

    for i in range(int((JIRA_ISSUE_LIST_LEN / 40)) + 1):

        yield 'key in ({keys}) ORDER BY updated DESC, priority DESC'.format(
            keys=','.join(JIRA_ISSUE_LIST[40 * i: 40 * (i + 1)]))


def update_tasks_in_db():
    """
    Обновляем инфу о всех тасках в базе
    """
    logger.info('Updating tasks from DB')

    for JQL in get_jql_for_tasks_update_in_db():

        if JQL.startswith('key in ()'):
            return

        for issue in jira_account.search_issues(
            jql_str=JQL,
            fields=JIRA_EXPAND_FIELDS,
            startAt=JIRA_JQL_SEARCH_MAX_RESULTS,
            maxResults=JIRA_JQL_SEARCH_MAX_RESULTS,
        ):
            with logger.catch():
                logger.debug(f'Updating task: {issue.key}')

                issue_model = Issue.get(Issue.key == issue.key)

                issue_status_model, _ = IssueStatus.get_or_create(
                    value=issue.fields.status.name
                )

                issue_model.issuetype = issue.fields.issuetype.name.strip()
                issue_model.status = issue_status_model
                issue_model.priority = map_priority(issue.fields)
                if issue.fields.assignee is not None and issue.fields.assignee.active:
                    try:
                        user_model, _ = User.get_or_create(
                            uin=issue.fields.assignee.emailAddress,
                            jira_name=issue.fields.assignee.name
                        )
                    except peewee.IntegrityError:
                        user_model = User.get(
                            User.uin == issue.fields.assignee.emailAddress
                        )
                    issue_model.assignee = user_model
                else:
                    issue_model.assignee = None
                issue_model.platform = map_customfields(issue.fields)
                issue_model.save()
    logger.success('Done - Updating tasks from DB')


def save_assigned_tasks_to_db():
    """
    Сохраняем все уже назначенные таски в целевых проектах в базу данных
    """
    for issue in get_all_tasks_by_assignee(assignees):
        with logger.catch():
            if Issue.select(Issue.key).where(
                    Issue.key == issue.key).exists():
                continue

            logger.info(
                f'Task: {issue.key}, status: {issue.fields.status.name}')

            issue_status_model, _ = IssueStatus.get_or_create(
                value=issue.fields.status.name
            )

            project_model, _ = Project.get_or_create(
                name=issue.fields.project.key
            )
            try:
                assignee_model, _ = User.get_or_create(
                    uin=issue.fields.assignee.emailAddress,
                    jira_name=issue.fields.assignee.name
                )
            except peewee.IntegrityError:
                assignee_model = User.get(
                    User.uin == issue.fields.assignee.emailAddress
                )

            try:
                issue_model, _ = Issue.get_or_create(
                    project=project_model,
                    key=issue.key,
                    issuetype=issue.fields.issuetype.name.strip(),
                    priority=map_priority(issue.fields),
                    status=issue_status_model,
                    assignee=assignee_model,
                    platform=map_customfields(issue.fields)
                )
            except peewee.IntegrityError:
                logger.warning('Task already exist')
                continue


def save_unassigned_tasks_to_db():
    """
    Сохраняем все не назначенные таски в целевых проектах в базу данных
    """
    logger.info('Getting unassigned IMSUPPORT tasks')
    for issue in get_unassigned_issues():
        if Issue.select(Issue.key).where(
                Issue.key == issue.key).exists():
            continue
        with logger.catch():
            logger.info(
                f'Task: {issue.key}, status: {issue.fields.status.name}')

            issue_status_model, _ = IssueStatus.get_or_create(
                value=issue.fields.status.name
            )

            project_model, _ = Project.get_or_create(
                name=issue.fields.project.key
            )
            try:
                issue_model, _ = Issue.get_or_create(
                    project=project_model,
                    key=issue.key,
                    issuetype=issue.fields.issuetype.name.strip(),
                    priority=map_priority(issue.fields),
                    status=issue_status_model,
                    assignee=None,
                    platform=map_customfields(issue.fields)
                )
            except peewee.IntegrityError:
                logger.warning('Task already exist')
                continue
    logger.success('Done - Getting unassigned IMSUPPORT tasks')


def rate_user(project_names: typing.Optional[str]) -> User:
    """
    Получаем пользователя с наименьшей загруженностью

    Если список проектов пуст - вернется t.kosterina@corp.mail.ru
    :param project_names: список задействованных проектов
    :return: Пользователь с наименьшей загруженностью
    """
    if project_names is None:
        logger.warning('Cant assign task, caused by empty platforms field')
        return User.get(User.uin == 't.kosterina@corp.mail.ru')

    targets = sql_get_users_rating_table_from_db(project_names)

    logger.debug(f'Rating result: {targets}')

    target_with_min_rate = min(targets, key=lambda x: x.rating)

    logger.debug(f'Target with min rating: {target_with_min_rate.uin}')

    return target_with_min_rate


def get_unassigned_tasks_from_db() -> Iterable[Issue]:
    """
    Получаем список не назначенных тасков из базы данных
    :return: Итератор по списку тасок
    """
    logger.info('Getting unassigned tasks aimed to assign')

    for issue_model in sql_get_tasks_for_assign():
        logger.info(
            f'Task: {issue_model.key}, '
            f'assignee: {issue_model.assignee}, '
            f'platform: {issue_model.platform}'
        )

        yield issue_model
    logger.success('Done - Getting unassigned tasks aimed to assign')


def check_all_users_are_active():

    for user_model in sql_get_all_users():

        jira_user = jira_account.user(user_model.jira_name)
        if not jira_user.active:
            user_model.delete()
