import re
from typing import Optional

import jira.exceptions
from loguru import logger

from imjarvis import imjarvis


ISSUE_REGEXP = r"[A-Za-z]+\-[0-9]+"


def check_defect_name_for_issue_key(name: str) -> Optional[str]:
    """
    Поиск задачи в названии дефекта
    :param name: Название дефекта
    :return: Если найдет - Key задачи в JIRA, иначе - None
    """
    result = re.findall(ISSUE_REGEXP, name)

    if result:
        for possible_issue in result:
            try:
                imjarvis.issue(possible_issue)
                return possible_issue
            except jira.exceptions.JIRAError as error:
                logger.warning(error)
