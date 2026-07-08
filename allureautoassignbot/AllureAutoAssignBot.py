import os
import pathlib
import re
from urllib.parse import urlparse

from pydantic.datetime_parse import datetime
from pyvkteamsbot.bot.bot import Bot
from pyvkteamsbot.bot.event import Event
from pyvkteamsbot.bot.types import KeyboardButton, InlineKeyboardMarkup

from loguru import logger
import openapi_client as allure

import models as md
from utils.event_filter import TextFilter
from utils.handler_wrapper import (
    model_wrapper,
    chat_id_context_wrapper,
    ChatIdContextVar,
)

from auto_assign.cli import assign
from auto_assign import database


assignbot = Bot(
    api_url_base="https://api.internal.myteam.mail.ru/bot/v1",
    token=os.getenv("BOT_TOKEN"),  # 1000001010
)


def error_handler(exc: BaseException):
    logger.info(f"exc: {exc}")
    logger.info(f"chat_id_context: {ChatIdContextVar.get()}")


@assignbot.start_handler()
@logger.catch(onerror=error_handler)
@chat_id_context_wrapper()
def start(bot: Bot, event: Event):
    user = event.message_author["userId"]
    logger.info(f"Chat ID: {event.from_chat}, User ID: {user}, text: '{event.text}'")

    text = """
    Для автоассайна скиньте ссылку на Launch и список пользователей, которых надо исключить из ассайна
    """

    bot.send_text(chat_id=event.from_chat, reply_msg_id=event.msgId, text=text.strip())


@assignbot.message_handler(filters=TextFilter(r"https://allure\.vk\.team/launch/\d+"))
@logger.catch(onerror=error_handler)
@chat_id_context_wrapper()
def start_launch_processing(bot: Bot, event: Event):
    global launch_ctlr

    launch_link = re.findall(r"https://allure\.vk\.team/launch/\d+", event.text)

    launch_path = urlparse(launch_link[0]).path

    launch_path_parts = launch_path.split("/")

    launch_id = launch_path_parts[-1]

    launch_info: allure.LaunchDto = launch_ctlr.find_one20(id=int(launch_id))

    ignore_list = re.findall(r"[a-zA-Z]+\.[a-zA-Z]+@[a-zA-Z.]+", event.text)

    ignore_list_str = "\n".join([f"@[{email}]" for email in ignore_list])

    text = (
        f"ID {launch_info.id} \"{launch_info.name}\"\n\n"
        f"Project ID: {launch_info.project_id}\n"
        f"Created by: @[{launch_info.created_by}]\n"
        f"Tags: {', '.join([tag.name for tag in launch_info.tags])}\n\n"
        f"Ignore users:\n{ignore_list_str}"
    )

    info = md.StartLaunchProcessingData(
        id=launch_info.id,
        project_id=launch_info.project_id,
        name=launch_info.name,
        exclude_users=ignore_list,
    )

    markup = InlineKeyboardMarkup()
    markup.row(
        KeyboardButton(
            text="Start auto assign of cases", callbackData=info.base64_dump()
        )
    )

    bot.send_text(chat_id=event.from_chat, text=text, inline_keyboard_markup=markup)


@assignbot.button_handler()
@logger.catch(onerror=error_handler)
@chat_id_context_wrapper()
@model_wrapper()
def start_launch_processing_button(
    bot: Bot, event: Event, launch_data: md.StartLaunchProcessingData
):
    global client, launch_ctlr, testresult_tree_ctlr, testresult_run_ctlr

    log_path = (
        pathlib.Path(".")
        .joinpath("logs")
        .joinpath(
            f"assign_log_id_{launch_data.id}_{int(datetime.now().timestamp())}.log"
        )
    )

    handler_id = logger.add(
        sink=str(log_path),
        level="DEBUG",
        colorize=False,
        enqueue=True,
        format="{time:HH:mm:ss} | {message}",
    )

    database.db.create_tables(
        [
            database.User,
            database.Team,
            database.Direction,
            database.ProductFunctionality,
            database.TestResult,
            database.TestResultProductFunctionality,
        ]
    )

    database.init_db(ignore_list=launch_data.exclude_users)

    assign(
        launch_ids=[launch_data.id],
        bot=bot,
        chat_id=event.from_chat,
        msg_id=event.msgId,
        launch_ctlr=launch_ctlr,
        testresult_tree_ctlr=testresult_tree_ctlr,
        testresult_run_ctlr=testresult_run_ctlr,
    )

    bot.answer_callback_query(
        query_id=event.queryId,
        text=f"ID: {launch_data.id} {launch_data.name} - Success!!!",
    )

    text = f"ID: {launch_data.id} {launch_data.name} - Success!!!"

    bot.edit_text(chat_id=event.from_chat, msg_id=event.msgId, text=text)

    database.db.drop_tables(
        [
            database.User,
            database.Team,
            database.ProductFunctionality,
            database.Direction,
            database.TestResult,
            database.TestResultProductFunctionality,
            database.User,
            database.UserTeam,
            database.UserDirection,
            database.UserProductFunctionality,
        ]
    )

    logger.remove(handler_id)

    with log_path.open(mode="r") as f:
        bot.send_file(
            chat_id=event.from_chat,
            caption=f"Assign log for launch ID {launch_data.id}",
            file=f,
        )


configuration = allure.Configuration()
configuration.verify_ssl = False


with allure.ApiClient(
    configuration=configuration,
    header_name="Authorization",
    header_value="Api-Token f5aa95f7-50d2-48aa-bdbe-52854dc0ca3c",
) as client:
    launch_ctlr = allure.LaunchControllerApi(api_client=client)
    testresult_tree_ctlr = allure.TestResultTreeControllerApi(api_client=client)
    testresult_run_ctlr = allure.TestResultRunControllerApi(api_client=client)

    assignbot.start_polling()
    assignbot.idle()
