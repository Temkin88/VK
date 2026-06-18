import json
import logging
import re
import time
import uuid

from typing import Optional, Literal, Dict, List
from urllib.parse import urlparse, parse_qsl
from uuid import uuid1

import httpx
from bs4 import BeautifulSoup
from imap_tools import AND, MailBox

from api.ABC.abstract_client import AbstractLoginAdapter
from api.teams.idm.idm_auth import IdmAuthMethod
from api.teams.idm.idm_provider import IdmProviderMethod
from api.teams.rapi.messages import MessagesMethods
from api.teams.rapi.search import SearchMethods
from api.teams.wim.wim import WimMethods
from api.ws.biz.biz_authorization import MethodBiz
from api.ws.ws import MethodWs, WSUser

logger = logging.getLogger(__name__)

class UserClientWS(MethodWs):
    __metaclass__ = AbstractLoginAdapter
    def __init__(
            self,
            base_url: str,
            username: str,
            password: str,
            login_adapter: "AbstractLoginAdapter",
            **kwargs
    ):
        super().__init__(base_url=base_url)
        self.access_token = None
        self.login_adapter = login_adapter
        self.base_url = base_url
        self.username = username
        self.password = password

        self.http_session.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "QtWebEngine/6.8.3 "
                          "Chrome/122.0.0.0 Safari/537.36",
            "Referer": self.base_url,
            "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS"

        })

    def act_token(self, url):
        response = self.get(url + '/jsapi/token').json()
        return response["token"]

    def login(self):
        auth_url = self.base_url.replace("://", "://auth.", 1)
        e_url = self.base_url.replace("://", "://e.", 1)
        act_token = self.act_token(url=auth_url)

        self.http_session.cookies.update(
            {
                "act": act_token,
            }
        )

        login_payload = self.http_session.post(
            url= auth_url + "/cgi-bin/auth?platform=web&project=login",
            params={
                "username": self.username,
                "Login": self.username,
                "password": self.password,
                "Password": self.password,
                "new_auth_form": 1,
                "FromAccount": "opener=account&twoSteps=1",
                "act_token": act_token,
                "page": e_url + "/inbox",
                "lang": "ru_RU",
            },
            allow_redirects=True,
        )

        login_payload.raise_for_status()

        url = f"{auth_url}/cgi-bin/auth"
        response = self.http_session.post(
            url=url,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=login_payload,
            allow_redirects=True,
        )

        # # Обработка редиректа после логина
        # redirect_after_login = response.headers.get("Location")
        #
        # # Шаг 3: Получение токена через GET-запрос
        # self.http_session.get(redirect_after_login, allow_redirects=False)

        # Шаг 4: Получение информации о пользователе

        response = self.http_session.get(url= f"{auth_url}/sdc?from={e_url}/api/v1/user/short")

        response_json = response.json()
        token = response_json.get("body").get("token")

        self.access_token = token
        return self.http_session

    def auth_check(self):
        auth_url = self.base_url.replace("://", "://auth.", 1)
        return self.get(auth_url + f"/cgi-bin/auth?mac=1&Login={self.username}&_=1776108572070", allow_redirects=True).json()


class UserClientWSSSO(MethodWs):
    __metaclass__ = AbstractLoginAdapter
    def __init__(
            self,
            base_url: str,
            username: str,
            password: str,
            login_adapter: "AbstractLoginAdapter",
            **kwargs
    ):
        super().__init__(base_url=base_url)
        self.login_adapter = login_adapter
        self.base_url = base_url
        self.username = username
        self.password = password

        self.http_session.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "QtWebEngine/6.8.3 "
                          "Chrome/122.0.0.0 Safari/537.36",
            "Referer": self.base_url,
            "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS"

        })

    def act_token(self, url):
        response = self.get(url + '/jsapi/token').json()
        return response["token"]

    def login(self):
        auth_url = self.base_url.replace("://", "://auth.", 1)
        e_url = self.base_url.replace("://", "://e.", 1)
        act_token = self.act_token(url=auth_url)

        self.http_session.cookies.update(
            {
                "act": act_token,
            }
        )
        import base64
        import requests
        import gssapi

        url = "https://vkwm-01-pub.release.vkwm.ru"
        host = "vkwm-01-pub.release.vkwm.ru"  # hostname из URL

        name = gssapi.Name(f"HTTP/{host}", name_type=gssapi.NameType.hostbased_service)

        ctx = gssapi.SecurityContext(name=name, usage="initiate")

        out_token = ctx.step()

        hdr = "Negotiate " + base64.b64encode(out_token).decode("ascii")

        r = requests.get(url, headers={"Authorization": hdr})
        # kerberos_auth = HTTPKerberosAuth(
        #     force_preemptive=True,
        #     hostname_override="vkwm-01-pub.release.vkwm.ru",
        #     principal="vkwm-01-pub.release.vkwm.ru@AD2013.ON-PREMISE.RU",
        #     # password=,
        #     mutual_authentication=OPTIONAL
        # )

        response = self.http_session.get(
            url= auth_url + f"/cgi-bin/oauth2_keycloak?page={e_url}",
            headers={"Authorization": hdr},
            allow_redirects=False,
        )

        response = self.http_session.get(
            url=response.headers["location"],
            headers={"Authorization": hdr},
            verify=False,
        )

        # # Получение URL из формы авторизации в keycloak
        # soup = BeautifulSoup(response.text, "html.parser")
        # action_url = soup.find(id="kc-form-login").attrs["action"]
        response.raise_for_status()

    def auth_check(self):
        auth_url = self.base_url.replace("://", "://auth.", 1)
        return self.get(auth_url + f"/cgi-bin/auth?mac=1&Login={self.username}&_=1776108572070", allow_redirects=True).json()



class UserClientTeamsOTP(MethodWs, WimMethods, SearchMethods, MessagesMethods):
    __metaclass__ = AbstractLoginAdapter
    def __init__(
            self,
            api_url: str,
            api_ver: int,
            uin: str,
            password: str,
            login_adapter: "AbstractLoginAdapter",
            org_struct_admin_token: Optional[str] = "tr-gajEkwov-akesadmin",
            imap_url: Optional[str] = None,
            assert_caps: Optional[list[str]] = None,
            interest_caps: Optional[list[str]] = [  # noqa
                "8eec67ce70d041009409a7c1602a5c84",
                "094613504c7f11d18222444553540000",
                "094613514c7f11d18222444553540000",
                "094613564c7f11d18222444553540000"
            ],
            **kwargs
    ):
        super().__init__(base_url=api_url)
        self.fetch_url = None
        self.session_started = None
        aimsid = None
        self.login_adapter = login_adapter
        self.api_url = api_url
        self.api_ver = api_ver
        self.token: Optional[str] = None
        self.assert_caps = assert_caps or [
            "094613584C7F11D18222444553540000",
            "0946135C4C7F11D18222444553540000",
            "0946135b4c7f11d18222444553540000",
            "0946135E4C7F11D18222444553540000",
            "AABC2A1AF270424598B36993C6231952",
            "1f99494e76cbc880215d6aeab8e42268",
            "A20C362CD4944B6EA3D1E77642201FD8",
            "B5ED3E51C7AC4137B5926BC686E7A60D",
            "094613504c7f11d18222444553540000",
            "094613514c7f11d18222444553540000",
            "094613564c7f11d18222444553540000",
            "094613503c7f11d18222444553540000"
        ],
        self.interest_caps = interest_caps,
        self.language: Literal["en-GB", "en-US", "ru-RU", "de-DE", "pt-PT"] = "ru-RU",
        self.uin = uin
        self.password = password
        self.imap_url = imap_url
        self.http_session.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "QtWebEngine/6.8.3 "
                          "Chrome/122.0.0.0 Safari/537.36",
            "Referer": self.api_url,
            "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS"

        })
        if "icq" in api_url:
            self.devId = "ic1nmMjqg7Yu-0hL"
            self.app = "icq"
        elif "myteam.vmailru" in api_url:
            self.devId = "ic1Go8AKqTJ-9QIQ"
            self.app = "vkteams"
        else:
            self.devId = "on2fah4R-linux"
            self.app = "vkteams"

        self.client_name = "VK Teams"
        self.client_version = "23.1.0.1"
        self.client_build_number = "1"
        self.device_id = str(uuid1())
        self.org_struct_admin_token = org_struct_admin_token

    def restart_session(self, subscriptions: Optional[list[dict]]=None):
        """
        Метод для рестарта сессии
        """
        result = self.wim_aim_startSession(
            url=self.api_url,
            api_version=self.api_ver,
            token=self.token,
            devId=self.devId,
            language=self.language[0],
            client_name=self.client_name,
            client_version=self.client_version,
            client_build_number=self.client_build_number,
            device_id=self.device_id,
            assert_caps=self.assert_caps,
            interest_caps=self.interest_caps,
            subscriptions=subscriptions
        ).json()
        aimsid = result["response"]["data"]["aimsid"]
        self.fetch_url = result["response"]["data"]["fetchBaseURL"]
        self.session_started = True

        return aimsid, self.fetch_url, self.session_started, result["response"]["statusCode"]

    def wim_auth_clientLoginFirst(self, tokenType: str = "otp_via_email") -> dict:
        """
        Устаревшая авторизация
        :return: тело ответа сервера
        """
        return self.post(
            url=self.api_url + "/wim/auth/clientLogin",
            headers={"Content-Type": "application/json"},
            params={
                "s": self.uin,
                "pwd": 1,
                "devId": self.devId,
                "tokenType": tokenType,
            },
            allow_redirects=False,
            timeout=5,
        )

    def get_otp_from_mail(self, email: str, password: str, ) -> str:
        domain = email.split("@")[1]
        auth = WSUser({"email": email,
                       "password": password,
                       "login": email,
                       "gender": "men",
                       "domain": domain,
                       "firstname": "qweqwe",
                       "lastname": "qweqwe",
                       "full_name": "asdasdasdasdasdasd"})
        msg = None
        MAX_RETRIES = 12
        for i in range(MAX_RETRIES):
            msg = auth.get_last_unread_email()['body']['newest_unread_message']['snippet']
            if "Вы зарегистрированы в Администрирование." in msg:
                self.wim_auth_clientLoginFirst()
                time.sleep(5)
            elif "Одноразовый пароль для доступа к VK Teams:" in msg:
                print(f"Шаг: {i}")
                break

        otp_token = re.findall(r"[A-Z0-9]{6}", msg)[-1]
        return otp_token

    def get_otp_token_from_mail_local(self, password: str, imap_url: str, invoke_token: bool = False):
        self.logger.debug(f"password: {password}, imap_url: {imap_url}, invoke_token: {invoke_token}")

        with MailBox(imap_url).login(username=self.uin, password=password) as mailbox:
            for msg in mailbox.fetch(AND(seen=False)):
                self.logger.debug(msg)
        if invoke_token:
            self.wim_auth_clientLoginFirst()

        otp_token = None

        with MailBox(imap_url).login(username=self.uin, password=password) as mailbox:
            for i in range(5):
                for msg in mailbox.fetch(AND(seen=False)):
                    self.logger.info(f"{msg.date} - {msg.subject}: {msg.text}")
                    otp_token = re.findall(r"[A-Z0-9]{6}", msg.text)[-1]
                if otp_token is not None:
                    self.logger.info(f"OTP Token: {otp_token}")
                    break
                time.sleep(i)

            assert otp_token, "OTP Token not found in incoming messages"

        return otp_token

    def hooks_after_user_auth(self):
        print("RealUserClient -> real_method")
        self.hooks_after_user_auth()

    def login(self, subscriptions: Optional = None, fix_otp: bool = True):
        self.wim_auth_clientLoginFirst()

        if fix_otp:
            result = self.wim_auth_clientLogin(url=self.api_url, pwd=self.password, uin=self.uin, devId=self.devId)
        else:
            token = self.get_otp_from_mail(email=self.uin, password=self.password)
            # token = self.get_otp_token_from_mail_local(password=self.password, imap_url=self.imap_url, invoke_token=True)
            result = self.wim_auth_clientLogin(url=self.api_url, pwd=token, uin=self.uin, devId=self.devId)
        login_data = result["response"]["data"]
        self.token = login_data["token"]["a"]
        print(f"base64: {self.token}")
        return self.restart_session(subscriptions)


class UserClientTeamsSSO(IdmAuthMethod, WimMethods):
    __metaclass__ = AbstractLoginAdapter
    def __init__(
            self,
            api_url: str,
            api_ver: int,
            uin: str,
            email_password: str,
            login_adapter: "AbstractLoginAdapter",
            org_struct_admin_token: Optional[str] = "tr-gajEkwov-akesadmin",
            assert_caps: Optional[list[str]] = None,
            interest_caps: Optional[list[str]] = [  # noqa
                "8eec67ce70d041009409a7c1602a5c84",
                "C094613504c7f11d18222444553540000",
                "C094613514c7f11d18222444553540000",
                "C094613564c7f11d18222444553540000",
                "8eec67ce70d041009409a7c1602a5c84",
                "094613504c7f11d18222444553540000",
                "094613514c7f11d18222444553540000",
                "094613503c7f11d18222444553540000",
            ],
            **kwargs
    ):
        super().__init__(base_url=api_url)
        self.login_adapter = login_adapter
        self.api_url = api_url
        self.api_ver = api_ver
        self.token: Optional[str] = None
        self.assert_caps = assert_caps or [
            "094613584C7F11D18222444553540000",
            "0946135C4C7F11D18222444553540000",
            "0946135b4c7f11d18222444553540000",
            "0946135E4C7F11D18222444553540000",
            "AABC2A1AF270424598B36993C6231952",
            "1f99494e76cbc880215d6aeab8e42268",
            "A20C362CD4944B6EA3D1E77642201FD8",
            "B5ED3E51C7AC4137B5926BC686E7A60D",
            "094613504c7f11d18222444553540000",
            "094613514c7f11d18222444553540000",
            "094613564c7f11d18222444553540000",
            "094613503c7f11d18222444553540000",
            "094613504c7f11d18222444553540000",
            "094613514c7f11d18222444553540000",
            "094613503c7f11d18222444553540000",
            "094613534c7f11d18222444553540000",
            "094613544c7f11d18222444553540000",
            "094613594c7f11d18222444553540000",
            "0946135b4c7f11d18222444553540000",
            "0946135a4c7f11d18222444553540000",
            "0946135c4c7f11d18222444553540000",
            "0946135e4c7f11d18222444553540000",
            "1f99494e76cbc880215d6aeab8e42268",
            "0946135d4c7f11d18222444553540000",
            "a20c362cd4944b6ea3d1e77642201fd8",
        ],
        self.interest_caps = interest_caps,
        self.language: Literal["en-GB", "en-US", "ru-RU", "de-DE", "pt-PT"] = "ru-RU"
        self.uin = uin
        self.email_password = email_password
        if "icq" in api_url:
            self.devId = "ic1nmMjqg7Yu-0hL"
            self.app = "icq"
        elif "myteam.vmailru" in api_url:
            self.devId = "ic1Go8AKqTJ-9QIQ"
            self.app = "vkteams"
        else:
            self.devId = "on2fah4R-linux"
            self.app = "vkteams"

        self.client_name = "VK Teams"
        self.client_version = "23.1.0.1"
        self.client_build_number = "1"
        self.device_id = str(uuid1())
        self.org_struct_admin_token = org_struct_admin_token

    def restart_session_with_SSO(self):
        """
        Метод для рестарта сессии
        """
        result = self.wim_aim_startSession_with_SSO(
            url=self.api_url,
            token=self.token,
            devId=self.devId,
            language=self.language,
            client_name=self.client_name,
            client_version=self.client_version,
            client_build_number=self.client_build_number,
            device_id=self.device_id,
            assert_caps=self.assert_caps,
            interest_caps=self.interest_caps,
        ).json()

        aimsid = result["response"]["data"]["aimsid"]
        fetch_url = result["response"]["data"]["fetchBaseURL"]
        session_started = True

        return aimsid, fetch_url, session_started

    # if self.env == "SANDBOX" and self.sso:
    #     self.sign_in_with_sso(redirect=self.api_url.replace("u", "webim", 1))
    # elif self.env in ["SAAS", "PRE_SAAS"] and self.sso:
    #     self.sign_in_with_sso(redirect="https://myteam.mail.ru/webim/")
    # elif self.env == "PRE_TARM" and self.swa:
    #     self.sign_in_with_swa(redirect="https://webim.tppr.vmailru.net/")
    # elif self.env == "TARM" and self.swa:
    #     self.sign_in_with_swa(redirect="https://webim.armgs.team/")
    def auth_authorize(self):
        """
                Вход с использованием SSO через Keycloak
                """
        state = str(uuid.uuid4())
        webim_url = self.api_url.replace("u", "webim", 1)

        response = self.idm_auth_authorize(
            url=self.api_url,
            client_id=self.devId,
            response_type="code",
            scope="openid",
            state=state,
            login_hint=self.uin,
            redirect_uri=webim_url,
            _type="SSO",
        )

        # Получение кук в keycloak
        response = self.request(
            method="GET",
            url=response.headers["location"],  # noqa
            # url=response["history"][0]["url"],  # noqa
        )

        # Получение URL из формы авторизации в keycloak
        soup = BeautifulSoup(response.text, "html.parser")
        action_url = soup.find(id="kc-form-login").attrs["action"]

        # Авторизация в keycloak
        response = self.request(
            method="POST",
            url=action_url,
            data={
                "username": self.uin,
                "password": self.email_password,
            },
            allow_redirects=False,
        )

        # Вызов callback
        response = self.request(
            method="GET",
            url=response.headers["location"],  # noqa
            allow_redirects=False,
        )

        url = urlparse(response.headers["location"])  # noqa
        parsed_query = dict(parse_qsl(url.query))

        response = self.idm_auth_token(
            url=self.api_url,
            client_id=self.devId,
            client_secret=self.devId,
            grant_type="authorization_code",
            code=parsed_query["code"],
            state=state,
            redirect_uri="https://myteam.mail.ru/webim/",
            scope="openid",
        )
        response_json = json.loads(response.text)
        self.token = response_json["access_token"]
        self.refresh_token = response_json["refresh_token"]
        self.id_token = response_json["id_token"]
        self.token_type = response_json["token_type"]
        return self.token, self.refresh_token, self.refresh_token, self.id_token, self.token_type

    def sign_in_with_sso(self):
        """
        Вход с использованием SSO через Keycloak
        """
        self.auth_authorize()

        return self.restart_session_with_SSO()

    def with_session(self, subscriptions):
        token, *_ = self.auth_authorize()
        silent_token = self.idm_auth_token_silent(url=self.api_url, access_token=token, client_id="messenger",
                                                  grant_type="silent_token")

        response = self.messenger_auth_withSession(url=self.api_url,
                                        silent_token=silent_token['silent_token'],
                                        uin=self.uin,
                                        api_version=self.api_ver,
                                        devId=self.devId,
                                        language=self.language,
                                        client_name=self.client_name,
                                        client_version=self.client_version,
                                        client_build_number=self.client_build_number,
                                        device_id=self.device_id,
                                        subscriptions=subscriptions)

        return response

    def login(self):
        return self.sign_in_with_sso()


class UserClientTeamsSWA(IdmAuthMethod, IdmProviderMethod, WimMethods):
    __metaclass__ = AbstractLoginAdapter
    def __init__(
            self,
            api_url: str,
            api_ver: int,
            uin: str,
            email_password: str,
            redirect,
            login_adapter: "AbstractLoginAdapter",
            org_struct_admin_token: Optional[str] = "tr-gajEkwov-akesadmin",
            assert_caps: Optional[list[str]] = None,
            interest_caps: Optional[list[str]] = [  # noqa
                "8eec67ce70d041009409a7c1602a5c84",
                "C094613504c7f11d18222444553540000",
                "C094613514c7f11d18222444553540000",
                "C094613564c7f11d18222444553540000",
                "8eec67ce70d041009409a7c1602a5c84",
                "094613504c7f11d18222444553540000",
                "094613514c7f11d18222444553540000",
                "094613503c7f11d18222444553540000",
            ],
            **kwargs
    ):
        super().__init__(base_url=api_url)
        self.login_adapter = login_adapter
        self.api_url = api_url
        self.api_ver = api_ver
        self.redirect = redirect
        self.token: Optional[str] = None
        self.assert_caps = assert_caps or [
            "094613584C7F11D18222444553540000",
            "0946135C4C7F11D18222444553540000",
            "0946135b4c7f11d18222444553540000",
            "0946135E4C7F11D18222444553540000",
            "AABC2A1AF270424598B36993C6231952",
            "1f99494e76cbc880215d6aeab8e42268",
            "A20C362CD4944B6EA3D1E77642201FD8",
            "B5ED3E51C7AC4137B5926BC686E7A60D",
            "094613504c7f11d18222444553540000",
            "094613514c7f11d18222444553540000",
            "094613564c7f11d18222444553540000",
            "094613503c7f11d18222444553540000",
            "094613504c7f11d18222444553540000",
            "094613514c7f11d18222444553540000",
            "094613503c7f11d18222444553540000",
            "094613534c7f11d18222444553540000",
            "094613544c7f11d18222444553540000",
            "094613594c7f11d18222444553540000",
            "0946135b4c7f11d18222444553540000",
            "0946135a4c7f11d18222444553540000",
            "0946135c4c7f11d18222444553540000",
            "0946135e4c7f11d18222444553540000",
            "1f99494e76cbc880215d6aeab8e42268",
            "0946135d4c7f11d18222444553540000",
            "a20c362cd4944b6ea3d1e77642201fd8",
        ],
        self.interest_caps = interest_caps,
        self.language: Literal["en-GB", "en-US", "ru-RU", "de-DE", "pt-PT"] = "ru-RU",
        self.uin = uin
        self.email_password = email_password
        if "icq" in api_url:
            self.devId = "ic1nmMjqg7Yu-0hL"
            self.app = "icq"
        elif "myteam.vmailru" in api_url:
            self.devId = "ic1Go8AKqTJ-9QIQ"
            self.app = "vkteams"
        else:
            self.devId = "on2fah4R-linux"
            self.app = "vkteams"

        self.http_session.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "QtWebEngine/6.8.3 "
                "Chrome/122.0.0.0 Safari/537.36",
                "Referer": self.api_url,
                "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "macOS"

        })

        self.client_name = "VK Teams"
        self.client_version = "23.1.0.1"
        self.client_build_number = "1"
        self.device_id = str(uuid1())
        self.org_struct_admin_token = org_struct_admin_token

    def restart_session_with_SWA(self):
        """
        Метод для рестарта сессии
        """
        result = self.wim_aim_startSession_with_SSO(
            url=self.api_url,
            token=self.token,
            devId=self.devId,
            language=self.language,
            client_name=self.client_name,
            client_version=self.client_version,
            client_build_number=self.client_build_number,
            device_id=self.device_id,
            assert_caps=self.assert_caps,
            interest_caps=self.interest_caps,
        ).json()

        aimsid = result["response"]["data"]["aimsid"]
        fetch_url = result["response"]["data"]["fetchBaseURL"]
        session_started = True

        return aimsid, fetch_url, session_started

    def sign_in_with_swa(self, o2_client_id: str):
        """
        Вход с использованием SWA через Keycloak
        """

        state = str(uuid.uuid4())

        webim_url = self.api_url.replace("u", "webim", 1)
        o2_url = self.api_url.replace("u", "o2", 1)
        account_url = self.api_url.replace("u", "account", 1).replace("vkt-", "", 1)
        auth_url = self.api_url.replace("u", "auth", 1).replace("vkt-", "", 1)

        first_authorize_response = self.get(
            url=f"{self.api_url}/api/v{self.api_ver}/idm/auth/authorize",
            params={
                "client_id": self.devId,
                "response_type": "code",
                "scope": "openid",
                "state": state,
                "login_hint": self.uin,
                "redirect_uri": f"{webim_url}/?redirectAction=StromaAuthRedirect",
            },
            allow_redirects=True,
        )

        first_authorize_response.raise_for_status()

        second_authorize_response = self.get(
            url=f"{self.api_url}/api/v{self.api_ver}/idm/auth/authorize",
            params={
                "client_id": self.devId,
                "response_type": "code",
                "scope": "openid",
                "state": state,
                "login_hint": self.uin,
                "redirect_uri": f"{webim_url}/?redirectAction=StromaAuthRedirect",
                "type": "SWA",
            },
            allow_redirects=True,
        )

        parsed_url = urlparse(str(second_authorize_response.url))
        query = {key: value for key, value in [i.split("=") for i in parsed_url.query.split("&")]}  # noqa

        account_login_response = self.get(
            url=f"{account_url.replace("vkt-", "", 1)}/login",
            params={
                "opener": "o2",
                "x": "login",
                "page": second_authorize_response.url,
                "email": self.uin,
                "logo_target": "_blank",
                "signup_target": "_self",
                "remind_target": "_self",
                "cancel_page": f"{o2_url}/xlogin?"
                f"client_id={o2_client_id}&"
                f"response_type=code&"
                f"scope=&"
                f"redirect_uri={self.api_url}/api/v1/idm/auth/callback&"
                f"state={query['state']}&"
                f"login={self.uin}&"
                f"fail=1",
            },
            allow_redirects=True,
        )

        account_login_response.raise_for_status()

        lines = [line for line in account_login_response.text.splitlines() if "csrf" in line]

        data = json.loads(lines[0])

        act_token = data["csrf"]

        self.http_session.cookies.update(
            {
                "act": act_token,
            }
        )

        cgi_response = self.post(
            url=f"{auth_url}/cgi-bin/auth",
            params={"platform": "touch", "project": "login"},
            data={
                "username": self.uin,
                "Login": self.uin,
                "password": self.email_password,
                "Password": self.email_password,
                "new_auth_form": 1,
                "FromAccount": "opener=o2&x=login&twoSteps=1&remind_target=_self",
                "act_token": act_token,
                "page": f"{o2_url}/login?"
                f"authid=mht9zny3.mri&"
                f"client_id={o2_client_id}&"
                f"from=o2&login={self.uin}&"
                f"redirect_uri={self.api_url}/api/v1/idm/auth/callback&"
                f"response_type=code&"
                f"scope=userinfo&"
                f"state={state}",
                "autotest": 1,
            },
            allow_redirects=False,
        )

        assert cgi_response.status_code == 302, f"{auth_url} responded with {cgi_response.status_code}"

        time.sleep(5)

        auth_response = self.get(
            url=cgi_response.headers.get("Location") or cgi_response.headers.get("location"),
            allow_redirects=True,
        )

        auth_response.raise_for_status()

        authorize_response = self.get(
            url=f"{self.api_url}/api/v{self.api_ver}/idm/auth/authorize",
            params={
                "client_id": self.devId,
                "response_type": "code",
                "scope": "openid",
                "state": state,
                "login_hint": self.uin,
                "redirect_uri": f"{webim_url}/?redirectAction=StromaAuthRedirect",
                "type": "SWA",
            },
            allow_redirects=True,
        )

        authorize_response.raise_for_status()

        parsed_url = urlparse(str(authorize_response.url))
        query = {key: value for key, value in [i.split("=") for i in parsed_url.query.split("&")]}  # noqa

        token_response = self.post(
            url=f"{self.api_url}/api/v{self.api_ver}/idm/auth/token",
            data={
                "client_id": self.devId,
                "client_secret": self.devId,
                "grant_type": "authorization_code",
                "code": query["code"],
                "state": state,
                "redirect_uri": webim_url,
                "scope": "openid",
            },
            allow_redirects=True,
        )

        response = token_response.json()

        self.http_session.headers.update({"Authorization": f"Bearer {response['access_token']}"})

        self.token = response["access_token"]
        self.refresh_token = response["refresh_token"]
        self.id_token = response["id_token"]
        self.token_type = response["token_type"]

        return self.restart_session_with_SWA()

    def login(self, o2_client_id="ncheipej6rzmtov6wa5b2uzzj3uuqfpt"):
        return self.sign_in_with_swa(o2_client_id=o2_client_id)


class BizAdminClient(MethodBiz):
    __metaclass__ = AbstractLoginAdapter
    def __init__(
        self,
        *,
        base_url: str,
        username: str,
        password: str,
        login_adapter: "AbstractLoginAdapter",
        cookies: Optional[httpx.Cookies] = None,
    ):
        super().__init__(base_url=base_url)
        self.base_url = base_url
        self.username = username
        self.password = password
        self.cookies = cookies
        self.login_adapter = login_adapter
    def __aenter__(self):
        if self.cookies is None:
            self.login()
        else:
            self.http_session.cookies = self.cookies

        self.http_session.headers.update({"referer": self.base_url})

        return self

    def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    def login(self):
        domain = self.base_url.replace("https://", "", 1)
        biz_base_url = self.base_url.replace("https://", "https://biz.", 1)
        account_base_url = self.base_url.replace("https://", "https://account.", 1)

        auth_base_url = self.base_url.replace("https://", "https://auth.", 1)

        self.http_session.request(method="GET", url=f"{biz_base_url}/login", params={"page": self.base_url})

        response = self.http_session.request(
            method="POST",
            url=f"{auth_base_url}/cgi-bin/auth",
            params={"from": "octavius", "platform": "web", "project": "login"},
            data={
                "username": self.username,
                "Login": self.username,
                "password": self.password,
                "Password": self.password,
                "saveauth": 1,
                "new_auth_form": 1,
                "act_token": self.http_session.cookies.get("act"),
                "lang": "en_US",
            },
        )

        response.raise_for_status()

        response = self.http_session.request(
            method="GET",
            url=f"{auth_base_url}/sdc",
            params={"from": f"{biz_base_url}/"},
            headers={"referer": f"{biz_base_url}/"},
        )

        response.raise_for_status()

        self.http_session.request(method="GET", url=f"{biz_base_url}/domains/{domain}/users/",
                                  headers={
                                      "Accept": "*/*",
                                      "Accept-Language": "ru",
                                      "Host": f"{biz_base_url}",
                                      "Referer": f"{biz_base_url}/",
                                      "Sec-Fetch-Dest": "document",
                                      "Sec-Fetch-Mode": "navigate",
                                      "Sec-Fetch-Site": "same-site",
                                  },
                                  allow_redirects=False)
        csrftoken = self.http_session.cookies.get("csrftoken")
        self.http_session.headers.update({"X-CSRFToken": csrftoken})
