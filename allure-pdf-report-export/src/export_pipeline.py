import time

from loguru import logger

from requests.exceptions import RequestException

from super_mario.base_pipeline import ImmutableContext
from super_mario import BasePipeline, input_pipe, process_pipe, output_pipe

from src.allure import AllureClient, AllureExportStatus

allure = AllureClient()


class ExportPdfPipeline(BasePipeline):

    pipeline = [
        'get_launch_name',
        'request_export',
        'wait_for_ready_status',
        'download_pdf_report'
    ]

    @input_pipe
    @staticmethod
    def get_launch_name(launchId: int) -> ImmutableContext:
        logger.info(f'Getting info about target launch ID {launchId}...')

        result = allure.get_launch_by_id(launchId=launchId)

        logger.success(f'Success! ID {result.id} {result.name}')

        return {
            'launch_id': launchId,
            'launch_name': result.name
        }

    @process_pipe
    @staticmethod
    def request_export(launch_id: int, launch_name: str) -> ImmutableContext:

        logger.info('Requesting launch report in PDF format...')

        result = allure.request_pdf(launchId=launch_id, filename=launch_name)

        logger.success(f'Success! Export ID is {result.id}')

        return {
            'export_id': result.id
        }

    @process_pipe
    @staticmethod
    def wait_for_ready_status(
            export_id: int) -> ImmutableContext:

        logger.info('Checking export status...')

        result = allure.export_status(file_id=export_id)

        logger.info(f'Status is {result.status}, waiting...')

        while result.status == AllureExportStatus.queued:

            time.sleep(5)

            result = allure.export_status(file_id=export_id)

            logger.info(f'Status is {result.status}, waiting...')

        if result.status == AllureExportStatus.failed:

            raise RequestException(f'Export failed: {result.json()}')

        logger.success(f'Success! Status is {result.status}')

        return {
            'export_success': True
        }

    @output_pipe
    @staticmethod
    def download_pdf_report(export_id: int, launch_name: str) -> None:

        logger.info('Trying to download report...')

        with open(f'Report:_{launch_name.replace("/","|").replace(" ", "_")}.pdf', 'wb') as f:
            f.write(
                allure.download_report(file_id=export_id)
            )

        logger.success('Success!')
