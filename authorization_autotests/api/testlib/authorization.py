import json
import re
from typing import Dict, List, Optional

import requests
from ..core.decorators import qacore_decorators
from ..core.exceptions import AutotestException, FrameworkException
from ..core.logger import FMT_DEFAULT, FMT_FAIL, FMT_OK, FMT_URL, fmtstring, log

from ..core.steps_common import compare_two_items
from requests import Session
from requests.models import Response
from const import VKWORKSPACE_DOMAIN
from helpers import sleep_or_exit


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
        self.DOMAIN = VKWORKSPACE_DOMAIN
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
            raise FrameworkException(f"Unsupported auth_type: {auth_type}")

        log.debug("auth_type %s", auth_type)
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
            raise AutotestException("Авторизованная сессия не создана")

        log.debug("session %s", session)
        return session

    @qacore_decorators
    def get_biz_session(self, init_url: str, from_url: str) -> Session:
        """Выполнение авторизации в бизе"""
        log.info(f"Выполнение авторизации в бизе под: {self.email}", extra=FMT_DEFAULT)
        session = requests.Session()
        response = session.get(init_url)
        self.check_codes(response, 200, None)
        cookies = response.cookies
        act_token = cookies.get_dict().get("act")
        if act_token is None:
            raise AutotestException(f"Не получен 'act' токен: {cookies.get_dict()}")

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
        self.check_codes(response, 200, None)

        url = f"https://auth.{self.DOMAIN}/sdc?from={from_url}"
        response = session.get(url)
        self.check_codes(response, 200, None)

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
        self.check_codes(response, 200, None)
        csrftoken = session.cookies.get("csrftoken")
        self.biz_csrf_token = csrftoken
        if csrftoken is None:
            raise AutotestException(f"Не получен 'csrftoken' токен из: {session.cookies}")

        self.biz_headers["X-CSRFToken"] = self.biz_csrf_token
        log.info("Авторизация в бизе выполнена", extra=FMT_OK)
        return session

    def get_cloud_token(self, session: Session) -> None:
        log.info(f"Получение токена облака для календаря для: {self.email}", extra=FMT_DEFAULT)
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
            raise AutotestException(f"Не удалось найти access_token в ответе: {html_content}")

        self.access_token = match.group(1)
        log.info(f"Токен успешно получен {self.access_token}", extra=FMT_OK)

    def get_mail_cookie(self) -> Session:
        """Выполнение авторизации в почте"""
        log.info(f"Выполнение авторизации в почте: {self.email}", extra=FMT_DEFAULT)
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
        self.check_codes(response, 200, None)
        act_token = session.cookies.get("act")
        if act_token is None:
            raise AutotestException(f"Не получен 'act' токен: {session.cookies.get_dict()}")

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
        self.check_codes(response, 302, None)
        # Обработка редиректа после логина
        redirect_after_login = response.headers.get("Location")

        # Шаг 3: Получение токена через GET-запрос
        response = session.get(redirect_after_login, headers=headers, allow_redirects=False)
        self.check_codes(response, 200, None)

        # Шаг 4: Получение информации о пользователе
        url = f"https://auth.{self.DOMAIN}/sdc?from=https://e.{self.DOMAIN}/api/v1/user/short"
        response = session.get(url=url, headers=headers)
        self.check_codes(response, 200, 200)

        response_json = response.json()
        token = response_json.get("body").get("token")
        if token is None:
            raise AutotestException(f"Нет ключа 'token' из тела запроса: {response_json}")

        self.access_token = token
        log.info(f"Авторизация в почте выполнена, получен токен длиной {len(token)}", extra=FMT_OK)
        return session

    def get_cloud_session(self) -> Session:
        """Выполнение авторизации в облаке"""
        session = self.get_or_create_session("mail_cookie")
        if session is None:
            raise AutotestException("Перед авторизацией в облако выполните вход в почту")

        log.info(f"Выполнение авторизации в облаке для: {self.email}", extra=FMT_DEFAULT)
        response = session.get(self.CLOUD_URL, allow_redirects=False)
        self.check_codes(response, 302, None)

        redirect_after_login = response.headers.get("Location")
        response = session.get(redirect_after_login, allow_redirects=False)
        self.check_codes(response, 302, None)

        redirect_after_login = response.headers.get("Location")
        response = session.get(redirect_after_login, allow_redirects=False)
        self.check_codes(response, 302, None)

        response = session.get(self.CLOUD_URL)
        self.check_codes(response, 200, None)

        self.cloud_csrf_token = response.headers.get("x-csrf-token")
        self.cloud_headers["x-csrf-token"] = self.cloud_csrf_token
        log.info("Авторизация в облаке выполнена", extra=FMT_OK)

        return session

    def send_gql_query(self, query: json) -> Dict:
        """Отправка gql запроса"""
        session = self.get_or_create_session("calendar")
        response = session.post(self.CALENDAR_GQL_URL, json=query, headers=self.calendar_headers)
        self.check_codes(response, 200, None)

        return response.json()

    @qacore_decorators
    def request_api(
        self,
        url: str,
        session: Session,
        headers: Optional[Dict] = None,
        tries: int = 1,
        timeout: int = 10,
        expected_http_code: Optional[int] = 200,
        expected_json_code: Optional[int] = None,
        method: str = "get",
        data: Optional[Dict] = None,
        params: Optional[Dict] = None,
        json: Optional[Dict] = None,
        files: Optional[List] = None,
    ) -> Response:
        args_info = f"    {fmtstring('Запрос')}:\n\tmethod: {method}"
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
                sleep_or_exit(f"{url}\n{args_info}\nПлохой ответ: {exc}", iteration, tries)
                continue

            if response is None or not hasattr(response, "status_code"):
                # Если нет ответа - пытаемся снова
                sleep_or_exit(f"Api doesn't respond for: {url}", iteration, tries)
                continue

            if expected_http_code is None:
                break

            # Проверяем коды ответа
            if self.check_codes(response, expected_http_code, expected_json_code, raise_if_fail=False):
                # Если проверка прошла успешно, выходим из цикла
                break

            # Если проверка не прошла, пытаемся снова или выводим всю инфу
            body_cut = response.text
            if len(body_cut) > max_body_length:
                body_cut = body_cut[:40] + " <CUT> " + body_cut[-40:]
            sleep_or_exit(
                f"Все попытки закончились:\n{args_info}\n    "
                f"{fmtstring('Ответ')}:\n\theaders: {response.headers}\n\tbody:{body_cut}",
                iteration,
                tries,
            )
            continue

        return response

    @qacore_decorators
    def check_codes(
        self,
        response: Response,
        expected_http_code: Optional[int],
        expected_json_status: Optional[int],
        raise_if_fail: bool = True,
    ) -> bool:
        """Проверяет коды ответа. Возвращает True если все проверки пройдены."""
        result = []

        log.info(response.url, extra=FMT_URL)

        # Проверка HTTP кода
        if expected_http_code is not None:
            http_check = compare_two_items(
                response.status_code,
                "==",
                expected_http_code,
                desc=fmtstring("HTTP код"),
                raise_if_fail=False,
                log_result=True,
            )
            result.append(http_check)

        # Проверка JSON статуса
        if expected_json_status is not None:
            json_resp = None
            json_status = None

            try:
                json_resp = response.json()
            except Exception:
                log.error(
                    f"{fmtstring('JSON статус')}: Ответ не содержит валидный JSON. Content-Type: "
                    f"{response.headers.get('Content-Type', 'не указан')}",
                    extra=FMT_FAIL,
                )
                result.append(False)

            if json_resp is not None:
                json_status = json_resp.get("status")
                if json_status is not None:
                    json_check = compare_two_items(
                        json_status,
                        "==",
                        expected_json_status,
                        desc=fmtstring("JSON статус"),
                        raise_if_fail=False,
                        log_result=True,
                    )
                    result.append(json_check)
                else:
                    log.warning(f"В JSON ответе отсутствует поле 'status'. JSON: {json_resp}")
                    result.append(False)
            else:
                # Если json_resp is None (не удалось распарсить), проверка уже добавлена выше
                pass

        # Если все проверки пройдены
        overall_result = all(result) if result else True
        if raise_if_fail and not overall_result:
            raise AutotestException(f"{fmtstring('Тело ответа:')} {response.text}")

        return overall_result
