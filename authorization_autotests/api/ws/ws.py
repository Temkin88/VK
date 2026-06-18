import json
import os
import time
import uuid
from datetime import datetime
from types import SimpleNamespace
from typing import Optional, Dict, TYPE_CHECKING, List

import pytest

from api.client.http_client import HttpClient
from api.client.user_auth import UserAuth
from api.testlib.helpers import generate_user_data, generate_string, add_minutes
from api.ws.calendar_queries import CreateEvent, CreateCalendar, CalendarsQuery, GetSingleEvent


class MethodWs(HttpClient):
    def hooks_after_user_auth(
            self,
            url,
            email,
            user_id,
            session_id,
            user_ip,
            useragent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
            auth_host="e.mail.ru",
            is_mobile=False,
            reset_password: Optional[bool] = False,
            reset_soft_vkid_bind: Optional[bool] = False,
            via_vkc: Optional[bool] = False,
    ):
        """
        Пост-авторизация пользователя
        :param url:
        :param email: REQUIRED E-mail авторизовавшегося пользователя
        :param user_id: REQUIRED ID авторизовавшегося пользователя
        :param session_id: REQUIRED ID сессии автоизовавшегося пользователя
        :param user_ip: REQUIRED IP, с которого произошла авторизация
        :param useragent: REQUIRED User-Agent пользователя
        :param auth_host: REQUIRED Домен, с которого была инициирована авторизация
        :param is_mobile: REQUIRED Мобильность девайса
        :param reset_password: OPTIONAL Сбросить пароль для аккаунта, привязанного к VKID (пробрасывается от клиента)
        :param reset_soft_vkid_bind: OPTIONAL Сбросить бит SOFT_VKID_BIND для аккаунта, привязанного к VKID (пробрасывается от клиента)
        :param via_vkc: OPTIONAL Авторизация была через VKC/VKID
        :return:
        """
        return self.post(
            url=url,
            path="hooks/after-user-auth",
            headers={"Content-Type": "application/json"},
            json={
                "params": {
                    "email": email,
                    "user_id": user_id,
                    "session_id": session_id,
                    "user_ip": user_ip,
                    "useragent": useragent,
                    "auth_host": auth_host,
                    "is_mobile": is_mobile,
                    "reset_password": reset_password,
                    "reset_soft_vkid_bind": reset_soft_vkid_bind,
                    "via_vkc": via_vkc
                },
            },
        )

    def esia_child_auth(self, url, email_child, child_esia_id, parent_esia_id, user_ip):
        """
        Получение авторизационной ссылки для доступа в детский почтовый ящик от имени родителя
        :param url:
        :param email_child: Емейл ребенка, доступ к которому требуется, аргумент обязателен (string)
        :param child_esia_id: Id ребенка как пользователя госуслуг (цифровой, аргумент обязателен) (string)
        :param parent_esia_id: Id родителя как пользователя госуслуг (цифровой, аргумент обязателен) (string)
        :param user_ip: IP адрес пользователя в формате 1.2.3.4, (аргумент обязателен) (string)
        :return:
        """
        return self.get(
            url=url,
            path="/esia/child/auth",
            params={
                "email": email_child,
                "child_esia_id": child_esia_id,
                "parent_esia_id": parent_esia_id,
                "ip": user_ip
            })

    def user_enable_auth_cookie(self, url, email):
        """
        Установить ukey куку для авторизации
        :param url:
        :param email: email(string) пользователя
        :return:
        """
        return self.get(url=url, path="test/user/enable/auth_cookie", params={"email": email})

    def user_2_step_auth(self):
        """
        Настройки 2-ф авторизации текущего пользователя
        :return:
        """
        return self.get("user/2-step-auth")

    def user_2_step_auth_unsafe_enable(
            self,
            url,
            phone_id,
            phone,
            password,
            reg_id,
            value,
            redirect_uri="http://e.mail.ru/settings/security?twostep=enabled"
    ):
        """
        Универсальное включение двухфакторной авторизации
        :param url:
        :param phone_id: Идентификатор телефона для 2х факторной авторизации (string) (Не обязательный параметр, в случае если указан phone)
        :param phone: Номер телефона (string) (Не обязательный параметр, в случае если указан phone_id)
        :param password: Текущий пароль пользователя (string)
        :param reg_id: Авторизационный токен (SMS-код, OAuth-токен и пр.)
        Временный идентификатор, который следует использовать для подтверждения последующих действий (string)
        :param value: Пароль введный пользователем из полученной СМС или письма (string)
        :param redirect_uri: На какой url вернуть пользователя, после сброса сессии в auth
        :return:
        """
        return self.get(url=url,
                        path="user/2-step-auth/unsafe/enable",
                        params={"phone_id": phone_id,
                                "phone": phone,
                                "password": password,
                                "reg_token": {"id": reg_id,
                                              "value": value
                                              },
                                "redirect_uri": redirect_uri
                                }
                        )

    def user_extra_emails_remove_noauth(self, url, token_id):
        """
        Удаление доп. имейла без авторизации по токену из письма
        :param url:
        :param token_id: Идентификатор токена (string)
        :return:
        """
        return self.get(url=url, path="user/extra-emails/remove/noauth", params={"id": token_id})

    def user_extra_emails_remove_noauth_check(self, url, token_id):
        """
        Получение информации из токена для удаления доп. имейла без авторизации
        :param url:
        :param token_id: Идентификатор токена (string)
        :return:
        """
        return self.get(url=url, path="user/extra-emails/remove/noauth/check", params={"id": token_id})

    def user_password_support_cancel(self, url, token_id):
        """
        Отмена замороженной заявки в саппорт без авторизации по токену из письма
        :param url:
        :param token_id: Идентификатор токена (string)
        :return:
        """
        return self.get(url=url, path="user/password/support/cancel", params={"id": token_id})

    def user_password_support_cancel_check(self, url, token_id):
        """
        Проверка валидности токена для отмены заявки в саппорт без авторизации
        :param url:
        :param token_id: Идентификатор токена (string)
        :return:
        """
        return self.get(url=url, path="user/password/support/cancel/check", params={"id": token_id})

    def users_auth_notify(
            self,
            url,
            email,
            requared_id,
            device_info=None,
            os_id: Optional[int]=5,
            browser_id: Optional[int]=123,
            user_agent: Optional[str]="MRMail/13718 CFNetwork/808.3 Darwin/16.3.0",
            nosms: Optional[bool]=False,
            session_flags: Optional[int]=123,
            force: Optional[bool]=False,
    ):
        """
        Уведомление об авторизации
        :param url:
        :param email: REQUIRED E-mail авторизовавшегося пользователя
        :param device_info: Информация об устройстве, с которого произошла авторизация (JSON)
        :param requared_id: REQUIRED IP, с которого произошла авторизация
        :param os_id: OPTIONAL. os_id from top.mail.ru dict
        :param browser_id: OPTIONAL. browser_id from top.mail.ru dict
        :param user_agent: OPTIONAL. User agent
        :param nosms: OPTIONAL. Не отправлять смс, только email. По умолчанию - false.
        :param session_flags: OPTIONAL. Флаги сессии
        :param force: OPTIONAL. Обход проверки джигурды и регулярки тестовых ящиков. По умолчанию - false.
        :return:
        """
        if not device_info:
            device_info = {"phone":"Samsung","device_id":"asklbcjsdlvbzsv"}

        return self.get(url=url, path="users/auth/notify",
                        params={"email": email,
                                "device_info":  device_info,
                                "ip": requared_id,
                                "os_id": os_id,
                                "browser_id": browser_id,
                                "user_agent": user_agent,
                                "nosms": nosms,
                                "session_flags": session_flags,
                                "force": force,
                                })


    def auth_login(self, base_url, username, password):
        auth_url = base_url.replace("u.", "auth.", 1)
        e_url = base_url.replace("u.", "e.", 1)
        act_token = self.act_token()

        return self.post(
            url=auth_url + "/cgi-bin/auth?platform=web&project=login",
            params={
                "username": username,
                "Login": username,
                "password": password,
                "Password": password,
                "new_auth_form": 1,
                "FromAccount": "opener=account&twoSteps=1",
                "act_token": act_token,
                "page": e_url + "/inbox?authid=mnhf6cnt.p1g&from=login",
                "lang": "ru_RU"
            }
        )

    def act_token(self):
        response = self.get('https://auth.mail.ru/jsapi/token').json()
        return response["token"]

    def get_message(self, base_url, email, message_id, password):
        auth_url = base_url.replace("https://", "https://e.", 1)
        act_token = self.act_token()

        return self.post(
            url=auth_url + "/api/v1/test/message/no_quotes",
            params={
                "email": email,
                "id": message_id,
                "password": password,
            }
        )

    def get_last_unread_email(self, url, session, access_token, email, add_in: Optional[Dict] = None) -> Dict:
        """
        GET LAST UNREAD EMAIL

        Возвращает последнее непрочитанное письмо, дополнительно можно указать папку
        Args:
            add_in: список дополнительных параметров: {'folder', '0'}
        """
        auth_url = url.replace("https://", "https://e.", 1)
        params = {"token": access_token, "email": email, "snippet_limit": 1000, "htmlencoded": "false"}
        if add_in:
            params = {**params, **add_in}
        return self.get(
            url=f"{auth_url}/api/v1/messages/status/unread/last", session=session, params=params
        ).json()


class WSUser:
    def __init__(self, user: Optional[Dict]):
        """
        Класс для работа с API

        Args:
            user: данные пользователя {"email":"pupok@mail.ru","password":"pupok"}
            Если нет указаны данные пользователя - будет выполнена авторизация под админом

        """
        self.email: str = user.get("email")
        self.password: str = user.get("password")
        self.login: str = user.get("login", self.email)
        self.gender: str = user.get("gender")
        self.domain: str = user.get("domain")
        self.first_name: str = user.get("firstname")
        self.last_name: str = user.get("lastname")
        self.full_name: str = user.get("full_name")
        self.auth = UserAuth(user)
        self.user_id = user.get("id")
        self.last_sent_mail = None
        self.last_event = None

    # biz api
    def biz_get_users(self) -> Dict:
        """BIZ GET USERS"""
        session = self.auth.get_or_create_session("biz")
        return self.auth.request_api(
            url=f"https://biz.{self.auth.DOMAIN}/api/v1/domains/{self.auth.DOMAIN_NUMBER}/users?limit=100",
            session=session,
            headers=self.auth.biz_headers,
        ).json()

    def biz_create_multiple_users(self, amount: int = 2) -> SimpleNamespace:
        """CREATE MULTIPLE BIZ USERS"""
        password = "qweasd123!@#"

        created_users = [self.biz_create_user(password) for _ in range(amount)]
        result_dict = {}
        # Добавляем каждого пользователя под своим ключом
        for i, user_data in enumerate(created_users, 1):
            user_data["password"] = password
            result_dict[f"user{i}"] = WSUser(user=user_data)
        return SimpleNamespace(**result_dict)

    
    def biz_create_user(self, password: str) -> Dict:
        """BIZ CREATE USER"""
        user = generate_user_data(password)
        session = self.auth.get_or_create_session("biz")
        url = f"https://biz.{self.auth.DOMAIN}/api/onpremise/domains/{self.auth.DOMAIN_NUMBER}/users/"
        return self.auth.request_api(
            url=url,
            session=session,
            headers=self.auth.biz_headers,
            method="post",
            json=user,
            expected_http_code=201,
        ).json()

    
    def biz_delete_user(self, user: "WSUser") -> Dict:
        """BIZ DELETE USER"""
        url = f"https://biz.{self.auth.DOMAIN}/api/v1/domains/{self.auth.DOMAIN_NUMBER}/users/{user.user_id}"
        session = self.auth.get_or_create_session("biz")
        resp = self.auth.request_api(
            url=url,
            session=session,
            headers=self.auth.biz_headers,
            method="delete",
            expected_http_code=200,
        ).json()
        status = resp.get("status")

        return resp

    
    def biz_create_user_cloud(self, for_user: "WSUser") -> Dict:
        """
        BIZ CREATE USER CLOUD

        Создание клауда для пользователя

        """
        session = self.auth.get_or_create_session("biz")
        data = {
            "email": for_user.email,
            "paid_space": 0,
            "quota": 5368709120,
            "blocked": False,
            "stime": 0,
            "name": None,
        }
        url = f"https://biz.{self.auth.DOMAIN}/api/domains/{self.auth.DOMAIN_NUMBER}/proxy/cloud/api/v1/user/create"
        headers = {**self.auth.biz_headers, "Content-Type": "application/x-www-form-urlencoded"}
        resp = self.auth.request_api(
            url=url,
            session=session,
            headers=headers,
            method="post",
            data=data,
            expected_http_code=201,
            expected_json_code=201,
        ).json()
        return resp

    
    def biz_update_user_info(self, for_user: "WSUser") -> Dict:
        """BIZ UPDATE USER INFO"""
        generate_new_user_info = generate_user_data("")
        session = self.auth.get_or_create_session("biz")
        data = {
            "firstname": generate_new_user_info.get("firstname"),
            "middlename": "",
            "lastname": generate_new_user_info.get("lastname"),
        }
        url = (
            f"https://biz.{self.auth.DOMAIN}/api/onpremise/domains/{self.auth.DOMAIN_NUMBER}/users/{for_user.user_id}/"
        )
        resp = self.auth.request_api(
            url=url,
            session=session,
            headers=self.auth.biz_headers,
            method="patch",
            json=data,
            expected_http_code=200,
        ).json()
        firstname = resp.get("firstname")
        lastname = resp.get("lastname")
        return resp

    # mail api
    def get_folders(self) -> Dict:
        """
        GET FOLDERS

        Получаем папки в почте у пользователя

        """
        session = self.auth.get_or_create_session("mail_cookie")
        params = {"email": self.email, "token": self.auth.access_token}
        return self.auth.request_api(
            url=f"https://e.{self.auth.DOMAIN}/api/v1/folders", session=session, params=params
        ).json()

    
    def get_last_unread_email(self, add_in: Optional[Dict] = None) -> Dict:
        """
        GET LAST UNREAD EMAIL

        Возвращает последнее непрочитанное письмо, дополнительно можно указать папку
        Args:
            add_in: список дополнительных параметров: {'folder', '0'}
        """
        session = self.auth.get_or_create_session("mail_cookie")
        params = {"token": self.auth.access_token, "email": self.email, "snippet_limit": 1000, "htmlencoded": "false"}
        if add_in:
            params = {**params, **add_in}
        return self.auth.request_api(
            url=f"https://e.{self.auth.DOMAIN}/api/v1/messages/status/unread/last", session=session, params=params
        ).json()

    def send_mail(self, to_user: "WSUser", attach_type: Optional[str] = None) -> Dict:
        """
        SEND MAIL

        Отправление письма, варианты отправки с аттачами:
        1) attach_type == "attach" - загрузка файла менее 25 МБ (без загрузки в клауд)
        2) attach_type == "cloud_stock" - загрузка файла более 25 МБ (с загрузкой в клауд)
        3) attach_type == "forward_attach_from_mail" - прикрепление файла из другого письма

        """
        attaches = []
        main_text = f"Полный текст письма {generate_string(32)}"
        message_id = generate_string(32)
        subject = generate_string(10)
        if attach_type == "attach":
            # загрузка аттача в почту и получение id аттача
            file_path = os.path.join(".", "test_data", "attach_07.jpg")
            attach_id = self.load_attach_to_mail(file_path=file_path, message_id=message_id)
            attaches = [{"id": attach_id, "type": "attach"}]

        if attach_type == "cloud_stock":
            # загрузка аттача в клауд и получение id аттача - attach_30.png
            file_path = os.path.join(".", "test_data", "attach_30.png")
            bundle_id = self.load_file_to_cloud_as_attach(file_path=file_path, message_id=message_id)
            attaches = [{"id": bundle_id, "type": "cloud_stock"}]

        if attach_type == "forward_attach_from_mail":
            # поиск файла в папке входящих
            file_id = self.search_file_in_folder()
            # прикрепление найденного файла
            attach_id = self.forward_attach_from_mail(file_id=file_id, message_id=message_id)
            attaches = [{"id": attach_id, "type": "attach"}]

        correspondents_to_string = f"<{to_user.email}>"
        body = json.dumps({"html": None, "text": main_text})
        corresponds = json.dumps({"to": correspondents_to_string, "cc": "", "bcc": ""})
        add_attaches = json.dumps({"list": attaches})
        data = {
            "id": message_id,
            "subject": subject,
            "body": body,
            "from": self.email,
            "correspondents": corresponds,
            "email": self.email,
            "SYNC_ADD_FORWARD_ATTACHMENTS": False,
            "ATTACHMENTS_RESTORE": True,
            "ATTACHMENTS_EXPIRATION_TIME": "14400000",
            "attaches": add_attaches,
        }
        session = self.auth.get_or_create_session("mail_cookie")
        params = {**data, "token": self.auth.access_token}
        # log.info("params %s", params)
        resp = self.auth.request_api(
            url=f"https://e.{self.auth.DOMAIN}/api/v1/messages/send", session=session, params=params, method="post"
        )
        self.auth.check_codes(resp, 200, None)
        ########### получаем отправленное письмо чтобы сохранить в памяти
        # Для ОУ стенда если загрузка в аттача в облако не прошло - письмо почему то может и не отправится
        # пока игнорируем, но выглядит странно
        self.last_sent_mail = self.get_thread(subject, folder="Sent")

        return self.last_sent_mail

    
    def check_inbox_mail(self, from_user: "WSUser", with_attach: bool = False, expected_messages: int = 1) -> dict:
        """
        CHECK INBOX MAIL FROM USER

        проверяем письмо во входящих у получателя (self - тот кто инициализировал проверку),
        уникальный текст письма берется у (from_user - отправитель),
        в итоге проверяется только subject и folder
        with_attach - проверка наличия аттача
        не проверяется его отсутствие
        """
        outbox_mail = from_user.last_sent_mail

        outbox_mail_text = outbox_mail.get("snippet")

        outbox_subject = outbox_mail.get("subject")
        messages = self.get_thread_messages(outbox_subject, "Inbox")

        lenght = len(messages)
        inbox_mail = messages[0]  # берем первое сообщение
        inbox_subject = inbox_mail.get("subject")
        inbox_folder = inbox_mail.get("folder")
        inbox_mail.get("flags")
        return inbox_mail

    
    def open_attach(self, from_mail: Dict, attach_type: str = "attach") -> None:
        """
        OPEN ATTACH FROM USER

        Проверяем что файл доступен для скачивания
        """
        # получить письмо по id
        mail_id = from_mail.get("id")

        mail = self.get_email_by_id(mail_id)
        body = mail.get("body")

        attaches = body.get("attaches")

        list_attaches = attaches.get("list")

        lenght = len(list_attaches)
        mail_attach = list_attaches[0]
        mail_attach_type = mail_attach.get("type")
        href = mail_attach.get("href")

        download_url = href.get("download")

        # качаем изображение по url
        self.download_image(from_url=download_url)
    
    def download_image(self, from_url: str) -> None:
        """
        DOWNLOAD IMAGE

        Скачивание файла

        Args:
            from_url: url изображения

        """
        session = self.auth.get_or_create_session("mail_cookie")
        self.auth.request_api(url=from_url, session=session, method="get", expected_http_code=200)
    
    def get_email_by_id(self, mail_id: int) -> Dict:
        """
        GET MAIL BY ID

        Получение письма по id

        Args:
            mail_id: айди письма

        """
        session = self.auth.get_or_create_session("mail_cookie")
        params = {"id": mail_id, "token": self.auth.access_token, "email": self.email}
        url = f"https://e.{self.auth.DOMAIN}/api/v1/messages/message"
        resp = self.auth.request_api(url=url, session=session, params=params, method="get")
        self.auth.check_codes(resp, 200, None)

        return resp.json()

    def get_thread_messages(self, search_subject: str, folder: str = "Sent") -> Dict:
        """
        FIND THREAD WITH

        Возвращает список писем треда найденного по теме
        """
        thread = self.get_thread(search_subject, folder)
        thread_id = thread.get("id")

        url = f"https://e.{self.auth.DOMAIN}/api/v1/threads/thread"
        session = self.auth.get_or_create_session("mail_cookie")
        params = {
            "id": thread_id,
            "token": self.auth.access_token,
            "email": self.email,
            "offset": "0",
            "limit": 25,
            "last_modified": "1",
            "htmlencoded": "false",
        }
        response = self.auth.request_api(url=url, session=session, params=params, method="get")
        self.auth.check_codes(response, 200, 200)
        body = response.json().get("body")
        messages = body.get("messages")

        return messages

    
    def get_thread(self, search_subject: str, folder: str = "Sent") -> Dict:
        """
        GET THREDS

        Возвращает тред писем c темой search_subject
        выполняется 8 попыток с 10 секундным таймаутом - пока что настроен большой delay - т/к письма переодически
        доходят спустя 1,5 минуты
        Args:
            search_subject: str, # тема письма
            folder_id: 0, # айди папки
        """
        attempt = 1
        # BUG: https://jira.vk.team/browse/MTA-2249
        max_attempts = 15
        backoff = 10
        thread = None

        session = self.auth.get_or_create_session("mail_cookie")
        params = {
            "folder": folder,
            "token": self.auth.access_token,
            "email": self.email,
            "offset": "0",
            "limit": 25,
            "last_modified": "1",
            "htmlencoded": "false",
        }
        url = f"https://e.{self.auth.DOMAIN}/api/v1/threads"

        while attempt <= max_attempts:
            try:
                response = self.auth.request_api(url=url, session=session, params=params, method="get").json()
            except Exception as e:
                # Ошибка при выполнении запроса
                # Подготовка к следующей попытке
                if attempt < max_attempts:
                    time.sleep(backoff)
                attempt += 1
                continue

            attempt += 1

            if not isinstance(response, Dict):
                if attempt <= max_attempts:
                    time.sleep(backoff)
                continue

            body = response.get("body")
            if not isinstance(body, List):
                if attempt <= max_attempts:
                    time.sleep(backoff)
                continue

            for item in body:
                subject = item.get("subject")
                if search_subject == subject:
                    thread = item
                    return thread

            if attempt <= max_attempts:
                time.sleep(backoff)

        raise

    
    def load_attach_to_mail(self, file_path: str, message_id: str) -> str:
        """
        LOAD ATTACH TO MAIL

        Загрузка атача (менее 25 МБ) к письму (не используется клауд)

        Args:
            file_path: путь к локальному файлу
            message_id: id письма - для прикрепления при отправке

        ожидаемый ответ:
        {
            "status": 200,
            "htmlencoded": false,
            "email": "3test3@vkwm-ou.release.vkwm.ru",
            "body": {
                "attach": {
                    "id": "h6waKw62Mi3IBXaz",
                    "content_type": "application/pdf",
                    "name": "Памятка новичка.pdf",
                    "size": 3849568
                },
                "space_left": 22364832
            }
        }

        """
        data = {
            "htmlencoded": "false",
            "message_id": message_id,
            "email": self.email,
        }
        session = self.auth.get_or_create_session("mail_cookie")
        params = {**data, "token": self.auth.access_token}
        url = f"https://e.{self.auth.DOMAIN}/api/v1/messages/attaches/add?fileapi17689014255554"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7",
        }
        with open(file_path, "rb") as file:
            files = {"file": (os.path.basename(file_path), file, "image/jpg")}
            resp = self.auth.request_api(
                url=url, session=session, params=params, method="post", headers=headers, files=files
            )
            self.auth.check_codes(resp, 200, None)
            body = resp.json().get("body")
            if not isinstance(body, dict):
                raise

            attach = body.get("attach")
            if attach is None:
                raise
            attach_id = attach.get("id")
            if attach_id is None:
                raise
            return attach_id

    
    def register_file_in_cloud_from_mail(self, bundle_id: str, file_path: str, hash_file: str) -> None:
        """
        REGISTER FILE IN CLOUD FROM MAIL

        Создаем связь между загруженным файлов в клауд через почту и бандлом
        в ответе получаем file_id

        ожидаемый ответ:
        {
            "body": {
                "duedate": 1769029108,
                "name": "qrcode_3bXOnXx4MV1.png",
                "file_id": "fgQJwdxqBk3"
            },
            "email": "m1oaoxr9ks1768993051@vkwm-ou.release.vkwm.ru",
            "htmlencoded": false,
            "status": 200
        }
        """
        if not hash_file:
            return
        file_name = os.path.basename(file_path)
        size = os.path.getsize(file_path)
        data = {
            "htmlencoded": "true",
            "bundle_id": bundle_id,
            "hash": hash_file,
            "size": size,
            "email": self.email,
            "name": file_name,
        }
        session = self.auth.get_or_create_session("mail_cookie")
        params = {**data, "token": self.auth.access_token}
        url = f"https://e.{self.auth.DOMAIN}/api/v1/cloud/attachment/add"
        resp = self.auth.request_api(
            url=url, session=session, params=params, method="post", expected_http_code=200, expected_json_code=200
        ).json()
        body = resp.get("body")
        if not isinstance(body, dict):
            raise

        file_id = body.get("file_id")
        if file_id is None:
            raise
    
    def upload_file_to_cloud_from_mail(self, loader_url: str, file_path: str) -> str:
        """
        UPLOAD FILE TO CLOUD FROM MAIL

        Загрузка файла из композера письма, если файл более 25 МБ - используется loader_url

        Args:
            loader_url: лоадер url
            file_path: путь к локальному файлу

        """
        session = self.auth.get_or_create_session("mail_cookie")
        url = f"{loader_url}upload/?x-email={self.email}&cloud_domain=2"
        with open(file_path, "rb") as file:
            file_content = file.read()

        headers = {
            "Content-Type": "application/octet-stream",
            "Content-Length": str(len(file_content)),
            "Content-Disposition": f'attachment; filename="{os.path.basename(file_path)}"',
            "accept-encoding": "gzip, deflate, br, zstd",
        }

        resp = self.auth.request_api(
            url=url,
            session=session,
            method="put",
            headers=headers,
            data=file_content,
            expected_http_code=201,
            tries=5 if "cloud_file_load" in pytest.test_cfg.ignore_checks else 1,
        )

        hash_load = resp.headers.get("Etag")
        if hash_load is None:
            raise
        return hash_load

    
    def load_file_to_cloud_as_attach(self, file_path: str, message_id: str) -> str:
        """
        LOAD ATTACH TO CLOUD

        1) создание bundle - Загрузка файла из композера письма,
        если файл слишком большой для помещения в обычный аттач (более 25 МБ) - В ответе получаем loader_url
        2) loader_url - для загрузки файла в клауд - используем self.upload_file_to_cloud_from_mail
        получаем в ответе хэш файла
        3) Регистрируем загруженный файл и bundle - self.register_file_in_cloud_from_mail

        Args:
            file_path: путь к локальному файлу
            message_id: id письма - для прикрепления при отправке

        ожидаемый ответ:
        {
            "status": 200,
            "htmlencoded": false,
            "email": "t7zmhxtg4j1768915073@vkwm-ou.release.vkwm.ru",
            "body": {
                "loader_url": "https://uploader.e.vkwm-ou.release.vkwm.ru/upload/",
                "bundle_id": "hrQqSHt3kVVeLafFZcUzXFSi"
            }
        }

        """
        data = {
            "htmlencoded": "false",
            "message_id": message_id,
            "email": self.email,
        }
        session = self.auth.get_or_create_session("mail_cookie")
        params = {**data, "token": self.auth.access_token}
        url = f"https://e.{self.auth.DOMAIN}/api/v1/cloud/attachment/create"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7",
        }

        resp = self.auth.request_api(
            url=url,
            session=session,
            params=params,
            method="post",
            headers=headers,
            expected_http_code=200,
            expected_json_code=200,
        ).json()

        # сервер часто отвечает 500
        body = resp.get("body")
        if not isinstance(body, dict):
            raise
        bundle_id = body.get("bundle_id")
        if bundle_id is None:
            raise
        loader_url = body.get("loader_url")
        if loader_url is None:
            raise

        hash_file = self.upload_file_to_cloud_from_mail(loader_url, file_path)
        if hash_file:
            self.register_file_in_cloud_from_mail(bundle_id, file_path, hash_file)

        return bundle_id

    
    def search_file_in_folder(self, folder: str = "Inbox") -> str:
        r"""
        SEARCH FILE IN FOLDER

        поиск файла в папке
        ожидаемый ответ:
        [
            "AjaxResponse",
            "OK",
            {
                "attach_host": "af.vkwm-ou.release.vkwm.ru",
                "version": "2.2",
                "total": 1,
                "cnt": 1,
                "list": [
                    {
                        "from_to": "\"Абрамова Алевтина\" \u003ctest_login_g7tbj3fg@vkwm-ou.release.vkwm.ru\u003e",
                        "DateShort": "12:30",
                        "name": "Памятка новичка.pdf",
                        "folder_id": 500000,
                        "n": [
                            0,
                            1
                        ],
                        "from_to_email": "test_login_g7tbj3fg@vkwm-ou.release.vkwm.ru",
                        "size": 3849568,
                        "from_to_name": "Абрамова Алевтина",
                        "time": 1768901417,
                        "content_type_id": 4,
                        "unsafe": false,
                        "subject": "Памятка новичка.pdf",
                        "flags": 2,
                        "id": "17689014170509804237"
                    }
                ]
            }
        ]

        Args:
            folder: имя папки в которой ищем файл, из словаря констант

        """
        expected_resp_elements = 3
        expected_attaches_elements = 1
        session = self.auth.get_or_create_session("mail_cookie")
        url = f"https://e.{self.auth.DOMAIN}/cgi-bin/filesearch_ajax"
        params = {
            "folder_id": folder,
            "limit": 40,
            "offset": 0,
            "func_name": "ajax_search",
            "ajax_call": 1,
            "email": self.email,
            "htmlencoded": False,
            "token": self.auth.access_token,
            "_": 1768901493193,
        }
        resp = self.auth.request_api(url=url, session=session, method="get", params=params).json()
        if not isinstance(resp, List):
            raise
        if len(resp) < expected_resp_elements:
            raise

        first_element = resp[0]
        second_element = resp[1]
        third_element = resp[2]
        if not isinstance(third_element, Dict):
            raise
        total = third_element.get("total")
        if total is None:
            raise
        list_attaches = third_element.get("list")
        if list_attaches is None:
            raise
        if not isinstance(list_attaches, List):
            raise
        if len(list_attaches) < expected_attaches_elements:
            raise

        attach = list_attaches[0]
        if not isinstance(attach, Dict):
            raise
        file_id = attach.get("id")
        if file_id is None:
            raise

        return file_id

    
    def forward_attach_from_mail(self, file_id: str, message_id: str) -> Dict:
        """
        FORWARD ATTACH FROM MAIL

        ожидаемый ответ:
        {
            "body": {
                "attach": {
                    "id": "UgS1zllGiuwTxRYd",
                    "content_type": "application/pdf",
                    "size": 3849568,
                    "name": "Памятка новичка.pdf"
                },
                "space_left": 22364832
            },
            "last_modified": 1768901498,
            "status": 200,
            "htmlencoded": false,
            "email": "3test3@vkwm-ou.release.vkwm.ru"
        }
        """
        data = {
            "htmlencoded": "false",
            "id": f"{file_id};0;1",
            "message_id": message_id,
            "email": self.email,
        }
        session = self.auth.get_or_create_session("mail_cookie")
        params = {**data, "token": self.auth.access_token}
        # headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = f"https://e.{self.auth.DOMAIN}/api/v1/messages/attaches/forward/add"
        resp = self.auth.request_api(url=url, session=session, params=params, method="post").json()
        status = resp.get("status")
        body = resp.get("body")
        if not isinstance(body, dict):
            raise
        attach = body.get("attach")
        if attach is None:
            raise
        attach_id = attach.get("id")
        if attach_id is None:
            raise

        return attach_id

    # calendar api
    
    def send_event(self, to_user: "WSUser") -> None:  # noqa: PLR0915
        """
        SEND EVENT

        СОЗДАНИЕ СОБЫТИЯ С ВЛОЖЕНИЕМ, УЧАСТНИКОМ И ССЫЛКОЙ
        """

        file_path = os.path.join(".", "test_data", "attach_07.jpg")
        size = None
        self.check_user_cloud_from_calendar()
        self.get_cloud_state()
        size = self.upload_attach_from_calendar(file_path)

        attaches = []
        if size is not None:
            filename = os.path.basename(file_path)
            share_id = self.create_long_weblink(file_path)
            attaches = [{"filename": filename, "shareID": share_id, "size": size, "url": None}]

        now = datetime.now()  # noqa: DTZ005
        date_string = now.strftime("%Y-%m-%d %H:%M:%S")
        fd = add_minutes(date_string, 60)
        td = add_minutes(date_string, 90)
        event_uid = f"{uuid.uuid4()}"
        title = "new event"
        description = "new description"
        location = {"description": "new location"}
        call_link = f"https://call.vkt-trueconf.{self.auth.DOMAIN}/{generate_string(32)}"

        CreateEvent["variables"] = {
            "input": {
                "uid": event_uid,
                "title": title,
                "description": description,
                "location": location,
                "from": fd,
                "to": td,
                "fullDay": False,
                "attendees": [{"email": to_user.email, "role": "REQUIRED"}],
                "attaches": attaches,
                "reminders": [{"type": "email", "interval": 900}],
                "color": "",
                "attendeesCanInvite": True,
                "call": call_link,
            }
        }
        resp = self.auth.send_gql_query(CreateEvent)
        data = resp.get("data")
        if data is None:
            raise
        create_event = data.get("createEvent")
        if create_event is None:
            raise

        resp_title = create_event.get("title")
        resp_description = create_event.get("description")
        resp_location = create_event.get("location")
        resp_attaches = create_event.get("attaches")
        if resp_attaches is None:
            raise

        if len(attaches) > 0:
            resp_share_id = resp_attaches[0].get("shareID")
            resp_filename = resp_attaches[0].get("filename")
            resp_size = resp_attaches[0].get("size")

        self.last_event = create_event


    
    def create_cloud_dir(self) -> None:
        """
        CREATE CLOUD DIRECTORY

        Создание папки в клауде
        """
        session = self.auth.get_or_create_session("calendar")
        headers = {
            "Authorization": f"Bearer {self.auth.access_token}",
            "Accept": "application/json",
            "Refer": f"https://calendarx.{self.auth.DOMAIN}/",
            "Origin": f"https://calendarx.{self.auth.DOMAIN}",
        }
        folder_name = "Календарь"
        url = f"https://openapi.cloud.{self.auth.DOMAIN}/api/v1/private/mkdir/{folder_name}"
        resp = self.auth.request_api(
            url=url, headers=headers, session=session, expected_http_code=201, method="post"
        ).json()
        name = resp.get("name")
    
    def get_cloud_state(self) -> None:
        """
        GET CLOUD STATE

        Проверка статуса папки клауда
        """
        session = self.auth.get_or_create_session("calendar")
        headers = {
            "Authorization": f"Bearer {self.auth.access_token}",
            "Accept": "application/json",
            "Refer": f"https://calendarx.{self.auth.DOMAIN}/",
            "Origin": f"https://calendarx.{self.auth.DOMAIN}",
        }
        url = f"https://openapi.cloud.{self.auth.DOMAIN}/api/v1/private/stat/Календарь"
        resp = self.auth.request_api(url=url, headers=headers, session=session, expected_http_code=None)
        not_found_code = 404
        if resp.status_code == not_found_code:
            self.create_cloud_dir()
        else:
            kind = resp.json().get("kind")
    
    def upload_attach_from_calendar(self, file_path: str) -> int:
        """
        UPLOAD ATTACH FROM CALENDAR

        Добавление файла в облако из календаря
        """
        session = self.auth.get_or_create_session("calendar")
        headers = {
            "Authorization": f"Bearer {self.auth.access_token}",
            "Content-Type": "image/jpeg",
            "Accept": "application/json, text/plain, */*",
            "Refer": f"https://calendarx.{self.auth.DOMAIN}/",
            "Origin": f"https://calendarx.{self.auth.DOMAIN}",
        }
        filename = os.path.basename(file_path)
        url = f"https://openapi.cloud.{self.auth.DOMAIN}/api/v1/private/create/Календарь/{filename}"
        with open(file_path, "rb") as file:
            files = {"file": (filename, file, "image/jpeg")}
            resp = self.auth.request_api(
                url=url,
                method="put",
                headers=headers,
                session=session,
                files=files,
                expected_http_code=200,
                tries=5 if "cloud_file_load" in pytest.test_cfg.ignore_checks else 1,
            ).json()
            size = resp.get("size")
            if size is None:
                raise
            return size

    
    def create_long_weblink(self, file_path: str) -> str:
        """
        CREATE LONG WEBLINK

        Создание веб ссылки для аттача
        """
        session = self.auth.get_or_create_session("calendar")
        headers = {
            "Authorization": f"Bearer {self.auth.access_token}",
            "Accept": "application/json",
            "Refer": f"https://calendarx.{self.auth.DOMAIN}/",
            "Origin": f"https://calendarx.{self.auth.DOMAIN}",
        }
        filename = os.path.basename(file_path)
        url = f"https://openapi.cloud.{self.auth.DOMAIN}/api/v1/private/share/Календарь/{filename}?long_weblink"
        resp = self.auth.request_api(
            url=url, method="post", headers=headers, session=session, expected_http_code=201
        ).json()
        share_id = resp.get("id")
        image_url = resp.get("url")
        if share_id is None:
            raise
        if image_url is None:
            raise

        return share_id

    def check_user_cloud_from_calendar(self) -> None:
        """
        CHECK USER CLOUD FROM CALENDAR

        Проверка активного диска у пользователя из календаря
        """
        session = self.auth.get_or_create_session("calendar")
        self.auth.get_cloud_token(session=session)
        headers = {
            "Authorization": f"Bearer {self.auth.access_token}",
            "Accept": "application/json",
            "Refer": f"https://calendarx.{self.auth.DOMAIN}/",
            "Origin": f"https://calendarx.{self.auth.DOMAIN}",
        }
        url = f"https://openapi.cloud.{self.auth.DOMAIN}/api/v1/private/check_cloud"
        resp = self.auth.request_api(url=url, headers=headers, session=session, expected_http_code=200).json()
        active = resp.get("active")
    
    def create_calendar(self) -> None:
        """
        CREATE CALENDAR

        Создание персонального календаря пользователю
        """
        calendar_uid = f"{uuid.uuid4()}".upper()
        title = "new calendar"
        color = "#FFEF9D"
        variables = {
            "input": {
                "uid": calendar_uid,
                "attendees": [],
                "color": color,
                "title": title,
                "description": "",
                "reminders": [{"interval": 900, "type": "email"}],
                "sortWeight": 1,
                "shareReminders": False,
                "freebusyEnabled": True,
            }
        }
        CreateCalendar["variables"] = variables
        resp = self.auth.send_gql_query(CreateCalendar)

        data = resp.get("data")
        if not isinstance(data, Dict):
            raise

        create_calendar = data.get("createCalendar")
        if not isinstance(create_calendar, Dict):
            raise

        uid_from_api = create_calendar.get("uid")
        title_from_api = create_calendar.get("title")
        color_from_api = create_calendar.get("color")
        type_from_api = create_calendar.get("type")

    def check_event(self, from_user: "WSUser") -> None:  # noqa: PLR0915
        """CHECK EVENT FROM USER"""
        outgoing_event = from_user.last_event
        if not isinstance(outgoing_event, Dict):
            raise
        outgoing_event_title = outgoing_event.get("title")
        if outgoing_event_title is None:
            raise
        outgoing_event_uid = outgoing_event.get("uid")
        if outgoing_event_uid is None:
            raise
        outgoing_event_from = outgoing_event.get("from")
        ioutgoing_event_to = outgoing_event.get("to")
        outgoing_event_description = outgoing_event.get("description")
        outgoing_event_attaches = outgoing_event.get("attaches")
        resp = self.auth.send_gql_query(CalendarsQuery)
        data = resp.get("data")
        if data is None:
            raise
        calendars = data.get("calendars")
        if calendars is None:
            raise
        calendar = calendars[0]
        if calendars is None:
            raise
        calendar_uid = calendar.get("uid")
        if calendar_uid is None:
            raise

        variables = {"eventUID": outgoing_event_uid, "calendarUID": calendar_uid, "recurrentID": None}
        GetSingleEvent["variables"] = variables
        resp = self.auth.send_gql_query(GetSingleEvent)
        data = resp.get("data")
        if data is None:
            raise
        event = data.get("event")
        if event is None:
            raise

        incomming_uid = event.get("uid")
        incomming_title = event.get("title")
        incomming_from = event.get("from")
        incomming_to = event.get("to")
        incomming_status = event.get("status")
        incomming_description = event.get("description")
        incomming_organizer = event.get("organizer")
        if incomming_organizer is None:
            raise

        incomming_owner_email = incomming_organizer.get("email")
        incomming_is_organizer = event.get("isOrganizer")
        incomming_attaches = event.get("attaches")

    def get_cloud_quota(self) -> None:
        """GET CLOUD QUOTA"""
        session = self.auth.get_or_create_session("cloud")
        url = f"{self.auth.CLOUD_URL}/api/v4/user/quota"
        resp = self.auth.request_api(
            url=url, headers=self.auth.cloud_headers, session=session, expected_http_code=200
        ).json()
        quota = resp.get("quota")

    
    def load_file_to_cloud(self, path: str, file_path: str) -> str:
        """
        LOAD FILE TO CLOUD

        Метод загружает файл, который никому не принадлежит и доступен по прямой ссылке.
        Чтобы сделать загруженный файл аттачом, нужно взывать self.register_cloud_file
        """
        session = self.auth.get_or_create_session("cloud")
        url = f"{path}/upload-web/?cloud_domain=2"
        headers = {
            "accept": "*/*",
            "accept-language": "en",
            "access-control-request-headers": "content-type,x-requested-with",
            "access-control-request-method": "PUT",
            "origin": f"https://cloud.{self.auth.DOMAIN}",
            "priority": "u=1, i",
            "referer": f"https://cloud.{self.auth.DOMAIN}/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",  # noqa: E501
        }
        resp = self.auth.request_api(
            url=url, session=session, method="options", headers=headers, expected_http_code=200
        )

        with open(file_path, "rb") as file:
            file_content = file.read()

        headers = {
            "Content-Type": "application/octet-stream",
            "Content-Length": str(len(file_content)),
            "Content-Disposition": f'attachment; filename="{os.path.basename(file_path)}"',
            "accept-encoding": "gzip, deflate, br, zstd",
        }

        resp = self.auth.request_api(
            url=url,
            session=session,
            method="put",
            headers=headers,
            data=file_content,
            expected_http_code=201,
            tries=5 if "cloud_file_load" in pytest.test_cfg.ignore_checks else 1,
        )

        hash_load = resp.headers.get("Etag")
        if hash_load is None:
            raise
        return hash_load

    
    def register_cloud_file(self, file_path: str, hash_file: str) -> str:
        """
        REGISTER CLOUD FILE

        Добавление файла в облако пользователя по хэшу из клауда (куда был загружен файл)
        """
        file_name = os.path.basename(file_path)
        # По неизвестной причине апи может отбивать файлы с точкой, ну нам здесь не принципиально
        file_name_for_api = file_name.replace(".", "_")
        size = os.path.getsize(file_path)
        json_data = {
            "conflict": "rewrite",
            "hash": hash_file,
            "home": f"/{file_name_for_api}",
            "path": f"/{file_name_for_api}",
            "size": size,
        }
        session = self.auth.get_or_create_session("cloud")
        headers = {
            **self.auth.cloud_headers,
            "x-vfs-action": "file_create",
            "x-email": self.email,
            "x-api-version": "4",
            "x-req-id": generate_string(8),
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "Origin": f"https://cloud.{self.auth.DOMAIN}",
            "priority": "u=1, i",
            "Referer": f"https://cloud.{self.auth.DOMAIN}/home/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/143.0.0.0 Safari/537.36",
        }
        url = f"https://cloud.{self.auth.DOMAIN}/api/v4/file/add"
        resp = self.auth.request_api(
            url=url, session=session, headers=headers, data=json.dumps(json_data), method="post"
        ).json()
        file_name_in_response: str = resp.get("body")
        if file_name_in_response is None:
            raise
        file_name_in_response = file_name_in_response.strip("/")
        return file_name_in_response

    
    def get_file_info_from_cloud(self, file_path: str) -> str:
        """GET FILE INFO FROM CLOUD"""
        file_name = os.path.basename(file_path)
        data = {
            "home": f"/{file_name}",
        }
        session = self.auth.get_or_create_session("cloud")
        self.auth.get_cloud_token(session)
        params = {
            **data,
            "access_token": f"{self.auth.access_token}",
        }
        url = f"https://cloud.{self.auth.DOMAIN}/api/v2/file"
        resp = self.auth.request_api(url=url, session=session, params=params, json=data).json()
        file_name = resp.get("body").get("name")
        return file_name

    
    def download_file_from_cloud(self, attach_name: str) -> None:
        """DOWNLOAD FILE INFO FROM CLOUD"""
        session = self.auth.get_or_create_session("cloud")
        url = f"https://cloclo.{self.auth.DOMAIN}/attach/{attach_name}"
        self.auth.request_api(url=url, session=session)

    
    def create_user_contact(self) -> Dict:
        """
        CREATE USER CONTACT

        Для создания контакта используется тот же генератор что и для создания пользователя в бизе
        """
        contact = generate_user_data("")
        session = self.auth.get_or_create_session("mail_cookie")
        url = f"https://e.{self.auth.DOMAIN}/api/v1/ab/contacts/add"
        params = {
            "token": self.auth.access_token,
            "email": self.email,
            "htmlencoded": "false",
            "contacts": json.dumps(
                [
                    {
                        "name": {"first": contact.get("firstname"), "last": contact.get("lastname")},
                        "nick": "",
                        "company": "",
                        "comment": "",
                        "job_title": "",
                        "boss": "",
                        "sex": contact.get("gender"),
                        "address": "",
                        "labels": [],
                        "emails": [contact.get("email")],
                        "phones": [],
                        "social": [],
                    }
                ]
            ),
        }
        resp = self.auth.request_api(
            url=url, session=session, params=params, method="post", expected_http_code=200, expected_json_code=200
        ).json()
        body = resp.get("body")
        if not isinstance(body, List):
            raise
        lenght = len(body)
        contact_id = body[0]
        if contact_id is None:
            raise

        contact["id"] = contact_id
        return contact

    
    def update_user_contact(self, contact: Dict) -> Dict:
        """UPDATE USER CONTACT"""
        updated_contact = generate_user_data("")
        session = self.auth.get_or_create_session("mail_cookie")
        url = f"https://e.{self.auth.DOMAIN}/api/v1/ab/contacts/edit"
        params = {
            "token": self.auth.access_token,
            "email": self.email,
            "htmlencoded": "false",
            "contacts": json.dumps(
                [
                    {
                        "id": contact.get("id"),
                        "name": {"first": updated_contact.get("firstname"), "last": updated_contact.get("lastname")},
                    }
                ],
            ),
        }
        resp = self.auth.request_api(
            url=url, session=session, params=params, method="post", expected_http_code=200, expected_json_code=200
        ).json()

        body = resp.get("body")
        if not isinstance(body, List):
            raise

        lenght = len(body)
        contact_id = body[0]
        contact["id"] = contact_id
        return contact

    
    def delete_user_contact(self, contact: Dict) -> None:
        """DELETE USER CONTACT"""
        session = self.auth.get_or_create_session("mail_cookie")
        url = f"https://e.{self.auth.DOMAIN}/api/v1/ab/contacts/remove"
        params = {
            "token": self.auth.access_token,
            "email": self.email,
            "htmlencoded": "false",
            "contacts": json.dumps(
                [contact.get("id")],
            ),
        }
        resp = self.auth.request_api(
            url=url, session=session, params=params, method="post", expected_http_code=200, expected_json_code=200
        ).json()
        body = resp.get("body")
        if not isinstance(body, List):
            raise

        lenght = len(body)
        contact_id = body[0]
