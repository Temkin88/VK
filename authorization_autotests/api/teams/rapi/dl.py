from ...client.http_client import HttpClient


class DlMethods(HttpClient):
    """
    Методы группы 'Авторизация' из https://im-docs.corp.mail.ru/
    """

    def rapi_dl_send(self, email: str):
        return self.post(
            url=url + f"/api/v{api_version}/rapi/dl/sendOtp",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": getReqId,
                "params": {
                    "email": email,
                },
            },
        )

    def rapi_dl_verify(self, email: str):
        return self.post(
            url=url + f"/api/v{api_version}/rapi/dl/verifyOtp",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": getReqId,
                "params": {"email": email, "password": self.fix_otp},
            },
        )

    def rapi_internal_dl_verify_hash(self, transient_hash: str):
        """
        Проверить существование хэша для формирования временных url для скачивания iOS приложения
        :param transient_hash: Временный hash, полученный при вызове /dl/verifyOtp
        :return: тело ответа сервера
        """
        return self.post(
            "rapi/internal/dl/verifyHash",
            params={"reqId": getReqId, "authToken": self.org_struct_admin_token, "hash": transient_hash},
        )
