import time
import uuid

import allure

from api.client.adapter import ClientAdapterBiz
from api.client.client import BizAdminClient
from common.config import LOGIN_WS, PASS_WS
from markers import WS_INTEGRATION


@allure.id("2489853")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("Админка")
@allure.feature("Интеграционное тестирование VKT+WorkSpace")
@allure.title("Авторизация через SuperApp с 2FA")
@WS_INTEGRATION
def test_authorization_superapp_2fa(get_config, SANDBOX, account_swa):
    biz_url = SANDBOX.replace("https://", "https://biz.", 1)
    # login_ws = "1@swadup.auth-test.vkteams.vkwm.ru"
    login_ws = account_swa['uin']
    gp_name = str(uuid.uuid4()).replace("-", "")[:9]

    user_biz = BizAdminClient(
        base_url=SANDBOX,
        username=LOGIN_WS,
        password=PASS_WS,
        login_adapter=ClientAdapterBiz(base_url=SANDBOX),
    )

    user_biz.login()
    biz_domain_list = user_biz.list_domains(biz_url)
    domain = [i for i in biz_domain_list if i["name"] == login_ws.split("@")[1]][0]
    search_users = user_biz.search_users(base_url=biz_url, user=login_ws, domain_id=domain["id"])
    search_user = [user for user in search_users["data"] if user["email"] == login_ws][0]
    user_id = search_user["id"]
    user = user_biz.user(base_url=biz_url, user_id=user_id, domain_id=domain["id"])

    gp = user_biz.create_gp_2fa(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], name=gp_name)
    gp_id = gp["id"]
    gp_2fa_policies = user_biz.set_gp_2fa_polices(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], gp_id=gp_id)
    user_biz.set_gp_policies(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], gp_id=gp_id, user=login_ws)
    user_biz.set_phone_2fa(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], user_id=user_id)
    gp_policies = user_biz.get_gp_policies(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], gp_id=gp_id, user=login_ws)

    assert gp_policies['data'][0]['is_2fa_enabled']
    assert gp_2fa_policies['value']['enabled']['value']
    assert gp_policies['data'][0]['email'] == login_ws

    MAX_RETRIES = 5
    for _ in range(MAX_RETRIES):
        two_step = user_biz.two_step_preserve(base_url=biz_url, domain_id=domain["id"], user_id=user_id)
        if two_step['enabled']:
            break
        else:
            time.sleep(1)
            continue

    two_factor_methods = user_biz.two_factor_methods(base_url=biz_url, domain_id=domain["id"], user_id=user_id)
    available_phones = user_biz.available_phones(base_url=biz_url, domain_id=domain["id"], user_id=user_id)

    assert two_step['enabled']
    assert two_factor_methods["methods"][0]['is_active']
    assert available_phones[0]['two_factor']
    assert LOGIN_WS in user_biz.username
    assert SANDBOX in user_biz.base_url

    # api_url = get_config(f"u.{SANDBOX.replace("https://", "vkt-", 1)}")['api-urls']['main-api']
    # api_ver = get_config(f"u.{SANDBOX.replace("https://", "vkt-", 1)}")['api-version']
    # imap_url = SANDBOX.replace("https://", "imap.", 1)
    # url = SANDBOX.replace("https://", "https://u.vkt-", 1)

    # user_teams = UserClientTeamsOTP(
    #     api_url=api_url,
    #     api_ver=api_ver,
    #     uin=login_ws,
    #     password=pass_ws,
    #     imap_url=imap_url,
    #     login_adapter=ClientAdapterTeamsOTP(base_url=api_url),
    # )
    # user = user_teams.login(fix_otp=False)
    # assert login_ws in user[0]
    # assert url in user[1]

    user_biz.delete_gp_2fa(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], gp_id=gp_id)