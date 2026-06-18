import sys

import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("79649")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Контакты")
@allure.feature("Запрос информации id")
@allure.title("Получение lastseen для списка пользователей")
def test_get_user_last_seen(
    auth_account,
    opponent_account,
    bot_class,
    fetch_until_empty_answer_with_filter,
):
    ids_list = [auth_account.uin, opponent_account.uin, bot_class.uin]
    errors_list = []
    lastseen_event = {}
    with allure.step("Подписываемся на userState пользователя"):
        auth_account.rapi_eventSubscribe(
            subscriptions=[
                {
                    "type": "userState",
                    "data": {
                        "contacts": ids_list,
                    },
                }
            ],
        )

    with allure.step("Проверяем что в событии userState приходит правильный lastseen"):
        opponent_event_lastseen = False
        auth_event_lastseen = False
        bot_event_lastseen = False

        for event in fetch_until_empty_answer_with_filter(auth_account, "userState")[::-1]:
            data = event["eventData"]

            if opponent_account.uin == data["sn"]:
                lastseen = data["userState"]["lastseen"]
                lastseen_event[data["sn"]] = lastseen
                opponent_event_lastseen = True

            elif auth_account.uin == data["sn"]:
                lastseen = data["userState"]["lastseen"]
                lastseen_event[data["sn"]] = lastseen
                auth_event_lastseen = True

            elif bot_class.uin == data["sn"]:
                lastseen = data["userState"]["lastseen"]
                lastseen_event[data["sn"]] = lastseen
                bot_event_lastseen = True

            if opponent_event_lastseen and auth_event_lastseen and bot_event_lastseen:
                break

        assert opponent_event_lastseen, "Lastseen not equal 0"
        assert auth_event_lastseen, "Lastseen equal 0"
        assert bot_event_lastseen, "Lastseen equal 0"

    with allure.step("Пробуем сделать запрос"):
        response = auth_account.rapi_getUserLastSeen(
            ids=ids_list,
        )
        for entry in response["results"]["entries"]:
            try:
                assert entry["sn"] in ids_list, f"{auth_account.env}:Wrong user in list"
                assert entry["userState"]["lastseen"] >= 0, f"{auth_account.env}:Wrong lastseen value"
                assert all(
                    entry["userState"]["lastseen"] == value
                    for keys, value in lastseen_event.items()
                    if keys == entry["sn"]
                ), f"{auth_account.env}:Wrong lastseen"
            except Exception as error:
                errors_list.append(error)

        if errors_list:
            if sys.version_info.minor > 10:
                raise ExceptionGroup(
                    f"{auth_account.env}:rapi/getUserLastSeen",
                    errors_list,
                )
            else:
                raise Exception(f"{auth_account.env}:Errors in rapi/getUserLastSeen:{errors_list}")
