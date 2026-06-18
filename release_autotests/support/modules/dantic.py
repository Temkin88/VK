from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Buddy(BaseModel):
    aimId: str
    autoAddition: Optional[str]
    displayId: str
    friendly: Optional[str]
    lastseen: Optional[str]
    userType: str
    capabilities: Optional[List[str]]
    bot: Optional[bool]
    nick: Optional[str]
    bigIconId: Optional[str]
    iconId: Optional[str]
    largeIconId: Optional[str]


class Group(BaseModel):
    buddies: List[Buddy]
    id: int
    name: str


class BuddyListEventData(BaseModel):
    groups: List[Group]


class BuddyListEventModel(BaseModel):
    eventData: BuddyListEventData
    seqNum: int
    type: str


class MyInfoEventData(BaseModel):
    aimId: str
    capabilities: List[str]
    displayId: str
    friendly: str
    globalFlags: int
    userAgreement: Optional[List[str]]
    userType: str


class MyInfoModel(BaseModel):
    eventData: MyInfoEventData
    seqNum: int
    type: str


class Status(BaseModel):
    code: int


class Deadline(BaseModel):
    type: str
    predefined: str


class Filter(BaseModel):
    id: str
    name: str
    order: int
    statuses: List[str]
    assignees: Optional[List[str]] = None
    creators: Optional[List[str]] = None
    deadline: Optional[Deadline] = None


class Person(BaseModel):
    sn: str
    friendly: str


class Results(BaseModel):
    filters: List[Filter]
    persons: List[Person]


class ResponseTasksFilters(BaseModel):
    status: Status
    results: Results
