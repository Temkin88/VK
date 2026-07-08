from bot.bot import Bot
from bot.event import Event
from bot.types import InlineKeyboardMarkup, KeyboardButton
from peewee import DoesNotExist

from project.database.models import \
    Chat, User, \
    CustomGroup, CustomGroupMember
from project.database.queries import \
    sql_get_custom_groups, \
    sql_get_custom_group_by_name, \
    sql_delete_members_of_custom_group, \
    sql_get_custom_group_users_list, \
    sql_is_custom_group_have_users, \
    sql_list_chat_users_not_in_custom_group, \
    sql_list_chat_users_uin_in_custom_group, \
    sql_list_chat_users_uin_not_in_custom_group


def callback_list_custom_groups(
        bot: Bot, chat_id: str, msg_id: str, target_chat_id: str):
    markup = InlineKeyboardMarkup()

    query = sql_get_custom_groups(target_chat_id)

    for custom_group_model in query:
        markup.row(
            KeyboardButton(
                text=custom_group_model.name,
                callbackData='|'.join([
                    'list_custom_groups',
                    target_chat_id,
                    custom_group_model.name,
                ])
            )
        )

    markup.row(
        KeyboardButton(
            text='Вернуться к списку доступных чатов',
            style='base',
            callbackData='list_chats'
        )
    )

    bot.edit_text(
        chat_id=chat_id,
        msg_id=msg_id,
        text=f'Чат: @[{target_chat_id}]\n\n'
             f'Список созданных подгрупп: '
        if query.count()
        else f'Чат: @[{target_chat_id}]\n\n'
             f'Нет доступных подгрупп в чате :(',
        inline_keyboard_markup=markup
    )


def callback_list_chats_custom_groups(
        bot: Bot,
        chat_id: str,
        msg_id: str,
        target_chat_id: str,
        target_custom_group_name: str
):
    markup = InlineKeyboardMarkup()

    markup.row(
        KeyboardButton(
            text='Добавить участников',
            callbackData='|'.join([
                'add_members_to_custom_group',
                target_chat_id,
                target_custom_group_name
            ])
        )
    )

    markup.row(
        KeyboardButton(
            text='Удалить участников',
            style='attention',
            callbackData='|'.join([
                'remove_members_to_custom_group',
                target_chat_id,
                target_custom_group_name
            ])
        )
    )

    markup.row(
        KeyboardButton(
            text='Удалить подгруппу',
            style='attention',
            callbackData='|'.join([
                'remove_custom_group',
                target_chat_id,
                target_custom_group_name
            ])
        )
    )

    markup.row(
        KeyboardButton(
            text='Вернуться к списку подгрупп',
            style='base',
            callbackData='|'.join([
                'list_groups',
                target_chat_id
            ])
        )
    )

    markup.row(
        KeyboardButton(
            text='Вернуться к списку доступных чатов',
            style='base',
            callbackData='list_chats'
        )
    )

    query = sql_list_chat_users_uin_in_custom_group(
        target_chat_id,
        target_custom_group_name
    )

    users_list = '\n'.join(
        map(lambda user: f'@[{user.uin}]', query)
    )

    bot.edit_text(
        chat_id=chat_id,
        msg_id=msg_id,
        text=f'Чат:  @[{target_chat_id}]\n'
             f'Подгруппа: {target_custom_group_name}\n\n'
             f'Список участников подгруппы:\n'
             f'{users_list}\n\n'
             f'Список доступных действий '
             f'для подгруппы:',
        inline_keyboard_markup=markup
    )


def callback_create_custom_group(bot: Bot, event: Event):

    _, cmd, *users = event.callback_query.split('|')

    chat_model = Chat.get(
        chat_id=event.from_chat
    )

    custom_group_model, exist = CustomGroup.get_or_create(
        name=cmd,
        chat=chat_model
    )

    for user in filter(lambda x: x.count('@') != 0, users):

        user_json = bot.get_chat_info(user).json()

        try:

            user_model = User.select().join(Chat).where(
                User.first_name == user_json['firstName'],
                User.last_name == user_json['lastName'],
                User.uin == user,
                Chat.chat_id == event.from_chat
            ).get()

            CustomGroupMember.get_or_create(
                custom_group=custom_group_model,
                user=user_model
            )
        except DoesNotExist:
            continue

    bot.edit_text(
        chat_id=event.from_chat,
        msg_id=event.msgId,
        text=f'Подгруппа {cmd} успешно создана'
    )


def callback_remove_custom_group(
        bot: Bot,
        chat_id: str,
        msg_id: str,
        query_id: str,
        target_chat_id: str,
        target_custom_group_name: str
):

    custom_group_model = sql_get_custom_group_by_name(
        target_chat_id,
        target_custom_group_name
    )

    sql_delete_members_of_custom_group(custom_group_model)

    custom_group_model.delete_instance()

    bot.answer_callback_query(
        query_id=query_id,
        text=f'Подгруппа {target_custom_group_name} удалена'
    )

    callback_list_custom_groups(
        bot,
        chat_id,
        msg_id,
        target_chat_id,
    )


def callback_list_users_for_removing(
        bot: Bot,
        chat_id: str,
        msg_id: str,
        target_chat_id: str,
        target_custom_group_name: str
):

    markup = InlineKeyboardMarkup()

    query = sql_get_custom_group_users_list(
        target_chat_id,
        target_custom_group_name
    )

    for custom_group_member in query:
        user = User.get_by_id(custom_group_member.user)

        markup.row(
            KeyboardButton(
                text=' '.join([user.first_name, user.last_name]),
                style='attention',
                callbackData='|'.join([
                    'remove_user',
                    target_chat_id,
                    target_custom_group_name,
                    str(custom_group_member.id)
                ])
            )
        )

    markup.row(
        KeyboardButton(
            text='Назад к списку действий',
            style='base',
            callbackData='|'.join([
                    'list_custom_groups',
                    target_chat_id,
                    target_custom_group_name
                ])
        )
    )

    users_query = sql_list_chat_users_uin_not_in_custom_group(
        target_chat_id,
        target_custom_group_name
    )

    users_list = '\n'.join(
        map(lambda user: f'@[{user.uin}]', users_query)
    )

    bot.edit_text(
        chat_id=chat_id,
        msg_id=msg_id,
        text=f'Чат: @[{target_chat_id}]\n'
             f'Подгруппа: {target_custom_group_name}\n\n'
             f'Пользователи чата, не состоящие в подгруппе:\n'
             f'{users_list}\n\n'
             f'Список пользователей в подгруппе:'
        if query.count()
        else 'В группе нет пользователей',
        inline_keyboard_markup=markup
    )


def callback_remove_user(
        bot: Bot,
        chat_id: str,
        msg_id: str,
        query_id: str,
        custom_group_member_id: str,
        target_chat_id: str,
        target_custom_group_name: str
):
    custom_group_member_model = CustomGroupMember.get_by_id(
        int(custom_group_member_id)
    )

    custom_group_model = CustomGroup.get_by_id(
        custom_group_member_model.custom_group
    )

    custom_group_member_uin = User.get_by_id(
        custom_group_member_model.user).uin

    custom_group_member_model.delete_instance()

    if sql_is_custom_group_have_users(custom_group_model):
        custom_group_model.delete_instance()

    bot.answer_callback_query(
        query_id=query_id,
        text=f'Пользователь @[{custom_group_member_uin}] '
             f'удален из подгруппы'
    )

    callback_list_users_for_removing(
        bot,
        chat_id,
        msg_id,
        target_chat_id,
        target_custom_group_name
    )


def callback_list_users_for_adding(
        bot: Bot,
        chat_id: str,
        msg_id: str,
        target_chat_id: str,
        target_custom_group_name: str
):

    query = sql_list_chat_users_not_in_custom_group(
        target_chat_id,
        target_custom_group_name
    )

    markup = InlineKeyboardMarkup()

    for user in query:

        markup.row(
            KeyboardButton(
                text=' '.join([user.first_name, user.last_name]),
                callbackData='|'.join([
                    'add_user',
                    target_chat_id,
                    target_custom_group_name,
                    str(user.id)
                ])
            )
        )

    markup.row(
        KeyboardButton(
            text='Назад к списку действий',
            style='base',
            callbackData='|'.join([
                    'list_custom_groups',
                    target_chat_id,
                    target_custom_group_name
                ])
        )
    )

    users_query = sql_list_chat_users_uin_in_custom_group(
        target_chat_id,
        target_custom_group_name
    )

    users_list = '\n'.join(
        map(lambda user: f'@[{user.uin}]', users_query)
    )

    bot.edit_text(
        chat_id=chat_id,
        msg_id=msg_id,
        text=f'Чат: @[{target_chat_id}]\n'
             f'Подгруппа: {target_custom_group_name}\n\n'
             f'Список участников подгруппы:\n'
             f'{users_list}\n\n'
             f'Список пользователей '
             f'доступных для добавления в подгруппу:'
        if query.count()
        else f'Чат: @[{target_chat_id}]\n'
             f'Подгруппа: {target_custom_group_name}\n\n'
             f'Все пользователи чата уже добавлены в подгруппу :)',
        inline_keyboard_markup=markup
    )


def callback_add_user_to_custom_group(
        bot: Bot,
        chat_id: str,
        msg_id: str,
        query_id: str,
        target_chat_id: str,
        target_custom_group_name: str,
        user_id: str
):

    user_model = User.get_by_id(int(user_id))

    CustomGroupMember.get_or_create(
        custom_group=CustomGroup.get(
            name=target_custom_group_name,
            chat=Chat.get(chat_id=target_chat_id)
        ),
        user=user_model
    )

    bot.answer_callback_query(
        query_id=query_id,
        text=f'Пользователь @[{user_model.uin}] '
             f'добавлен в подгруппу "{target_custom_group_name}"'
    )

    callback_list_users_for_adding(
        bot,
        chat_id,
        msg_id,
        target_chat_id,
        target_custom_group_name
    )
