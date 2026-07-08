from common.db_schema import db, tables
from common.logger import logger


if __name__ == "__main__":
    logger.info('Creating db schema')
    try:
        db.create_tables(tables, safe=True)
        logger.success('Schema created successfully')
    except Exception as error:
        logger.error(f"Error occured: {error}")
        logger.exception(error)
