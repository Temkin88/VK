"""
Модели для базы подсчета метрик
"""
from peewee import Model, BooleanField
from peewee import SqliteDatabase
from peewee import TextField, DateTimeField, \
    ForeignKeyField, IntegerField, DateField


from datetime import datetime

db = SqliteDatabase('./jira/jira.db', pragmas={
    'foreign_keys': 1,
    'journal_mode': 'WAL',
    'journal_size_limit': 16384,
})


class BaseModel(Model):
    """
    Базовая модель с прописанным подключением к базе
    """
    class Meta:
        """
        Подключение к базе данных
        """
        database = db


class jira_issue(BaseModel):
    """
    Задача из MRG Jira
    """
    name = TextField()
    project = TextField()
    status = TextField(null=True)
    priority = TextField()
    created = DateField()
    last_update = DateTimeField(null=True)


class jira_issue_sprint(BaseModel):
    """
    Указанный спринт для задачи в Jira
    """
    issue = ForeignKeyField(jira_issue, backref='sprint')
    name = TextField()


class period(BaseModel):
    """
    Базовый класс для периодов
    """
    author = TextField()
    start = DateTimeField(default=lambda: datetime.now())
    end = DateTimeField(default=lambda: datetime.now(), null=True)
    value = IntegerField(null=True)
    issue = ForeignKeyField(jira_issue, backref='periods')
    project = TextField()
    status = TextField()
    business = BooleanField()

#
# class calendar_period(period):
#     """
#     Календарные периоды тестирования задачи
#     """
#     issue = ForeignKeyField(jira_issue, backref='calendar_periods')
#     project = TextField()
#
#
# class business_period(period):
#     """
#     Бизнес периоды тестирования задачи
#     """
#     issue = ForeignKeyField(jira_issue, backref='business_periods')
#     project = TextField()
#
#
# class await_calendar_period(period):
#     """
#     Календарные периоды ожидания тестирования задачи
#     """
#     issue = ForeignKeyField(jira_issue, backref='await_calendar_periods')
#     project = TextField()
#
#
# class await_business_period(period):
#     """
#     Бизнес периоды ожидания тестирования задачи
#     """
#     issue = ForeignKeyField(jira_issue, backref='await_business_periods')
#     project = TextField()
