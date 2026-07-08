import logging
import typing

import jira
from jira.resources import CustomFieldOption, PropertyHolder

from project.logger import logger
from project.Jira.JiraAccount import jira_account, \
    JIRA_ALL_UNASSIGNED_TASKS_JQL, \
    JIRA_ALL_ASSIGNED_ON_USER_TASKS_JQL, \
    JIRA_PROJECTS_LIST, JIRA_EXPAND_FIELDS, JIRA_JQL_SEARCH_MAX_RESULTS

PLATFORM_FIELDS = {
    'ios': 'IMIOS',
    'android': 'IMA',
    'desktop': 'IMDESKTOP',
    'web': 'IMWEB',
    'server': 'IMSERVER'
}


def get_unassigned_issues() -> typing.Iterable[jira.Issue]:
    """
    Получение списка неназначенных задач
    :return: Итератор по списку задач
    """
    for i in range(4):
        for issue in filter(
            lambda x: x.fields.project.key in JIRA_PROJECTS_LIST,
            jira_account.search_issues(
                jql_str=JIRA_ALL_UNASSIGNED_TASKS_JQL,
                startAt=JIRA_JQL_SEARCH_MAX_RESULTS * i,
                maxResults=JIRA_JQL_SEARCH_MAX_RESULTS,
                fields=JIRA_EXPAND_FIELDS
            )
        ):

            yield issue


def get_all_tasks_by_assignee(
        users: typing.Set[str]) -> typing.Iterable[jira.Issue]:
    """
    Получить все таски пользователей
    :param users: Список пользователей
    :return: Итератор по списку задач
    """
    for i in range(4):
        for issue in filter(
            lambda x: x.fields.project.key in JIRA_PROJECTS_LIST,
            jira_account.search_issues(
                JIRA_ALL_ASSIGNED_ON_USER_TASKS_JQL.format(
                    users=','.join([f'"{user}"' for user in users])),
                startAt=JIRA_JQL_SEARCH_MAX_RESULTS * i,
                maxResults=JIRA_JQL_SEARCH_MAX_RESULTS,
                fields=JIRA_EXPAND_FIELDS
            )
        ):

            yield issue


def map_customfield(value: CustomFieldOption) -> typing.Optional[str]:
    """
    Маппинг списка задействованных проектов
    """
    if value.value.strip().upper() in PLATFORM_FIELDS.values():
        return value.value.strip().upper()

    return PLATFORM_FIELDS.get(value.value.strip().lower())


def map_customfields(values: PropertyHolder) -> typing.Optional[str]:
    """
    Маппинг списка задействованных проектов
    :param values: jira.Issue.fields
    :return: Список задействованных проектов одной строкой
    """

    return ','.join([
        map_customfield(x) for x in values.customfield_18216
    ]) \
        if hasattr(values, 'customfield_18216') \
           and values.customfield_18216 is not None else None


def int_priority(value: str) -> float:

    if value in ['Желательный', 'Незначительный', 'Низкий', 'Самый низкий']:
        return 1.0
    elif value in ['Средний', 'Стандартный']:
        return 2.0
    elif value == 'Высокий':
        return 3.0
    elif value == 'Критический':
        return 4.0
    elif value == 'Блокирующий':
        return 5.0
    else:
        raise ValueError(f'Unknown priority value: {value}')


def map_priority(value: PropertyHolder) -> float:
    """
    Маппинг приоритета задачи в инт
    :param value: Строковое значение приоритета
    :return: Числовое значение приоритета
    """
    priority_int = int_priority(value.priority.name)

    try:
        return priority_int * \
               (value.aggregatetimeestimate / value.aggregatetimeoriginalestimate)
    except Exception as exc:
        if isinstance(exc, AttributeError) \
                or isinstance(exc, TypeError) \
                or isinstance(exc, ZeroDivisionError):
            return priority_int
        else:
            logger.exception(exc)
            raise exc
