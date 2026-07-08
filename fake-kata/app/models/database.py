import traceback

from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise import fields

from uuid import uuid4

from datetime import datetime, timedelta


def datetime_now():

    dt = datetime.now()

    return dt + timedelta(hours=3)


class User(Model):

    id = fields.IntField(pk=True)
    email = fields.TextField()
    x_real_ip = fields.TextField()

    class Meta:
        unique_together=(("email", "x_real_ip"), )


class UserLoader(Model):

    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    file_path = fields.TextField(null=True)


class UserFileInfo(Model):

    node_id = fields.IntField(pk=True)
    type = fields.TextField()
    path = fields.TextField()
    name = fields.TextField()
    hash = fields.TextField()
    size = fields.IntField()
    virus_scan = fields.TextField(default='safe')
    mtime = fields.IntField(default=datetime_now().timestamp())
    rev = fields.IntField(default=1)


UserFileInfo_Pydantic = pydantic_model_creator(
    UserFileInfo, name="UserFileInfo")


class Scan(Model):

    id = fields.IntField(pk=True)
    sensorId = fields.TextField()
    sensorInstanceId = fields.TextField()
    scanId = fields.CharField(unique=True, max_length=150)
    result = fields.TextField(default="processing")


class Error(Model):

    id = fields.IntField(pk=True)
    uuid = fields.CharField(
        default=lambda: str(uuid4()), unique=True, max_length=37)
    exc_msg = fields.TextField()
    traceback = fields.TextField(default=lambda: traceback.format_exc())
    datetime = fields.DatetimeField(default=datetime_now)
