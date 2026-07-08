import asyncio
import json

from web.project.logger import logger
from tortoise.exceptions import IntegrityError

from web.project.db import init_db, Account, Product
from web.project.v1.product import ProductTypeEnum


async def init():
    logger.info('Initializing DB...')
    await init_db()
    logger.info('Initializing DB - COMPLETED')
    logger.info('Creating account row in Account table...')
    with open("accounts.json", "rb") as f:
        accounts = json.load(f)
    try:
        await Account.bulk_create([
            Account(**account) for account in accounts
        ])
    except IntegrityError as error:
        logger.warning(error)
    finally:
        logger.info('Creating account row in Account table - COMPLETED')
    logger.info("Creating product row in Product table")
    try:
        await Product.bulk_create([
            Product(
                name=product,
                status=True if product != ProductTypeEnum.armgs else False
            ) for product in ProductTypeEnum
        ])
    except IntegrityError as error:
        logger.warning(error)
    finally:
        logger.info('Creating product row in Product table - COMPLETED')
    quit(0)


if __name__ == '__main__':
    try:
        asyncio.new_event_loop().run_until_complete(init())
        quit(0)
    except Exception as error:
        logger.exception(error)
        quit(0)
