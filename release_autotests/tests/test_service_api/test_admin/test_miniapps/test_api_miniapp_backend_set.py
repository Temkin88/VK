import random

import allure

from support.markers import SANDBOX

certificate = """-----BEGIN CERTIFICATE-----
MIIFMjCCBBqgAwIBAgIJAIDSBbzPyJjqMA0GCSqGSIb3DQEBCwUAMIGfMQswCQYD
VQQGEwJSVTEPMA0GA1UECAwGTW9zY293MQ8wDQYDVQQHDAZNb3Njb3cxCzAJBgNV
BAoMAlZLMRAwDgYDVQQLDAdWSyBUZWNoMSgwJgYDVQQDDB9mYWtlLWthdGEuaW0t
c2FuZGJveC5kZXZtYWlsLnJ1MSUwIwYJKoZIhvcNAQkBFhZ2Lmtvcm9ib3ZAY29y
cC5tYWlsLnJ1MB4XDTIzMDMwMTE5MjczOFoXDTMzMDIyNjE5MjczOFowgZ8xCzAJ
BgNVBAYTAlJVMQ8wDQYDVQQIDAZNb3Njb3cxDzANBgNVBAcMBk1vc2NvdzELMAkG
A1UECgwCVksxEDAOBgNVBAsMB1ZLIFRlY2gxKDAmBgNVBAMMH2Zha2Uta2F0YS5p
bS1zYW5kYm94LmRldm1haWwucnUxJTAjBgkqhkiG9w0BCQEWFnYua29yb2JvdkBj
b3JwLm1haWwucnUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDPgFiw
Qp83Pf7UVOoYR6sF7eDiQ7X5gMqU92DnLInvuEHvEvGr31W3s3OW2jPXVClgeAl/
jms+h6X5ZeOdVNEYTwpuejd6S+SkvEOgEA3lMiSwSss460B222rWU6ADJM3zpO5P
uBF5hAdFgiaNdIWcozd6fYj+JmxhLjJQ1m0iNA7bvhMFL6sWeCVzoxh5DhpkDTNK
ZEsE8R/3900rkwJYy2fv/EwiBmCmcEJhwnnSYcRyZAtuKB7TNGLdPqc6aemP7lBO
GwWsoRxu7tavYNK72BNcGMZcW525sTTCuPe3ywvr3575bnMrIIb6PlWVisCI5nDp
qnykQKBNn/L6dvEDAgMBAAGjggFtMIIBaTAdBgNVHQ4EFgQU7/C40XyD1wH8n4pA
wvWC2duP6fUwgdQGA1UdIwSBzDCByYAU7/C40XyD1wH8n4pAwvWC2duP6fWhgaWk
gaIwgZ8xCzAJBgNVBAYTAlJVMQ8wDQYDVQQIDAZNb3Njb3cxDzANBgNVBAcMBk1v
c2NvdzELMAkGA1UECgwCVksxEDAOBgNVBAsMB1ZLIFRlY2gxKDAmBgNVBAMMH2Zh
a2Uta2F0YS5pbS1zYW5kYm94LmRldm1haWwucnUxJTAjBgkqhkiG9w0BCQEWFnYu
a29yb2JvdkBjb3JwLm1haWwucnWCCQCA0gW8z8iY6jAMBgNVHRMEBTADAQH/MAsG
A1UdDwQEAwIC/DAqBgNVHREEIzAhgh9mYWtlLWthdGEuaW0tc2FuZGJveC5kZXZt
YWlsLnJ1MCoGA1UdEgQjMCGCH2Zha2Uta2F0YS5pbS1zYW5kYm94LmRldm1haWwu
cnUwDQYJKoZIhvcNAQELBQADggEBAEoDqrnPrw/pQL4sU5Mc7f+sjwFyMu3IPW02
1WnL9mmHgFGyiRynRjU7vEDNLree/UN4XC82KeQc0zPi73MkrpGwo80INJljrMeq
95a2I9X/AdZntlMqa84JFvMC7pjO5oJ5V4pV7rh8rMm9Yz430vyDODctUym2GOX5
retbKfRwJmHGTlgbRJUSw0vQ6nVENZjplTGC/BxcLg5gxgfT7uVyyDLmxkuvNf2p
jRoolXaU/Ogn1mjwXQApyO9jfMw8HdjM7X96o2qskwzzDJ+5imPWrFNUK7hpbC13
CENJmaD4ufUCDHOWI4j8rsLMDA4hbfR3I8RdsGjwuJaGpK2uk+0=
-----END CERTIFICATE-----"""


@allure.id("28790")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Миниаппы")
@allure.title(
    "Обновление настроек миниаппа",
)
@SANDBOX
# @pytest.mark.skip('Broken test')
def test_api_miniapp_backend_set(
    admin_account,
    auth_account,
    admin_url,
    outlined_icon_id,
    filled_icon_id,
    showcase_icon_id,
):
    with allure.step("Пробуем создать миниапп"):
        result = admin_account.api_miniapps_create(
            name="Test miniapp autotest",
            description="Test description",
            filled_icon_id=filled_icon_id,
            outlined_icon_id=outlined_icon_id,
            showcase_icon_id=showcase_icon_id,
            allowed_cross_origin_api_hosts=("cdn.jsdelivr.net",),
        )
        miniapp_id = result["result"]["miniappId"]
    with allure.step("Отправляем запрос обновление настроек"):
        admin_account.api_miniapps_backend_set(
            miniapp_id=miniapp_id,
            start_url="/spa/index.html",
            backend_url="https://fake-kata.im-sandbox.devmail.ru",
            backend_certificate=certificate,
        )
        admin_account.api_miniapps_enable(miniapp_id=miniapp_id)

    with allure.step("Пробуем открыть страницу миниаппа"):
        admin_account.request(
            method="GET",
            url=admin_url.replace("admin", miniapp_id) + "/spa/index.html",
            params={
                "platform": "web",
                "aimsid": auth_account.aimsid,
            },
        )

    with allure.step("Пробуем отправить запрос к бэкенду миниаппу"):
        query_data = {"key": str(random.randint(0, 10**6))}
        json_data = {"test": str(random.randint(0, 10**6))}

        response = admin_account.request(
            method="POST",
            url=admin_url.replace("admin", miniapp_id) + "/test/anything",
            params=query_data,
            json=json_data,
            ignore_check=True,
        )

        assert response["args"] == query_data, "Wrong query"
        assert response["data"] == json_data, "Wrong data"

        assert response["headers"]["content-type"] == "application/json", "Wrong headers"
        assert response["headers"]["x-user-id"] == auth_account.uin, "Wrong headers"
