import peewee
import typing

from project.logger import logger
from project.db.models import IssueStatus, Issue, User, UserProjects, Project

NOT_WORKING_STATUSES = (
    "Closed",
    "Ожидание",
    "Не воспроизводится",
    "Локализация разработчиком",
    "Помощь Support",
    "Закрыт",
    "Готов к разработке",
    "Need info",
    "Запрошена информация",
    "Требуется информация",
    "Решенные",
    "Canceled",
    "Design Review"
)


ASSIGNEBLE_WORKING_STATUSES = (
    'Ready for QA',
    'Тестирование',
    'In progress',
    'Testing',
    'ToDo',
    'Готово к тестированию'
)


def sql_get_working_statuses_from_db() -> typing.Iterable[IssueStatus]:
    """
    Получаем из базы ID рабочих статусов
    """
    return IssueStatus.select(IssueStatus.id).where(
        IssueStatus.value.not_in(NOT_WORKING_STATUSES)
    )


def sql_get_users_for_rating(platforms: str) -> typing.Iterable[User]:
    """
    Получаем список пользователей для рейтинга по указанным проектам
    """
    if platforms == 'ALL':
        platforms = ','.join([project.name for project in Project.select()])

    return User.select(User.id) \
        .join(UserProjects) \
        .join(Project) \
        .where(Project.name.in_([
            platform.strip() for platform in platforms.split(',')
        ]))


def sql_get_users_for_rating_with_uin(platforms: str) -> typing.Iterable[User]:
    """
    Получаем список пользователей для рейтинга по указанным проектам
    """
    if platforms == 'ALL':
        platforms = ','.join([project.name for project in Project.select()])

    return User.select(User.id, User.uin) \
        .join(UserProjects) \
        .join(Project) \
        .where(Project.name.in_([
            platform.strip() for platform in platforms.split(',')
        ]))


def sql_get_users_rating_table_from_db(
        platforms: str) -> typing.Iterable[User]:
    """
    Получаем таблицу рейтинга пользователей из базы
    """
    return User.select(
        User.id,
        User.uin,
        User.jira_name,
        peewee.fn.COALESCE(peewee.fn.SUM(Issue.priority), 0).alias('rating')
    ).join(Issue, 'LEFT JOIN').where(
        User.id.in_(
            sql_get_users_for_rating(platforms)
        ),
        Issue.status.in_(
            sql_get_working_statuses_from_db()) | Issue.status.is_null()
    ).group_by(User.id)


def sql_get_users_issues_from_db(uin: str) -> typing.Iterable[Issue]:

    try:
        return Issue.select(
            Issue.key,
            Issue.status,
            Issue.priority
        ).where(
            Issue.assignee == User.get(User.uin == uin),
            Issue.status.in_(
                sql_get_working_statuses_from_db()
            )
        )
    except Exception as error:
        logger.warning(error)
        return ()


def sql_get_tasks_for_assign() -> typing.Iterable[Issue]:
    """
    Получаем таски, которые нужно заасайнить
    """
    IMSUPPORT_PROJECT_MODEL, _ = Project.get_or_create(
        name='IMSUPPORT'
    )

    return Issue.select().where(
        Issue.project == IMSUPPORT_PROJECT_MODEL,
        Issue.assignee.is_null(),
        Issue.issuetype == 'Incident',
        Issue.status.in_(
            IssueStatus.select().where(
                IssueStatus.value.in_(ASSIGNEBLE_WORKING_STATUSES)
            ))
        )


def sql_get_all_users() -> typing.Iterable[User]:
    for user_model in User.select():
        yield user_model
