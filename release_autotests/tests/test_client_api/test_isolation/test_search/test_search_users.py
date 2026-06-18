import allure
import pytest
from support.markers import SAAS, PRE_SAAS, ISOLATION
from tests.test_client_api.common import keywords_iterator, user_in_search_result


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск пользователей внутри изоляции")
@allure.title("Поиск пользователей внутри изоляции")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize(
    ("title", "finder_fixture_name", "target_fixture_name", "result"),
    [
        (
            "Пользователь в тенанте ищет другого пользователя в тенанте",
            "first_auth_account_in_tenant",
            "second_auth_account_in_tenant",
            True,
        ),
        (
            "Пользователь не в тенанте ищет пользователя в тенанте",
            "first_auth_account_in_tenant",
            "first_auth_account_not_in_tenant",
            False,
        ),
        (
            "Пользователь в тенанте ищет пользователя не в тенанте",
            "first_auth_account_not_in_tenant",
            "first_auth_account_in_tenant",
            False,
        ),
        (
            "Пользователь не в тенанте ищет пользователя не в тенанте в своем домене",
            "first_auth_account_not_in_tenant",
            "second_auth_account_not_in_tenant",
            True,
        ),
    ],
)
@pytest.mark.parametrize("keyword_part_count", [1, 5])
@pytest.mark.parametrize("keyword_type", ["uin", "full_friendly"])
def test_search_user_isolation(
    request,
    title,
    finder_fixture_name,
    target_fixture_name,
    result,
    keyword_type,
    keyword_part_count,
):
    """
    Проверяем поиск пользователей
    """
    finder = request.getfixturevalue(finder_fixture_name)
    target = request.getfixturevalue(target_fixture_name)
    with allure.step(title):
        if keyword_type == "uin":
            keyword = target.uin
        else:
            user_info = target.rapi_getUserInfo(sn=target.uin)
            assert user_info["status"]["code"] == 20000, "Response code error"
            keyword = " ".join([user_info.get(element, "") for element in ["firstName", "lastName", "middleName"]])

        found = False
        keywords = keywords_iterator(keyword, keyword_part_count)
        while not found:
            keyword = next(keywords, None)
            if keyword is None:
                break
            with allure.step(f"Ищет по ключевому слову {keyword}"):
                search_result = finder.rapi_search(keyword)
                found = user_in_search_result(search_result, target)
        assert result == found, "Ошибка поиска"
