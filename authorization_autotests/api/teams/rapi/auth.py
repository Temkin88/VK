from typing import Optional

from ...client.http_client import HttpClient


class AuthMethods(HttpClient):
    """
    Методы группы 'Авторизация' из https://im-docs.corp.mail.ru/
    """

    def rapi_auth_guest(self, name: str, scopes: list[str]):
        return self.post(
            url=url + f"/api/v{api_version}/rapi/auth/guest",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": getReqId,
                "params": {
                    "name": name,
                    "scopes": [f"call/{x}" for x in scopes],
                },
            },
        )

    def rapi_auth_oidc_authorize(self) -> dict:
        """
        Начать OpenID Connect авторизацию
        OIDC авторизация через IDP, зарегистрированный на сервере. Клиент должен вызывать этот метод из secure browser.
        :param redirectUri: Адрес, на который через redirect в параметрах запроса будет возвращён результат
        Example : myteam-messenger://webauth
        :param userAgent: userAgent приложения Example : VKTeams iOS user_id 22.6.0(221423) iOS_11.3.1 iPhone_20
        :param userSn: screenname пользователя, ОБЯЗАТЕЛЕН С РЕЛИЗА 23.2 Example : test@sandbox.local
        :return: тело ответа сервера
        """
        return self.get(
            url=url + f"/api/v{api_version}/rapi/auth/oidc/authorize",
            redirectUri=self.session.headers["Referer"],
            userAgent="VKTeams",
            userSn=self.uin,
            allow_redirects=False,
        )

    def rapi_auth_oidc_submitCode(self, state: str, code: str) -> dict:
        """
        Продолжить OpenID Connect авторизацию
        Вызывается автоматически через redirect от IDP по окончании первого этапа /rapi/auth/oidc/authorize.
        :param state: state, переданный сервером в параметры redirect на первом этапе
        Example : HGIbyBjILehYPRiEtLIm58n4lsDTaejq
        :param code: Код из OIDC механизма авторизации
        Example : 72c51c7a-41f7-4a3c-bf74-4530a328cfe2.a2d97302-18c7-4f1a-80d0-7fc3a3cf728f.a827434e-3a38-4f20-bd27
        -a5be40ac0130
        :return: тело ответа сервера
        """
        return self.get(url=url + f"/api/v{api_version}/rapi/auth/oidc/submitCode", state=state, code=code)

    def rapi_auth_is_strong_password(self, password: str):
        """
        Проверить надежность пароля
        Проверяет надежность пароля пользователя и что этот пароль не используется этим пользователеем сейчас.
        :param password: Пароль пользователя
        """
        return self.post(
            "rapi/auth/isStrongPassword",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": getReqId,
                "aimsid": aimsid,
                "params": {"password": password},
            },
        )

    def rapi_auth_webapp_session_start(self, password: str):
        return self.post(
            "rapi/auth/webapp/session/start",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": getReqId,
                "aimsid": aimsid,
                "params": {"password": password},
            },
        )

    def rapi_auth_send_сode(self, language: Optional[str] = "ru-RU", route: Optional[str] = "sms"):
        """
        Отправить проверочный код
        Отправляет проверочный код на номер указанный в phone. Возвращает идентификатор сессии sessionId, который в
        дальнейшем необходимо использовать в методах требующих проверку кода, например /rapi/auth/signIn или
        /rapi/auth/attachPhone.
        Телефонный номер phone передается клиентом в свободной форме и нормализуется на стороне сервера.
        Кроме телефона, необходимо передать идентификатор приложения devId (иногда называемый akes) и его наименование
        application, например: icq, agent или myteam.
        При необходимости, можно указать язык language для формирования сообщения с проверочным кодом. Язык задаётся в
        формате xx-YY, где xx - это язык соответствующий стандарту ISO 639-1, а YY - ISO 3166-1 alpha-2. Значение по
        умолчанию "en-GB".
        Метод позволяет указать желаемый метод отправки проверочного кода route, доступные варианты: sms - доставка
        числового кода через короткое сообщение; ivr - доставка кода через диктовку сообщения голосом; callui -
        доставка через "звонок-сброс", в этом случае пользователю будет необходимо ввести последние четыре цифры
        телефонного номера, с которого будет осуществлен звонок. По умолчанию используется метод доставки через смс.
        Сервер оставляет за собой возможность изменить метод доставки по причине невозможности отправки кода выбранным
        методом, фактический метод будет возвращен в поле results.route.
        :param phone: example: +79161234567 Телефонный номер пользователя
        :param application: example: icq Наименование приложения [ icq, agent, myteam ]
        param language: default: en-GB Язык для формирования сообщения с проверочным кодом
        param route: default: sms Желаемый метод отправки проверочного кода [ sms, ivr, callui ]
        """
        return self.post(
            "rapi/auth/sendCode",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": getReqId,
                "aimsid": aimsid,
                "params": {
                    "phone": self.phone,
                    "application": self.app,
                    "devId": self.devId,
                    "language": language,
                    "route": route,
                },
            },
        )

    def rapi_auth_sign_in(self, session_id: str):
        """
        Авторизоваться по телефону и проверочному коду
        Авторизовывает пользователя по телефону phone проверочному коду smsCode и идентификатору сессии sessionId
        которые были получены в ходе запроса /rapi/auth/sendCode. Также необходимо передать идентификатор приложения
        devId.
        Телефонный номер phone передается клиентом в свободной форме и нормализуется на стороне сервера.
        При получение results.settings.needFillProfile, клиенту необходимо показать диалог для заполнения профиля
        нового пользователя.
        :param phone: example: +79161234567 Телефонный номер пользователя
        :param sms_code: example: 123456 Проверочный код, полученный в ходе запроса /rapi/auth/sendCode
        :param session_id: example: 784fd34508a0dba62e4dd4c9a513c940 Идентификатор сессии, полученный в ходе запроса
        """
        return self.post(
            "rapi/auth/signIn",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": getReqId,
                "aimsid": aimsid,
                "params": {
                    "phone": self.phone,
                    "smsCode": self.code,
                    "devId": self.devId,
                    "sessionId": session_id,
                },
            },
        )

    def rapi_auth_sign_in_with_password(self, password: str):
        """
        Авторизоваться по логину и паролю
        Авторизовывает пользователя по логину login и паролю password. В зависимости от приложения логином может
        выступать либо uin, либо почтовый адрес пользователя. Также необходимо передать идентификатор приложения
        devId и его наименование application, например: icq, agent или myteam.
        Формат ответа соответствует /rapi/auth/signIn.
        :param login: Логин пользователя
        :param password: Пароль пользователя
        :param application: Наименование приложения
        """
        return self.post(
            "rapi/auth/signInWithPassword",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": getReqId,
                "aimsid": aimsid,
                "params": {
                    "login": self.uin,
                    "password": password,
                    "devId": self.devId,
                    "application": self.app,
                },
            },
        )

    def rapi_auth_attach_phone(self, session_id: str):
        """
        Привязать номер телефона
        Привязывает номер телефона phone к учетной записи sn. Проверка аутентификации происходит по проверочному
        коду smsCode и идентификатору сессии sessionId, которые были получены через /rapi/auth/sendCode.
        Телефонный номер phone передается клиентом в свободной форме и нормализуется на стороне сервера.
        :param phone: example: +79161234567 Телефонный номер пользователя
        :param sms_code: example: 123456 Проверочный код, полученный в ходе запроса /rapi/auth/sendCode
        :param sn: Уникальный идентификатор пользователя внутри сервиса
        :param session_id: example: 784fd34508a0dba62e4dd4c9a513c940 Идентификатор сессии, полученный в ходе запроса
        """
        return self.post(
            "rapi/auth/attachPhone",
            headers={"Content-Type": "application/json"},
            json={
                "aimsid": aimsid,
                "reqId": getReqId,
                "params": {
                    "sn": self.uin,
                    "phone": self.phone,
                    "smsCode": self.code,
                    "sessionId": session_id,
                },
            },
        )

    def rapi_auth_reset_password(self, new_password: str):
        """
        Изменить пароль пользователя
        Изменяет пароль пользователя на новый newPassword. Новый пароль будет проверен на сложность и похожесть,
        например если пароль слишком похож на логин пользователя, то он не подойдет, подробнее возможные коды
        ошибок при валидации описаны ниже.
        :param new_password: Новый пароль. Максимальная длина пароля 40 символов.
        """
        return self.post(
            "rapi/auth/resetPassword",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": getReqId,
                "aimsid": aimsid,
                "params": {"newPassword": new_password},
            },
        )

    def rapi_auth_appToken(self, app_key: str):
        """
        Получить новый токен для доступа к API
        Выдает токен на использование API, выданный токен не дает прав для отправки сообщений,
        добавления в группы и т.п.
        :param app_key: Токен приложения, для которого необходим доступ к API
        """
        return self.get(
            "rapi/auth/appToken",
            headers={"Content-Type": "application/json"},
            appKey=self.app,
        )

    def rapi_auth_refreshImserverTokens(self):
        """
        Обновить imserver токены
        Обновление ранее полученных accessToken и refreshToken
        :param app_key: Токен приложения, для которого необходим доступ к API
        """
        return self.get(
            "rapi/auth/refreshImserverTokens",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": self.getReqId,
                "aimsid": aimsid,
                "params": {"senderSn": self.uin, "refreshToken": self.token},
            },
        )
