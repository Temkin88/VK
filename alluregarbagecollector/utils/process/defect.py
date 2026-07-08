from datetime import datetime

import openapi_client as allure
from loguru import logger

from enums import AllureProjects
from imjarvis import imjarvis

from utils.config import configuration as cfg
from utils.attrs.defect import check_defect_name_for_issue_key
from utils.load.issue import create_issue_for_defect


def set_defect_attrs_from_issue(
    defect_controller: allure.DefectControllerApi,
    defect_overview: allure.DefectOverviewDto,
    issue_key: str,
):
    """
    Выставляем название и описание дефекта на основе задачи в Jira
    :param defect_controller:
    :param defect_overview:
    :param issue_key:
    :return:
    """
    logger.info(f"Setting attrs from issue {issue_key}")

    issue = imjarvis.issue(issue_key)

    defect_controller.patch35(
        id=defect_overview.id,
        defect_patch_dto=allure.DefectPatchDto(
            name=issue.fields.summary, description=issue.fields.description
        ),
    )


def has_automation_rules(
    defect_controller: allure.DefectControllerApi,
    defect: allure.DefectOverviewDto,
) -> bool:
    """
    Проверка что к дефекту созданы automation rules
    :param defect_controller: API Controller
    :param defect: дефект
    :return: True - если их больше нуля
    """
    return defect_controller.get_matchers(id=defect.id).total_elements > 0


def process_opened_defects(
    defect_controller: allure.DefectControllerApi,
    defect: allure.DefectCountRowDto,
    project_id: AllureProjects,
):
    """
    Проверка что к дефекту прикреплена задача или указана в названии
    :param defect_controller: API Controller
    :param defect: Ифно о дефекте
    :param project_id: ID проекта
    :return:
    """
    with logger.contextualize(defect_id=defect.id):
        defect_overview = defect_controller.find_by_id3(id=defect.id)

        if defect_overview.issue is not None:
            logger.success(
                f"Defect already linked to issue "
                f"{defect_overview.issue.name}"
            )
            set_defect_attrs_from_issue(
                defect_controller=defect_controller,
                defect_overview=defect_overview,
                issue_key=defect_overview.issue.name,
            )
            return

        possible_issue_key = check_defect_name_for_issue_key(
            defect_overview.name
        )

        if possible_issue_key is not None:
            defect_controller.link_issue(
                id=defect_overview.id,
                defect_issue_link_dto=allure.DefectIssueLinkDto(
                    integration_id=2, name=possible_issue_key
                ),
            )

            logger.success(
                f"Defect succesfully linked to issue {possible_issue_key}"
            )

            set_defect_attrs_from_issue(
                defect_controller=defect_controller,
                defect_overview=defect_overview,
                issue_key=possible_issue_key,
            )
            return

        project_name = str(project_id).split(".")[-1]
        current_date = datetime.now()
        week_number = current_date.isocalendar().week

        defect_link = cfg["allure.template.links"]["defect"].format(
            project_id=project_id.value, defect_id=defect_overview.id
        )

        issue_key = create_issue_for_defect(
            title=f"[{project_name}][{defect_overview.id}] "
            f"Актуализация дефекта (Неделя: {week_number})",
            description=f"{defect_link} - Отсутствует прилинкованный баг.",
            product_functionality="36. Autotests"
            if has_automation_rules(
                defect_controller=defect_controller, defect=defect_overview
            )
            else "35. Core QA",
        )

        defect_controller.link_issue(
            id=defect_overview.id,
            defect_issue_link_dto=allure.DefectIssueLinkDto(
                integration_id=2, name=issue_key
            ),
        )

        set_defect_attrs_from_issue(
            defect_controller=defect_controller,
            defect_overview=defect_overview,
            issue_key=issue_key,
        )


def _iter_defects_by_project(
    defect_controller: allure.DefectControllerApi,
    project_id: AllureProjects,
    page_size: int,
    stage_name: str,
):
    """
    Поиск всех открытых дефектов по проекту
    :param defect_controller: API Controller
    :param project_id: ID проекта
    :param page_size: размер страницы с дефектами
    :param stage_name: название этапа (для логгера)
    :return:
    """
    i = 1

    logger.info(f"[{stage_name}] Requesting first page of tree")

    defects = defect_controller.find_all_by_project_id(
        project_id=project_id.value, size=page_size, page=i, status=["Open"]
    )

    logger.info(
        f"[{stage_name}] "
        f"Total pages count - {defects.total_pages}, "
        f"page size - {page_size}"
    )

    while True:
        i += 1

        for defect in defects.content:
            yield defect

        if defects.last:
            break

        logger.info(
            f"[{stage_name}] "
            f"Requesting {i}/{defects.total_pages} page of tree"
        )

        defects = defect_controller.find_all_by_project_id(
            project_id=project_id.value, size=page_size, page=i, status=["Open"]
        )


def process_defects(
    defect_controller: allure.DefectControllerApi,
    project_id: AllureProjects,
    stage_name: str,
):
    """
    Проверка дефекта на наличие прикрепленной задачи в Jira
    :param defect_controller: API Controller
    :param project_id: ID проекта
    :param stage_name: Название этапа (для логгера)
    :return:
    """
    with logger.contextualize(project_id=str(project_id).split(".")[-1]):
        for defect in _iter_defects_by_project(
            defect_controller=defect_controller,
            project_id=project_id,
            page_size=100,
            stage_name=stage_name,
        ):
            with logger.catch():
                process_opened_defects(
                    defect_controller=defect_controller,
                    defect=defect,
                    project_id=project_id,
                )
