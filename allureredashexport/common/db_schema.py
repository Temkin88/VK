import os
from urllib.parse import urlparse
from datetime import datetime

import peewee
from playhouse.postgres_ext import PostgresqlExtDatabase


postgre_dsn = urlparse(
    os.getenv(
        "POSTGRES_DSN",
        "postgres://postgres:postgres@pgbouncer:5432/postgres",
    )
)

db = PostgresqlExtDatabase(
    database=postgre_dsn.path[1:],
    user=postgre_dsn.username,
    password=postgre_dsn.password,
    host=postgre_dsn.hostname,
    port=postgre_dsn.port,
    application_name=os.getenv("CONTAINER_NAME", "UNKNOWN_CONTAINER"),
)


class BaseModel(peewee.Model):
    class Meta:
        database = db


class TestCaseStatus(BaseModel):
    allure_id = peewee.IntegerField()
    name = peewee.TextField()


class TestCaseWorkFlow(BaseModel):
    allure_id = peewee.IntegerField()
    name = peewee.TextField()


class TestCase(BaseModel):
    allure_id = peewee.IntegerField()
    project_id = peewee.IntegerField()
    automated = peewee.BooleanField(default=False)
    created_by = peewee.TextField()
    created_date = peewee.DateTimeField()
    deleted = peewee.BooleanField(default=False)
    name = peewee.TextField()
    status = peewee.ForeignKeyField(TestCaseStatus, backref='cases')
    workflow = peewee.ForeignKeyField(TestCaseWorkFlow, backref='cases')
    redash_date = peewee.DateField(default=lambda: datetime.now().date())

    class Meta:
        constraints = [peewee.SQL("UNIQUE (project_id, allure_id, redash_date)")]


class TestCaseLink(BaseModel):
    name = peewee.TextField()
    type = peewee.TextField(default='url')
    url = peewee.TextField()
    test_case = peewee.ForeignKeyField(TestCase, backref='links')


class TestCaseTag(BaseModel):
    allure_id = peewee.IntegerField()
    name = peewee.TextField()
    cases = peewee.ManyToManyField(TestCase, backref='tags')


class TestCaseIssue(BaseModel):
    allure_id = peewee.IntegerField()
    name = peewee.TextField()
    url = peewee.TextField()
    closed = peewee.BooleanField(default=False)
    cases = peewee.ManyToManyField(TestCase, backref='issues')


TestCaseIssues = TestCaseIssue.cases.get_through_model()
TestCaseTags = TestCaseTag.cases.get_through_model()


class TestCaseCustomFieldValue(BaseModel):
    allure_id = peewee.IntegerField()
    name = peewee.TextField()
    value = peewee.TextField()
    cases = peewee.ManyToManyField(TestCase, backref='cfv')


TestCaseCfv = TestCaseCustomFieldValue.cases.get_through_model()


tables = [
    TestCase,
    TestCaseLink,
    TestCaseStatus,
    TestCaseTag,
    TestCaseTags,
    TestCaseIssue,
    TestCaseIssues,
    TestCaseWorkFlow,
    TestCaseCustomFieldValue,
    TestCaseCfv
]
