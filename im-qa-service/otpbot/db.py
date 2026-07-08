import platform

from tortoise.models import Model
from tortoise import fields, Tortoise


class OTP_Token(Model):
    id = fields.IntField(pk=True, unique=True)
    uin = fields.TextField(null=False)
    token = fields.TextField(null=False)


async def init_db():
    await Tortoise.init(
        db_url='postgres://postgres:postgres@db:5432/postgres'
        if platform.system() != "Darwin" else "sqlite://db.sqlite",
        modules={'models': ['db']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
