from typing import Optional

from api.client.http_client import HttpClient


class IdmAdminProviderMethod(HttpClient):
    """
    Методы группы 'Аутентификации домена' из https://im-docs.corp.mail.ru/
    """
    def idm_admin_provider_create(self, url, _type: str, domain: str) -> dict:
        """
        Добавить тип аутентификации домену
        Добавление нового типа аутентификации домену из Панели администратора
        :param _type: Тип аутентификации
        :param domain: Название домена
        :return: тело ответа сервера
        """
        return self.post(
            url + "/api/v133/idm/admin/provider/create",
            headers={"Authorization": f"Bearer {self.token}"},
            data={
                "type": _type,
                "domain": domain,
            },
        )

    def idm_admin_provider_delete(self, url, _type: str, domain: str) -> dict:
        """
        Удалить тип аутентификации из домена
        Удаление типа аутентификации из Панели администратора
        :param _type: Тип аутентификации
        :param domain: Название домена
        :return: тело ответа сервера
        """
        return self.post(
            url + "/api/v133/idm/admin/provider/delete",
            headers={"Authorization": f"Bearer {self.token}"},
            data={
                "type": _type,
                "domain": domain,
            },
        )

    def idm_admin_provider_list(self, url, domain: str) -> dict:
        """
        Получить список доступных типов аутентификации для домена
        Получение списка доступных типов аутентификации
        :param domain: Название домена
        :return: тело ответа сервера
        """
        return self.post(
            url + "/api/v133/idm/admin/provider/list",
            headers={"Authorization": f"Bearer {self.token}"},
            data={
                "domain": domain,
            },
        )

    def idm_admin_provider_account_delete(self, url, user_sn: str, _type: str, domain: Optional[str] = None) -> dict:
        """
        Удалить тип аутентификации из аккаунта
        Удаление привязанного типа аутентификации из аккаунта
        :param user_sn: Идентификатор пользователя
        :param _type: Тип аутентификации
        :param domain: Название домена
        :return: тело ответа сервера
        """
        return self.post(
            url + "/api/v133/idm/admin/provider/account/delete",
            headers={"Authorization": f"Bearer {self.token}"},
            data={
                "aimsid": aimsid,
                "r": getReqId,
                "userSn": user_sn,
                "type": type,
                "domain": domain,
            },
        )

    def idm_admin_provider_account_listProviders(self, url, user_sn: str, domain: Optional[str] = None) -> dict:
        """
        Показать список типов аутентификаций у пользователя
        Показать список возможных типов аутентификаций у пользователя
        :param user_sn: Идентификатор пользователя
        :param domain: Название домена
        :return: тело ответа сервера
        """
        return self.post(
            url + "/api/v133/idm/admin/provider/account/listProviders",
            headers={"Authorization": f"Bearer {self.token}"},
            data={
                "aimsid": aimsid,
                "r": getReqId,
                "userSn": user_sn,
                "domain": domain,
            },
        )
