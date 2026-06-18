import allure

from support.markers import SAAS, ISOLATION, PRE_SAAS
from tests.test_client_api.test_isolation.common import subscribe_thread_if_not_subscribed


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Треды")
@allure.feature("Информация о треде")
@allure.title("Поиск по списку подписчиков треда")
@ISOLATION
@PRE_SAAS
@SAAS
def test_thread_subscribers_get_isolation(
    prepared_thread_isolation,
):
    """
    Проверяем создание тредов
    """
    auth_account, opponent_account, chat, msg_id, thread_id = prepared_thread_isolation
    subscribe_thread_if_not_subscribed(acc=auth_account, thread_id=thread_id)
    subscribe_thread_if_not_subscribed(acc=opponent_account, thread_id=thread_id)

    with allure.step("Проверяем список подписчиков треда"):
        response = auth_account.rapi_thread_subscribers_search(thread_id, auth_account.uin)

        subsribers_list = [x["sn"] for x in response["results"]["subscribers"]]

        assert auth_account.uin in subsribers_list, "Failed to search self in subs list"

    with allure.step("Проверяем список подписчиков треда оппонентом"):
        response = opponent_account.rapi_thread_subscribers_search(thread_id, opponent_account.uin)

        subsribers_list = [x["sn"] for x in response["results"]["subscribers"]]

        assert opponent_account.uin in subsribers_list, "Failed to search self in subs list"
