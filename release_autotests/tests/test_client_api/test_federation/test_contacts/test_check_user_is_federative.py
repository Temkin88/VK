import allure
import pytest
from support.markers import SANDBOX


@allure.id("1535558")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Группы")
@allure.feature("Признак федеративности у пользователя")
@allure.title("Наличие признака федеративности у федеративного пользователя")
@SANDBOX
@pytest.mark.parametrize(
    ("checker", "acc_for_check", "check_result"),
    [
        ("fed_acc_on_host1_host2", "fed_acc_on_host2_host1", True),
        ("fed_acc_on_host1_host2", "main_acc_on_host1", False),
        ("main_acc_on_host1", "opponent_acc_on_host1", False),
        ("main_acc_on_host1", "fed_acc_on_host1_host2", True),
        ("fed_acc_on_host2_host1", "fed_acc_on_host1_host2", True),
        ("fed_acc_on_host2_host1", "main_acc_on_host2", False),
        ("main_acc_on_host2", "opponent_acc_on_host2", False),
        ("main_acc_on_host2", "fed_acc_on_host2_host1", True),
    ],
)
def test_check_user_is_federative(request, checker, acc_for_check, check_result):
    checker = request.getfixturevalue(checker)
    acc_for_check = request.getfixturevalue(acc_for_check)
    with allure.step("Проверяем наличие валидного признака федеративности у пользователя"):
        response = checker.rapi_search(acc_for_check.uin)
        assert response["status"]["code"] == 20000, "Ошибка при поиске пользователя"
        assert response["results"]["data"], "Пустой результат поиска"
        for data in response["results"]["data"]:
            if "anketa" in data:
                if "isFederation" in data["anketa"]:
                    assert data["anketa"]["isFederation"] == check_result, "Неверное значение признака федеративности"
                elif "isFederation" not in data["anketa"] and not check_result:
                    assert True, "Неверное значение признака федеративности"
        response = checker.rapi_getUserInfo(sn=acc_for_check.uin)
        assert response["status"]["code"] == 20000, "Ошибка при попытке получить User_info"
        if "federation" in response["results"]:
            assert response["results"]["isFederation"] == check_result, "Неверный признак федеративности пользователя"
        elif not check_result:
            assert True, "Неверный признак федеративности пользователя"
