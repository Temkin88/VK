import datetime
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

from requests_ratelimiter import LimiterAdapter

import requests
import pathlib
import peewee

from loguru import logger
from pyvkteamsclient.stentor.methods import Client
from pyvkteamsclient.client import DesktopClient
from faker import Faker
from urllib3.exceptions import InsecureRequestWarning

from db.db import AccountInfo, ChatInfo, MessageInfo, ThreadInfo, AttachmentInfo, AttachmentThreadInfo, AccountStentorInfo


url = "gpuat-vkteams.dev.onprem.ru"


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class StentorClient(Client):
    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)


fake = Faker("en_US")
Faker.seed(0)


# Получение информации из myteaam-config
def get_account_data(url_main):
    accounts_data = {
        "SANDBOX": {
            'im_api': requests.get(f'https://{url_main}/myteam-config.json').json(),
            "accounts": [
                {
                    "autotest": True,
                    "password": "ONPREM",
                    "username": "autotest001@autotest.clients"
                },
                {
                    "autotest": True,
                    "password": "ONPREM",
                    "username": "autotest002@autotest.clients"
                }
            ],
        }
    }

    return accounts_data['SANDBOX']['im_api']


# Генерируем наименоваание аккаунта
def gen_email():
    return uuid.uuid4().hex[9:] + "@autotest.clients"


def set_rate_limit(session, url_path: str, limit_second: Optional[int] = None, limit_minutes: Optional[int] = None):
    accounts = get_account_data(url_main=url)
    adapter = LimiterAdapter(per_second=limit_second) if limit_second else LimiterAdapter(per_minute=limit_minutes)
    session.mount("/".join([f"{accounts['api-urls']['main-api']}/api/v{accounts['api-version']}", url_path]), adapter)


# Создание session
def get_session():
    web_url = get_account_data(url_main=url)["templates-urls"]["web-view"].replace("/view.html", "")

    with requests.Session() as session:
        session.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/113.0.0.0 Safari/537.36",
            "Referer": web_url,
            "Sec-Ch-Ua": '"Google Chrome";v="113", ' '"Chromium";v="113", ' '"Not-A.Brand";' 'v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS",
        }
        session.verify = False
        return session


session = get_session()


# Создание аккаунта в Stentor
def create_account_stentor(session):
    accounts = get_account_data(url_main=url)
    stentor_url = accounts['api-urls']['main-api'].replace("u", "stentor", 1)
    stentor = StentorClient(session, api_url=stentor_url)

    user_info = {
        "firstName": fake.first_name(),
        "middleName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": gen_email(),
        "phone": fake.phone_number(),
        "domainID": "test_domain",
        "disable": ["mail", "calendar", "teambox"],
    }

    try:
        logger.info(user_info["email"])
        time.sleep(3)
        stentor.biz_createUser(
            **user_info,
        )

    except Exception as e:
        logger.info(e)

    return user_info


def generation(user_info_email, c, session):
    t = datetime.datetime.now()
    logger.info(f"Начал {c}")
    accounts = get_account_data(url_main=url)

    # логинимся в VK Teams
    with DesktopClient(
        uin=user_info_email,
        session=session,
        api_url=accounts['api-urls']['main-api'],
        binary_api=accounts['api-urls']['main-binary-api'],
        api_ver=accounts['api-version'],
        fix_otp="ONPREM",
        env="SANDBOX",
    ) as client:
        account = AccountInfo.create(account=client.uin)

        path = pathlib.Path("support").joinpath("files").joinpath("common").joinpath("download.png")

        avatar_id = client.upload_file(path)

        # получаем рандомных пользователй и добавляем их в группу
        service_model = (
            AccountInfo.select(AccountInfo.account).order_by(peewee.fn.Random()).limit(10)
        )
        service = [i.account for i in service_model]

        for _ in range(11):
            name = f"Test {uuid.uuid4().hex}"
            about = f"Test description {uuid.uuid4().hex}"
            rules = "Test rules"
            public = True
            join_moderation = True
            default_role = "member"

            # создаем группу
            chat_id = client.create_chat(
                name=name,
                avatarId=avatar_id,
                members=service,
                about=about,
                rules=rules,
                public=public,
                joinModeration=join_moderation,
                defaultRole=default_role,
            )
            chat = ChatInfo.create(chat_id=chat_id, account=account)

            # Загружаем аттачи и отправляем в чат
            common_file = [str(i) for i in pathlib.Path("support").joinpath("files").joinpath("common").glob("*.*")]
            for file in common_file:
                file_id, file_url = client.upload_file(
                    file_path=file,
                )

                client.send_basic_message(
                    sn=chat_id,
                    text=file_url,
                )
                AttachmentInfo.create(attach_id=file_id, account=account)

            for _ in range(11):
                # пишем сообщшение в группу
                msg_id = client.send_basic_message(
                    sn=chat_id,
                    text=f"test{uuid.uuid4().hex}",
                )
                message = MessageInfo.create(message_id=msg_id, chat=chat)

                # Добавляем тред
                response = client.rapi_thread_add(
                    chatId=chat_id,
                    messageId=msg_id,
                )
                thread_id = response["results"]["threadId"]

                thread = ThreadInfo.create(thread_id=thread_id, message=message)

                # Отправляем сообщение в тред
                client.send_basic_message(
                    sn=thread_id,
                    text="Test msg to thread",
                )
                common_file = common_file[:4]
                for file in common_file:
                    file_id, file_url = client.upload_file(
                        file_path=file,
                    )

                    client.send_basic_message(
                        sn=chat_id,
                        text=file_url,
                    )
                    AttachmentThreadInfo.create(attach_thread_id=file_id, thread=thread)
    t_out = datetime.datetime.now() - t
    logger.info(f"Закончил {c}, время на прогон: {t_out}")


if __name__ == '__main__':
    for i in range(101):
        acc_stentor = create_account_stentor(session)
        AccountStentorInfo.create(account_stentor=acc_stentor['email'])

    service_model = (
        AccountStentorInfo.select(AccountStentorInfo.account_stentor)
    )
    service_info = [i.account_stentor for i in service_model]

    with ThreadPoolExecutor(max_workers=10) as executor:
        t = datetime.datetime.now()
        try:
            futures = [executor.submit(generation, value, index, session) for index, value in enumerate(service_info)]
            results = [future.result() for future in futures]

            t_out = datetime.datetime.now() - t
            logger.info(t_out)
        except Exception as e:
            logger.info(f"Произошла ошибка: {e}")
