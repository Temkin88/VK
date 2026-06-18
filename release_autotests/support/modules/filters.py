import typing

from enum import Enum


def filters_enum(uin: str) -> typing.Type[Enum]:
    class TaskFilters(Enum):
        ALL_TASKS: typing.ClassVar = {
            "name": "Все",
            "order": 1,
            "statuses": [
                "new",
                "in_progress",
                "ready",
                "rejected",
            ],
        }
        SELF_ASSIGNED: typing.ClassVar = {
            "name": "На меня",
            "order": 2,
            "assignees": [
                uin,
            ],
            "statuses": [
                "new",
                "in_progress",
                "ready",
                "rejected",
            ],
        }
        FROM_SELF_ASSIGNED: typing.ClassVar = {
            "name": "От меня",
            "order": 3,
            "creators": [
                uin,
            ],
            "statuses": [
                "new",
                "in_progress",
                "ready",
                "rejected",
            ],
        }
        SELF_TASKS: typing.ClassVar = {
            "name": "Задачи себе",
            "order": 4,
            "assignees": [
                uin,
            ],
            "creators": [
                uin,
            ],
            "statuses": [
                "new",
                "in_progress",
                "ready",
                "rejected",
            ],
        }
        CLOSED: typing.ClassVar = {
            "name": "Закрытые",
            "order": 5,
            "statuses": ["closed"],
        }
        TODAY: typing.ClassVar = {
            "name": "Сегодня",
            "order": 6,
            "statuses": [
                "new",
                "in_progress",
                "ready",
                "rejected",
            ],
            "deadline": {
                "type": "predefined",
                "predefined": "today",
            },
        }
        CURRENT_WEEK: typing.ClassVar = {
            "name": "Текущая неделя",
            "order": 7,
            "statuses": [
                "new",
                "in_progress",
                "ready",
                "rejected",
            ],
            "deadline": {
                "type": "predefined",
                "predefined": "thisWeek",
            },
        }
        CURRENT_MONTH: typing.ClassVar = {
            "name": "Текущий месяц",
            "order": 8,
            "statuses": [
                "new",
                "in_progress",
                "ready",
                "rejected",
            ],
            "deadline": {
                "type": "predefined",
                "predefined": "month",
            },
        }

    return TaskFilters
