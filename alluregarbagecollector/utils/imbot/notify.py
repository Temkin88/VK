"""
Отправка уведомлений о задаче в JIRA в VK Teams через Bot API
"""

import datetime

from loguru import logger

from utils.config import configuration
from utils.imbot import imbot


description_template = """
Task: <a href=\"https://jira.vk.team/browse/{jira_key}\">{jira_key}</a>
Priority: Стандартный
Epic Link: <a href=\"https://jira.vk.team/browse/IMQA-3877\">IMQA-3877</a>
Summary: [ {feature} ] Кейсы на актуализацию (Неделя:{week_number})
Product Functionality: {product_functionality}
Planned End: {planned_end}
""".strip()


@logger.catch(reraise=False)
def send_notification(
    jira_key: str,
    product_functionality: str,
    feature: str,
    week_number: int,
    planned_end: str | datetime.date | datetime.datetime,
):
    """
    Отправка уведомлений о задаче в JIRA в VK Teams через Bot API
    :param jira_key:
    :param product_functionality:
    :param feature:
    :param week_number:
    :param planned_end:
    :return:
    """
    logger.info(f"Sending notification about task {jira_key}")

    description = description_template.format(
        jira_key=jira_key,
        product_functionality=product_functionality,
        feature=feature,
        week_number=week_number,
        planned_end=planned_end,
    )

    logger.debug(description)

    response = imbot.send_text(
        chat_id=configuration["notify"]["chat_id"],
        text=description,
        parse_mode="HTML",
    ).json()

    assert response.get("ok", False), response.get(
        "description", response.get("reason", "Reason unknown")
    )

    logger.success(f'Notify sended successful, msg_id={response.get("msgId")}')
