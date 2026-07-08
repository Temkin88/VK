import os
# import multiprocessing

from loguru import logger

from src.export_pipeline import ExportPdfPipeline

ALLURE_LAUNCH_IDS = os.getenv('ALLURE_LAUNCH_IDS')

if ALLURE_LAUNCH_IDS is None:
    logger.warning(f'Invalid env.ALLURE_LAUNCH_IDS value: {ALLURE_LAUNCH_IDS}')

launchIds = [
    int(x.strip()) for x in ALLURE_LAUNCH_IDS.split(',')
]


def process_logger(launchId: int):
    with logger.catch():
        logger.info(f'Starting mario-pipeline for Launch ID {launchId}')
        ExportPdfPipeline().run(launchId=launchId)
        logger.success(f'Done mario-pipeline for Launch ID {launchId}')


# with multiprocessing.Pool(len(launchIds)) as p:
#     p.map(process_logger, launchIds)

for launchId in launchIds:
    process_logger(launchId)
