import pathlib

import yaml
import peewee as pw

from database.base import BaseModel, db

from database.direction import Direction
from database.product_functionality import ProductFunctionality
from database.team import Team


class User(BaseModel):
    email = pw.TextField()
    teams = pw.ManyToManyField(Team, backref="users")
    product_functionalities = pw.ManyToManyField(ProductFunctionality, backref="users")
    directions = pw.ManyToManyField(Direction, backref="users")

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email


UserTeam = User.teams.get_through_model()
UserProductFunctionality = User.product_functionalities.get_through_model()
UserDirection = User.directions.get_through_model()

db.create_tables(
    [
        Direction,
        ProductFunctionality,
        Team,
        User,
        UserTeam,
        UserProductFunctionality,
        UserDirection,
    ]
)

users_yaml = pathlib.Path().joinpath("config.yaml")

with users_yaml.open() as f:
    users_config = yaml.safe_load(f)


Direction.create(name="Buff")
Team.create(name="Buff")


for ignored_pf in users_config["ignored_product_functionality"]:
    ProductFunctionality.get_or_create(
        name=ignored_pf,
        direction=Direction.get(name="Buff"),
        team=Team.get(name="Buff"),
    )


for user in users_config["users"].keys():
    if user in users_config["ignore"]:
        continue

    user_model, _ = User.get_or_create(email=user)

    for team in users_config["users"][user]["commands"]:
        team_model, _ = Team.get_or_create(name=team)

        try:
            user_model.teams.add(team_model)
        except pw.IntegrityError:
            continue

    for direction in users_config["users"][user]["directions"]:
        direction_model, _ = Direction.get_or_create(name=direction)

        try:
            user_model.directions.add(direction_model)
        except pw.IntegrityError:
            continue

    for functionality in users_config["users"][user]["functionalities"]:
        team_model, _ = Team.get_or_create(
            name=users_config["product_functionality"][functionality]["team"]
        )
        direction_model, _ = Direction.get_or_create(
            name=users_config["product_functionality"][functionality]["direction"]
        )

        functionality_model, _ = ProductFunctionality.get_or_create(
            name=functionality,
            direction=direction_model,
            team=team_model,
        )

        try:
            user_model.product_functionalities.add(functionality_model)
        except pw.IntegrityError:
            continue
