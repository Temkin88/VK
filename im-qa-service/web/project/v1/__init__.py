from fastapi import APIRouter, Header, HTTPException, Depends

from web.project.v1.account import account_router
from web.project.v1.allure import allure_router
from web.project.v1.image import image_router
from web.project.v1.tasks import tasks_router
from web.project.v1.builds import builds_router
from web.project.v1.product import product_router
from web.project.v1.ws import ws_router
from web.project.v1.night_release import night_release_router


async def get_token_header(
        x_token: str = Header(
            ...,
            example='X-Tests',
            description="Заголовок авторизации",
            alias='X-Token'
        )
):
    if x_token != "X-Tests":
        raise HTTPException(status_code=403, detail="X-Token header invalid")


v1_router = APIRouter(prefix='/v1')
v1_router.include_router(account_router, dependencies=[Depends(get_token_header)])
v1_router.include_router(allure_router, dependencies=[Depends(get_token_header)])
v1_router.include_router(image_router, dependencies=[Depends(get_token_header)])
v1_router.include_router(tasks_router)
v1_router.include_router(builds_router, dependencies=[Depends(get_token_header)])
v1_router.include_router(product_router, dependencies=[Depends(get_token_header)])
v1_router.include_router(night_release_router, dependencies=[Depends(get_token_header)])
v1_router.include_router(ws_router)
