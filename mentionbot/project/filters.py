from typing import Dict, Union, Optional

from functools import lru_cache

from bot.event import Event, EventType

from project.logger import logger
from project.database.models import User, CustomGroup, Chat
from project.constants import COMMANDS_LIST



def is_author_bot(event_data: Dict[str, Union[str, int]]) -> bool:

    author = event_data.get('from', {}).get('userId', None)

    if author is not None and author.count('@'):
        return False
    else:
        return True



def get_command(event_text: str) -> Optional[str]:

    if event_text is not None:
        return event_text.split(' ')[0].strip()
    return event_text



def is_not_command(event_text: Optional[str]) -> bool:

    if event_text is None or not get_command(event_text).startswith('/'):
        return True
    else:
        return False



@logger.catch(default=False)
def custom_group_cmd_filter(event: Event) -> bool:

    if event.type != EventType.NEW_MESSAGE \
            or event.chat_type == 'private' \
            or is_author_bot(event.data) \
            or is_not_command(event.text):
        return False

    command = get_command(event.text)

    if command is None:
        return False

    is_group_name_collistion_with_commands = command not in COMMANDS_LIST

    is_cmd = event.text.startswith('/')

    is_have_parts = bool(
        list(filter(
            lambda x: x['type'] == 'mention', event.data.get('parts', []))))

    query = CustomGroup.select(CustomGroup.name).join(Chat).where(
        CustomGroup.name == event.text.split('@')[0].strip(),
        Chat.chat_id == event.from_chat
    )

    is_group_exist_in_db = query.count() != 0

    if is_cmd \
            and is_have_parts \
            and is_group_name_collistion_with_commands \
            and not is_group_exist_in_db:
        return True
    else:
        return False



@logger.catch(default=False)
def custom_group_call_filter(event: Event) -> bool:

    if event.type == EventType.NEW_MESSAGE \
            and not is_author_bot(event.data) \
            and not is_not_command(event.text):

        command = get_command(event.text)

        query = CustomGroup.select(CustomGroup.name).join(Chat).where(
            CustomGroup.name == command,
            Chat.chat_id == event.from_chat
        )

        return query.count() != 0 \
            and command not in COMMANDS_LIST
    else:
        return False



@logger.catch(default=False)
def admin_filter(event: Event) -> bool:

    if event.type != EventType.NEW_MESSAGE or is_author_bot(event.data):
        return False

    if event.text != '/admin' or event.chat_type != 'private':
        return False

    count = User.select(User.uin).where(
        # User.is_admin == True,
        User.uin == event.from_chat
    ).count()

    logger.bind(
        chat_id=event.from_chat,
        user_id=event.message_author["userId"],
        event_type=event.type,
        cmd_text='/admin'
    ).debug(f'count = {count}')

    return bool(count)



def callback_base_filter(
        event: Event,
        callbackData: str,
        call_len: int = 2
) -> bool:

    if event.type != EventType.CALLBACK_QUERY:
        return False

    if event.callback_query.startswith(callbackData) \
            and len(event.callback_query.split('|')) == call_len:
        return True
    else:
        return False


def callback_create_custom_group_filter(
        event: Event
) -> bool:

    if event.type != EventType.CALLBACK_QUERY:
        return False

    if event.callback_query.startswith('create_custom_group') \
            and len(event.callback_query.split('|')) >= 3:
        return True
    else:
        return False



def callback_delete_message_filter(event: Event) -> bool:

    return callback_base_filter(event, 'delete_message', 1)


def callback_list_chats_filter(event: Event) -> bool:

    return callback_base_filter(event, 'list_chats', 1)



def callback_list_groups_filter(event: Event) -> bool:

    return callback_base_filter(event, 'list_groups')



def callback_list_chats_custom_groups_filter(event: Event) -> bool:

    return callback_base_filter(event, 'list_custom_groups', 3)



def callback_remove_custom_group_filter(event: Event) -> bool:

    return callback_base_filter(event, 'remove_custom_group', 3)



def callback_list_users_for_removing_filter(event: Event) -> bool:

    return callback_base_filter(event, 'remove_members_to_custom_group', 3)



def callback_remove_user_filter(event: Event) -> bool:

    return callback_base_filter(event, 'remove_user', 4)



def callback_list_users_for_adding_filter(event: Event) -> bool:

    return callback_base_filter(event, 'add_members_to_custom_group', 3)



def callback_add_user_to_custom_group_filter(event: Event) -> bool:

    return callback_base_filter(event, 'add_user', 4)
