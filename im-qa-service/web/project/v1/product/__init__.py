from fastapi import APIRouter, Query

from web.project.v1.product.dantic import ProductResponseModel, ProductTypeEnum

from web.project.db import Product, Product_Pydantic

product_router = APIRouter(prefix='/product', tags=["product"])


@product_router.get(
    path='/status',
    name='Получение статуса автотестов по продукту',
    responses={
        200: {
            "description": "Success",
            "model": ProductResponseModel
        }
    }
)
async def status(
        PRODUCT_TYPE: ProductTypeEnum = Query(
            ...,
            description="Тип клиента в автотестах",
            alias="type"
        )
):
    product_model = await Product.filter(
        name=PRODUCT_TYPE.value
    ).first()

    product_dantic = await Product_Pydantic.from_tortoise_orm(product_model)

    return {
        "success": True,
        "product": product_dantic
    }