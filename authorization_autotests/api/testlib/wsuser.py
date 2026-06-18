import json
import os
from types import SimpleNamespace
from typing import TYPE_CHECKING, Dict, List, Optional

import pytest
from ..core.decorators import qacore_decorators
from ..core.exceptions import AutotestException, FrameworkException
from ..core.helpers import generate_string
from ..core.logger import FMT_DEFAULT, FMT_OK, FMT_WARN, log
from ..core.steps_common import compare_two_items
from authorization import UserAuth
from const import ADMIN_USER, CLOUD_UPLOAD_DOMAIN, DEFAULT_USER_PASSWORD
from helpers import add_minutes, generate_user_data

if TYPE_CHECKING:
    from __main__ import WSUser


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
    @qacore_decorators
    def biz_get_users(self) -> Dict:
        """BIZ GET USERS"""
        session = self.auth.get_or_create_session("biz")
        return self.auth.request_api(
            url=f"https://biz.{self.auth.DOMAIN}/api/v1/domains/{self.auth.DOMAIN_NUMBER}/users?limit=100",
            session=session,
            headers=self.auth.biz_headers,
        ).json()

    @qacore_decorators
    def biz_create_multiple_users(self, amount: int = 2) -> SimpleNamespace:
        """CREATE MULTIPLE BIZ USERS"""
        password = DEFAULT_USER_PASSWORD
        if self.email != ADMIN_USER:
            raise FrameworkException("Please use admin to create users in biz")
        created_users = [self.biz_create_user(password) for _ in range(amount)]
        result_dict = {}
        # Добавляем каждого пользователя под своим ключом
        for i, user_data in enumerate(created_users, 1):
            user_data["password"] = password
            result_dict[f"user{i}"] = WSUser(user=user_data)
            log.info(f"Создан пользователь: {user_data.get('email')}", extra=FMT_OK)
        return SimpleNamespace(**result_dict)

    @qacore_decorators
    def biz_create_user(self, password: str) -> Dict:
        """BIZ CREATE USER"""
        user = generate_user_data(password)
        log.info(f"Создание пользователя в biz: {user['email']}", extra=FMT_DEFAULT)
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

    @qacore_decorators
    def biz_delete_user(self, user: "WSUser") -> Dict:
        """BIZ DELETE USER"""
        log.info("Удаление пользователя в biz: %s", self.email, extra=FMT_DEFAULT)
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
        if status is None:
            raise AutotestException("Ожидается получить поле 'status' в ответе")
        compare_two_items(status, "==", "deleted", log_result=False)
        log.info(f"Пользователь удален: {user.email}", extra=FMT_OK)
        return resp

    @qacore_decorators
    def biz_create_user_cloud(self, for_user: "WSUser") -> Dict:
        """
        BIZ CREATE USER CLOUD

        Создание клауда для пользователя

        """
        log.info(f"Создание облака для пользователя: {for_user.email}", extra=FMT_DEFAULT)
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
        log.info(f"Создано облака для пользователя: {for_user.email}", extra=FMT_OK)
        return resp

    @qacore_decorators
    def biz_update_user_info(self, for_user: "WSUser") -> Dict:
        """BIZ UPDATE USER INFO"""
        log.info(f"Обновление данных пользователя: {self.email}", extra=FMT_DEFAULT)
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
        if firstname is None:
            raise AutotestException(f"Ожидается получить поле 'firstname' в ответе: {resp.text}")
        if lastname is None:
            raise AutotestException(f"Ожидается получить поле 'lastname' в ответе: {resp.text}")
        compare_two_items(firstname, "==", data.get("firstname"), log_result=False)
        compare_two_items(lastname, "==", data.get("lastname"), log_result=False)

        log.info(
            f"Данные пользователя изменены: {for_user.first_name} -> {firstname}, {for_user.last_name} -> {lastname}",
            extra=FMT_OK,
        )
        return resp

    # mail api
    @qacore_decorators
    def get_folders(self) -> Dict:
        """
        GET FOLDERS

        Получаем папки в почте у пользователя

        """
        log.info("Получение папок пользователя: %s", self.email, extra=FMT_DEFAULT)
        session = self.auth.get_or_create_session("mail_cookie")
        params = {"email": self.email, "token": self.auth.access_token}
        return self.auth.request_api(
            url=f"https://e.{self.auth.DOMAIN}/api/v1/folders", session=session, params=params
        ).json()

    @qacore_decorators
    def get_last_unread_email(self, add_in: Optional[Dict] = None) -> Dict:
        """
        GET LAST UNREAD EMAIL

        Возвращает последнее непрочитанное письмо, дополнительно можно указать папку
        Args:
            add_in: список дополнительных параметров: {'folder', '0'}
        """
        log.info(f"Получение последнего непрочитанного письма для: {self.email}", extra=FMT_DEFAULT)
        session = self.auth.get_or_create_session("mail_cookie")
        params = {"token": self.auth.access_token, "email": self.email, "snippet_limit": 1000, "htmlencoded": "false"}
        if add_in:
            params = {**params, **add_in}
        return self.auth.request_api(
            url=f"https://e.{self.auth.DOMAIN}/api/v1/messages/status/unread/last", session=session, params=params
        ).json()

    @qacore_decorators
    def send_mail(self, to_user: "WSUser", attach_type: Optional[str] = None) -> Dict:
        """
        SEND MAIL

        Отправление письма, варианты отправки с аттачами:
        1) attach_type == "attach" - загрузка файла менее 25 МБ (без загрузки в клауд)
        2) attach_type == "cloud_stock" - загрузка файла более 25 МБ (с загрузкой в клауд)
        3) attach_type == "forward_attach_from_mail" - прикрепление файла из другого письма

        """
        log.info(f"Отправка письма от: {self.email} для: {to_user.email}", extra=FMT_DEFAULT)
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
        log.info(f"Отправлено письмо от: {self.email}, к: {to_user.email}", extra=FMT_OK)
        ########### получаем отправленное письмо чтобы сохранить в памяти
        # Для ОУ стенда если загрузка в аттача в облако не прошло - письмо почему то может и не отправится
        # пока игнорируем, но выглядит странно
        try:
            self.last_sent_mail = self.get_thread(subject, folder="Sent")
        except AutotestException:
            if "cloud_file_load" in pytest.test_cfg.ignore_checks:
                self.last_sent_mail = None
                log.warning("Ignored cloud_file_load check", extra=FMT_WARN)
            else:
                raise

        return self.last_sent_mail

    @qacore_decorators
    def check_inbox_mail(self, from_user: "WSUser", with_attach: bool = False, expected_messages: int = 1) -> dict:
        """
        CHECK INBOX MAIL FROM USER

        проверяем письмо во входящих у получателя (self - тот кто инициализировал проверку),
        уникальный текст письма берется у (from_user - отправитель),
        в итоге проверяется только subject и folder
        with_attach - проверка наличия аттача
        не проверяется его отсутствие
        """
        log.info(f"Проверка письма во входящих для {self.email}", extra=FMT_DEFAULT)
        outbox_mail = from_user.last_sent_mail

        if not isinstance(outbox_mail, Dict):
            raise AutotestException("Текст письма не найден у отправителя")

        outbox_mail_text = outbox_mail.get("snippet")
        if outbox_mail_text is None:
            raise AutotestException("'snippet' письма не найден у отправителя")

        outbox_subject = outbox_mail.get("subject")
        messages = self.get_thread_messages(outbox_subject, "Inbox")
        if not isinstance(messages, List):
            raise AutotestException("Текст письма не найден у получателя")
        lenght = len(messages)
        compare_two_items(lenght, "==", expected_messages, log_result=False)
        inbox_mail = messages[0]  # берем первое сообщение
        inbox_subject = inbox_mail.get("subject")
        inbox_folder = inbox_mail.get("folder")
        compare_two_items(inbox_subject, "==", outbox_subject, log_result=False)
        compare_two_items(inbox_folder, "==", 0, log_result=False)
        if with_attach:
            flags = inbox_mail.get("flags")
            if flags is None:
                raise AutotestException("Ожидается поле 'flags'")
            attach = flags.get("attach")
            if attach is None:
                raise AutotestException("Ожидается поле 'attach'")
            compare_two_items(attach, "is", with_attach, log_result=False)
            log.info(
                "Письмо получено пользователем: %s, от: %s, аттач присутствует",
                self.email,
                from_user.email,
                extra=FMT_OK,
            )
        else:
            log.info("Письмо получено пользователем: %s, от: %s", self.email, from_user.email, extra=FMT_OK)
        return inbox_mail

    @qacore_decorators
    def open_attach(self, from_mail: Dict, attach_type: str = "attach") -> None:
        """
        OPEN ATTACH FROM USER

        Проверяем что файл доступен для скачивания
        """
        log.info("Открытие аттача пользователем: %s", self.email, extra=FMT_DEFAULT)
        # получить письмо по id
        mail_id = from_mail.get("id")
        if mail_id is None:
            raise AutotestException("Ожидается поле 'id'")

        mail = self.get_email_by_id(mail_id)
        body = mail.get("body")

        if not isinstance(body, Dict):
            raise AutotestException("Ожидалось получить 'body' письма")

        attaches = body.get("attaches")

        if not isinstance(attaches, Dict):
            raise AutotestException("Ожидалось получить 'attaches' в 'body' письма")

        list_attaches = attaches.get("list")
        if not isinstance(list_attaches, List):
            raise AutotestException("Ожидалось получить 'list' в 'attaches' письма")
        lenght = len(list_attaches)
        compare_two_items(lenght, "==", 1, log_result=False)
        mail_attach = list_attaches[0]
        mail_attach_type = mail_attach.get("type")
        compare_two_items(mail_attach_type, "==", attach_type, log_result=False)
        href = mail_attach.get("href")
        if not isinstance(href, Dict):
            raise AutotestException("Ожидалось получить 'href' в 'mail_attach' письма")
        download_url = href.get("download")
        if download_url is None:
            raise AutotestException("Ожидалось получить 'download' в 'href' письма")

        # качаем изображение по url
        self.download_image(from_url=download_url)
        log.info("Изображение успешно открывается по ссылке", extra=FMT_OK)

    @qacore_decorators
    def download_image(self, from_url: str) -> None:
        """
        DOWNLOAD IMAGE

        Скачивание файла

        Args:
            from_url: url изображения

        """
        log.info(f"Скачивание изображения: {from_url}", extra=FMT_DEFAULT)
        session = self.auth.get_or_create_session("mail_cookie")
        resp = self.auth.request_api(url=from_url, session=session, method="get", expected_http_code=200)
        # Проверяем, что ответ содержит данные
        if not resp.content:
            raise AutotestException("Получен пустой ответ вместо изображения")

        log.info(f"Изображение получено длина: {len(resp.content)}", extra=FMT_OK)

    @qacore_decorators
    def get_email_by_id(self, mail_id: int) -> Dict:
        """
        GET MAIL BY ID

        Получение письма по id

        Args:
            mail_id: айди письма

        """
        log.info("Получение письма по id: %s", mail_id, extra=FMT_DEFAULT)
        session = self.auth.get_or_create_session("mail_cookie")
        params = {"id": mail_id, "token": self.auth.access_token, "email": self.email}
        url = f"https://e.{self.auth.DOMAIN}/api/v1/messages/message"
        resp = self.auth.request_api(url=url, session=session, params=params, method="get")
        self.auth.check_codes(resp, 200, None)

        log.info(f"Получено письмо с id: {mail_id}, у пользователя: {self.email}", extra=FMT_OK)
        return resp.json()

    @qacore_decorators
    def get_thread_messages(self, search_subject: str, folder: str = "Sent") -> Dict:
        """
        FIND THREAD WITH

        Возвращает список писем треда найденного по теме
        """
        log.info(f"Получения треда писем в ящике: {self.email}/{folder} c темой: {search_subject}", extra=FMT_DEFAULT)
        thread = self.get_thread(search_subject, folder)
        thread_id = thread.get("id")
        if thread_id is None:
            raise AutotestException("Ожидалось получить 'id' треда")
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
        if not isinstance(body, Dict):
            raise AutotestException(f"Ожидется получить поле 'body' в ответе: {response.json()}")

        messages = body.get("messages")
        if messages is None:
            raise AutotestException(f"Ожидется получить поле 'messages' в ответе: {body}")

        log.info(f"Получен список писем треда с темой: {search_subject}", extra=FMT_OK)
        return messages

    @qacore_decorators
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
        log.info(f"Загрузка аттача на почту: {file_path}", extra=FMT_DEFAULT)
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
                raise AutotestException(f"body имеет некорректный тип: {body}")

            attach = body.get("attach")
            if attach is None:
                raise AutotestException("Ожидалось получить 'attach' в ответе")
            attach_id = attach.get("id")
            if attach_id is None:
                raise AutotestException("Ожидалось получить 'id' в ответе")
            log.info(f"Загружен аттач: {attach_id}, к письму: {message_id}, от: {self.email}", extra=FMT_OK)
            return attach_id

    @qacore_decorators
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
        log.info("Добавление аттача из облака к письму: %s", bundle_id, extra=FMT_DEFAULT)
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
        log.debug("data: %s", data)
        url = f"https://e.{self.auth.DOMAIN}/api/v1/cloud/attachment/add"
        resp = self.auth.request_api(
            url=url, session=session, params=params, method="post", expected_http_code=200, expected_json_code=200
        ).json()
        body = resp.get("body")
        if not isinstance(body, dict):
            raise AutotestException(f"body имеет некорректный тип: {body}")

        file_id = body.get("file_id")
        if file_id is None:
            raise AutotestException("Ожидалось получить 'file_id' в ответе")
        log.info(f"Файл с id: {file_id} прикреплен к письму пользователя: {self.email}", extra=FMT_OK)

    @qacore_decorators
    def upload_file_to_cloud_from_mail(self, loader_url: str, file_path: str) -> str:
        """
        UPLOAD FILE TO CLOUD FROM MAIL

        Загрузка файла из композера письма, если файл более 25 МБ - используется loader_url

        Args:
            loader_url: лоадер url
            file_path: путь к локальному файлу

        """
        log.info("Загрузка файла в клауд через почту: %s", loader_url, extra=FMT_DEFAULT)
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

        try:
            resp = self.auth.request_api(
                url=url,
                session=session,
                method="put",
                headers=headers,
                data=file_content,
                expected_http_code=201,
                tries=5 if "cloud_file_load" in pytest.test_cfg.ignore_checks else 1,
            )
        except AutotestException:
            if "cloud_file_load" in pytest.test_cfg.ignore_checks:
                log.warning("Ignored cloud_file_load check", extra=FMT_WARN)
                return ""
            raise

        hash_load = resp.headers.get("Etag")
        if hash_load is None:
            raise AutotestException("Ожидалось получить 'etag' в ответе")
        log.info(f"Аттач загружен в облако {hash_load}", extra=FMT_OK)
        return hash_load

    @qacore_decorators
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
        log.info(f"Загрузка аттача в клауд через почту: {file_path}", extra=FMT_DEFAULT)
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

        log.debug("resp: %s", resp)
        # сервер часто отвечает 500
        body = resp.get("body")
        if not isinstance(body, dict):
            raise AutotestException(f"body имеет некорректный тип: {body}")
        bundle_id = body.get("bundle_id")
        if bundle_id is None:
            raise AutotestException("Ожидалось получить 'bundle_id' в ответе")
        loader_url = body.get("loader_url")
        if loader_url is None:
            raise AutotestException("Ожидалось получить 'loader_url' в ответе")
        log.info("Файл ожидает загрузки: %s, к письму: %s, от: %s", bundle_id, message_id, self.email, extra=FMT_OK)

        hash_file = self.upload_file_to_cloud_from_mail(loader_url, file_path)
        if hash_file:
            self.register_file_in_cloud_from_mail(bundle_id, file_path, hash_file)

        return bundle_id

    @qacore_decorators
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
        log.info("Пересылка аттача по почте: %s", file_id, extra=FMT_DEFAULT)
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
        compare_two_items(status, "==", 200, log_result=False)
        body = resp.get("body")
        if not isinstance(body, dict):
            raise AutotestException(f"body имеет некорректный тип: {body}")
        attach = body.get("attach")
        if attach is None:
            raise AutotestException("Ожидалось получить 'attach' в ответе")
        attach_id = attach.get("id")
        if attach_id is None:
            raise AutotestException("Ожидалось получить 'id' в ответе")
        log.info(f"Прикреплен аттач: {attach_id}, к письму id: {message_id}, от: {self.email}", extra=FMT_OK)
        return attach_id

    @qacore_decorators
    def create_cloud_dir(self) -> None:
        """
        CREATE CLOUD DIRECTORY

        Создание папки в клауде
        """
        log.info("Создание папки в клауде пользователю: %s", self.email, extra=FMT_DEFAULT)
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
        compare_two_items(name, "==", folder_name, log_result=False)
        log.info(f"Папка 'Календарь' создана для: {self.email}", extra=FMT_OK)

    @qacore_decorators
    def get_cloud_state(self) -> None:
        """
        GET CLOUD STATE

        Проверка статуса папки клауда
        """
        log.info("Проверка статуса папки клауда: %s", self.email, extra=FMT_DEFAULT)
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
            log.info("Папка 'Календарь' отсутствует: %s", self.email, extra=FMT_OK)
            self.create_cloud_dir()
        else:
            kind = resp.json().get("kind")
            compare_two_items(kind, "==", "folder", log_result=False)
            log.info("Папка 'Календарь' присутствует: %s", self.email, extra=FMT_OK)

    @qacore_decorators
    def upload_attach_from_calendar(self, file_path: str) -> int:
        """
        UPLOAD ATTACH FROM CALENDAR

        Добавление файла в облако из календаря
        """
        log.info("Добавление файла в облако из календаря: %s", file_path, extra=FMT_DEFAULT)
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
                raise AutotestException("Ожидалось получить 'size' в ответе")
            log.info(f"Загружен аттач: {filename}, в папку 'Календарь', пользователю: {self.email}", extra=FMT_OK)
            return size

    @qacore_decorators
    def create_long_weblink(self, file_path: str) -> str:
        """
        CREATE LONG WEBLINK

        Создание веб ссылки для аттача
        """
        log.info("Создание веб ссылки для аттача: %s", file_path, extra=FMT_DEFAULT)
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
            raise AutotestException("Ожидалось получить 'id' в ответе")
        if image_url is None:
            raise AutotestException("Ожидалось получить 'image_url' в ответе")
        log.info("Веб ссылка создана: %s", share_id, extra=FMT_OK)
        return share_id

    @qacore_decorators
    def check_user_cloud_from_calendar(self) -> None:
        """
        CHECK USER CLOUD FROM CALENDAR

        Проверка активного диска у пользователя из календаря
        """
        log.info("Проверка активного диска у пользователя из календаря: %s", self.email, extra=FMT_DEFAULT)
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
        compare_two_items(active, "is", True, desc=f"Активный статус облака у пользователя {self.email}")
        log.info("Диск активен для пользователя: %s", self.email, extra=FMT_OK)

    @qacore_decorators
    def get_cloud_quota(self) -> None:
        """GET CLOUD QUOTA"""
        log.info("Получение доступной квоты в облаке: %s", self.email, extra=FMT_DEFAULT)
        session = self.auth.get_or_create_session("cloud")
        url = f"{self.auth.CLOUD_URL}/api/v4/user/quota"
        resp = self.auth.request_api(
            url=url, headers=self.auth.cloud_headers, session=session, expected_http_code=200
        ).json()
        quota = resp.get("quota")
        log.info("Размер квоты: %s", quota, extra=FMT_OK)

    @qacore_decorators
    def load_file_to_cloud_from_disk(self) -> str:
        """
        LOAD FILE TO CLOUD FROM DISK

        Загрузка файла в клауд из веб - диска
        """
        log.info("Начало загрузки файла в облако", extra=FMT_DEFAULT)
        file_path = os.path.join(".", "test_data", "attach_04.png")
        loader_url = f"https://{CLOUD_UPLOAD_DOMAIN}"
        hash_file = self.load_file_to_cloud(loader_url, file_path)
        if not hash_file:
            return ""

        log.info("Загрузка файла в облако завершена", extra=FMT_OK)
        return self.register_cloud_file(file_path, hash_file)

    @qacore_decorators
    def load_file_to_cloud(self, path: str, file_path: str) -> str:
        """
        LOAD FILE TO CLOUD

        Метод загружает файл, который никому не принадлежит и доступен по прямой ссылке.
        Чтобы сделать загруженный файл аттачом, нужно взывать self.register_cloud_file
        """
        log.info(f"Загрузка файла в облако: {file_path}", extra=FMT_DEFAULT)
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

        try:
            resp = self.auth.request_api(
                url=url,
                session=session,
                method="put",
                headers=headers,
                data=file_content,
                expected_http_code=201,
                tries=5 if "cloud_file_load" in pytest.test_cfg.ignore_checks else 1,
            )
        except AutotestException:
            if "cloud_file_load" in pytest.test_cfg.ignore_checks:
                log.warning("Ignored cloud_file_load check", extra=FMT_WARN)
                return ""

            raise

        hash_load = resp.headers.get("Etag")
        if hash_load is None:
            raise AutotestException(f"Не получен 'etag' в ответе: {resp.headers}")
        log.info(f"Файл загружен в облако: {hash_load}", extra=FMT_OK)
        return hash_load

    @qacore_decorators
    def register_cloud_file(self, file_path: str, hash_file: str) -> str:
        """
        REGISTER CLOUD FILE

        Добавление файла в облако пользователя по хэшу из клауда (куда был загружен файл)
        """
        log.info(f"Добавление файла в облако к пользователю: {file_path}", extra=FMT_DEFAULT)
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
            raise AutotestException("Ожидалось получить поле 'body' в ответе")
        file_name_in_response = file_name_in_response.strip("/")
        compare_two_items(file_name_in_response, "==", file_name_for_api, log_result=False)
        log.info(f"Aттач добавлен в облако: {file_name_in_response}", extra=FMT_OK)
        return file_name_in_response

    @qacore_decorators
    def get_file_info_from_cloud(self, file_path: str) -> str:
        """GET FILE INFO FROM CLOUD"""
        log.info("Получени информации о файле из облака: %s", file_path, extra=FMT_DEFAULT)
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
        log.info("Информация о файле получена: %s", file_name, extra=FMT_OK)
        return file_name

    @qacore_decorators
    def download_file_from_cloud(self, attach_name: str) -> None:
        """DOWNLOAD FILE INFO FROM CLOUD"""
        log.info("Загрузка файла из облака: %s", attach_name, extra=FMT_DEFAULT)
        session = self.auth.get_or_create_session("cloud")
        url = f"https://cloclo.{self.auth.DOMAIN}/attach/{attach_name}"
        self.auth.request_api(url=url, session=session)
        log.info("Файл успешно загружен", extra=FMT_OK)

    @qacore_decorators
    def create_user_contact(self) -> Dict:
        """
        CREATE USER CONTACT

        Для создания контакта используется тот же генератор что и для создания пользователя в бизе
        """
        contact = generate_user_data("")
        log.info("Создание пользовательского контакта: %s", contact.get("email"), extra=FMT_DEFAULT)
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
            raise AutotestException(f"Ожидается получить поле 'body' как список: {resp.text}")
        lenght = len(body)
        compare_two_items(lenght, "==", 1, log_result=False)
        contact_id = body[0]
        if contact_id is None:
            raise AutotestException(f"Ожидается получить в ответе 'id' созданного контакта: {body}")

        log.info("Контакт c 'id': %s, создан", contact_id, extra=FMT_OK)
        contact["id"] = contact_id
        return contact

    @qacore_decorators
    def update_user_contact(self, contact: Dict) -> Dict:
        """UPDATE USER CONTACT"""
        updated_contact = generate_user_data("")
        log.info(
            f"Изменение пользовательского контакта: {contact.get('email')}: "
            f"{contact.get('firstname')} -> {updated_contact.get('firstname')}; "
            f"{contact.get('lastname')} -> {updated_contact.get('lastname')}",
            extra=FMT_DEFAULT,
        )
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
            raise AutotestException(f"Ожидается получить поле 'body' как список: {resp.text}")

        lenght = len(body)
        compare_two_items(lenght, "==", 1, log_result=False)
        contact_id = body[0]
        compare_two_items(contact_id, "==", contact.get("id"), log_result=False)
        contact["id"] = contact_id
        log.info("Контакт %s обновлен 'id': %s, создан", contact.get("email"), contact_id, extra=FMT_OK)
        return contact

    @qacore_decorators
    def delete_user_contact(self, contact: Dict) -> None:
        """DELETE USER CONTACT"""
        log.info("Удаление пользовательского контакта: %s", contact.get("email"), extra=FMT_DEFAULT)
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
            raise AutotestException(f"Ожидается получить поле 'body' как список: {resp.text}")

        lenght = len(body)
        compare_two_items(lenght, "==", 1, log_result=False)
        contact_id = body[0]
        compare_two_items(contact_id, "==", contact.get("id"), log_result=False)
        log.info("Контакт %s удален", contact.get("email"), extra=FMT_OK)
