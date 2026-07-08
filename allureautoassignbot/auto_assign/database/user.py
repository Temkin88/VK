import pathlib
from typing import Optional

import yaml
import peewee as pw

from .base import BaseModel, db

from .direction import Direction
from .product_functionality import ProductFunctionality
from .team import Team


class User(BaseModel):
    email = pw.TextField()
    teams = pw.ManyToManyField(Team, backref="users")
    product_functionalities = pw.ManyToManyField(ProductFunctionality, backref="users")
    directions = pw.ManyToManyField(Direction, backref="users")
    active = pw.BooleanField(default=True)

    assigned_by_team = pw.IntegerField(default=0)
    assigned_by_pf = pw.IntegerField(default=0)
    assigned_by_direction = pw.IntegerField(default=0)
    assigned_by_left_cases = pw.IntegerField(default=0)

    def __str__(self):
        return f"User(id={self.id}, name={self.email})"

    def __repr__(self):
        return f"User(id={self.id}, name={self.email})"


UserTeam = User.teams.get_through_model()
UserProductFunctionality = User.product_functionalities.get_through_model()
UserDirection = User.directions.get_through_model()


users_yaml = pathlib.Path().joinpath("config.yaml")

with users_yaml.open() as f:
    users_config = yaml.safe_load(f)


def init_db(local_users_config: Optional[dict] = None, ignore_list: list[str] = []):  # noqa
    global users_config

    if local_users_config is None:
        local_users_config = users_config

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

    Direction.create(name="Buff")
    Team.create(name="Buff")
    ProductFunctionality.create(
        name="Buff",
        direction=Direction.get(name="Buff"),
        team=Team.get(name="Buff"),
    )

    for ignored_pf in local_users_config["ignored_product_functionality"]:
        ProductFunctionality.get_or_create(
            name=ignored_pf,
            direction=Direction.get(name="Buff"),
            team=Team.get(name="Buff"),
        )

    for user in local_users_config["users"].keys():
        if user in local_users_config["ignore"] + ignore_list:
            continue

        user_model, _ = User.get_or_create(email=user)

        for team in local_users_config["users"][user]["commands"]:
            team_model, _ = Team.get_or_create(name=team)

            try:
                user_model.teams.add(team_model)
            except pw.IntegrityError:
                continue

        for direction in local_users_config["users"][user]["directions"]:
            direction_model, _ = Direction.get_or_create(name=direction)

            try:
                user_model.directions.add(direction_model)
            except pw.IntegrityError:
                continue

        for functionality in local_users_config["users"][user]["functionalities"]:
            team_model, _ = Team.get_or_create(
                name=local_users_config["product_functionality"][functionality]["team"]
            )
            direction_model, _ = Direction.get_or_create(
                name=local_users_config["product_functionality"][functionality][
                    "direction"
                ]
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
