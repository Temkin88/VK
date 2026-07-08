from enum import Enum

import orjson
import os
import platform

from tortoise.models import Model
from tortoise import fields, Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator


class Account(Model):
    id = fields.IntField(pk=True, unique=True)
    group_name = fields.TextField()
    product = fields.TextField(default='icq')
    api_url = fields.TextField(default='https://u.icq.net')
    phone = fields.TextField(null=True)
    code = fields.TextField(null=True)
    uin = fields.TextField(null=True)
    password = fields.TextField(null=True)
    nickname = fields.TextField(null=True)
    available = fields.IntField(default=1)
    count_used = fields.IntField(default=0)
    ts = fields.IntField(null=True)


Account_Pydantic = pydantic_model_creator(
    Account,
    # exclude=('available', 'count_used', 'ts')
)


class Build(Model):
    id = fields.IntField(pk=True)
    build_id = fields.IntField()
    branch = fields.CharField(max_length=200)
    platform = fields.CharField(max_length=15)
    kind = fields.CharField(max_length=15)
    major = fields.IntField()
    minor = fields.IntField()
    patch = fields.IntField()
    buildnumber = fields.IntField()
    full_version = fields.CharField(max_length=20)

    build_urls: fields.ReverseRelation["BuildUrl"]


class BuildUrl(Model):
    id = fields.IntField(pk=True)
    build = fields.ForeignKeyField('models.Build', related_name='build_urls')
    url = fields.TextField()
    file_name = fields.CharField(max_length=100)


Build_Pydantic = pydantic_model_creator(
    Build,
    # exclude=('available', 'count_used', 'ts')
)

BuildUrl_Pydantic = pydantic_model_creator(
    BuildUrl,
    exclude=('id',)
)


class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20, unique=True)
    status = fields.BooleanField(default=True)


Product_Pydantic = pydantic_model_creator(
    Product,
    exclude=('id',)
)


class NightRelease(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=30, unique=True)
    value = fields.JSONField(
        decoder=orjson.loads
    )


class JiraEventTypeEnum(str, Enum):
    JIRA_ISSUE_CREATED = 'jira:issue_created'
    JIRA_ISSUE_UPDATED = 'jira:issue_updated'
    JIRA_ISSUE_DELETED = 'jira:issue_deleted'

    JIRA_WORKLOG_CREATED = 'jira:worklog_created'
    JIRA_WORKLOG_UPDATED = 'jira:worklog_updated'
    JIRA_WORKLOG_DELETED = 'jira:worklog_deleted'

    JIRA_ISSUELINK_CREATED = 'jira:issuelink_created'
    JIRA_ISSUELINK_UPDATED = 'jira:issuelink_updated'
    JIRA_ISSUELINK_DELETED = 'jira:issuelink_deleted'

    JIRA_COMMENT_CREATED = 'jira:comment_created'
    JIRA_COMMENT_UPDATED = 'jira:comment_updated'
    JIRA_COMMENT_DELETED = 'jira:comment_deleted'

    ISSUE_CREATED = 'issue_created'
    ISSUE_UPDATED = 'issue_updated'
    ISSUE_DELETED = 'issue_deleted'

    WORKLOG_CREATED = 'worklog_created'
    WORKLOG_UPDATED = 'worklog_updated'
    WORKLOG_DELETED = 'worklog_deleted'

    ISSUELINK_CREATED = 'issuelink_created'
    ISSUELINK_UPDATED = 'issuelink_updated'
    ISSUELINK_DELETED = 'issuelink_deleted'

    COMMENT_CREATED = 'comment_created'
    COMMENT_UPDATED = 'comment_updated'
    COMMENT_DELETED = 'comment_deleted'


class JiraProjectEnum(str, Enum):
    COMMON = 'COMMON'
    IMSUPPORT = 'IMSUPPORT'
    IMQA = 'IMQA'
    IMOPS = 'IMOPS'
    IMSERVER = 'IMSERVER'
    IMDESKTOP = 'IMDESKTOP'
    IMA = 'IMA'
    IMIOS = 'IMIOS'
    IMWEB = 'IMWEB'
    IMVOIP = 'IMVOIP'
    IMDEVOPS = 'IMDEVOPS'
    TODO = 'TODO'


class JiraJsonData(Model):
    id = fields.IntField(pk=True)
    user_id = fields.TextField(null=True)
    user_key = fields.TextField(null=True)
    project_key = fields.CharEnumField(JiraProjectEnum)
    issue_key = fields.TextField()
    date = fields.DatetimeField()
    event_type = fields.CharEnumField(JiraEventTypeEnum)

    issue = fields.JSONField(decoder=orjson.loads, null=True)
    issue_link = fields.JSONField(decoder=orjson.loads, null=True)
    user = fields.JSONField(decoder=orjson.loads, null=True)
    changelog = fields.JSONField(decoder=orjson.loads, null=True)
    comment = fields.JSONField(decoder=orjson.loads, null=True)

    is_proccessed = fields.BooleanField(default=False)


JiraJsonData_Pydantic = pydantic_model_creator(
    JiraJsonData,
    exclude=('id',)
)


class FailedRequest(Model):
    id = fields.IntField(pk=True)
    url = fields.TextField()
    error_details = fields.JSONField()


class OTP_Token(Model):
    id = fields.IntField(pk=True, unique=True)
    uin = fields.TextField(null=False)
    token = fields.TextField(null=False)


OTP_Token_Pydantic = pydantic_model_creator(
    OTP_Token,
    exclude=('id',)
)


async def init_db():
    await Tortoise.init(
        db_url=os.getenv('TORTOISE_DSN')
        if platform.system() != "Darwin" else "sqlite://db.sqlite",
        modules={'models': ['web.project.db']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()

