"""
Инициализация бота в JIRA
"""

from jira import JIRA

from utils.config import configuration


imjarvis = JIRA(**configuration["jira"])
