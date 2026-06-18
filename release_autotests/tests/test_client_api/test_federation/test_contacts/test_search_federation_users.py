import allure
import pytest
from support.markers import SANDBOX
from tests.test_client_api.common import keywords_iterator, user_in_search_result
from tests.test_client_api.test_federation.common import get_user_full_name


@allure.id("1197544")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск федеративных пользователей")
@allure.title(
    "Поиск федеративных пользователей одной инсталяции в другой инсталяции."
    "Поиск по полному/частичному совпадению ФИО/email"
)
@SANDBOX
@pytest.mark.parametrize(
    ("title", "account1_var", "account2_var", "result"),
    [
        (
            "Федеративный пользователь из инсталяции А ищет федеративного пользователя из инсталяции Б",
            "fed_acc_on_host1_host2",
            "fed_acc_on_host2_host1",
            True,
        ),
        (
            "Федеративный пользователь из инсталяции Б ищет федеративного пользователя из инсталяции А",
            "fed_acc_on_host2_host1",
            "fed_acc_on_host1_host2",
            True,
        ),
        (
            "Федеративный пользователь из инсталяции А ищет нефедеративного пользователя из инсталяции Б",
            "fed_acc_on_host1_host2",
            "main_acc_on_host2",
            False,
        ),
        (
            "Нефедеративный пользователь из инсталяции Б ищет федеративного пользователя из инсталяции А",
            "main_acc_on_host2",
            "fed_acc_on_host1_host2",
            False,
        ),
        (
            "Нефедеративный пользователь из инсталяции Б ищет нефедеративного пользователя из инсталяции Б",
            "main_acc_on_host2",
            "opponent_acc_on_host2",
            True,
        ),
    ],
)
@pytest.mark.parametrize("keyword_part_count", [1, 5])
@pytest.mark.parametrize("keyword_type", ["uin", "full_friendly"])
def test_search_federation_users(title, keyword_part_count, keyword_type, request, account1_var, account2_var, result):
    finder = request.getfixturevalue(account1_var)
    target = request.getfixturevalue(account2_var)
    with allure.step(title):
        keyword = target.uin if keyword_type == "uin" else get_user_full_name(target, target.uin)
        found = False
        keywords = keywords_iterator(keyword, keyword_part_count)

        while not found:
            keyword = next(keywords, None)
            if keyword is None:
                break
            with allure.step(f"Ищет по ключевому слову {keyword}"):
                search_result = finder.rapi_search(keyword)
                found = user_in_search_result(search_result, target)
        assert found == result, "Ошибка поиска"
