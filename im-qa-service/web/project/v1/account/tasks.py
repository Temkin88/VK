from typing import Union

from web.project.logger import logger

from pyvkteamsclient.client import DesktopClient

from web.project.celery import celery_app


def test():
    logger.info('test')


def clean_client(
        json_model: dict[str, Union[str, int]]
):
    logger.info(
        f'Cleaning account: '
        f'ID {json_model.get("id")} uin {json_model.get("uin")}'
    )

    wrapper = DesktopClient(
        uin=json_model['uin'],
        phone=json_model['phone'],
        code=json_model['code'],
        api_url=json_model['api_url'],
        binary_api_url=json_model['api_url'].replace('https://u',
                                                       'https://ub'),
        fix_otp=json_model['password'],
        env='SANDBOX' if 'im-sandbox' in json_model['api_url'] else 'ICQ'
    )

    logger.info(wrapper)

    wrapper.fetch()

    wrapper.restore_privacy_settings()

    try:
        wrapper.fetch()

        for chat_id in [
            chat['aimId']
            for chat_list in wrapper.events[0]['eventData']['groups']
            for chat in chat_list['buddies']
        ]:
            wrapper.wim_buddyList_hideChat(buddy=chat_id)
            wrapper.wim_buddyList_removeBuddy(buddy=chat_id)
    except Exception as error:
        logger.error(error)

    if wrapper.env == 'SANDBOX':
        try:
            for thread in wrapper.iter_thread_list(page_size=50):
                try:
                    wrapper.rapi_thread_unsubscribe(
                        thread['threadId']
                    )
                except Exception as error:
                    logger.error(error)
        except Exception as error:
            logger.error(error)




@celery_app.task(name="clean_client")
def clean_client_task(
        json_model: dict[str, Union[str, int]],
        group_name: str,
        reset_all_sessions: bool = True
):
    return clean_client(json_model)
