import json
import logging
import re
import time

from typing import Optional, Dict, List

import requests
from requests import Session, Response
from api.ws.calendar_queries import UserQuery, CreateCalendarUser

logger = logging.getLogger(__name__)


class UserAuth:
    def __init__(self, user: Dict):
        """
        Класс для работа с API

        Args:
            user: данные пользователя {"email":"pupok@mail.ru","password":"pupok"}
            Если нет указаны данные пользователя - будет выполнена авторизация под админом

        """
        self.email = user.get("email")
        self.password = user.get("password")

        if not self.email or not self.password:
            raise ValueError("Email и пароль не могут быть пустыми")

        self.access_token = None
        self.biz_session = None
        self.mail_cookie_session = None
        self.mail_token_session = None
        self.calendar_session = None
        self.cloud_session = None
        self.biz_csrf_token = None
        self.calendar_csrf_token = None
        self.cloud_csrf_token = None
        self.DOMAIN = "auth-test.vkteams.vkwm.ru"
        self.CALENDAR_SUB_DOMAIN = "calendarx"
        self.CALENDAR_URL = f"https://{self.CALENDAR_SUB_DOMAIN}.{self.DOMAIN}"
        self.CALENDAR_GQL_URL = f"{self.CALENDAR_URL}/graphql"
        self.CLOUD_URL = f"https://cloud.{self.DOMAIN}"
        self.DOMAIN_NUMBER = 1
        self.DOMAIN_NAME = self.DOMAIN  # на случай использования другого домена на окружении
        self.calendar_headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Origin": self.CALENDAR_URL,
            "Referer": f"{self.CALENDAR_URL}/week/today/",
            "DNT": "1",
            "Sec-GPC": "1",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers",
            "x-csrf-token": self.calendar_csrf_token,
        }
        self.biz_headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7",
            "Content-Type": "application/json",
            "Origin": f"https://biz.{self.DOMAIN}",
            "Referer": f"https://biz.{self.DOMAIN}/domains/{self.DOMAIN_NAME}/users/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": self.biz_csrf_token,
        }
        self.cloud_headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Origin": self.CLOUD_URL,
            "Referer": f"{self.CLOUD_URL}/",
            "DNT": "1",
            "Sec-GPC": "1",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers",
            "x-csrf-token": self.cloud_csrf_token,
        }

    def get_or_create_session(self, auth_type: str) -> Optional[Session]:
        if auth_type not in ("biz", "calendar", "mail_cookie", "cloud"):
            raise

        session = None
        if auth_type == "biz":
            if self.biz_session is not None:
                return self.biz_session
            self.biz_session = self.get_biz_session(
                init_url=f"https://biz.{self.DOMAIN}/login", from_url=f"https://biz.{self.DOMAIN}"
            )
            session = self.biz_session
        if auth_type == "calendar":
            if self.calendar_session is not None:
                return self.calendar_session
            self.calendar_session = self.get_calendar_session(
                init_url=self.CALENDAR_URL, from_url=f"{self.CALENDAR_URL}/week/today"
            )
            session = self.calendar_session
        if auth_type == "mail_cookie":
            if self.mail_cookie_session is not None:
                return self.mail_cookie_session
            self.mail_cookie_session = self.get_mail_cookie()
            session = self.mail_cookie_session
        if auth_type == "cloud":
            if self.cloud_session is not None:
                return self.cloud_session
            self.cloud_session = self.get_cloud_session()
            session = self.cloud_session

        if session is None:
            raise

        return session

    def get_biz_session(self, init_url: str, from_url: str) -> Session:
        """Выполнение авторизации в бизе"""
        session = requests.Session()
        response = session.get(init_url)
        cookies = response.cookies
        act_token = cookies.get_dict().get("act")
        if act_token is None:
            raise

        login_data = {
            "username": self.email,
            "Login": self.email,
            "password": self.password,
            "Password": self.password,
            "saveauth": "1",
            "new_auth_form": "1",
            "FromAccount": "opener=account&twoSteps=1",
            "page": f"https://biz.{self.DOMAIN}",
            "act_token": act_token,
        }
        url = f"https://auth.{self.DOMAIN}/cgi-bin/auth"
        response = session.post(url, data=login_data)

        url = f"https://auth.{self.DOMAIN}/sdc?from={from_url}"
        response = session.get(url)

        url = f"https://biz.{self.DOMAIN}/domains/{self.DOMAIN_NAME}/users/"
        response = session.get(
            url,
            headers={
                "Accept": "*/*",
                "Accept-Language": "ru",
                "Host": f"biz.{self.DOMAIN}",
                "Referer": f"https://biz.{self.DOMAIN}/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-site",
            },
            allow_redirects=False,
        )
        csrftoken = session.cookies.get("csrftoken")
        self.biz_csrf_token = csrftoken
        if csrftoken is None:
            raise

        self.biz_headers["X-CSRFToken"] = self.biz_csrf_token
        return session


    def get_calendar_session(self, init_url: str, from_url: str) -> Session:
        """Выполнение авторизации в календаре"""
        session = requests.Session()
        response = session.get(init_url)
        cookies = response.cookies
        act_token = cookies.get_dict().get("act")
        if act_token is None:
            raise

        login_data = {
            "username": self.email,
            "Login": self.email,
            "password": self.password,
            "Password": self.password,
            "saveauth": "1",
            "new_auth_form": "1",
            "lang": "ru_RU",
            "page": f"{self.CALENDAR_URL}/week/today",
            "act_token": act_token,
        }
        # log.info("act_token %s", act_token)
        url = f"https://auth.{self.DOMAIN}/cgi-bin/auth"
        response = session.post(url, data=login_data)

        url = f"https://auth.{self.DOMAIN}/sdc?from={from_url}"
        response = session.get(url)

        response = session.post(self.CALENDAR_GQL_URL, json=UserQuery, headers=self.calendar_headers)
        csrftoken = session.cookies.get("calendarapi_csrf")
        self.calendar_csrf_token = csrftoken
        if csrftoken is None:
            raise

        self.calendar_headers["x-csrf-token"] = self.calendar_csrf_token
        # проверяем наличие пользователя в календаре - если его нет - создаем (флоу нового пользователя)
        errors = response.json().get("errors", None)
        if errors is not None:
            if len(errors) > 0:
                extensions = errors[0].get("extensions")
                if extensions.get("type") == "user_not_exists":
                    # создание пользователя в бд календаря
                    resp = session.post(self.CALENDAR_GQL_URL, json=CreateCalendarUser, headers=self.calendar_headers)
                    self.check_codes(resp, 200, None)
                else:
                    raise
            else:
                raise

        return session

    def get_cloud_token(self, session: Session) -> None:
        params = {
            "client_id": "88fe1bee755944e29239e23611ec2ab5",
            "response_type": "token",
            "scope": "calls.api mail.api.contacts_smart mail.api.helpers mail.api.helpers.update mail.api.helpers.remove userinfo calendar.events.create calendar.events.update calendar.events.delete pushme.api.v2.setsettings cloud.openapi.dnd cloud.openapi.dnd.zip.weblink",  # noqa: E501
            "redirect_uri": f"https://calendarx.{self.DOMAIN}",
        }
        response = self.request_api(
            url=f"https://o2.{self.DOMAIN}/login/token",
            session=session,
            expected_http_code=200,
            params=params,
            method="post",
        )
        html_content = response.text
        match = re.search(r'"access_token"\s*:\s*"([^"]+)"', html_content)
        if not match:
            raise
        self.access_token = match.group(1)

    def get_mail_cookie(self) -> Session:
        """Выполнение авторизации в почте"""
        session = requests.Session()
        headers = {
            "User-Agent": "PostmanRuntime/7.43.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }
        # Шаг 1: Получение редиректа и автоматическая установка cookies
        url = f"https://account.{self.DOMAIN}/login?page=https://e.{self.DOMAIN}"
        response = session.get(url=url, headers=headers, allow_redirects=False)
        act_token = session.cookies.get("act")
        if act_token is None:
            raise

        # Шаг 2: Авторизация (POST-запрос) - Cookies устанавливаются автоматически при ответе сервера
        login_payload = {
            "username": self.email,
            "Login": self.email,
            "password": self.password,
            "Password": self.password,
            "saveauth": "1",
            "new_auth_form": "1",
            "act_token": act_token,
            "page": f"https://e.{self.DOMAIN}/api/v1/user/short",
            "lang": "ru_RU",
        }
        url = f"https://auth.{self.DOMAIN}/cgi-bin/auth"
        response = session.post(
            url=url,
            headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
            data=login_payload,
            allow_redirects=False,
        )
        # Обработка редиректа после логина
        redirect_after_login = response.headers.get("Location")

        # Шаг 3: Получение токена через GET-запрос
        response = session.get(redirect_after_login, headers=headers, allow_redirects=False)

        # Шаг 4: Получение информации о пользователе
        url = f"https://auth.{self.DOMAIN}/sdc?from=https://e.{self.DOMAIN}/api/v1/user/short"
        response = session.get(url=url, headers=headers)

        response_json = response.json()
        token = response_json.get("body").get("token")
        if token is None:
            raise

        self.access_token = token
        return session

    def get_cloud_session(self) -> Session:
        """Выполнение авторизации в облаке"""
        session = self.get_or_create_session("mail_cookie")
        if session is None:
            raise

        response = session.get(self.CLOUD_URL, allow_redirects=False)

        redirect_after_login = response.headers.get("Location")
        response = session.get(redirect_after_login, allow_redirects=False)

        redirect_after_login = response.headers.get("Location")
        response = session.get(redirect_after_login, allow_redirects=False)

        response = session.get(self.CLOUD_URL)

        self.cloud_csrf_token = response.headers.get("x-csrf-token")
        self.cloud_headers["x-csrf-token"] = self.cloud_csrf_token

        return session

    def send_gql_query(self, query: json) -> Dict:
        """Отправка gql запроса"""
        session = self.get_or_create_session("calendar")
        response = session.post(self.CALENDAR_GQL_URL, json=query, headers=self.calendar_headers)

        return response.json()


    def request_api(
            self,
            url: str,
            session: Session,
            headers: Optional[Dict] = None,
            tries: int = 1,
            timeout: int = 12,  # BUG: https://jira.vk.team/browse/MAILAPI-17994
            expected_http_code: Optional[int] = 200,
            expected_json_code: Optional[int] = None,
            method: str = "get",
            data: Optional[Dict] = None,
            params: Optional[Dict] = None,
            json: Optional[Dict] = None,
            files: Optional[List] = None,
    ) -> Response:
        args_info = f"\n\tmethod: {method}"
        max_body_length = 240
        if headers:
            args_info += f"\n\theaders: {headers}"
        if data:
            data_cut = data
            if len(str(data_cut)) > max_body_length:
                data_cut = str(data_cut)[:40] + " <CUT> " + str(data_cut)[-40:]
            args_info += f"\n\tdata: {data_cut}"
        if params:
            args_info += f"\n\tparams: {params}"
        if json:
            args_info += f"\n\tjson: {json}"
        if files:
            args_info += f"\n\tfiles: {files}"
        for iteration in range(1, tries + 1):
            response = None
            try:
                response = getattr(session, method)(
                    url, timeout=timeout, data=data, json=json, headers=headers, params=params, files=files
                )
            except Exception as exc:
                # Если исключение - пытаемся снова
                time.sleep(iteration)
                continue

            if response is None or not hasattr(response, "status_code"):
                # Если нет ответа - пытаемся снова
                time.sleep(iteration)
                continue

            if expected_http_code is None:
                break

            # Если проверка не прошла, пытаемся снова или выводим всю инфу
            body_cut = response.text
            if len(body_cut) > max_body_length:
                body_cut = body_cut[:40] + " <CUT> " + body_cut[-40:]
            time.sleep(iteration)
            continue

        return response
