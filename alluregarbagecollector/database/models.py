"""
Декларативное описание таблиц базы данных
"""

import peewee as pw
import apsw.bestpractice

from playhouse.apsw_ext import APSWDatabase


db = APSWDatabase(
    "./data.db",
    pragmas={
        "journal_mode": "wal",
        "cache_size": -1024 * 64,
        "synchronous": True,
    },
)


apsw.bestpractice.apply(apsw.bestpractice.recommended)


class BaseModel(pw.Model):
    """
    Базовая модель для наследования меты
    """

    class Meta:
        """
        Мета базовой модели
        """

        database = db


class JiraIssue(BaseModel):
    """
    Модель для таблицы JIRA Issues тест кейсов
    """

    jira_id = pw.TextField(unique=True)


class TestCase(BaseModel):
    """
    Модель для таблицы найденных тест кейсов
    """

    project_id = pw.IntegerField()
    test_case_id = pw.IntegerField()
    name = pw.TextField()
    product_functionality = pw.TextField()
    feature = pw.TextField()
    jira = pw.ForeignKeyField(JiraIssue, backref="testcases", null=True)

    class Meta:
        """
        Дополнительные ограничения для таблицы
        """

        constraints = (pw.SQL("UNIQUE (project_id, test_case_id)"),)


JiraIssue.create_table()
TestCase.create_table()
