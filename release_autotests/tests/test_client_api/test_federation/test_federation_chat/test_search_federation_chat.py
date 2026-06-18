import allure
import pytest

from support.markers import SANDBOX
from tests.test_client_api.test_federation.common import find_chat_by_some_criterion


@allure.id("1242709")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск чатов")
@allure.title("Поиск чатов в пределах федерации")
@SANDBOX
@pytest.mark.parametrize(
    "chat_type",
    [
        ("group"),
        ("channel"),
    ],
)
@pytest.mark.parametrize(
    (
        "finder",
        "target",
        "isFederation",
        "result",
    ),
    [
        ("fed_acc_on_host1_host2", "GA2", True, True),
        ("fed_acc_on_host1_host2", "GA4", True, False),
        ("fed_acc_on_host2_host1", "GA2", True, True),
        ("fed_acc_on_host2_host1", "GA4", True, False),
        ("fed_acc_on_host1_host2", "GA1", False, True),
        ("fed_acc_on_host1_host2", "GA3", True, False),
        ("fed_acc_on_host2_host1", "GA1", False, False),
        ("fed_acc_on_host2_host1", "GA3", False, False),
        ("main_acc_on_host1", "GA2", True, False),
        ("main_acc_on_host1", "GA4", True, False),
        ("main_acc_on_host1", "GA1", False, True),
        ("main_acc_on_host1", "GA3", False, False),
    ],
)
def test_search_federation_chat(chat_type, finder, target, result, request, isFederation):
    finder = request.getfixturevalue(finder)
    with allure.step("Создаем чат для поиска"):
        chat_name, _, _ = request.getfixturevalue(chat_type + "_" + target)

    with allure.step("Пользователь ищет чат"):
        assert (
            find_chat_by_some_criterion(
                finder,
                chat_name,
                {"isFederation": isFederation},
            )
            is not None
        ) == result, "Неверный результат поиска"
