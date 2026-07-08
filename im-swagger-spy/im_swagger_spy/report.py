import json
import re
from typing import Optional, TypedDict

import pathlib
import logging

import peewee
import requests
from jinja2 import Environment, FileSystemLoader, select_autoescape
from playhouse.shortcuts import model_to_dict  # noqa
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

from im_swagger_spy.syncdb import HttpMethodModel, UsedHttpMethodModel

logger = logging.getLogger(__name__)


class SwaggerInfoTypedDict(TypedDict):
    service: str
    report_path: str
    exclude_json: list[str]
    backend_url: str


class SwaggerReport:
    exclude_json: list[str] = []
    report_info_path: pathlib.Path = pathlib.Path().joinpath(".swagger-info.json")

    @classmethod
    def build_report(cls, push_gateway_url: Optional[str] = None):
        logger.info("Trying to build report from .swagger-spy-db.sqlite")

        logger.info("Searching for .swagger-info.json")

        with cls.report_info_path.open(mode="r") as f:
            swagger_info: SwaggerInfoTypedDict = json.load(f)

        service = swagger_info["service"]
        report_folder = swagger_info["report_path"]
        exclude_json_paths = swagger_info["exclude_json"]
        backend_url = swagger_info["backend_url"]

        if exclude_json_paths and isinstance(exclude_json_paths, list):
            for path in exclude_json_paths:
                with pathlib.Path(path).open(mode="r") as f:
                    cls.exclude_json += json.load(f)
        else:
            cls.exclude_json = []

        cls.render(service, report_folder, backend_url, push_gateway_url)

    @classmethod
    def render(
        cls,
        service,
        report_path,
        backend_url: str,
        push_gateway_url: Optional[str] = None,
    ):
        USED_METHODS_LIST, SKIPPED_METHODS_LIST = cls.report_models()

        TOTAL_METHODS_COUNT = len(USED_METHODS_LIST) + len(SKIPPED_METHODS_LIST)

        env = Environment(
            loader=FileSystemLoader(pathlib.Path(__file__).parent.absolute().__str__()),
            autoescape=select_autoescape(["html"]),
        )

        template = env.get_template("template.html")

        rendered_page = template.render(
            service=service,
            used_methods=list(USED_METHODS_LIST),
            used_methods_count=len(USED_METHODS_LIST),
            skipped_methods=SKIPPED_METHODS_LIST,
            skipped_methods_count=len(SKIPPED_METHODS_LIST),
            total_methods_count=TOTAL_METHODS_COUNT,
            exclude_method_count=len(cls.exclude_json),
            exclude_methods=cls.exclude_json,
        )

        registry = CollectorRegistry()

        gauge = Gauge(
            "autotest", "Процент покрытия", ["env", "backend_url"], registry=registry
        )
        gauge.labels(env=service, backend_url=backend_url).set(
            int(len(USED_METHODS_LIST) * 100 / TOTAL_METHODS_COUNT)
        )

        def handler(
            url: str,
            method: str,
            timeout: Optional[float],
            headers: list[tuple[str, str] | dict[str, str]],
            data: bytes,
        ):
            headers = {k: v for k, v in headers}

            def request():
                logger.info(
                    f"Pushing info for: service={service}, backend_url={backend_url}"
                )

                response = requests.request(
                    url=url,
                    method=method,
                    timeout=timeout,
                    headers=headers,
                    data=data,
                    verify=False,
                )

                logger.info(
                    f"Response from push gateway: {response.status_code} {response.reason}"
                )

                return response

            return request

        if push_gateway_url is not None and isinstance(push_gateway_url, str):
            push_to_gateway(
                gateway=push_gateway_url,
                # "https://victoria-dev.imdevops.ru/prometheus/api/v1/import/prometheus"
                job="autotest",
                registry=registry,
                handler=handler,
            )

        report_folder_object = pathlib.Path(report_path)

        report_folder_object.mkdir(parents=True, exist_ok=True)

        report_path_object = report_folder_object.joinpath(f"spy-report-{service}.html")

        report_path_object.write_text(rendered_page)

        logger.info(f"Report is saved to {report_path_object.absolute()}")

    @classmethod
    def report_models(cls):
        USED_METHODS_MODELS_LIST = []
        SKIPPED_METHODS_MODELS_LIST = []

        for method in HttpMethodModel.select().where(
            HttpMethodModel.path.not_in(cls.exclude_json)
        ):
            query = (
                UsedHttpMethodModel.select(
                    UsedHttpMethodModel.method,
                    UsedHttpMethodModel.host,
                    UsedHttpMethodModel.path,
                    peewee.fn.COUNT("*").alias("count"),
                )
                .where(
                    UsedHttpMethodModel.method == method.method,
                )
                .group_by(UsedHttpMethodModel.method, UsedHttpMethodModel.path)
            )

            logger.debug(f"Grouped stats count: {query.count()}")

            for used_method in filter(lambda x: x.count, query):
                if method.path in used_method.path or (
                    method.regexp is not None
                    and re.compile(method.regexp).findall(used_method.path)
                ):
                    method_dict = model_to_dict(method)
                    method_dict["count"] = used_method.count
                    method_dict["host"] = used_method.host

                    USED_METHODS_MODELS_LIST.append(method_dict)
                    break

            else:
                SKIPPED_METHODS_MODELS_LIST.append(model_to_dict(method))

        logger.debug(f"USED_METHODS_MODELS_LIST: {USED_METHODS_MODELS_LIST}")
        logger.debug(f"SKIPPED_METHODS_MODELS_LIST: {SKIPPED_METHODS_MODELS_LIST}")

        return USED_METHODS_MODELS_LIST, SKIPPED_METHODS_MODELS_LIST
