import pytest
import allure

from support.markers import SANDBOX


@allure.id("544182")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Biz")
@allure.title("Получение политик доступности разделов и приложений")
@SANDBOX
def test_gp_section_availability(stentor, stentor_account, myteam_config):
    """
    Получение политик доступности разделов и приложений
    """
    if "group-policy-enabled" not in myteam_config or not myteam_config["group-policy-enabled"]:
        pytest.skip("Функционала групповых политик выключен на стенде")

    with allure.step("Пробуем получить политикм доступности разделов и приложений"):
        response = stentor.biz_gpSectionAvailability(screenname=stentor_account["email"])

        assert response["status"]["code"] == 20000, "Response error code"
