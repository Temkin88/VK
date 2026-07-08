import peewee as pw

from .base import BaseModel
from .direction import Direction
from .team import Team


class ProductFunctionality(BaseModel):
    name = pw.TextField()
    direction = pw.ForeignKeyField(Direction, backref="product_functionality")
    team = pw.ForeignKeyField(Team, backref="product_functionality")

    def __str__(self):
        return f"ProductFunctionality(id={self.id}, name={self.name})"

    def __repr__(self):
        return f"ProductFunctionality(id={self.id}, name={self.name})"
