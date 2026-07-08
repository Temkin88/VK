import peewee as pw

from .base import BaseModel


class Team(BaseModel):
    name = pw.TextField()

    def __str__(self):
        return f"Team(id={self.id}, name={self.name})"

    def __repr__(self):
        return f"Team(id={self.id}, name={self.name})"
