import pytest

from im_swagger_spy import file_spy, http_spy
from im_swagger_spy.syncdb import HttpMethodModel


@pytest.mark.parametrize(
    "swagger_path",
    [
        "./openapi_example/yaml/refs/api.yaml",
        "./openapi_example/yaml/strict/api.yaml",
        "./openapi_example/json/refs/api.json",
        "./openapi_example/json/strict/api.json",
    ],
)
def test_load_from_file(swagger_path, clear_db):
    spy = file_spy.SwaggerFileSpy(
        service_name="vk_teams.botapi",
        targets=[swagger_path],
        api_prefix="/api/v101",
        report_path=".",
    )

    spy.load_schema()

    assert HttpMethodModel.select().count()


@pytest.mark.parametrize(
    "swagger_url",
    [
        "https://teams.vk.com/botapi/api.yaml?4624464",
        "https://petstore.swagger.io/v2/swagger.json",
        # 'http://100.99.4.29:8000/client/v101/u/api.yaml'
    ],
)
def test_load_from_url(swagger_url, clear_db):
    spy = http_spy.SwaggerHttpSpy(
        service_name="vk_teams.botapi",
        targets=[swagger_url],
        api_prefix="/bot/v1",
        report_path=".",
    )

    spy.load_schema()

    assert HttpMethodModel.select().count()
