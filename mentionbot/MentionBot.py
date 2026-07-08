from bot.bot import Bot
from bot.event import Event, EventType

from project.callbacks import callback_list_custom_groups, \
    callback_list_chats_custom_groups, callback_remove_custom_group, \
    callback_list_users_for_removing, callback_remove_user, \
    callback_list_users_for_adding, callback_add_user_to_custom_group, \
    callback_create_custom_group
from project.commands import mention_all, assemble_admin_panel
from project.logger import logger

from project.utils import \
    collect_chat_users_to_db, \
    delete_lefted_members, \
    create_custom_group_request, \
    custom_group_call_text

from project.filters import \
    custom_group_cmd_filter, \
    custom_group_call_filter, \
    admin_filter, \
    callback_list_chats_filter, \
    callback_list_groups_filter, \
    callback_list_chats_custom_groups_filter, \
    callback_remove_custom_group_filter, \
    callback_list_users_for_removing_filter, \
    callback_remove_user_filter, \
    callback_list_users_for_adding_filter, \
    callback_add_user_to_custom_group_filter, is_author_bot, is_not_command, \
    callback_create_custom_group_filter, callback_delete_message_filter

from project.constants import HELP_TEXT, API_URL, TOKEN

mention_bot = Bot(
    token=TOKEN,
    api_url_base=API_URL,
)


@mention_bot.default_handler()
@logger.catch
def event_logging(bot: Bot, event: Event):
    if is_author_bot(event.data) \
            or is_not_command(event.data.get('text')) \
            or event.type != EventType.NEW_MESSAGE:
        return

    with logger.contextualize(
            user_id=event.data.get('from', {}).get('userId', 'null'),
            chat_id=event.data.get('chat', {}).get('chatId', 'null'),
            cmd_text=event.text.split(' ')[0].strip(),
            event_type=event.type
    ):

        logger.debug(event.data)


@mention_bot.new_member_handler()
def handle_adding_to_group(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.data.get('addedBy', {}).get('userId', 'null'),
            chat_id=event.data['chat']['chatId'],
            cmd_text='null',
            event_type=event.type
    ):
        with logger.catch(onerror=lambda error: bot.send_text(
            chat_id=event.data['chat']['chatId'],
            text='ОШИБКА: ' + str(error)
        )):

            logger.info('Trying to handle new members in chat members list')

            collect_chat_users_to_db(bot, event.data['chat']['chatId'])


@mention_bot.member_left_chat_handler()
def handle_member_left_chat(bot: Bot, event: Event):
    with logger.contextualize(
            user_id=event.data.get('removedBy', {}).get('userId', 'null'),
            chat_id=event.data['chat']['chatId'],
            cmd_text='null',
            event_type=event.type
    ):
        with logger.catch(onerror=lambda error: bot.send_text(
            chat_id=event.data['chat']['chatId'],
            text='ОШИБКА: ' + str(error)
        )):
            logger.info('Trying to handle deleting members from chat members list')

            delete_lefted_members(
                chat_id=event.data['chat']['chatId'],
                left_members=event.data['leftMembers']
            )


@mention_bot.command_handler('all')
def call_to_all(bot: Bot, event: Event):

    chat_id = event.from_chat

    with logger.contextualize(
            user_id=event.message_author["userId"],
            chat_id=event.data['chat']['chatId'],
            cmd_text='/all',
            event_type=event.type
    ):
        with logger.catch(onerror=lambda error: bot.send_text(
            chat_id=event.data['chat']['chatId'],
            text='ОШИБКА: ' + str(error)
        )):
            mention_all(bot, event, chat_id)


@mention_bot.message_handler(filters=custom_group_call_filter)
def handle_custom_group_call(bot: Bot, event: Event):
    chat_id = event.from_chat

    with logger.contextualize(
            user_id=event.message_author["userId"],
            chat_id=event.data['chat']['chatId'],
            cmd_text=event.text.split(' ')[0].strip(),
            event_type=event.type
    ):
        with logger.catch(onerror=lambda error: bot.send_text(
            chat_id=event.data['chat']['chatId'],
            text='ОШИБКА: ' + str(error)
        )):

            logger.info('User trying to call custom group')

            msg_text = custom_group_call_text(
                event.from_chat,
                event.text.split(' ')[0].strip(),
                exclude=[event.message_author['userId']]
            )

            event_text_words = event.text.split(' ')

            if len(event_text_words) > 1:
                msg_text = ' '.join([msg_text, '\n\n'] + event_text_words[1:])

            if msg_text:

                bot.send_text(
                    chat_id=chat_id,
                    text=msg_text
                )

                logger.success('Successfully mentioned custom users group in chat')

            else:

                logger.warning('Empty members list, msg not sent')


@mention_bot.message_handler(filters=custom_group_cmd_filter)
def handle_custom_group_create(bot: Bot, event: Event):
    chat_id = event.from_chat
    cmd = event.text.split(' ')[0].strip()

    with logger.contextualize(
            user_id=event.message_author["userId"],
            chat_id=chat_id,
            cmd_text=cmd,
            event_type=event.type
    ):
        with logger.catch(onerror=lambda error: bot.send_text(
            chat_id=event.data['chat']['chatId'],
            text='ОШИБКА: ' + str(error)
        )):

            create_custom_group_request(bot, event)


@mention_bot.help_handler()
def bot_help(bot: Bot, event: Event):
    with logger.contextualize(
            user_id=event.message_author["userId"],
            chat_id=event.data['chat']['chatId'],
            cmd_text=event.text.split(' ')[0].strip(),
            event_type=event.type
    ):
        with logger.catch(onerror=lambda error: bot.send_text(
            chat_id=event.data['chat']['chatId'],
            text='ОШИБКА: ' + str(error)
        )):

            logger.info('User requesting help cmd')

            bot.send_text(
                chat_id=event.from_chat,
                text=HELP_TEXT
            )


@mention_bot.command_handler('admin', filters=admin_filter)
def admin_panel(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.message_author["userId"],
            chat_id=event.from_chat,
            cmd_text=event.text.split(' ')[0].strip(),
            event_type=event.type
    ):
        with logger.catch(onerror=lambda error: bot.send_text(
            chat_id=event.data['chat']['chatId'],
            text='ОШИБКА: ' + str(error)
        )):

            logger.info('User requested admin panel')

            assemble_admin_panel(bot, event.from_chat)


@mention_bot.button_handler()
def button_logger(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.message_author,
            chat_id=event.from_chat,
            cmd_text=event.callback_query,
            event_type=event.type
    ):
        with logger.catch(onerror=lambda error: bot.answer_callback_query(
            query_id=event.queryId,
            text='ОШИБКА: ' + str(error)
        )):

            logger.debug(event.data)


@mention_bot.button_handler(filters=callback_list_chats_filter)
def list_chats(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.message_author,
            chat_id=event.from_chat,
            cmd_text=event.callback_query,
            event_type=event.type
    ):
        with logger.catch(onerror=lambda error: bot.answer_callback_query(
            query_id=event.queryId,
            text='ОШИБКА: ' + str(error)
        )):

            logger.info('User requested admin panel')

            assemble_admin_panel(bot, event.from_chat, event.msgId)


@mention_bot.button_handler(filters=callback_list_groups_filter)
def list_custom_groups(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.message_author,
            chat_id=event.from_chat,
            cmd_text=event.callback_query,
            event_type=event.type
    ):

        with logger.catch(onerror=lambda error: bot.answer_callback_query(
            query_id=event.queryId,
            text='ОШИБКА: ' + str(error)
        )):

            target_chat_id = event.callback_query.split('|')[-1]

            callback_list_custom_groups(
                bot, event.from_chat, event.msgId, target_chat_id)


@mention_bot.button_handler(filters=callback_list_chats_custom_groups_filter)
def list_chats_custom_groups(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.message_author,
            chat_id=event.from_chat,
            cmd_text=event.callback_query,
            event_type=event.type
    ):

        with logger.catch(onerror=lambda error: bot.answer_callback_query(
            query_id=event.queryId,
            text='ОШИБКА: ' + str(error)
        )):

            _, target_chat_id, target_custom_group_name = event.callback_query.split('|')

            callback_list_chats_custom_groups(
                bot,
                event.from_chat,
                event.msgId,
                target_chat_id,
                target_custom_group_name
            )


@mention_bot.button_handler(filters=callback_create_custom_group_filter)
def create_custom_group(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.message_author,
            chat_id=event.from_chat,
            cmd_text=event.callback_query,
            event_type=event.type
    ):

        with logger.catch(onerror=lambda error: bot.answer_callback_query(
            query_id=event.queryId,
            text='ОШИБКА: ' + str(error)
        )):
            callback_create_custom_group(bot, event)


@mention_bot.button_handler(filters=callback_remove_custom_group_filter)
def remove_custom_group(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.message_author,
            chat_id=event.from_chat,
            cmd_text=event.callback_query,
            event_type=event.type
    ):

        with logger.catch(onerror=lambda error: bot.answer_callback_query(
            query_id=event.queryId,
            text='ОШИБКА: ' + str(error)
        )):

            _, target_chat_id, target_custom_group_name = event.callback_query.split('|')

            callback_remove_custom_group(
                bot,
                event.from_chat,
                event.msgId,
                event.queryId,
                target_chat_id,
                target_custom_group_name
            )


@mention_bot.button_handler(filters=callback_list_users_for_removing_filter)
def list_users_for_removing(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.message_author,
            chat_id=event.from_chat,
            cmd_text=event.callback_query,
            event_type=event.type
    ):

        with logger.catch(onerror=lambda error: bot.answer_callback_query(
            query_id=event.queryId,
            text='ОШИБКА: ' + str(error)
        )):
            _, target_chat_id, target_custom_group_name = event.callback_query.split('|')

            callback_list_users_for_removing(
                bot,
                event.from_chat,
                event.msgId,
                target_chat_id,
                target_custom_group_name
            )


@mention_bot.button_handler(filters=callback_remove_user_filter)
def remove_user(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.message_author,
            chat_id=event.from_chat,
            cmd_text=event.callback_query,
            event_type=event.type
    ):

        with logger.catch(onerror=lambda error: bot.answer_callback_query(
            query_id=event.queryId,
            text='ОШИБКА: ' + str(error)
        )):
            _, target_chat_id, target_custom_group_name, custom_group_member_id = event.callback_query.split('|')

            callback_remove_user(
                bot,
                event.from_chat,
                event.msgId,
                event.queryId,
                custom_group_member_id,
                target_chat_id,
                target_custom_group_name
            )


@mention_bot.button_handler(filters=callback_list_users_for_adding_filter)
def list_users_for_adding(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.message_author,
            chat_id=event.from_chat,
            cmd_text=event.callback_query,
            event_type=event.type
    ):

        with logger.catch(onerror=lambda error: bot.answer_callback_query(
            query_id=event.queryId,
            text='ОШИБКА: ' + str(error)
        )):
            _, target_chat_id, target_custom_group_name = event.callback_query.split('|')

            callback_list_users_for_adding(
                bot,
                event.from_chat,
                event.msgId,
                target_chat_id,
                target_custom_group_name
            )


@mention_bot.button_handler(filters=callback_add_user_to_custom_group_filter)
def add_user_to_custom_group(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.message_author,
            chat_id=event.from_chat,
            cmd_text=event.callback_query,
            event_type=event.type
    ):

        with logger.catch(onerror=lambda error: bot.answer_callback_query(
            query_id=event.queryId,
            text='ОШИБКА: ' + str(error)
        )):
            _, target_chat_id, target_custom_group_name, user_id = event.callback_query.split('|')

            callback_add_user_to_custom_group(
                bot,
                event.from_chat,
                event.msgId,
                event.queryId,
                target_chat_id,
                target_custom_group_name,
                user_id
            )


@mention_bot.button_handler(filters=callback_delete_message_filter)
def delete_message(bot: Bot, event: Event):

    with logger.contextualize(
            user_id=event.message_author,
            chat_id=event.from_chat,
            cmd_text=event.callback_query,
            event_type=event.type
    ):

        with logger.catch(onerror=lambda error: bot.answer_callback_query(
            query_id=event.queryId,
            text='ОШИБКА: ' + str(error)
        )):

            bot.delete_messages(
                chat_id=event.from_chat,
                msg_id=event.msgId
            )


logger.info('Trying to start bot')

mention_bot.start_polling()
logger.success('Events polling initialized')

mention_bot.idle()
