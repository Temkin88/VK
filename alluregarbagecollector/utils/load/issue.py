"""
Создание задачи в JIRA
"""

from loguru import logger
from datetime import datetime, timedelta

from imjarvis import imjarvis
from utils.imbot import imbot

from enums import PD_RESOURCES
from utils.config import configuration


PLANNED_END_DATE = str((datetime.now() + timedelta(weeks=4)).date())


def create_issue(
    title: str,
    description: str,
    product_functionality,
) -> str:
    """
    Создание задачи в JIRA для актуализации тест кейса/ов
    :param title: Тема
    :param description: Описание
    :param product_functionality: Значение поля Product Functionality
    :return: Номер задачи в JIRA
    """
    issue_fields = {
        "summary": title,
        "description": description,
        "customfield_10051": PLANNED_END_DATE,
        "customfield_78005": [
            {
                "id": PD_RESOURCES[product_functionality],
                "name": product_functionality,
            }
        ],
        **configuration["jira.settings"],
        **configuration["jira.settings.extra"]["test_cases"],
    }

    logger.info("Creating JIRA task")
    logger.debug(
        "Task fields value: "
        + ", ".join([f"{k}={v}" for k, v in issue_fields.items()])
    )

    issue = imjarvis.create_issue(fields=issue_fields)

    logger.info(f"Task created - {issue.key}")

    imjarvis.transition_issue(issue, transition="51")

    logger.debug('Transition to status "To Do" is successful')

    logger.info("Linking chat to task")

    with logger.catch():
        imbot.send_text(
            chat_id=configuration["notify"]["chat_id"],
            text=f"/link {issue.key}",
        )

        logger.info("Command to link chat is successfully sended")

    return issue.key


def create_issue_for_defect(
    title: str,
    description: str,
    product_functionality,
) -> str:
    """
    Создание задачи в JIRA для актуализации тест кейса/ов
    :param title: Тема
    :param description: Описание
    :param product_functionality: Значение поля Product Functionality
    :return: Номер задачи в JIRA
    """
    issue_fields = {
        "summary": title,
        "description": description,
        "customfield_10051": PLANNED_END_DATE,
        "customfield_78005": [
            {
                "id": PD_RESOURCES[product_functionality],
                "name": product_functionality,
            }
        ],
        **configuration["jira.settings"],
        **configuration["jira.settings.extra"]["defects"],
    }

    logger.info("Creating JIRA task")
    logger.debug(
        "Task fields value: "
        + ", ".join([f"{k}={v}" for k, v in issue_fields.items()])
    )

    issue = imjarvis.create_issue(fields=issue_fields)

    logger.info(f"Task created - {issue.key}")

    imjarvis.transition_issue(issue, transition="51")

    logger.debug('Transition to status "To Do" is successful')

    logger.info("Linking chat to task")

    with logger.catch():
        imbot.send_text(
            chat_id=configuration["notify"]["chat_id"],
            text=f"/link {issue.key}",
        )

        logger.info("Command to link chat is successfully sended")

    return issue.key
