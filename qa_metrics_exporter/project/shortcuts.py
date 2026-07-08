from typing import List, Dict, Optional

import numpy as np

from datetime import datetime, timedelta
from jira import Issue

from project.log import logger


def str2obj(string: str) -> datetime:
    """
    Преобразование строки в объект даты
    :param string: дата в виде строки
    :return: дата в виде объекта
    """
    return datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%f%z')


def str3obj(string: str) -> datetime:
    """
    Преобразование строки в объект даты
    :param string: дата в виде строки
    :return: дата в виде объекта
    """
    return datetime.strptime(string, '%Y-%m-%d %H:%M:%S%z')


def get_issue_last_update(issue: Issue) -> Optional[datetime]:
    """
    Получение даты последнего изменения задачи
    :param issue:
    :return:
    """
    if issue.changelog.histories:
        obj = str2obj(issue.changelog.histories[-1].created)
    else:
        obj = str2obj(issue.fields.created)

    logger.debug(f'{issue.key}: get_issue_last_update = {obj}')

    return obj


def recreate_date(date_obj: datetime) -> datetime:
    if date_obj.hour < 9:
        date_obj = datetime(year=date_obj.year, month=date_obj.month,
                            day=date_obj.day,
                            hour=9, minute=0, second=0,
                            tzinfo=date_obj.tzinfo)
    elif date_obj.hour > 20 or (date_obj.hour == 20 and date_obj.minute > 0):
        date_obj = datetime(year=date_obj.year, month=date_obj.month,
                            day=date_obj.day,
                            hour=20, minute=0, second=0,
                            tzinfo=date_obj.tzinfo)
    else:
        pass
    return date_obj


def business_seconds(start: datetime, end: datetime) -> int:
    start = recreate_date(start)
    end = recreate_date(end)

    if start.date() == end.date():
        return end.timestamp() - start.timestamp()
    else:
        central_period_seconds = (end.date() - start.date() - timedelta(
            days=1)).days * 11 * 3600

        start_day_end = datetime(year=start.year, month=start.month,
                                 day=start.day,
                                 hour=20, minute=0, second=0,
                                 tzinfo=start.tzinfo)

        start_day_seconds = start_day_end.timestamp() - start.timestamp()

        end_day_start = datetime(year=end.year, month=end.month, day=end.day,
                                 hour=9, minute=0, second=0,
                                 tzinfo=end.tzinfo)

        end_day_seconds = end.timestamp() - end_day_start.timestamp()

        return int(
            start_day_seconds + central_period_seconds + end_day_seconds)


def periods(
        issue: Issue,
        project: str,
        last_update: Optional[datetime] = None,
        business: bool = False
) -> List[Dict[str, datetime]]:

    statuses = set()

    for change in issue.changelog.histories:
        for item in change.items:
            if item.field == 'status':
                statuses.add(item.toString)
                statuses.add(item.fromString)

    periods_list = []

    for target_status in statuses:

        period = {
            'project': project,
            'status': target_status,
            'business': business
        }

        for change in issue.changelog.histories:

            if last_update and str2obj(change.created) < last_update:
                continue

            for item in change.items:

                if item.field == 'status':
                    if item.toString == target_status:
                        period['start'] = str2obj(change.created)
                        period['author'] = change.author.emailAddress

                    elif item.fromString == target_status:
                        period['end'] = str2obj(change.created)
                elif period.get('start') and not period.get('end'):
                    if issue.raw['fields'].get('assignee'):
                        period['author'] = issue.fields.assignee.emailAddress

            if period.get('start') and period.get('end'):
                if business:
                    period['value'] = \
                        business_seconds(period['start'], period['end'])
                else:
                    period['value'] = \
                        period['end'].timestamp() - period['start'].timestamp()

                periods_list.append(period)

                period = {
                    'project': project,
                    'status': target_status,
                    'business': business
                }

        if period.get('start'):
            period['value'] = None

            periods_list.append(period)

        logger.info(
            f'{issue.key} - {target_status} '
            f'({len(periods_list)}) - {periods_list}')

    return periods_list


def percentile(arr: List[int], percent: int = 100):

    arr = np.array(arr)

    return np.percentile(arr, percent)
