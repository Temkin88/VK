from ...client.http_client import HttpClient


class BizMethods(HttpClient):
    """
    Методы группы 'BIZ' из https://im-docs.corp.mail.ru/
    """

    def rapi_biz_domain_info_get(self, domain: str):
        """
        Проверка домена
        Проверяет наличие домена, переданного в запросе, в stdb таблице "myteam-old-domains".
        Для выполнения метода необходим prism token.
        Запрос обрабатывается в сервисе front.
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/biz/domain/info/get",
            json={
                "reqId": getReqId,
                "aimsid": aimsid,
                "authToken": self.org_struct_admin_token,
                "params": {"domain": domain},
            },
        )
