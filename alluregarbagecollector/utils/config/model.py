from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class Oauth(BaseModel):
    access_token: str
    access_token_secret: str
    consumer_key: str
    key_cert: str


class Jira(BaseModel):
    oauth: Oauth
    server: str


class Priority(BaseModel):
    name: str


class JiraSettings(BaseModel):
    project: str
    issuetype: str
    priority: Priority


class TestCases(BaseModel):
    customfield_15500: str
    labels: List[str]


class Defects(BaseModel):
    customfield_15500: str
    labels: List[str]


class JiraSettingsExtra(BaseModel):
    test_cases: TestCases
    defects: Defects


class LoguruStd(BaseModel):
    level: str
    format: str
    colorize: bool


class LoguruFile(BaseModel):
    level: str
    sink: str
    format: str
    rotation: str
    retention: str
    compression: str
    colorize: bool
    backtrace: bool
    diagnose: bool
    delay: bool
    watch: bool


class LoguruExtra(BaseModel):
    project_id: str
    test_case_id: str


class Allure(BaseModel):
    token: str


class AllureTemplateLinks(BaseModel):
    defect: str
    test_case: str


class AllureExtra(BaseModel):
    page_size: int
    forgotten_after_period: int
    ignore_statuses: List[str]


class Notify(BaseModel):
    chat_id: str


class VkTeamBot(BaseModel):
    api_url_base: str
    token: str
    is_myteam: bool
    poll_time_s: int
    timeout_s: int
    version: str
    name: str


class ConfigModel(BaseModel):
    jira: Jira
    jira_settings: JiraSettings = Field(..., alias="jira.settings")
    jira_settings_extra: JiraSettingsExtra = Field(
        ..., alias="jira.settings.extra"
    )
    loguru_std: LoguruStd = Field(..., alias="loguru.std")
    loguru_file: LoguruFile = Field(..., alias="loguru.file")
    loguru_extra: LoguruExtra = Field(..., alias="loguru.extra")
    allure: Allure
    allure_template_links: AllureTemplateLinks = Field(
        ..., alias="allure.template.links"
    )
    allure_extra: AllureExtra = Field(..., alias="allure.extra")
    notify: Notify
    vk_team_bot: VkTeamBot
