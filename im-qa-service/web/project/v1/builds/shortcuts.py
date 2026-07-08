import os

import aioboto3
from aiohttp import ClientSession, BasicAuth, TCPConnector

from web.project.logger import logger
from pydantic import AnyHttpUrl

session = aioboto3.Session(
    aws_access_key_id='93eayBDR8hRx8PJcHupT5u',
    aws_secret_access_key='89RwV2xy4PUq59A8SwQh7bh34sLSQyH3oGGtX4jTfAYR'
)


@logger.catch
async def s3_upload_to_bucket(
        FILE_BODY: bytes,
        FILE_NAME: str,
        *folders
):
    folders = list(folders)
    folders.append(FILE_NAME)

    async with session.client('s3', endpoint_url='https://hb.bizmrg.com') as s3:
        await s3.put_object(
            Bucket='im.builds',
            Key='/'.join(folders),
            Body=FILE_BODY,
            ACL='public-read'
        )


@logger.catch
async def load_from_url_to_s3(
        JENKINS_URL: AnyHttpUrl,
        FILE_NAME: str,
        *folders
):
    async with ClientSession(
            auth=BasicAuth('imbuildbot', '11c6471423a3e8ce17e2a1174208f3da72'),
            connector=TCPConnector(verify_ssl=False)
    ) as client:
        async with client.get(JENKINS_URL) as response:
            content = await response.read()

    await s3_upload_to_bucket(
        content,
        FILE_NAME,
        *folders
    )


@logger.catch
async def send_build_text(
        TEXT: str
):
    async with ClientSession(
            base_url=os.getenv('BOT_API_URL'),
            connector=TCPConnector(verify_ssl=False)
    ) as client:
        await client.get(
            url='/bot/v1/messages/sendText',
            params={
                'token': os.getenv('BUILD_BOT_TOKEN'),
                'chatId': os.getenv('BUILD_CHAT'),
                'text': TEXT,
                'parseMode': "HTML"
            }
        )
