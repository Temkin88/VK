import uuid
from typing import Union

from locust import FastHttpUser, constant

from pyvkteamsclient.highload import HighLoadClient
from pyvkteamsclient.stentor import StentorClient

def index(index: Union[str, int], digits_count: int):
    index_string = str(index)
    return '0' * (digits_count - len(index_string)) + index_string


all_users_uin_list = [
    f'autotest{index(i, 3)}@autotest.clients'
    for i in range(1, 100)
]

class VkTeamsUser(FastHttpUser):

    abstract = True

    wait_time = constant(1)

    def on_start(self):
        self.new_user_uin = f'{uuid.uuid4().hex[:8]}@autotest.clients'

        with self.rest(
            method='GET',
            url='/myteam-config.json'
        ) as response:
            config = response.js

            api_url = config['api-urls']['main-api']
            binary_api_url = config['api-urls']['main-binary-api']
            api_version = config['api-version']

        self.stentor = StentorClient(
            session=self.client,
            api_url=api_url.replace('u', 'stentor', 1),
        )

        self.stentor.biz_createUser(
            email=self.new_user_uin,
            firstName=self.new_user_uin,
            lastName=self.new_user_uin
        )

        self.user = HighLoadClient(
            uin=self.new_user_uin,
            fix_otp='ONPREM',
            api_url=api_url,
            binary_api_url=binary_api_url,
            api_ver=api_version,
            session=self.client
        )

    def on_stop(self):

        self.stentor.biz_deleteUser(
            email=self.new_user_uin
        )
