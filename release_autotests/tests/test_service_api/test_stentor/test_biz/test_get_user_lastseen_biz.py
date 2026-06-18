import allure

import random
import string

from support.markers import SANDBOX


@allure.id("513331")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Biz")
@allure.title("Проверка получения lastseen для списка пользователей /api/v1/biz/getUserLastSeenBiz")
@SANDBOX
def test_get_user_lastseen_biz(auth_account, opponent_account, stentor):
    invalid_email = ["".join(random.choices(string.ascii_letters + string.digits, k=25))]
    valid_emails = [auth_account.uin, opponent_account.uin]

    with allure.step("Пытаемся получить lastseen пользователей"):
        response = stentor.biz_getUsersLastSeenBiz(emails=valid_emails + invalid_email)

        assert response["status"]["code"] == 20000

    with allure.step("Проверяем наличие lastseen для переданных пользователей"):
        for email in valid_emails + invalid_email:
            assert email in response["results"], f"Email {email} not found"

            error_response = response["results"][email].get("error")
            last_seen_ts = response["results"][email].get("lastSeenTimeStamp")

            if email in valid_emails:
                assert error_response is None, f"Error for valid email {email}"
                assert last_seen_ts is not None, f"Lastseen not found for valid email {email}"
            else:
                assert error_response is not None, f"Error not found for invalid email {email}"
