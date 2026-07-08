import peewee as pw

from database.base import BaseModel


class Direction(BaseModel):
    name = pw.TextField()
