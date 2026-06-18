import time
import uuid

from api.client.http_client import HttpClient

from typing import Optional, Union, Literal, TYPE_CHECKING


class MethodBiz(HttpClient):
    def get_api_domains_auth_types(self, url):
        """
        Список доступных типов аутентификации для домена
        :param url:
        :return:
        """
        return self.get(url=url, path="api/domains//auth-types")

    def post_api_domains_auth_types(self, url, auth_type):
        """
        Добавление нового типа аутентификации для домена
        :param url:
        :param auth_type: Тип аутентификации
        :return:
        """
        return self.post(url=url, path="api/domains//auth-types", params={"type": auth_type})

    def del_api_domains_auth_types(self, url, auth_type):
        """
        Удаление типа аутентификации для домена
        :param url:
        :param auth_type: Тип аутентификации
        :return:
        """
        return self.delete(url=url, path="api/domains//auth-types", params={"type": auth_type})

    def get_api_domains_users_auth_types(self, url):
        """
        Список доступных типов аутентификации у пользователя
        :param url:
        :return:
        """
        return self.get(url=url, path="api/domains//users//auth-types")

    def del_api_domains_users_auth_types(self, url, auth_type):
        """
        Удаление типа аутентификации у пользователя
        :param url:
        :param auth_type: Тип аутентификации
        :return:
        """
        return self.delete(url=url, path="api/domains//users//auth-types", params={"type": auth_type})

    def get_api_domains_idp_sso(self, url):
        """
        Получить sso провайдер для домена
        :param url:
        :return:
        """
        return self.get("api/domains//idp/sso")

    def post_api_domains_idp_sso(
            self,
            url: str,
            title,
            auth_uri,
            token_uri,
            userinfo_uri,
            client_id,
            client_secret,
            description: Optional[str]=None
    ):
        """
        Создать sso провайдер для домена
        :param url:
        :param title: название
        :param auth_uri: url cтарта авторизации и получения code
        :param token_uri: url для обмена code на token_uri
        :param userinfo_uri: url получения информации о пользователе по токену
        :param client_id: идентификатор клиента
        :param client_secret: секрет клиента
        :param description: описание
        :return:
        """
        return self.post(url=url,
                         path="api/domains//idp/sso",
                         params={"title": title,
                                 "description": description,
                                 "auth_uri": auth_uri,
                                 "token_uri": token_uri,
                                 "userinfo_uri": userinfo_uri,
                                 "client_id": client_id,
                                 "client_secret": client_secret
                                 }
                         )

    def put_api_domains_idp_sso(
            self,
            url: str,
            title,
            auth_uri,
            token_uri,
            userinfo_uri,
            client_id,
            client_secret,
            description: Optional[str]=None
    ):
        """
        Редактировать sso провайдер для домена
        :param url:
        :param title: название
        :param auth_uri: url cтарта авторизации и получения code
        :param token_uri: url для обмена code на token_uri
        :param userinfo_uri: url получения информации о пользователе по токену
        :param client_id: идентификатор клиента
        :param client_secret: секрет клиента
        :param description: описание
        :return:
        """
        return self.put(url=url, path="api/domains//idp/sso",
                         params={"title": title,
                                 "description": description,
                                 "auth_uri": auth_uri,
                                 "token_uri": token_uri,
                                 "userinfo_uri": userinfo_uri,
                                 "client_id": client_id,
                                 "client_secret": client_secret})

    def del_api_domains_idp_sso(self, url):
        """
        Удаление sso провайдера для домена
        :param url:
        :return:
        """
        return self.delete(url=url, path="api/domains//idp/sso")

    def api_auth_login(self, url, username, password):
        """
        Аутентификация пользователя
        :param url:
        :param username: Юзернейм пользователя
        :param password: Пароль пользователя
        :return:
        """
        return self.post(url=url, path="api/auth/login", params={"username": username, "password": password})

    def api_auth_login_view(self, url, next: Optional[str]=None):
        """
        Аутентификация пользователя
        :param url:
        :param next: Куда произвести редирект в случае успешной авторизации
        :return:
        """
        return self.get(url=url, path="api/auth/login-view", params={"next": next})

    def get_api_auth_logout_view(self, url):
        """
        Эндпоинт для разлогина текущего пользователя
        :param url:
        :return:
        """
        return self.get(url=url, path="api/auth/logout-view")

    def post_api_auth_logout_view(self, url):
        """
        Эндпоинт для разлогина текущего пользователя
        :param url:
        :return:
        """
        return self.post(url=url, path="api/auth/logout-view")



    def list_domains(self, base_url):
        return self.get(url=base_url + "/api/domains").json()

    def list_policies_projections(self, domain_id: int, limit: int = 100, offset: int = 0):
        return self.get(
            url=f"/api/domains/{domain_id}/gp/policy-projections/", params={"limit": limit, "offset": offset}
        ).json()

    def list_gp_services(self, domain_id: int, limit: int = 100, offset: int = 0):
        return self.get(url=f"/api/domains/{domain_id}/gp/services/", params={"limit": limit, "offset": offset}).json()

    def get_gp_service_policies(self, domain_id: int, service_name: str, app_name: str = "vkt"):
        return self.get(
            url=f"/api/domains/{domain_id}/gp/policies/", params={"service_name": service_name, "app_name": app_name}
        ).json()

    def create_policy_projection(self, domain_id: int, policy_id: int, title: str, description: str, value: dict):
        return self.post(
            url=f"/api/domains/{domain_id}/gp/policy-projections/",
            json={
                "policy_id": policy_id,
                "title": title,
                "description": description,
                "value": value,
            },
        ).json()

    def edit_policy_projection(
        self, domain_id: int, policy_projection_id: int, title: str, description: str, value: dict
    ):
        return self.patch(
            url=f"/api/domains/{domain_id}/gp/policy-projections/{policy_projection_id}/",
            json={
                "title": title,
                "description": description,
                "value": value,
            },
        ).json()

    def delete_policy_projection(self, domain_id: int, policy_projection_id: int):
        return self.delete(url=f"/api/domains/{domain_id}/gp/policy-projections/{policy_projection_id}/").json()

    def assign_policy_projection_to_user(self, domain_id: int, policy_projection_id: int, username: str):
        return self.post(
            url=f"/api/domains/{domain_id}/gp/policy-projections/{policy_projection_id}/users/",
            json={"username": username},
        ).json()

    def disassign_policy_projection_to_user(self, domain_id: int, policy_projection_id: int, user_id: int):
        return self.delete(
            url=f"/api/domains/{domain_id}/gp/policy-projections/{policy_projection_id}/users/{user_id}/"
        ).json()

    def list_user_groups(self, domain_id: int, limit: int = 100, offset: int = 0):
        return self.get(url=f"/api/domains/{domain_id}/gp/groups/", params={"limit": limit, "offset": offset}).json()

    def create_user_group(self, domain_id: int, group_name: str, description: str):
        return self.post(
            url=f"/api/domains/{domain_id}/gp/groups/", json={"name": group_name, "description": description}
        ).json()

    def add_user_to_group(self, domain_id: int, group_id: int, username: str):
        return self.post(url=f"/api/domains/{domain_id}/gp/groups/{group_id}/users/", json={"username": username}).json()

    def delete_user_from_group(self, domain_id: int, group_id: int, user_id: int):
        return self.delete(url=f"/api/domains/{domain_id}/gp/groups/{group_id}/users/{user_id}/").json()

    def delete_user_group(self, domain_id: int, group_id: int):
        return self.delete(url=f"/api/domains/{domain_id}/gp/groups/{group_id}/").json()

    def assign_policy_projection_to_group(self, domain_id: int, policy_projection_id: int, group_id: int):
        return self.post(
            url=f"/api/domains/{domain_id}/gp/policy-projections/{policy_projection_id}/groups/",
            json={"group_id": group_id},
        ).json()

    def disassign_policy_projection_to_group(self, domain_id: int, policy_projection_id: int, group_id: int):
        return self.delete(
            url=f"/api/domains/{domain_id}/gp/policy-projections/{policy_projection_id}/groups/{group_id}/"
        ).json()

    def create_user(
        self,
        base_url: str,
        domain_id: int,
        domain_name: str,
        firstname: str,
        lastname: str,
        username: str,
        middlename: Optional[str] = None,
        structure_unit: Optional[str] = None,
        position: Optional[str] = None,
        phone: str = "+79251286544",
        password: str = "DEFAULT_PWD",
    ):
        # str_uuid = str(uuid.uuid4()).replace("-", "")[:9]
        json_data = {
            "firstname": firstname,
            "lastname": lastname,
            "middlename": middlename,
            "username": username,
            "password": password,
        }

        if structure_unit is not None:
            json_data["structure_unit"] = structure_unit

        if position is not None:
            json_data["position"] = position

        if phone is not None:
            json_data["phone"] = phone

        return self.post(url=base_url + f"/api/onpremise/domains/{domain_id}/users/",
                         headers={"Referer": f"{base_url}/domains/{domain_name}/users/"},
                         json=json_data).json()

    def delete_user(self,base_url: str, domain_name: str, domain_id: int, user_id: int):
        return self.delete(url=base_url + f"/api/onpremise/domains/{domain_id}/users/{user_id}/",
                           headers={"Referer": f"{base_url}/domains/{domain_name}/users/"},)

    def search_users(self, base_url, user, domain_id, limit=25,):
        return self.get(url=base_url + f"/api/onpremise/domains/{domain_id}/users/",
                 params={
                     "q": user,
                     "limit": limit,
                     "ordering": "lastname",
                     "offset": 0,
                     "additional_param": "aliases",
                     "status": "",
                     "_": int(time.time()),
                 }).json()

    def user(self, base_url, user_id, domain_id):
        return self.get(url=base_url + f"/api/onpremise/domains/{domain_id}/users/{user_id}/").json()

    def two_step_preserve(self, base_url, domain_id, user_id):
        return self.get(url=base_url + f"/api/domains/{domain_id}/users/{user_id}/two-step-preserve/").json()

    def two_factor_methods(self, base_url, domain_id, user_id):
        return self.get(url=base_url + f"/api/domains/{domain_id}/users/{user_id}/two-factor-methods/").json()

    def available_phones(self, base_url, domain_id, user_id):
        return self.get(url=base_url + f"/api/domains/{domain_id}/users/{user_id}/two-factor/available-phones/").json()

    def set_phone_2fa(self, base_url, domain_name, domain_id, user_id):
        return self.post(url=base_url + f"/api/domains/{domain_id}/users/{user_id}/two-factor/available-phones/active/",
                         headers={"Referer": f"{base_url}/domains/{domain_name}/user/1/2fa/"},
                         json={"phone": "9999999999"}).json()

    def create_gp_2fa(self, base_url, domain_name, domain_id, name):
        return self.post(url=base_url + f"/api/domains/{domain_id}/policies/2fa/projections/",
                         headers={"Referer": f"{base_url}/domains/{domain_name}/users/"},
                         json={"title": name}).json()

    def delete_gp_2fa(self, base_url, domain_name, domain_id, gp_id):
        return self.delete(
            url=base_url + f"/api/domains/{domain_id}/policies/2fa/projections/{gp_id}/",
            headers={"Referer": f"{base_url}/domains/{domain_name}/onpremise/config/two-factor-authentication-policy/"})

    def get_policies(self, base_url, domain_id, user_id):
        return self.get(url=base_url + f"/api/domains/{domain_id}/users/{user_id}/policies/",
                        psrams={
                            "limit": 10,
                        }).json()

    def set_gp_policies(self, base_url, domain_name, domain_id, gp_id, user):
        return self.post(url=base_url + f"/api/domains/{domain_id}/gp/policy-projections/{gp_id}/users/",
                        headers={"Referer": f"{base_url}/domains/{domain_name}/users/"},
                        json={"username": user}).json()

    def set_gp_2fa_polices(self, base_url, domain_name, domain_id, gp_id):
        return self.patch(
            url=base_url + f"/api/domains/{domain_id}/policies/2fa/projections/{gp_id}/",
            headers={"Referer": f"{base_url}/domains/swadup.auth-test.vkteams.vkwm.ru/onpremise/config/two-factor-authentication-policy/"},
            json={
                "value":{
                    "enabled":{
                        "type":"Boolean","value": True
                    }
                }
            }).json()

    def get_gp_policies(self, base_url, domain_name, domain_id, gp_id, user):
        return self.get(url=base_url + f"/api/domains/{domain_id}/gp/policy-projections/{gp_id}/users/",
                        headers={"Referer": f"{base_url}/domains/{domain_name}/group-policies/{gp_id}/user-groups"},
                        params={"limit": 10}).json()
