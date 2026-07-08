from typing import Optional

from bot.bot import Bot
from bot.event import Event
from bot.types import KeyboardButton, InlineKeyboardMarkup

from project.logger import logger
from project.database.models import Chat, User
from project.utils import msg_call_all


@logger.catch
def mention_all(
        bot: Bot,
        event: Event,
        chat_id: str
):
    logger.info('User trying to mention all members in chat')

    msg_text = msg_call_all(
        chat_id=chat_id,
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

        logger.success('Successfully mentioned all users in chat')

    else:

        logger.warning('Empty members list, msg not sent')


@logger.catch
def assemble_admin_panel(bot: Bot, chat_id: str, msg_id: Optional[str] = None):
    markup = InlineKeyboardMarkup()

    query = Chat.select(
        Chat.title, Chat.chat_id
    ).join(User).where(
        User.uin == chat_id,
        # User.is_admin == True
    )

    for chat in query:
        markup.row(
            KeyboardButton(
                text=chat.title,
                callbackData=f'list_groups|{chat.chat_id}'
            )
        )

    if msg_id is None:
        bot.send_text(
            chat_id=chat_id,
            text='Список доступных чатов:'
            if query.count() else 'Нет доступных чатов :(',
            inline_keyboard_markup=markup
        )
    else:

        bot.edit_text(
            chat_id=chat_id,
            msg_id=msg_id,
            text='Список доступных чатов:'
            if query.count() else 'Нет доступных чатов :(',
            inline_keyboard_markup=markup
        )
