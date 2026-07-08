import functools
import os

from enum import Enum
from typing import Union, Optional, List
from datetime import datetime

import requests

from loguru import logger
from pydantic import BaseModel, HttpUrl, EmailStr


def log(func):
    @functools.wraps(func)
    def logging(*args, **kwargs):
        try:
            logger.debug(f'{func.__name__}() -> args: {args}, kwargs: {kwargs}')
            result = func(*args, **kwargs)
            if not func.__name__.startswith('download'):
                logger.debug(f'{func.__name__}() <- {result}')
            else:
                logger.debug(f'{func.__name__}() <- Length: {len(result)}')
            return result
        except Exception as e:
            logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")
            raise e
    return logging

class AllureExportStatus(str, Enum):
    queued: str = 'queued'
    failed: str = 'failed'
    ready: str = 'ready'


class AllureExportType(str, Enum):
    launch_pdf = 'LAUNCH_PDF'
    testcase_pdf = 'TEST_CASE_PDF'
    testcase_csv = 'TEST_CASE_CSV'
    test_result_csv = 'TEST_RESULT_CSV'


class AllureExportResponse(BaseModel):
    id: int
    projectId: int
    type: AllureExportType
    status: AllureExportStatus
    storageKey: str
    name: str
    shared: bool
    createdDate: datetime
    lastModifiedDate: datetime
    createdBy: Union[EmailStr, str]
    lastModifiedBy: Union[EmailStr, str]


class AllureAttrModel(BaseModel):
    id: Optional[int] = None
    name: str
    type: Optional[str] = None
    url: Optional[HttpUrl] = None


class AllureIssueModel(AllureAttrModel):
    integrationId: int
    summary: Optional[str] = None
    status: Optional[str] = None
    closed: bool


class AllureLaunchResponse(BaseModel):
    id: Optional[int] = None
    name: str
    closed: bool
    external: bool
    autoclose: bool
    projectId: int
    tags: List[AllureAttrModel]
    links: List[AllureAttrModel]
    issues: List[AllureIssueModel]
    createdDate: datetime
    lastModifiedDate: datetime
    createdBy: Union[EmailStr, str]
    lastModifiedBy: Union[EmailStr, str]


class AllureClient(BaseModel):
    token: str = os.getenv('ALLURE_TOKEN', 'ALLURE_TOKEN_DEFAULT')
    base_url: HttpUrl = os.getenv('ALLURE_BASE_URL', 'ALLURE_BASE_URL_DEFAULT')

    def __str__(self):
        return f'AllureClient(url={self.base_url}, token={self.token})'

    def __repr__(self):
        return f'AllureClient(url={self.base_url}, token={self.token})'

    @log
    def get_launch_by_id(self, launchId: int) -> AllureLaunchResponse:
        return AllureLaunchResponse.parse_obj(
            requests.get(
                url=f'{self.base_url}/launch/{launchId}',
                headers={
                    'Authorization': f'Api-Token {self.token}'
                }
            ).json()
        )

    @log
    def request_pdf(self, launchId: int, filename: str) -> AllureExportResponse:
        return AllureExportResponse.parse_obj(
            requests.post(
                url=f'{self.base_url}/export/launch/pdf',
                headers={
                    'Authorization': f'Api-Token {self.token}'
                },
                json={
                    "launchId": launchId,
                    "name": filename,
                    "skipScenario": True,
                    "withPageNumbers": True,
                    "structure": [
                        "header",
                        "title",
                        "statistic",
                        "summary",
                        "trByStatuses"
                    ]
                }
            ).json()
        )

    @log
    def export_status(self, file_id: int) -> AllureExportResponse:
        return AllureExportResponse.parse_obj(
            requests.get(
                url=f'{self.base_url}/export/{file_id}',
                headers={
                    'Authorization': f'Api-Token {self.token}'
                }
            ).json()
        )

    @log
    def download_report(self, file_id: int) -> bytes:
        return requests.get(
            url=f'{self.base_url}/export/download/{file_id}',
            headers={
                'Authorization': f'Api-Token {self.token}'
            }
        ).content
