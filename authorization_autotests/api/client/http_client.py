import logging
import os
from datetime import datetime
from urllib.parse import urlparse

import allure
import requests
from api.ABC.abstract_client import AbstractUserClient

logger = logging.getLogger(__name__)

class HttpClient:
    __metaclass__ = AbstractUserClient

    def __init__(self, base_url: str):

        self.http_session = requests.Session()
        self.http_session.verify = False
        self.http_session.base_url = base_url
        self.http_session.hooks = {
            "response": [self.check_response, self.allure_attach],
        }
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    def get_jira_issue(self):
        JIRA_ISSUE = os.getenv("JIRA_ISSUE")
        logger.info(f"JIRA_ISSUE: {JIRA_ISSUE}")

        if JIRA_ISSUE is not None:
            return JIRA_ISSUE

        SANDBOX = os.getenv("SANDBOX")
        logger.info(f"SANDBOX: {SANDBOX}")

        if SANDBOX is not None:
            POTENCIAL_JIRA_ISSUE = SANDBOX.split(".")[0].upper()

            for JIRA_PROJECT_KEY in ("IMSERVER", "IMOPS", "IMDEVOPS", "IMQA"):
                if POTENCIAL_JIRA_ISSUE.startswith(JIRA_PROJECT_KEY):
                    return POTENCIAL_JIRA_ISSUE

        return None

    def allure_attach(
        self,
        response: requests.Response,
        return_str: bool = False,
        *args,
        **kwargs,
    ):
        """
        Функция для логирования запроса-ответа в Allure отчете

        """
        response.encoding = "UTF-8"

        date_str = str(datetime.now())
        headers_str = "\n".join([f"{k}: {v}" for k, v in response.request.headers.items()])

        text = f"{date_str}\n" f"{response.request.method} {response.request.url}\n" f"{headers_str}\n"

        if response.request.body:
            if isinstance(response.request.body, str):
                text += "\n" f"{response.request.body}"

            elif isinstance(response.request.body, (bytes, bytearray)) and len(response.request.body) < 1000:
                try:
                    text += "\n" f"{response.request.body.decode()}"
                except UnicodeDecodeError:
                    text += "\n" f"Bytes {len(response.request.body)}"

            else:
                text += "\n" f"{type(response.request.body)}"

        text = text.strip()

        headers_str = "\n".join([f"{k}: {v}" for k, v in response.headers.items()])

        text += f"\n\n{response.status_code} {response.reason}\n" f"{headers_str}\n"

        if response.text:
            if isinstance(response.text, str):
                text += "\n" f"{response.text}"
            else:
                text += "\n" f"{response.content.decode()}"

        logger.info(text)

        url_path = urlparse(response.url).path.replace("/", "_")

        allure.attach(
            text,
            name=f"{url_path}.log.txt",
            extension=allure.attachment_type.TEXT,
        )

        if return_str:
            return text
        return None

    def check_response(self, response, *args, **kwargs):
        print(response)

    def request(self, method, url, **kwargs):
        return self.http_session.request(method, url, **kwargs)

    def get(self, url, **kwargs):
        return self.request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        return self.request("POST", url, **kwargs)

    def put(self, url, **kwargs):
        return self.request("PUT", url, **kwargs)

    def patch(self, url, **kwargs):
        return self.request("PATCH", url, **kwargs)

    def delete(self, url, **kwargs):
        return self.request("DELETE", url, **kwargs)
