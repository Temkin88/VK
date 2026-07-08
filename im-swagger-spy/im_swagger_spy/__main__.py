import logging
from typing import Optional
from typing_extensions import Annotated

import typer

from im_swagger_spy.report import SwaggerReport


cli = typer.Typer()

logging.basicConfig(
    level=logging.INFO,
    format=" ".join(
        [
            "[%(asctime)s]",
            "[%(levelname)s]",
            "[%(name)s]",
            "%(message)s",
            "(%(filename)s:%(lineno)s)",
        ]
    ),
)

logger = logging.getLogger(__name__)


@cli.command()
def check():
    logger.info("Command executed: check")


@cli.command()
def build(
    push_gateway_url: Annotated[
        Optional[str],
        typer.Argument(
            help="URL для отправки метрик в Prometheus PushGateway/Victoria Metrics"
        ),
    ] = None,
):
    """
    :param push_gateway_url: URL для отправки метрик в Prometheus PushGateway/Victoria Metrics
    """
    logger.info("Command executed: build")
    SwaggerReport.build_report(push_gateway_url=push_gateway_url)


@cli.command()
def docs():
    """
    Открыть репозиторий с кодом плагина im-swagger-spy
    """
    logger.info("Command executed: docs")
    typer.launch(url="https://gitlab.corp.mail.ru/imqa/im-swagger-spy")


if __name__ == "__main__":
    cli()
