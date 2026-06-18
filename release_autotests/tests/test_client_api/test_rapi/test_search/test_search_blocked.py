import allure

from support.markers import VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM


@allure.id("171245")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Проверяем, что в поиске нет заблокированных пользователей")
@allure.title("Проверяем, что в поиске нет заблокированных пользователей")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
def test_search_blocked(
    ENV_PLATFORM,
    auth_account,
    stentor,
    stentor_account,
):
    """
    Проверяем, что в поиске нет заблокированных пользователей
    :param ENV_PLATFORM: Определяет с какого окружения запущен тест
    :param auth_account: Основной аккаунт
    :param stentor: Сессия stentor
    :param stentor_account: Аккаунт stentor пользователя
    """
    search_name_blocked = {}

    if ENV_PLATFORM == "VKTI" or ENV_PLATFORM == "PRE_VKTI":
        search_name_blocked["sn"] = "o.novikov@vk.team"
        search_name_blocked["name"] = "Олег Новиков"

    elif ENV_PLATFORM == "TARM":
        search_name_blocked["sn"] = "a.tester_blocked@armgs.team"
        search_name_blocked["name"] = "tester auto"

    elif ENV_PLATFORM == "PRE_TARM":
        search_name_blocked["sn"] = "autotester_blocked@tppr.vmailru.net"
        search_name_blocked["name"] = "tester auto"

    else:
        response = auth_account.rapi_getUserInfo(sn=stentor_account["email"])

        with allure.step("Блокируем пользователя"):
            stentor.biz_deleteUser(
                email=stentor_account["email"],
            )

        search_name_blocked["sn"] = stentor_account["email"]
        search_name_blocked["name"] = response["results"]["friendly"]

    with allure.step("Проверяем что пользователь заблокирован"):
        response = auth_account.rapi_getUserInfo(sn=search_name_blocked["sn"])
        user_state = response["results"]["userState"]["state"]

        assert user_state == "blocked", "User state not match blocked"

    with allure.step("Проверяем что пользователь не найден"):
        response = auth_account.rapi_search(
            keyword=search_name_blocked["name"],
        )
        results = response["results"]["data"]

        found_user = list(
            filter(
                lambda x: x["sn"] == search_name_blocked["sn"],
                results,
            )
        )

        assert not found_user, "Blocked profile was found"
