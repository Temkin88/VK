import asyncio
import sqlite3
from datetime import datetime, timedelta

from aiojira import JIRA
from peewee import fn

from project.data_models import jira_issue, db, period, jira_issue_sprint

from project.config import JIRA_CRED

from project.jql import BASER_JQL

from project.shortcuts import \
    get_issue_last_update, \
    str2obj, str3obj, periods, \
    business_seconds, percentile

from project.log import logger


from prometheus_client import start_http_server, Gauge


metrics_jira = JIRA(**JIRA_CRED)

total_status = Gauge(
    'total_tasks_status', 'count', ['days', 'status', 'priority']
)

project_status = Gauge(
    'project_tasks_status', 'count', ['days', 'project', 'status', 'priority']
)


stats_hours_avg = Gauge(
    'stats_hours_avg', 'hours',
    ['project', 'priority', 'status', 'days', 'hours_type']
)


stats_hours_avg_count_by_author = Gauge(
    'stats_hours_avg_count_by_author', 'hours',
    ['author', 'project', 'priority', 'status', 'days', 'hours_type']
)


stats_hours_percentile_by_status = Gauge(
    'stats_hours_percentile_by_status', 'percents',
    ['project', 'priority', 'status', 'days', 'hours_type', 'percent']
)


stats_task_return_count = Gauge(
    'stats_task_return_count', 'count',
    ['task', 'project', 'priority', 'days']
)


db.create_tables(
    [
        jira_issue,
        period,
        jira_issue_sprint
    ],
    safe=True
)


async def scan_project(JQL: str, project: str):

    issue_list = await metrics_jira.search_issues(
        JQL.format(project=project), expand='changelog', maxResults=2000)

    for issue in issue_list:

        with db.atomic():
            model, exist = jira_issue.get_or_create(
                name=issue.key,
                project=project,
                priority=issue.fields.priority.name,
                created=str2obj(issue.fields.created).date(),
            )

            last_update = get_issue_last_update(issue)

            logger.debug(
                f'{issue.key}: model.last_update = {model.last_update}')

            model_last_update_obj = str3obj(model.last_update) \
                if model.last_update else None

            if not model.last_update or model_last_update_obj < last_update:

                for business in (False, True):
                    for new_period in periods(
                            issue,
                            project,
                            model_last_update_obj,
                            business=business
                    ):
                        try:
                            period.create(issue=model, **new_period)
                        except sqlite3.IntegrityError as error:
                            logger.error(f'{error} - {new_period}')

                model.status = issue.fields.status.name
                model.last_update = last_update
                model.save()

            if jira_issue_sprint.select().where(
                jira_issue_sprint.issue == model
            ).count() != len(issue.fields.fixVersions):
                jira_issue_sprint.delete().where(
                    jira_issue_sprint.issue == model
                )

            for version in issue.fields.fixVersions:
                jira_issue_sprint.get_or_create(
                    issue=model,
                    name=version.name
                )


async def main():

    tasks = [
        scan_project(JQL_EXPRESSION, project) for JQL_EXPRESSION, project in [
            (BASER_JQL, 'IMA'),
            (BASER_JQL, 'IMIOS'),
            (BASER_JQL, 'IMWEB'),
            (BASER_JQL, 'IMDESKTOP'),
            (BASER_JQL, 'IMSERVER')
        ]
    ]

    await asyncio.wait(tasks)


def project_tasks_count(project, priority, status, days_obj, days):

    task_count = jira_issue.select(jira_issue.project).where(
            jira_issue.project == project,
            jira_issue.status == status,
            jira_issue.priority == priority,
            jira_issue.created >= days_obj
        ).count()

    project_status.labels(
        days=days, project=project, status=status, priority=priority
    ).set(
        task_count
    )


def total_tasks_count(priority, status, days_obj, days):

    task_count = jira_issue.select(jira_issue.project).where(
            jira_issue.status == status,
            jira_issue.priority == priority,
            jira_issue.created >= days_obj
        ).count()

    total_status.labels(days=days, status=status, priority=priority).inc(
        task_count
    )


def stats_hours_avg_count(
    project, priority, status, days_obj, days, hours_type
):

    task_periods = period.select(
        period.start,
        period.value
    ).join(
        jira_issue, on=(jira_issue.id == period.issue)
    ).where(
        period.status == status,
        period.business == (hours_type == 'business'),
        period.issue.project == project,
        period.issue.priority == priority,
        period.issue.created >= days_obj
    )

    summary = 0

    if task_periods.count():

        for task_period in task_periods:
            if task_period.value is not None:
                summary += task_period.value
            else:
                if hours_type == 'calendar':
                    summary += \
                        datetime.now().timestamp() \
                        - str3obj(task_period.start).timestamp()
                else:
                    summary += \
                        business_seconds(
                            str3obj(task_period.start), datetime.now())

        stats_hours_avg.labels(
            project=project, priority=priority,
            status=status, days=days,
            hours_type=hours_type
        ).set(int(summary / (task_periods.count())))


def stats_hours_avg_count_by_author_math(
    project, priority, status, days_obj, days, hour_type
):

    for author in period.select(period.author).distinct():

        task_periods = period.select(
            period.start,
            period.value
        ).join(
            jira_issue, on=(jira_issue.id == period.issue)
        ).where(
            period.author == author.author,
            period.status == status,
            period.business == (hour_type == 'business'),
            period.issue.project == project,
            period.issue.priority == priority,
            period.issue.created >= days_obj
        )

        summary = 0

        if task_periods.count():

            logger.info(
                f'[{project}][{priority}][{status}][{hour_type}][{days}] '
                f'{author.author} - {task_periods.count()}')

            for task_period in task_periods:
                if task_period.value is not None:
                    summary += task_period.value
                else:
                    if hour_type == 'calendar':
                        summary += \
                            datetime.now().timestamp() \
                            - str3obj(task_period.start).timestamp()
                    else:
                        summary += \
                            business_seconds(
                                str3obj(task_period.start), datetime.now())

            result = int(summary / (task_periods.count()))

            if result:

                stats_hours_avg_count_by_author.labels(
                    author=author.author,
                    project=project, priority=priority,
                    status=status, days=days,
                    hours_type=hour_type
                ).set(result)


def stats_hours_percent_count(
        project, priority, status, days_obj, days, hours_type, percents):

    task_period_values_list = [
        task_period.value
        for task_period in period.select(
            period.value
        ).join(
            jira_issue, on=(jira_issue.id == period.issue)
        ).where(
            period.status == status,
            period.business == (hours_type == 'business'),
            period.value != None,
            period.issue.project == project,
            period.issue.priority == priority,
            period.issue.created >= days_obj
        )
    ]

    for percent in percents:
        stats_hours_percentile_by_status.labels(
            project=project, priority=priority,
            status=status, days=days,
            hours_type=hours_type,
            percent=f'p{percent}'
        ).set(
            percentile(task_period_values_list, percent)
            if task_period_values_list else 0
        )


def stats_task_return_count_math(
    project, priority, status, days_obj, days):

    tasks = jira_issue.select(
        jira_issue.name, fn.COUNT(period).alias('count')
    ).join(
        period
    ).where(
        jira_issue.project == project,
        jira_issue.priority == priority,
        period.status == status,
        jira_issue.created >= days_obj,
        period.business == True,
    ).group_by(
        jira_issue.name
    )

    for task in tasks:

        if task.count:
            stats_task_return_count.labels(
                task=task.name, project=project, priority=priority, days=days,
            ).set(
                task.count - 1
            )


loop = asyncio.new_event_loop()

start_http_server(80)

math_periods = (7, 30, 90)


percents = [50, 80, 95]

while True:
    try:

        # statuses = {
        #     status.status for status in
        #     jira_issue.select(jira_issue.status).distinct()
        # }

        statuses = {
            'Ready for test', 'Testing', 'Тестирование'
        }

        priorities = {
            priority.priority for priority in
            jira_issue.select(jira_issue.priority).distinct()
        }

        projects = {
            project.project for project in
            jira_issue.select(jira_issue.project).distinct()
        }

        for days in math_periods:

            days_obj = datetime.now().date() - timedelta(days=days)

            for project in projects:
                for priority in priorities:
                    for status in statuses:

                        project_tasks_count(
                            project, priority, status, days_obj, days)

                        total_tasks_count(
                            priority, status, days_obj, days)

                    # for status in statuses:
                        for hour_type in ('calendar', 'business'):
                            stats_hours_avg_count(
                                project, priority,
                                status, days_obj, days, hour_type
                            )
                            stats_hours_avg_count_by_author_math(
                                project=project,
                                priority=priority,
                                status=status,
                                days_obj=days_obj,
                                days=days,
                                hour_type=hour_type
                            )
                            stats_hours_percent_count(
                                project=project,
                                priority=priority,
                                status=status,
                                days_obj=days_obj,
                                days=days,
                                hours_type=hour_type,
                                percents=percents
                            )
                    stats_task_return_count_math(
                        project=project,
                        priority=priority,
                        status='Ready for test',
                        days_obj=days_obj,
                        days=days
                    )

        loop.run_until_complete(main())

    except Exception as error:
        logger.exception(error)
