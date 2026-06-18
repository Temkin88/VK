from ...client.http_client import HttpClient


class MiniappsMethods(HttpClient):
    """
    Методы группы 'Мини-аппы' из https://im-docs.corp.mail.ru/
    """

    def rapi_miniapp_get(self, miniAppId: str) -> dict:
        """
        Получить информацию о мини-аппе
        :param miniAppId: Идентификатор мини-аппа
        """
        return self.post(
            "rapi/miniapp/get",
            headers={"Content-Type": "application/json"},
            json={
                "aimsid": aimsid,
                "reqId": getReqId,
                "params": {"miniAppId": miniAppId},
            },
        )
