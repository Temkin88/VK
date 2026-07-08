import json
import logging

from urllib.parse import parse_qsl

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

data_router = APIRouter(prefix='/test')

data_default = {
    "message": "No JSON/bad JSON supplied.  "
               "If you used Swagger, "
               "you'll need to use curl on the CLI with the "
               "-d option instead for non-GET methods, "
               "or GET-method data for GET."
}


logger = logging.getLogger(__name__)


def core(request: Request):

    retval = {}

    retval["args"] = request.query_params
    retval["headers"] = request.headers
    retval["source"] = {
        "ip": request.client[0],
        "port": request.client[1]
        }
    retval["url"] = request.url

    return(retval)


@data_router.api_route(
    path="/anything",
    methods=['GET', 'POST', 'PUT', 'DELETE'],
    summary = "Returns anything that is passed into the request.",
    response_class=JSONResponse)
async def delete(request: Request):

    data = data_default
    try:
        data = await request.json()
    except json.decoder.JSONDecodeError as e:
        data = dict(parse_qsl(await request.body()))
        logger.warning(
            f"{__name__}:{request.method}(): "
            f"Caught error deserializing JSON: {e}"
        )

    retval = core(request)
    retval["data"] = data
    retval["verb"] = request.method
    return(retval)
