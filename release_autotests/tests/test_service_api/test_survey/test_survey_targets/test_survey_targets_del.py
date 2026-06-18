import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@pytest.fixture(scope="session")
def add_targets(survey_miniapp, survey_id, opponent_survey_miniapp):
    def _add_targets():
        response = survey_miniapp.internal_survey_targets(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
        targets = response["results"]["targets"]
        responders = [target["responder"] for target in targets]

        if opponent_survey_miniapp.account.uin not in responders:
            response = survey_miniapp.internal_survey_targets_add(
                sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_list=[opponent_survey_miniapp.account.uin]
            )
        return response

    yield _add_targets

    with allure.step("Удаляем списки целей"):
        survey_miniapp.internal_survey_targets_del(
            sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_all=True
        )


@allure.id("511445")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Опросы")
@allure.feature("Опросы про")
@allure.title("Удаление пользователей из списка целей (возможных респондентов)")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
@SANDBOX
@pytest.mark.parametrize("sn_all", [False, True])
def test_internal_survey_targets_del(
    survey_miniapp,
    survey_id,
    survey_start,
    sn_all,
    add_targets,
    opponent_survey_miniapp,
):
    """
    Удаление пользователей из списка целей (возможных респондентов)

    Используемые фикстуры:
    :param survey_miniapp: Клиент для создания опросов
    :param survey_id: ид опроса созданного в фикстуре
    :param survey_start: фикстура предназначенная для старта опроса
    """
    with allure.step("Пробуем удалить пользователей из списка целей"):
        if sn_all:
            add_targets()
            response = survey_miniapp.internal_survey_targets_del(
                sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_all=sn_all
            )
        else:
            add_targets()
            response = survey_miniapp.internal_survey_targets_del(
                sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_list=[opponent_survey_miniapp.account.uin]
            )

        assert response["status"]["code"] == 20000, "Response code error"
