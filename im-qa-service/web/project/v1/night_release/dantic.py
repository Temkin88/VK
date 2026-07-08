from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, Field, AnyHttpUrl


class OtpSuccessResponse(BaseModel):
    success: bool
    otp_token: str


class OtpFailResponse(BaseModel):
    success: bool = False
    error: str


class PhoneAccount(BaseModel):
    phone: str
    uin: str
    code: str


class UinAccount(BaseModel):
    username: str
    password: str
    autotest: bool = False


class MainUrls(BaseModel):
    main_api: AnyHttpUrl = Field(..., alias='main-api')
    binary_api: AnyHttpUrl = Field(..., alias='binary-api')


class ImApi(BaseModel):
    api_urls: Union[MainUrls] = Field(..., alias='api-urls')
    base_urls: dict[str, dict] = Field(..., alias='base-urls')
    template_urls: dict[str, str] = Field(..., alias='template-urls')


class FileLinks(BaseModel):
    sticker: str
    lotti: str
    photo: str
    voice: str


class Bot(BaseModel):
    token: str
    api_url_base: AnyHttpUrl


class ModelItem(BaseModel):
    accounts: Union[List[Union[PhoneAccount, UinAccount]], str]
    bot: Bot
    im_api: Union[ImApi, AnyHttpUrl]
    imap: Optional[str] = None
