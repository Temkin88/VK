import allure

from support.markers import SAAS, ISOLATION, PRE_SAAS


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Треды")
@allure.feature("Подписка на тред")
@allure.title("Автоподписка на все треды чата, проверка поля you")
@ISOLATION
@PRE_SAAS
@SAAS
def test_thread_check_you_autosubscribe_isolation(
    prepared_thread_isolation,
):
    """
    Проверяем создание тредов
    """
    auth_account, opponent_account, chat, msg_id, thread_id = prepared_thread_isolation

    with allure.step("Включаем автоподписку на треды"):
        auth_account.rapi_thread_autosubscribe(
            chatId=chat,
        )

    with allure.step("Проверяем поле you"):
        response = auth_account.rapi_thread_get(
            threadId=thread_id,
        )
        assert response["results"]["you"]["subscriber"], "Not subscribed"
