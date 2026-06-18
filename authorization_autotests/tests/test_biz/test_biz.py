from api.client.adapter import ClientAdapterBiz
from api.client.client import BizAdminClient
from common.config import HOSTS_TEAMS, LOGIN_WS, PASS_WS
from conftest import get_config
from markers import BIZ


@BIZ
def test_biz(get_config):
    host_ws = f"https://{HOSTS_TEAMS}"
    user_ws = BizAdminClient(
        base_url=host_ws,
        username=LOGIN_WS,
        password=PASS_WS,
        login_adapter=ClientAdapterBiz(base_url=host_ws),
    )
    user_ws.get_list_domains()
    assert "admin@admin.qdit" in user_ws.username
    assert host_ws in user_ws.base_url



    # "autotest{001-10}@sso.auth-test.vkteams.vkwm.ru" - кейклок
    # "autotest{001-10}@swa.auth-test.vkteams.vkwm.ru" - по паролю почты
    # "autotest{001-10}@otp.auth-test.vkteams.vkwm.ru" - одноразовый пароль
