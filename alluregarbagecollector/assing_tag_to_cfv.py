import sys

import urllib3
from loguru import logger

import openapi_client as allure

from enums import AllureProjects
from utils.config.config import configuration as cfg


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


logger.remove()
logger.add(sink=sys.stderr, **cfg["loguru.std"])
logger.add(**cfg["loguru.file"])
logger.configure(extra=cfg["loguru.extra"])


configuration = allure.Configuration()
configuration.verify_ssl = False

search_crit = (
    "W3siaWQiOiJhdXRvbWF0ZWQiLCJ2YWx1ZSI6ZmFsc2UsI"
    "mxhYmVsIjoiTm8iLCJ0eXBlIjoiYm9vbGVhbiJ9LHsiaWQiOiJjZnYuLTU"
    "iLCJ2YWx1ZSI6WzYxOTAzXSwibGFiZWwiOlsiQ3JpdFdheV9DaGV"
    "ja0xpc3QiXSwidHlwZSI6ImxvbmdBcnJheSJ9XQ=="
)
search_crit_no_value = (
    "W3siaWQiOiJhdXRvbWF0ZWQiLCJ2YWx1ZSI6ZmFsc2Us"
    "ImxhYmVsIjoiTm8iLCJ0eXBlIjoiYm9vbGVhbiJ9LHsiaWQiO"
    "iJjZnYuLTUiLCJ2YWx1ZSI6WzYxOTAzXSwibGFiZWwi"
    "OlsiQ3JpdFdheV9DaGVja0xpc3QiXSwidHlwZSI6ImxvbmdBc"
    "nJheSJ9LHsiaWQiOiJjZnYuMTU1IiwidmFsdWUiOltdL"
    "CJsYWJlbCI6WyJObyB2YWx1ZSJdLCJ0eXBlIjoibG9uZ0"
    "FycmF5In1d"
)


logger.info("Starting pipeline")


pf = {
    "02": "02. Messaging",
    "03": "03. Contacts",
    "04": "04. Base App",
    "09": "09. Calls",
    "10": "10. Federations",
    "11": "11. Group Policies (WorkSpace)",
    "12": "12. Search",
    "13": "13. Profile",
    "14": "14. Orgstructure",
    "16": "16. Mail",
    "17": "17. Calendar",
    "18": "18. Cloud",
    "19": "19. MiniApps",
    "20": "20. Bot API",
    "21": "21. Notifications",
    "22": "22. Settings",
    "23": "23. Authentication",
    "24": "24. Surveys",
    "25": "25. Tasks",
    "31": "31. Core Web",
    "32": "32. Core Desktop",
    "33": "33. Core iOS",
    "34": "34. Core Android",
    "56": "56. Security",
}


with allure.ApiClient(
    configuration=configuration,
    header_name="Authorization",
    header_value=cfg["allure"]["token"],
) as client:
    test_case_tree_controller = allure.TestCaseTreeControllerApi(
        api_client=client
    )
    test_case_overview_controller = allure.TestCaseOverviewControllerApi(
        api_client=client
    )
    test_case_cfv_controller = allure.TestCaseCustomFieldControllerApi(
        api_client=client
    )

    for project_id in AllureProjects:
        logger.info("-" * 10 + f"Project: {project_id}" + "-" * 10)
        with logger.contextualize(project_id=str(project_id).split(".")[-1]):
            response = test_case_tree_controller.get_leaves1(
                project_id=project_id.value, search=search_crit, size=2500
            )

            for case in response.content:
                with logger.contextualize(test_case_id=case.id):
                    case_info = test_case_overview_controller.get_overview(
                        test_case_id=case.id
                    )

                    tags = [
                        tag.name
                        for tag in case_info.tags
                        if tag.name.startswith("CritWay_")
                    ]
                    cfvs = [
                        cfv.name
                        for cfv in case_info.custom_fields
                        if cfv.custom_field.name == "CritWayValue"
                    ]

                    tags_cfvs = set(tags + cfvs)
                    logger.info(set(tags + cfvs))

                    pfv = []

                    for c in tags_cfvs:
                        value = pf.get(c.split("_")[1].split(".")[0])
                        if value is not None:
                            pfv.append(value)

                    test_case_cfv_controller.set_cfv(
                        test_case_id=case.id,
                        custom_field_value_dto=[
                            allure.CustomFieldValueDto(
                                name="CritWay_CheckList",
                                custom_field=allure.CustomFieldDto(id=-5),
                            ),
                            allure.CustomFieldValueDto(
                                name="blocker",
                                custom_field=allure.CustomFieldDto(id=57),
                            ),
                            allure.CustomFieldValueDto(
                                name="VK Teams (On-Premise)",
                                custom_field=allure.CustomFieldDto(id=2),
                            ),
                            allure.CustomFieldValueDto(
                                name="VK Teams (SaaS)",
                                custom_field=allure.CustomFieldDto(id=2),
                            ),
                            allure.CustomFieldValueDto(
                                name="Среда",
                                custom_field=allure.CustomFieldDto(id=2),
                            ),
                        ]
                        + [
                            allure.CustomFieldValueDto(
                                name=name,
                                custom_field=allure.CustomFieldDto(id=155),
                            )
                            for name in tags_cfvs
                        ]
                        + [
                            allure.CustomFieldValueDto(
                                name=name,
                                custom_field=allure.CustomFieldDto(id=70),
                            )
                            for name in pfv
                        ],
                    )
