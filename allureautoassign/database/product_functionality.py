import peewee as pw

from database.base import BaseModel
from database.direction import Direction
from database.team import Team


class ProductFunctionality(BaseModel):
    name = pw.TextField()
    direction = pw.ForeignKeyField(Direction, backref="product_functionality")
    team = pw.ForeignKeyField(Team, backref="product_functionality")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
