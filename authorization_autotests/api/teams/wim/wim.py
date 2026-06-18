import time
from typing import Optional
from uuid import uuid1

from ...client.http_client import HttpClient


class WimMethods(HttpClient):
    def getReqId(self) -> str:
        """
        Генерация уникального ID запроса
        :return: str
        """
        return str(uuid1())

    def wim_aim_startSession_with_SSO(
            self,
            url,
            token,
            devId,
            language,
            client_name,
            client_version,
            client_build_number,
            device_id,
            assert_caps,
            interest_caps,
    ) -> dict:
        """
        Метод используется для создания пользовательской сессии,
        в рамках которой в дальнейшем выполняются запросы,
        требующие идентификатор сессии - aimsid.
        Также метод возвращает fetchBaseURL,
        используемый клиентом в дальнейшем для получения событий от сервера.
        Кроме того, метод позволяет подписаться на события,
        доставляемые при помощи push-уведомлений,
        и получить информацию о пользователе, выполнившем вход в приложение.

        Параметры сессии в дальнейшем могут быть изменены
        при помощи метода /wim/aim/setSessionParam

        Для завершения начатой сессии следует использовать
        метод /wim/aim/endSession
        :return: тело ответа сервера
        """
        data = {
            "a": token,
            "k": devId,
            "ts": int(time.time()),
            "sessionTimeout": 7200,
            "view": "online",
            "mobile": False,
            "events": ",".join(
                [
                    "myInfo",
                    "presence",
                    "buddylist",
                    "typing",
                    "hiddenChat",
                    "hist",
                    "mchat",
                    "sentIM",
                    "imState",
                    "dataIM",
                    "offlineIM",
                    "userAddedToBuddyList",
                    "service",
                    "lifestream",
                    "apps",
                    "permitDeny",
                    "diff",
                    "webrtcMsg",
                ],
            ),
            "includePresenceFields": ",".join(
                [
                    "aimId",
                    "iconId",
                    "bigIconId",
                    "largeIconId",
                    "displayId",
                    "friendly",
                    "offlineMsg",
                    "state",
                    "statusMsg",
                    "userType",
                    "phoneNumber",
                    "cellNumber",
                    "smsNumber",
                    "workNumber",
                    "otherNumber",
                    "capabilities",
                    "ssl",
                    "abPhoneNumber",
                    "moodIcon",
                    "lastName",
                    "abPhones",
                    "abContactName",
                    "lastseen",
                    "mute",
                    "counterEnabled",
                    "livechat",
                    "official",
                    "public",
                    "autoAddition",
                    "readonly",
                    "nick",
                    "bot",
                ],
            ),
            "language": language,
            "clientName": client_name,
            "clientVersion": client_version,
            "buildNumber": client_build_number,
            "deviceId": device_id,
        }

        if assert_caps is not None:
            data["assertCaps"] = (",".join(assert_caps[0]))

        if interest_caps is not None:
            data["interestCaps"] = ",".join(interest_caps[0])

        return self.post(
            url + "/wim/aim/startSession",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Bearer {token}",
            },
            data=data,
            allow_redirects=False
        )

    def wim_aim_startSession(
            self,
            url,
            api_version,
            token,
            devId,
            language,
            client_name,
            client_version,
            client_build_number,
            device_id,
            assert_caps,
            interest_caps,
            subscriptions: Optional[list[dict]]=None,
    ) -> dict:
        """
        Метод используется для создания пользовательской сессии,
        в рамках которой в дальнейшем выполняются запросы,
        требующие идентификатор сессии - aimsid.
        Также метод возвращает fetchBaseURL,
        используемый клиентом в дальнейшем для получения событий от сервера.
        Кроме того, метод позволяет подписаться на события,
        доставляемые при помощи push-уведомлений,
        и получить информацию о пользователе, выполнившем вход в приложение.

        Параметры сессии в дальнейшем могут быть изменены
        при помощи метода /wim/aim/setSessionParam

        Для завершения начатой сессии следует использовать
        метод /wim/aim/endSession
        :return: тело ответа сервера
        """
        data = {
            "a": token,
            "k": devId,
            "ts": int(time.time()),
            "sessionTimeout": 7200,
            "view": "online",
            "mobile": False,
            "events": ",".join(
                [
                    "myInfo",
                    "presence",
                    "buddylist",
                    "typing",
                    "hiddenChat",
                    "hist",
                    "mchat",
                    "sentIM",
                    "imState",
                    "dataIM",
                    "offlineIM",
                    "userAddedToBuddyList",
                    "service",
                    "lifestream",
                    "apps",
                    "permitDeny",
                    "diff",
                    "webrtcMsg",
                ],
            ),
            "includePresenceFields": ",".join(
                [
                    "aimId",
                    "iconId",
                    "bigIconId",
                    "largeIconId",
                    "displayId",
                    "friendly",
                    "offlineMsg",
                    "state",
                    "statusMsg",
                    "userType",
                    "phoneNumber",
                    "cellNumber",
                    "smsNumber",
                    "workNumber",
                    "otherNumber",
                    "capabilities",
                    "ssl",
                    "abPhoneNumber",
                    "moodIcon",
                    "lastName",
                    "abPhones",
                    "abContactName",
                    "lastseen",
                    "mute",
                    "counterEnabled",
                    "livechat",
                    "official",
                    "public",
                    "autoAddition",
                    "readonly",
                    "nick",
                    "bot",
                ],
            ),
            "language": language,
            "clientName": client_name,
            "clientVersion": client_version,
            "buildNumber": client_build_number,
            "deviceId": device_id,
        }
        if subscriptions:
            data["subscriptions"] = subscriptions

        if assert_caps is not None:
            data["assertCaps"] = (",".join(assert_caps[0]))

        if interest_caps is not None:
            data["interestCaps"] = ",".join(interest_caps[0])

        return self.post(
            url=url + f"/api/v{api_version}/wim/aim/startSession",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            params=data,
            allow_redirects=False,
        )

    def wim_aim_endSession(self, aimsid, url, api_version) -> dict:
        """
        Метод используется для завершения сессии,
        начатой посредством вызова метода /wim/aim/startSession
        :return: тело ответа сервера
        """
        return self.post(
            url=url + f"/api/v{api_version}/wim/aim/endSession",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={"r": self.getReqId, "aimsid": aimsid},
        )

    def wim_auth_clientLogin(self, url, pwd: str, uin, devId, tokenType: str = "longterm") -> dict:
        """
        Устаревшая авторизация
        :return: тело ответа сервера
        """
        return self.post(
            url + "/wim/auth/clientLogin",
            params={
                "s": uin,
                "k": devId,
                "pwd": pwd,
                "devId": devId,
                "tokenType": tokenType,
            },
            allow_redirects=False,
        ).json()

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
            json={"pwd": 1},
            allow_redirects=False,
        )

    def messenger_auth_withSession(
            self,
            silent_token,
            uin,
            api_version,
            url,
            devId,
            language,
            client_name,
            client_version,
            client_build_number,
            device_id,
            subscriptions: Optional[list[dict]]=None,) -> dict:
        """
        Устаревшая авторизация
        :return: тело ответа сервера

        """
        data = {
            "k": devId,
            "ts": int(time.time()),
            "sessionTimeout": 7200,
            "view": "online",
            "mobile": False,
            "events": ",".join(
                [
                    "myInfo",
                    "presence",
                    "buddylist",
                    "typing",
                    "hiddenChat",
                    "hist",
                    "mchat",
                    "sentIM",
                    'imState',
                    "dataIM",
                    "offlineIM",
                    "userAddedToBuddyList",
                    "service",
                    "lifestream",
                    "apps",
                    "permitDeny",
                    "diff",
                    "webrtcMsg"
                ],
            ),
            "includePresenceFields": ",".join(
                [
                    "aimId",
                    "displayId",
                    "friendly",
                    "friendlyName",
                    "state",
                    "userType",
                    "statusMsg",
                    "statusTime",
                    "ssl",
                    "mute",
                    "counterEnabled",
                    "abContactName",
                    "abPhoneNumber",
                    "abPhones",
                    "official",
                    "quiet",
                    "autoAddition",
                    "largeIconId",
                    "nick",
                    "userState",
                ],
            ),
            "userSn": uin,
            "trigger": "normalLogin",
            "language": language,
            "clientName": client_name,
            # "clientVersion": client_version,
            # "buildNumber": client_build_number,
            "deviceId": device_id,
        }
        if subscriptions:
            data["subscriptions"] = subscriptions

        data["assertCaps"] = "094613584C7F11D18222444553540000,0946135C4C7F11D18222444553540000,0946135b4c7f11d18222444553540000,0946135E4C7F11D18222444553540000,AABC2A1AF270424598B36993C6231952,1f99494e76cbc880215d6aeab8e42268,A20C362CD4944B6EA3D1E77642201FD8,B5ED3E51C7AC4137B5926BC686E7A60D,094613504c7f11d18222444553540000,094613514c7f11d18222444553540000,094613564c7f11d18222444553540000,094613503c7f11d18222444553540000"

        data["interestCaps"] = "8eec67ce70d041009409a7c1602a5c84,094613504c7f11d18222444553540000,094613514c7f11d18222444553540000,094613564c7f11d18222444553540000"

        return self.post(
            url=url + f"/api/v{api_version}/messenger/auth/withSession",
            headers={"Content-Type": "application/json"},
            json={
                "context": data,
                "silent_token": silent_token
            },
            allow_redirects=False,
        ).json()