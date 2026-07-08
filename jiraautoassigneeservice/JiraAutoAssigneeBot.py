import hashlib
import json

from bot.bot import Bot
from bot.event import Event, EventType
from bot.types import InlineKeyboardMarkup, KeyboardButton

from prettytable import PrettyTable
import sentry_sdk

from project.logger import logger

from project.logger import vkteams_log_sending
from project.db.models import Project, assignees, User
from project.db.sql_functions import sql_get_users_rating_table_from_db, \
    sql_get_users_issues_from_db, sql_get_users_for_rating_with_uin


sentry_sdk.init("http://b59cd0944b0143ae9bff42fbfb8e7995@100.99.5.41:8000/4")


assignee_bot = Bot(
    token='001.4004526681.4019241748:1000000649',
    api_url_base='https://api.internal.myteam.mail.ru/bot/v1/',
    is_myteam=True
)


ACCESS_LIST = assignees.copy()


ACCESS_LIST.add('v.korobov@corp.mail.ru')
ACCESS_LIST.add('p.vazhnov@vk.team')


def save_new_users_json():
    users_json_backup = dict()

    for project in Project.select():
        users_json_backup[project.name] = []
        for user in project.users:
            users_json_backup[project.name].append(
                user.uin)

    with open('users.json', 'w') as f:

        json.dump(users_json_backup, f, indent=2)

    with open('state.json', 'r') as f:

        state = json.load(f)

    with open('state.json', 'w') as f:
        state['hash'] = hashlib.md5(json.dumps(
            users_json_backup).encode()).hexdigest()

        json.dump(state, fp=f, indent=2)


def assemble_table(projects: str) -> PrettyTable:
    str_table = PrettyTable()

    str_table.field_names = ["ID", "User", "Rating"]

    if projects == "ALL":
        projects = ','.join(row.name for row in Project.select())

    for row in sorted(sql_get_users_rating_table_from_db(projects), key=lambda x: x.rating):
        str_table.add_row([row.id, row.uin, round(row.rating, 3)])

    return str_table


START_TEXT = """Доступные команды:
/rating - Выдает список доступных проектов в виде кнопок
/rating {PROJECT_NAMES} - Сразу выдает таблицу рейтинга в указанных проектах
Проекты надо указывать через запятую
/issues - получить таблицу задач, назначенных на себя
/issues {UIN} - получить таблицу задач, назначенных на пользователя
/current_users - получить список связей пользователь<->проект
/edit_projects - открыть меню редактирования связей пользователь<->проект
"""


ACCESS_DENIED_TEXT = 'Access denied, please, contact @[v.korobov@corp.mail.ru] or @[p.vazhnov@vk.team]'


def access_filter(func):
    def wrapper(bot: Bot, event: Event, *args, **kwargs):
        if event.from_chat in ACCESS_LIST:
            func(bot, event, *args, **kwargs)
        else:
            if event.type in (EventType.NEW_MESSAGE, EventType.EDITED_MESSAGE):
                bot.send_text(
                    chat_id=event.from_chat,
                    text=ACCESS_DENIED_TEXT
                )
            elif event.type == EventType.CALLBACK_QUERY:
                bot.answer_callback_query(
                    query_id=event.queryId,
                    text=ACCESS_DENIED_TEXT
                )
    return wrapper


@assignee_bot.start_handler()
@access_filter
@logger.catch(onerror=vkteams_log_sending)
def start(bot: Bot, event: Event):

    bot.send_text(
        chat_id=event.from_chat,
        text=START_TEXT
    )


@assignee_bot.help_handler()
@access_filter
@logger.catch
def help(bot: Bot, event: Event):

    bot.send_text(
        chat_id=event.from_chat,
        text=START_TEXT
    )


@assignee_bot.command_handler('current_users')
@access_filter
@logger.catch(onerror=vkteams_log_sending)
def backup(bot: Bot, event: Event):

    users_json_backup = dict()

    for project in Project.select():
        users_json_backup[project.name] = []
        for user in project.users:
            users_json_backup[project.name].append(
                f'@[{user.uin}]')

    bot.send_text(
        chat_id=event.from_chat,
        text="<code>{}</code>".format(
            json.dumps(users_json_backup, indent=2)),
        parse_mode='HTML'
    )


@assignee_bot.command_handler('edit_projects')
@access_filter
@logger.catch(onerror=vkteams_log_sending)
def edit_projects(bot: Bot, event: Event):

    markup = InlineKeyboardMarkup()

    for project in Project.select():

        markup.row(
            KeyboardButton(
                text=project.name, callbackData=f'edit_projects|{project.name}'
            )
        )

    bot.send_text(
        chat_id=event.from_chat,
        text='Выберите проект для редактирования состава',
        inline_keyboard_markup=markup
    )


@assignee_bot.command_handler('issues')
@access_filter
@logger.catch(onerror=vkteams_log_sending)
def issues(bot: Bot, event: Event):

    is_cmd_with_uin = event.text.split()

    if len(is_cmd_with_uin) == 1:

        uin = event.from_chat

    else:

        uin = is_cmd_with_uin[-1]

    str_table = PrettyTable()

    str_table.field_names = ["ID", "Status", "Priority"]

    for row in sql_get_users_issues_from_db(uin=uin):

        str_table.add_row([row.key, row.status.value, round(row.priority, 3)])

    bot.send_text(
        chat_id=event.from_chat,
        text='<code>{}</code>'.format(
            str_table.get_string(
                title=f'Tasks for {uin}')),
        parse_mode='HTML'
    )


@assignee_bot.command_handler('rating')
@access_filter
@logger.catch(onerror=vkteams_log_sending)
def rating(bot: Bot, event: Event):

    is_cmd_with_projects = event.text.replace(',', ' ').split()

    markup = InlineKeyboardMarkup()

    if len(is_cmd_with_projects) == 1:

        text = 'Список доступных проектов:'

        for project in Project.select():
            markup.row(
                KeyboardButton(
                    text=project.name, callbackData=f'rating|{project.name}'
                )
            )

        markup.row(
            KeyboardButton(
                text='All projects', callbackData='rating|ALL'
            )
        )

        bot.send_text(
            chat_id=event.from_chat,
            text=text,
            inline_keyboard_markup=markup
        )

    else:

        project = ','.join(is_cmd_with_projects[1:])

        str_table = assemble_table(project)

        for user in sql_get_users_for_rating_with_uin(project):

            markup.row(
                KeyboardButton(
                    text=user.uin, callbackData=f'issues|{user.uin}'
                )
            )

        bot.send_text(
            chat_id=event.from_chat,
            text='<code>{}</code>\n\n'
                 'Также можно посмотреть таски пользователя из рейтинга:'
                 .format(
                    str_table.get_string(
                        title=f'User rating in projects "{project}"')),
            inline_keyboard_markup=markup,
            parse_mode='HTML'
        )


@assignee_bot.button_handler()
@access_filter
@logger.catch(onerror=vkteams_log_sending)
def callback(bot: Bot, event: Event):

    markup = InlineKeyboardMarkup()

    if event.callback_query.startswith('rating'):

        project = event.callback_query.split('|')[-1]

        str_table = assemble_table(project)

        for user in sql_get_users_for_rating_with_uin(project):

            markup.row(
                KeyboardButton(
                    text=user.uin, callbackData=f'issues|{user.uin}'
                )
            )

        bot.edit_text(
            chat_id=event.from_chat,
            msg_id=event.msgId,
            text='<code>{}</code>'.format(
                str_table.get_string(
                    title=f'User rating in projects "{project}"')),
            inline_keyboard_markup=markup,
            parse_mode='HTML'
        )

    elif event.callback_query.startswith('issues'):

        uin = event.callback_query.split('|')[-1]

        str_table = PrettyTable()

        str_table.field_names = ["ID", "Status", "Priority"]

        for row in sql_get_users_issues_from_db(uin=uin):
            str_table.add_row([row.key, row.status.value, round(row.priority, 3)])

        bot.edit_text(
            chat_id=event.from_chat,
            msg_id=event.msgId,
            text='<code>{}</code>'.format(
                str_table.get_string(
                    title=f'Tasks for {uin}')),
            parse_mode='HTML'
        )

    elif event.callback_query.startswith('edit_projects'):

        base, cmd, *args = event.callback_query.split('|')

        if cmd == 'add':
            if len(args) == 1:
                project = args[0]
                project_model = Project.get(Project.name == project)
            else:
                project, uin = args
                project_model = Project.get(Project.name == project)
                user_model = User.get(User.uin == uin)

                project_model.users.add(user_model)
                save_new_users_json()

            for uin in filter(
                lambda x: User.get(User.uin == x) not in project_model.users,
                assignees
            ):
                markup.row(
                    KeyboardButton(
                        text=uin,
                        callbackData=f'edit_projects|add|{project}|{uin}'
                    )
                )

            bot.edit_text(
                chat_id=event.from_chat,
                msg_id=event.msgId,
                text=f'Проект: {project}\n\nКого нужно добавить?',
                inline_keyboard_markup=markup
            )

        elif cmd == 'remove':

            if len(args) == 1:
                project = args[0]
                project_model = Project.get(Project.name == project)
            else:
                project, uin = args
                project_model = Project.get(Project.name == project)
                user_model = User.get(User.uin == uin)

                project_model.users.remove(user_model)
                save_new_users_json()

            for user_model in project_model.users:
                markup.row(
                    KeyboardButton(
                        text=user_model.uin,
                        callbackData=f'edit_projects|remove|{project}|{user_model.uin}'
                    )
                )

            bot.edit_text(
                chat_id=event.from_chat,
                msg_id=event.msgId,
                text=f'Проект: {project}\n\nКого нужно удалить?',
                inline_keyboard_markup=markup
            )
        else:
            markup.row(
                KeyboardButton(
                    text='Добавить',
                    callbackData=f'edit_projects|add|{cmd}'
                ),
                KeyboardButton(
                    text='Удалить',
                    callbackData=f'edit_projects|remove|{cmd}'
                )
            )

            bot.edit_text(
                chat_id=event.from_chat,
                msg_id=event.msgId,
                text=f'Проект: {cmd}\n\nВыберите действие с пользователями:',
                inline_keyboard_markup=markup
            )

    else:

        bot.answer_callback_query(
            query_id=event.queryId,
            text=f'Unknown callback query: {event.callback_query}'
        )


assignee_bot.start_polling()
assignee_bot.idle()
