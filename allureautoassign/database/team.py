import peewee as pw

from database.base import BaseModel


class Team(BaseModel):
    name = pw.TextField()
