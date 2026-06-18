import uuid

import allure

from api.client.adapter import ClientAdapterTeamsOTP, ClientAdapterBiz
from api.client.client import UserClientTeamsOTP, BizAdminClient
from common.config import LOGIN_WS, PASS_WS
from markers import WS_INTEGRATION


@allure.id("2489736")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("Админка")
@allure.feature("Интеграционное тестирование VKT+WorkSpace")
@allure.title("Новый пользователь. Отображение в ВКТ")
@WS_INTEGRATION
def test_new_user_view_is_vkt(get_config, SANDBOX, account_otp):
    biz_url = SANDBOX.replace("https://", "https://biz.", 1)
    # login_ws = "1@otp.auth-test.vkteams.vkwm.ru"
    login_ws = account_otp['uin']

    user_biz = BizAdminClient(
        base_url=SANDBOX,
        username=LOGIN_WS,
        password=PASS_WS,
        login_adapter=ClientAdapterBiz(base_url=SANDBOX),
    )

    user_biz.login()
    biz_domain_list = user_biz.list_domains(biz_url)
    domain = [i for i in biz_domain_list if i["name"] == login_ws.split("@")[1]][0]

    user_uuid = str(uuid.uuid4()).replace("-", "")[:9]
    password = "Q-12345"

    user_biz.create_user(
        base_url=biz_url,
        domain_id=domain["id"],
        domain_name=domain["name"],
        firstname=user_uuid,
        lastname=user_uuid,
        password=password,
        middlename=user_uuid,
        username=user_uuid
    )

    search_users = user_biz.search_users(base_url=biz_url, user=user_uuid, domain_id=domain["id"])
    search_user_id = search_users["data"][0]["id"]
    search_email_user = search_users["data"][0]["email"]
    assert search_users["data"][0]["username"] == user_uuid

    api_url = get_config(f"u.{SANDBOX.replace("https://", "vkt-", 1)}")['api-urls']['main-api']
    api_ver = get_config(f"u.{SANDBOX.replace("https://", "vkt-", 1)}")['api-version']
    url = SANDBOX.replace("https://", "https://u.vkt-", 1)

    user_teams = UserClientTeamsOTP(
        api_url=api_url,
        api_ver=api_ver,
        uin=search_email_user,
        password=password,
        login_adapter=ClientAdapterTeamsOTP(base_url=api_url),
    )
    user = user_teams.login(fix_otp=False)

    assert search_email_user in user[0]
    assert url in user[1]

    user_biz.delete_user(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], user_id=search_user_id)