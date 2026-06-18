import allure
import pytest

from pyvkteamsclient.client.exceptions import ServerException
from support.markers import SAAS, TARM, PRE_TARM, VKTI, PRE_VKTI, PRE_SAAS


@allure.id("82794")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Пуш-уведомления")
@allure.feature("Инвалидировать пуш-токен")
@allure.title("Инвалидируем пуш-токен")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@VKTI
@PRE_VKTI
def test_rapi_invalidate_push_token(auth_account):
    with allure.step("Пробуем анулировать токен"):
        auth_account.rapi_invalidatePushToken(
            sn=auth_account.uin,
            sid=auth_account.aimsid,
            push_token="ckHBpc_BRJWdNY4A-O3IUC:APA91bHCJntQCOD4qwCfxAOjEE-76SX88ymcmC_xevnEMozLFA6BYIFFNFJdkcd6TmNQ_ItJKgS"
            "AijsVsz4B-3V4duYISlV40Ww2nJ8Lazj8eA41Tmb6skjTqlGsYWf86-8Igl4ddU_W",
            voip_push_token="020b2336fc5cc5c92010615301af40c10c4d4cd91d9b3d4fa97c06120c92873a",
        )


@allure.id("82793")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Пуш-уведомления")
@allure.feature("Инвалидировать пуш-токен")
@allure.title("Инвалидируем пуш-токен с пустыми токенами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
def test_rapi_invalidate_push_token_with_empty_tokens(auth_account):
    with allure.step("Пробуем отправить запрос с пустыми параметрами"), pytest.raises(ServerException):
        auth_account.rapi_invalidatePushToken(
            sn=auth_account.uin,
            sid=auth_account.aimsid,
            push_token="",
            voip_push_token="",
        )
