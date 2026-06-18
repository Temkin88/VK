import allure

from support.markers import SANDBOX


@allure.id("513334")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Biz")
@allure.title("Проверка завершения всех сессий для пользователя /api/v1/biz/dropSessions")
@SANDBOX
def test_drop_sessions(
    fourth_account,
    fourth_account_second_instance,
    stentor,
):
    def send_msg_without_check_response(instance_account):
        response = instance_account.request(
            method="POST",
            url="/".join([instance_account.base_url, "/wim/im/sendIM"]),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "aimsid": instance_account.aimsid,
                "r": instance_account.getReqId(),
                "t": instance_account.uin,
                "message": "Test message",
            },
            ignore_check=True,
        )
        return response

    first_instance_account = fourth_account
    second_instance_account = fourth_account_second_instance

    with allure.step(f"Получаем текущий списoк сессий для {first_instance_account.uin}"):
        first_instance_account.rapi_session_list()

    with allure.step("Пытаемся отправить сообщение в сессии 1"):
        first_instance_account.wim_im_sendIM(t=first_instance_account.uin, message="Test text msg 1")

    with allure.step("Пытаемся отправить сообщение в сессии 2"):
        first_instance_account.wim_im_sendIM(t=second_instance_account.uin, message="Test text msg 2")

    with allure.step(f"Заканчиваем все сессии для {first_instance_account.uin}"):
        stentor.biz_dropSessions(email=first_instance_account.uin)

    with allure.step("Пытаемся отправить сообщение в сессии 1"):
        response = send_msg_without_check_response(first_instance_account)

        assert response["response"]["statusCode"] == 401, "Sessions not closed"
        assert response["response"]["statusText"] == "Authentication Required", "Sessions not closed"

    with allure.step("Пытаемся отправить сообщение в сессии 2"):
        response = send_msg_without_check_response(second_instance_account)

        assert response["response"]["statusCode"] == 401, "Sessions not closed"
        assert response["response"]["statusText"] == "Authentication Required", "Sessions not closed"
