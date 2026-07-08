import time

import requests

from fastapi import APIRouter, Query
from fastapi.responses import ORJSONResponse

from pydantic import EmailStr, AnyHttpUrl

from imap_tools import MailBox, AND

from web.project.db import NightRelease, OTP_Token, OTP_Token_Pydantic
from web.project.logger import logger
from web.project.db import Account, Account_Pydantic
from web.project.v1.night_release.dantic import ModelItem, \
    OtpSuccessResponse

night_release_router = APIRouter(prefix='/night', tags=['nignt release'])


@night_release_router.get('/accounts/{env}')
async def get_accounts(env: str):

    data = await NightRelease.get(name=env)

    config = data.value

    if isinstance(config['im_api'], str):
        config['im_api'] = requests.get(config['im_api']).json()

    if isinstance(config['accounts'], str):

        accounts = []

        async for account in Account \
                .filter(group_name=config['accounts']) \
                .order_by('ts', 'count_used') \
                .limit(2):

            account.count_used += 1
            await account.save()

            accounts.append(
                (await Account_Pydantic.from_tortoise_orm(account)).dict()
            )

        config['accounts'] = accounts

    return ORJSONResponse(
        content={
            env: config
        }
    )


@night_release_router.get(
    path='/otp',
    responses={
        200: {
            "description": "Successful Response",
            "model": OtpSuccessResponse
        }
    }
)
async def get_otp(
        uin: EmailStr = Query(
            ...,
            description='UIN целевой учетки',
            example='v.korobov@corp.mail.ru'
        ),
        email: EmailStr = Query(
            None,
            description='e-mail учетки, если он отличается от UIN',
            example='v.korobov@corp.mail.ru'
        ),
        password: str = Query(
            ...,
            description='Пароль от почты'
        ),
        backend_url: AnyHttpUrl = Query(
            ...,
            description='URL API целевой инсталяции VK Teams',
            example='https://u.internal.myteam.mail.ru/api/v91'
        ),
        imap_url: str = Query(
            ...,
            description='Адрес IMAP-сервера почты',
            example='imap.mail.ru'
        ),
        invoke_token: bool = Query(
            True,
            description='Нужен ли первичный запрос токена'
        )
):
    """
    Ручка для получения OTP токена для входа в VK Teams
    """

    with MailBox(imap_url).login(
            username=email if email else uin,
            password=password
    ) as mailbox:
        for msg in mailbox.fetch(
                AND(seen=False)
        ):
            pass
    if invoke_token:
        result = requests.post(
            url=f'{backend_url}/wim/auth/clientLogin',
            params={
                "s": uin,
                "devId": "on2fah4R-mac",
                "tokenType": "otp_via_email",
                "pwd": "1"
            }
        )

        text = f'[{result.request.method}] {result.request.url}\n'

        text += '\n'.join([
            f'{k}: {v}' for k, v in result.request.headers.items()])

        text += '\n\n'

        text += f'Status code: {result.status_code}\n'

        text += '\n'.join([
            f'{k}: {v}' for k, v in result.headers.items()])

        text += '\n\n'

        text += result.text

        logger.info(text)

        result.raise_for_status()

        result = result.json()
        assert 200 <= result["response"]["statusCode"] < 300 \
               and result["response"]["statusText"] == "OK"

    otp_token = None

    with MailBox(imap_url).login(
            username=email if email else uin,
            password=password
    ) as mailbox:
        for i in range(5):
            for msg in mailbox.fetch(
                    AND(seen=False)
            ):
                logger.info(f'{msg.date} - {msg.subject}: {msg.text}')
                otp_token = msg.text.splitlines()[-1]
            if otp_token is not None:
                break
            time.sleep(i)

        assert otp_token, 'OTP Token not found in incoming messages'

        return ORJSONResponse(
            content={
                "success": True,
                "otp_token": otp_token
            }
        )


@night_release_router.post('/accounts')
async def post_accounts(configs: dict[str, ModelItem]):

    for key, value in configs.items():

        if await NightRelease.filter(name=key).exists():
            model = await NightRelease.get(name=key)
            model.value = value.json()
            await model.save()
        else:
            await NightRelease.create(name=key, value=value.json())


@night_release_router.post('/dev/otp')
async def post_otp(uin: str = Query(...)):

    if await OTP_Token.filter(uin=uin).exists():
        model = OTP_Token.filter(uin=uin).order_by("-id").first()
        return (await OTP_Token_Pydantic.from_queryset_single(model)).dict()
    else:
        return {
            'error': f"UIN {uin} not found"
        }
