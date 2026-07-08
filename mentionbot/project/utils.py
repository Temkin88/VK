from typing import List, Dict, Union, Optional

from bot.bot import Bot
from bot.event import Event
from bot.types import InlineKeyboardMarkup, KeyboardButton
from peewee import DoesNotExist

from project.database.queries import sql_list_chat_users_uin_in_custom_group
from project.filters import get_command
from project.logger import logger

from project.database.models import Chat, User, UserPhoto, \
    CustomGroup, CustomGroupMember


def collect_chat_users_to_db(bot: Bot, chat_id: str):

    logger.debug('Trying to get chat info from API')

    chat_info_json = bot.get_chat_info(chat_id).json()

    if chat_info_json['ok']:

        logger.debug(f'Trying to add chat ID {chat_id} to DB')

        chat_model, exist = Chat.get_or_create(
            chat_id=chat_id,
            is_group=True if chat_info_json['type'] == 'group' else False,
            title=chat_info_json['title'],
            invite_link=chat_info_json.get('inviteLink'),
            join_moderation=chat_info_json['joinModeration'],
            public=chat_info_json['public']
        )
        if exist:
            logger.debug(
                'Chat already exist id DB'
            )
        else:
            logger.success('Chat added to DB')

    else:
        logger.warning(f'Failed to get chat_info: {chat_info_json}')
        return

    for member in bot.get_chat_members(chat_id).json().get('members', []):

        logger.debug(f'Trying to add {member["userId"]} to DB')

        member_json = bot.get_chat_info(
            chat_id=member['userId']
        ).json()

        if not member_json.get('ok', False):
            logger.warning(
                f"{member['userId']} - "
                f"Failed to get chat_info: {chat_info_json}"
            )
            continue

        if member_json.get('isBot', False):
            logger.debug(f"{member['userId']} - isBot = True")
            continue

        user_model, exist = User.get_or_create(
            first_name=member_json['firstName'],
            last_name=member_json['lastName'],
            # about=member_json['about'],
            uin=member['userId'],
            chat=chat_model
        )

        user_model.is_admin = True \
            if member.get('admin', False) \
            or member.get('creator', False) \
            else False
        user_model.save()

        logger.success(
            f'Member ID {member["userId"]} is added to DB'
            if exist else
            f'Member ID {member["userId"]} is renewed to DB'
        )

        for user_photo in member_json['photo']:

            UserPhoto.get_or_create(
                user=user_model,
                url=user_photo['url']
            )

    logger.success('Successfully added new members to chat')


def delete_lefted_members(
        chat_id: str, left_members: List[Dict[str, Union[str, int]]]):

    logger.debug(f'Trying to get chat ID {chat_id} from DB')

    chat_model = Chat.get(
        Chat.chat_id == chat_id
    )

    logger.success(chat_model)

    for user in User.select().where(
        User.chat == chat_model,
        User.uin.in_(
            list(map(lambda user: user['userId'], left_members))
        )
    ):

        UserPhoto.delete().where(
            UserPhoto.user == user
        )
        CustomGroupMember.delete().where(
            CustomGroupMember.user == user
        )
        user.delete_instance()

    logger.success('Successfully deleted members from chat')


@logger.catch(default='')
def msg_call_all(chat_id: str, exclude: List[str]) -> str:

    logger.debug('Trying to assemble mentions for all command')

    return ' '.join(
        map(
            lambda user: f'@[{user.uin}]',
            User.select(User.uin).join(Chat).where(
                Chat.chat_id == chat_id,
                User.uin.not_in(exclude)
            )
        )
    )


def create_custom_group_request(bot: Bot, event: Event) -> Optional[str]:

    if event.data.get('parts', []):

        logger.info('User tried to create new custom group')

        chat_model = Chat.get(
            Chat.chat_id == event.from_chat
        )

        cmd = get_command(event.text)

        custom_group_model_count = CustomGroup.select().where(
            CustomGroup.name == cmd,
            CustomGroup.chat == chat_model
        ).count()

        logger.debug(f'custom_group_model_count = {custom_group_model_count}')

        if custom_group_model_count == 0:

            logger.info('Trying to assemble checking message')

            text = f'Вы уверены что хотите создать подгруппу {cmd}?\n\n' \
                   f'В ней будут состоять следующие сотрудники:\n'

            callback_data = f'create_custom_group|{cmd}'

            for part in filter(
                    lambda part: part['type'] == 'mention'
                                 and part['payload'].get('lastName', False),
                    event.data.get('parts', [])
            ):
                user_id = part['payload']['userId']
                text += f'@[{user_id}]\n'
                callback_data += f'|{user_id}'

            markup = InlineKeyboardMarkup()
            markup.row(
                KeyboardButton(
                    text='Да, конечно',
                    callbackData=callback_data
                ),
                KeyboardButton(
                    text='Нет!',
                    callbackData='delete_message'
                )
            )

            bot.send_text(
                chat_id=event.from_chat,
                text=text,
                inline_keyboard_markup=markup
            )

            logger.success('Checking msg is sent')
        else:
            logger.warning('Custom group already exist')


@logger.catch(default='')
def custom_group_call_text(
        target_chat_id:str,
        target_custom_group_name: str,
        exclude: List[str]
) -> str:

    return ' '.join(
        map(
            lambda user_model:
            f'@[{user_model.uin}]',
            sql_list_chat_users_uin_in_custom_group(
                target_chat_id,
                target_custom_group_name,
                exclude
            )
            # User.select()
            #     .join(CustomGroupMember)
            #     .where(
            #     CustomGroupMember.custom_group == custom_group_model,
            #     User.uin.not_in(exclude)
            # )
        )
    )

