import hashlib
import json
import os.path

import peewee

from project.logger import logger
from project.Jira.JiraAccount import jira_account

db = peewee.SqliteDatabase('data.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64}
)


class BaseModel(peewee.Model):
    """
    Базовая модель для peewee
    """
    class Meta:
        """
        Мета-класс для связи базой данных
        """
        database = db


class User(BaseModel):
    """
    Модель пользователя в Jira
    """
    uin: str = peewee.TextField(unique=True)
    jira_name: str = peewee.TextField(unique=True)


class Project(BaseModel):
    """
    Модель проекта в Jira
    """
    name: str = peewee.TextField(default='IMSUPPORT', unique=True)
    users = peewee.ManyToManyField(User, backref='projects')


UserProjects = Project.users.get_through_model()


class IssueStatus(BaseModel):
    """
    Модель статуса в Jira
    """
    value: str = peewee.TextField(unique=True)


class Issue(BaseModel):
    """
    Модель задачи в Jira
    """
    project: Project = peewee.ForeignKeyField(Project, backref='project')
    priority: str = peewee.FloatField()
    issuetype: str = peewee.TextField()
    key: str = peewee.TextField(unique=True)
    status: IssueStatus = peewee.ForeignKeyField(
        IssueStatus, backref='statuses')
    assignee: User = peewee.ForeignKeyField(User, backref='user', null=True)
    platform: str = peewee.TextField(null=True)


with open('state.json', 'rb') as f:
    state = json.load(f)

with open('users.json', 'rb') as f:
    users = json.load(f)

assignees = set()


def reinit_user_project_relations():
    for key in users.keys():
        logger.debug(f'Project: {key}')
        project_model, _ = Project.get_or_create(
            name=key
        )

        for uin in users[key]:
            logger.debug(f'User: {uin}')
            try:
                assignees.add(uin)

                jira_user = jira_account.search_users(uin)[::-1][-1]

                user_model, _ = User.get_or_create(
                    uin=uin,
                    jira_name=jira_user.name
                )
                project_model.users.add(user_model)
            except peewee.IntegrityError:
                pass
            except IndexError:
                User.delete().where(User.uin == uin)
            logger.success(f'Done - User: {uin}')
        logger.success(f'Done - Project: {key}')
    logger.success('Done - Creating projects and users in database')


if not state['inited']:

    logger.info('Initializing database')
    db.create_tables((Project, IssueStatus, User, UserProjects, Issue))
    logger.success('Done - Initializing database')

    logger.info('Creating projects and users in database')
    Project.get_or_create(
        name='IMSUPPORT'
    )

    reinit_user_project_relations()

    state['inited'] = True
    state['hash'] = hashlib.md5(json.dumps(users).encode()).hexdigest()
    with open('state.json', 'w') as f:
        json.dump(state, f, indent=2)

else:

    users_hash = state.get('hash')
    logger.debug(f'Users hash from state: {users_hash}')

    current_users_hash = hashlib.md5(json.dumps(users).encode()).hexdigest()
    logger.debug(f'Users hash from users: {current_users_hash}')

    if users_hash is None or users_hash != current_users_hash:
        logger.debug('Reinitializing user-project relations')
        for project in Project.select():
            project.users.remove(User.select())

        for user in User.select():
            user.projects.remove(Project.select())

        reinit_user_project_relations()

        state['hash'] = current_users_hash
        with open('state.json', 'w') as f:
            json.dump(state, f, indent=2)
    else:
        logger.debug('Getting full assignees set')
        for key in users.keys():
            for uin in users[key]:
                assignees.add(uin)
        logger.success('Done - Getting full assignees set')
