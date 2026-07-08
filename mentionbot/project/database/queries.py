from typing import List

from peewee import ModelSelect

from project.logger import logger
from project.database.models import \
    Chat, User, \
    CustomGroup, CustomGroupMember


def sql_get_custom_groups(target_chat_id: str) -> ModelSelect:

    return CustomGroup.select(
        CustomGroup.name
    ).join(Chat).where(
        Chat.chat_id == target_chat_id
    )


def sql_get_custom_group_by_name(
        target_chat_id: str,
        target_custom_group_name: str
) -> CustomGroup:

    return CustomGroup.select().join(Chat).where(
        CustomGroup.name == target_custom_group_name,
        Chat.chat_id == target_chat_id
    ).get()


def sql_delete_members_of_custom_group(
        custom_group_model: CustomGroup
):
    CustomGroupMember.delete().where(
        CustomGroupMember.custom_group == custom_group_model
    )


def sql_get_custom_group_users_list(
        target_chat_id: str,
        target_custom_group_name: str
) -> ModelSelect:

    return CustomGroupMember.select().join(User).switch(CustomGroupMember).join(
        CustomGroup).join(Chat).where(
        CustomGroup.name == target_custom_group_name,
        Chat.chat_id == target_chat_id
    )


def sql_is_custom_group_have_users(
        custom_group_model: CustomGroup
) -> bool:

    return CustomGroupMember.select().where(
        CustomGroupMember.custom_group == custom_group_model
    ).count() == 0


def sql_list_chat_users_not_in_custom_group(
        target_chat_id: str,
        target_custom_group_name: str
) -> ModelSelect:

    return User.select(
        User.id,
        User.first_name,
        User.last_name
    ).join(Chat).where(
        User.id.not_in(
            CustomGroupMember.select(
                CustomGroupMember.user
            ).join(CustomGroup).join(Chat).where(
                Chat.chat_id == target_chat_id,
                CustomGroup.name == target_custom_group_name
            )
        ),
        Chat.chat_id == target_chat_id
    )


def sql_list_chat_users_uin_in_custom_group(
        target_chat_id: str,
        target_custom_group_name: str,
        exclude: List[str] = []
) -> ModelSelect:

    return User.select(
        User.uin
    ).join(Chat).join(CustomGroup).where(
        User.id.in_(
            CustomGroupMember.select(
                CustomGroupMember.user
            ).join(CustomGroup).join(Chat).where(
                Chat.chat_id == target_chat_id,
                CustomGroup.name == target_custom_group_name
            )
        ),
        User.uin.not_in(exclude),
        Chat.chat_id == target_chat_id,
        CustomGroup.name == target_custom_group_name
    )


def sql_list_chat_users_uin_not_in_custom_group(
        target_chat_id: str,
        target_custom_group_name: str
) -> ModelSelect:

    return User.select(
        User.uin
    ).join(Chat).where(
        User.id.not_in(
            CustomGroupMember.select(
                CustomGroupMember.user
            ).join(CustomGroup).join(Chat).where(
                Chat.chat_id == target_chat_id,
                CustomGroup.name == target_custom_group_name
            )
        ),
        Chat.chat_id == target_chat_id
    )
