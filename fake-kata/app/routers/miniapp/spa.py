from typing import Optional

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, Response

from fastapi.templating import Jinja2Templates

spa = APIRouter(prefix='/spa')


templates = Jinja2Templates(directory="app/templates")


@spa.api_route(
    "/{template_name}", methods=["GET", "HEAD"], response_class=HTMLResponse)
async def read_item(
        request: Request,
        template_name: str,
        platform: Optional[str] = 'web',
        aimsid: Optional[str] = None
):
    if request.method == "GET":
        return templates.TemplateResponse(
            template_name, {
                "request": request, "platform": platform, "aimsid": aimsid})
    else:
        return Response()
