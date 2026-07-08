from __future__ import annotations
from enum import Enum

from typing import List

from pydantic import BaseModel


class BuildVersionModel(BaseModel):
    major: str
    minor: str
    patch: str
    buildnumber: str


class BuildModel(BaseModel):
    BRANCH_NAME: str
    BUILD_ID: int
    BUILD_URLS: List[str]
    BUILD_PLATFORM: str
    BUILD_TYPE: str
    BUILD_VERSION: BuildVersionModel
    BUILD_TEXT: str
    WITH_TESTING: bool


class BuildPlatformEnum(str, Enum):
    windows = 'windows'
    linux = 'linux'
    macos = 'macos'


class BuildTypeEnum(str, Enum):
    agent = 'agent'
    armgs = 'armgs'
    icq = 'icq'
    myteam = 'myteam'
    myteam_onpremise = 'myteam_onpremise'
