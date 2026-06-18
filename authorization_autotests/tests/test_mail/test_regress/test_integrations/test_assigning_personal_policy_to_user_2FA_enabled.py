import uuid

import allure

from api.client.adapter import ClientAdapterBiz
from api.client.client import BizAdminClient
from common.config import LOGIN_WS, PASS_WS
from markers import WS_INTEGRATION


@allure.id("2489847")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("Админка")
@allure.feature("Интеграционное тестирование VKT+WorkSpace")
@allure.title("Назначение личной политики пользователю - 2FA включено")
@WS_INTEGRATION
def test_assigning_personal_policy_to_user_2FA_enabled(get_config, SANDBOX, account_swa):
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
    gp = user_biz.create_gp_2fa(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], name=gp_name)
    gp_id = gp["id"]
    gp_2fa_policies = user_biz.set_gp_2fa_polices(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], gp_id=gp_id)
    user_biz.set_gp_policies(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], gp_id=gp_id, user=login_ws)
    user_biz.set_phone_2fa(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], user_id=user_id)
    gp_policies = user_biz.get_gp_policies(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], gp_id=gp_id, user=login_ws)

    assert gp_2fa_policies['value']['enabled']['value']
    assert gp_policies['data'][0]['email'] == login_ws
    assert gp_policies['data'][0]['is_2fa_enabled']

    user_biz.delete_gp_2fa(base_url=biz_url, domain_name=domain["name"], domain_id=domain["id"], gp_id=gp_id)