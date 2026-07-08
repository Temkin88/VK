"""
Enum'ы
"""

import base64
import json
from datetime import datetime, timedelta
from enum import Enum

from utils.config import configuration as cfg


class AllureProjects(Enum):
    """
    Список проектов в Allure TestOps
    """

    IMDESKTOP = 6
    IMSERVER = 7
    IMWEB = 8
    IMIOS = 9
    IMA = 10
    IMQA = 13
    IMVOIP = 14
    # IMDAI = 28  noqa: ERA001


class AllureCaseStatus(Enum):
    """
    Список статусов тест кейсов в Allure TestOps
    """

    ACTIVE = -3
    ACTUAL = 36
    DRAFT = -1
    OUTDATED = -4
    TEST = 00000


class ProductFunctionality(Enum):
    """
    Список возможных продуктовых функциональностей в Allure TestOps
    """

    MESSAGING = "02. Messaging"
    CONTACTS = "03. Contacts"
    BASE_APP = "04. Base App"
    CALLS = "09. Calls"
    FEDERATIONS = "10. Federations"
    GROUP_POLICIES = "11. Group Policies"
    SEARCH = "12. Search"
    PROFILE = "13. Profile"
    ORGSTRUCTURE = "14. Orgstructure"
    MAIL = "16. Mail"
    CALENDAR = "17. Calendar"
    CLOUD = "18. Cloud"
    MINIAPPS = "19. MiniApps"
    BOT_API = "20. BotAPI"
    NOTIFICATIONS = "21. Notifications"
    SETTINGS = "22. Settings"
    AUTHENTICATION = "23. Authentication"
    SURVEYS = "24. Surveys"
    TASKS = "25. Tasks"
    DIGITAL_ASSISTANT = "26. Digital Assistant"
    CORE_DESIGN = "27. Core Design"
    DESIGN_SYSTEM = "28. Design System"
    CORE_BACKEND = "29. Core Backend"
    CORE_DEVOPS = "30. Core DevOps"
    CORE_WEB = "31. Core Web"
    CORE_DESKTOP = "32. Core Desktop"
    CORE_IOS = "33. Core iOS"
    CORE_ANDROID = "34. Core Android"
    CORE_QA = "35. Core QA"
    SUPPORT = "37. Support"
    RELEASE_AND_INFRA = "38. Release and Infrastructure"
    KUBERNETES = "39. Kubernetes"
    PLATFORM_INFRASTRUCTURE = "40. Platform Infrastructure"
    DEPLOYER_WORKSPACE = "41. Deployer (WorkSpace)"
    MAIL_WORKSPACE = "42. Mail (WorkSpace)"
    CALENDAR_WORKSPACE = "43. Calendar (WorkSpace)"
    ADMIN_PANEL_WORKSPACE = "44. Admin Panel (WorkSpace)"
    CLOUD_WORKSPACE = "45. Cloud (WorkSpace)"
    WORKMAIL_DESKTOP_WORKSPACE = "46. Workmail Desktop (WorkSpace)"
    RATES_AND_FUNNEL_WORKSPACE = "47. Rates and Funnel (WorkSpace)"
    BACK_OFFICE_WORKSPACE = "48. Back Office (Workspace)"
    SRE_CORE = "49. SRE Core"
    SRE_VKT = "50. SRE VKT"
    SRE_WS = "51. SRE WS"
    SRE_SKTI = "52. SRE СКЗИ"


# Mapping продуктовых функциональностей в Allure TestOps к ID в JIRA
PD_RESOURCES = {
    "02. Messaging": "37112",
    "03. Contacts": "37113",
    "04. Base App": "39823",
    "09. Calls": "37119",
    "10. Federations": "37120",
    "11. Group Policies": "37121",
    "12. Search": "37122",
    "13. Profile": "37123",
    "14. Orgstructure": "37124",
    "16. Mail": "37126",
    "17. Calendar": "37132",
    "18. Cloud": "37133",
    "19. MiniApps": "37134",
    "20. BotAPI": "37135",
    "21. Notifications": "37136",
    "22. Settings": "37137",
    "23. Authentication": "37138",
    "24. Surveys": "37139",
    "25. Tasks": "37140",
    "26. Digital Assistant": "37141",
    "27. Core Design": "37142",
    "28. Design System": "37143",
    "29. Core Backend": "37144",
    "30. Core DevOps": "37145",
    "31. Core Web": "37146",
    "32. Core Desktop": "37147",
    "33. Core iOS": "37148",
    "34. Core Android": "37149",
    "35. Core QA": "37150",
    "36. Autotests": "37151",
    "37. Support": "39711",
    "38. Release and Infrastructure": "43590",
    "39. Kubernetes": "43591",
    "40. Platform Infrastructure": "43592",
    "41. Deployer (WorkSpace)": "44499",
    "42. Mail (WorkSpace)": "44500",
    "43. Calendar (WorkSpace)": "44501",
    "44. Admin Panel (WorkSpace)": "44502",
    "45. Cloud (WorkSpace)": "44512",
    "46. Workmail Desktop (WorkSpace)": "44647",
    "47. Rates and Funnel (WorkSpace)": "44648",
    "48. Back Office (WorkSpace)": "44649",
    "49. SRE Core": "62594",
    "50. SRE VKT": "62595",
    "51. SRE WS": "62596",
    "52. SRE СКЗИ": "62597",
}
ALTER_PD_RESOURCES = {
    "37112": "02. Messaging",
    "37113": "03. Contacts",
    "37119": "09. Calls",
    "37120": "10. Federations",
    "37121": "11. Group Policies",
    "37122": "12. Search",
    "37123": "13. Profile",
    "37124": "14. Orgstructure",
    "37126": "16. Mail",
    "37132": "17. Calendar",
    "37133": "18. Cloud",
    "37134": "19. MiniApps",
    "37135": "20. BotAPI",
    "37136": "21. Notifications",
    "37137": "22. Settings",
    "37138": "23. Authentication",
    "37139": "24. Surveys",
    "37140": "25. Tasks",
    "37141": "26. Digital Assistant",
    "37142": "27. Core Design",
    "37143": "28. Design System",
    "37144": "29. Core Backend",
    "37145": "30. Core DevOps",
    "37146": "31. Core Web",
    "37147": "32. Core Desktop",
    "37148": "33. Core iOS",
    "37149": "34. Core Android",
    "37150": "35. Core QA",
    "37151": "36. Autotests",
    "39711": "37. Support",
    "39823": "04. Base App",
    "43590": "38. Release and Infrastructure",
    "43591": "39. Kubernetes",
    "43592": "40. Platform Infrastructure",
    "44499": "41. Deployer (WorkSpace)",
    "44500": "42. Mail (WorkSpace)",
    "44501": "43. Calendar (WorkSpace)",
    "44502": "44. Admin Panel (WorkSpace)",
    "44512": "45. Cloud (WorkSpace)",
    "44647": "46. Workmail Desktop (WorkSpace)",
    "44648": "47. Rates and Funnel (WorkSpace)",
    "44649": "48. Back Office (WorkSpace)",
    "62594": "49. SRE Core",
    "62595": "50. SRE VKT",
    "62596": "51. SRE WS",
    "62597": "52. SRE СКЗИ",
}


current_date = datetime.now()
year_ago_date = current_date - timedelta(days=365)


# Для поиска кейсов в статусе OUTDATED
outdated_search_dict = [{"id": "status", "type": "longArray", "value": [-4]}]
outdated_search_str = base64.b64encode(
    json.dumps(outdated_search_dict).encode()
).decode()


# Для поиска кейсов в статусе ACTUAL и ACTIVE
active_search_dict = [
    {"id": "status", "type": "longArray", "value": [36, -3]},
    {"id": "automated", "type": "boolean", "value": False},
]
active_search_str = base64.b64encode(
    json.dumps(active_search_dict).encode()
).decode()


# Все ручные тест-кейсы
all_manual_search_dict = [
    {"id": "automated", "type": "boolean", "value": False}
]
all_manual_search_str = base64.b64encode(
    json.dumps(all_manual_search_dict).encode()
).decode()


# Все кейсы в статусах "NEED REVIEW" и "Draft"
created_before = int(
    (
        datetime.now()
        - timedelta(seconds=cfg["allure.extra"]["forgotten_after_period"])
    ).timestamp()
    * 1000
)
need_review_and_draft_search_dict = [
    {"id": "status", "type": "longArray", "value": [35, -1]},
    {"id": "createdAfter", "type": "long", "value": 1704056400000},
    {"id": "createdBefore", "type": "long", "value": created_before},
]
need_review_and_draft_search_str = base64.b64encode(
    json.dumps(need_review_and_draft_search_dict).encode()
).decode()
