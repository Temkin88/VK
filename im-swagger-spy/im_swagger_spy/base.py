import json
import logging
import os
import pathlib
from string import Formatter
from typing import Mapping, Optional
from urllib.parse import urlparse

import requests
import yaml

from filelock import FileLock
from playhouse.shortcuts import model_to_dict  # noqa
from requests import PreparedRequest, Response
from requests.adapters import HTTPAdapter

from im_swagger_spy.syncdb import HttpMethodModel, UsedHttpMethodModel

logger = logging.getLogger("im-swagger-spy.base")


class SwaggerBaseSpy:
    decoder = None
    exclude_json = []
    report_info_path: pathlib.Path = pathlib.Path().joinpath(".swagger-info.json")

    def __init__(
        self,
        service_name: str,
        targets: list[str],
        api_prefix: str = "",
        report_path: str = ".",
        exclude_json: Optional[list[str]] = (),
    ):
        self.service = service_name

        self.API_PATH_PREFIX = api_prefix

        self.report_path = report_path

        self.target = targets

        self.swagger_urls = []
        self.base_paths = []

        self.exclude_json = exclude_json

        for target in targets:
            if target.startswith("http://") or target.startswith("https://"):
                self.swagger_urls.append(target)
            else:
                self.base_paths.append(pathlib.Path(target))

    @staticmethod
    def safe_load(file_content: str):
        return yaml.safe_load(file_content)

    @staticmethod
    def add_path(path: str, method_info_json: dict):
        logger.debug(f"path: {path}, method_info_json: {method_info_json}")

        for method in filter(
            lambda x: x.upper()
            in [
                "GET",
                "HEAD",
                "POST",
                "PUT",
                "DELETE",
                "CONNECT",
                "OPTIONS",
                "TRACE",
                "PATCH",
            ],
            method_info_json.keys(),
        ):
            api_path_format_keys = {
                i[1]: ".+" for i in Formatter().parse(path) if i[1] is not None
            }
            api_path = path

            HttpMethodModel.get_or_create(
                method=method.upper(),
                path=api_path,
                regexp=api_path.format(**api_path_format_keys)
                if api_path_format_keys
                else None,
            )

    def handle_response(self, response: requests.Response):
        self.handle_strings(
            method=response.request.method,
            host=urlparse(response.url).netloc,
            path=response.request.path_url.split("?")[0],
        )

    @staticmethod
    def handle_strings(method: str | None, host: str, path: str):
        logger.debug(f"[{method}] {path}")

        model = UsedHttpMethodModel.create(method=method, host=host, path=path)

        logger.debug(f"[{method}] {path} - {model}")

    def register_as_hook(self, session: "requests.Session"):
        # logger.debug("Registering as hook")
        #
        # session.hooks["response"] = self.handle_response
        #
        # logger.debug(session.hooks)

        for scheme in ("http://", "https://"):
            session.mount(scheme, LoggingHTTPAdapter(swagger=self))

    def get_env_backend_url(self):
        if self.service == "SANDBOX":
            url = os.getenv("SANDBOX", "UNKNOWN")
        elif self.service in ["VKTI", "PRE_VKTI"]:
            url = "(u|ub).internal.myteam.mail.ru"
        elif self.service == "PRE_TARM":
            url = "(u|ub).tppr.vmailru.net"
        elif self.service == "TARM":
            url = "(u|ub).armgs.team"
        elif self.service in ["SAAS", "PRE_SAAS"]:
            url = "(u|ub).myteam.vmailru.net"
        else:
            url = "UNKNOWN"

        return url

    def report(self):
        logger.debug("Assembling report in worker")

        if self.report_path is None:
            raise ValueError("Report path is None")

        swagger_info = {
            "service": self.service,
            "report_path": self.report_path,
            "exclude_json": self.exclude_json,
            "backend_url": self.get_env_backend_url(),
        }
        with FileLock(str(self.report_info_path) + ".lock"):
            with self.report_info_path.open(mode="w") as f:
                json.dump(swagger_info, f)

        logger.info(
            "Report saved in database, "
            "ensure to run 'python -m im_swagger_spy build' to get html report"
        )


class LoggingHTTPAdapter(HTTPAdapter):
    def __init__(self, swagger, *args, **kwargs):
        super(LoggingHTTPAdapter, self).__init__(*args, **kwargs)

        self.swagger = swagger

    def send(
        self,
        request: PreparedRequest,
        stream: bool = False,
        timeout: None | float | tuple[float, float] | tuple[float, None] = None,
        verify: bool | str = True,
        cert: None | bytes | str | tuple[bytes | str, bytes | str] = None,
        proxies: Mapping[str, str] | None = None,
    ) -> Response:
        response = super(LoggingHTTPAdapter, self).send(
            request=request,
            stream=stream,
            timeout=timeout,
            verify=verify,
            cert=cert,
            proxies=proxies,
        )

        self.swagger.handle_response(response)

        return response
