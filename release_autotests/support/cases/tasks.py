import typing

TASK_TITLE_CASES: typing.Iterable[str] = ("new test",)
TASK_DURATION_CASES: typing.Iterable[int] = (32400,)
TASK_STATUS_CASES: typing.Iterable[str] = ("in_progress",)
TASK_TAGS_CASES: typing.Iterable[list[str]] = (
    [],
    ["tag_1", "tag_2"],
)
TASK_ASSIGNEE_CASES: typing.Iterable[typing.Optional[str]] = (
    "me",
    "opponent",
)
TASK_PRIORITY_CASES: typing.Iterable[str] = ("low",)
TASK_LABEL_CASES: typing.Iterable[str] = (
    "none",
    "red",
)
