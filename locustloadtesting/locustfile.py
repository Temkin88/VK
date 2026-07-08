import logging

import urllib3
from locust import User, task, HttpUser
from locust.clients import LocustHttpAdapter, HttpSession
from requests.sessions import Session

from pyvkteamsclient.client import DesktopClient


logging.basicConfig(
    level=logging.WARNING
)

# pool_manager = urllib3.PoolManager()
# session = Session()
# session.mount("https://", LocustHttpAdapter(pool_manager=pool_manager))
# session.mount("http://", LocustHttpAdapter(pool_manager=pool_manager))


class VKTeamsUser(HttpUser):

    host = 'https://u-stage-stable.v3.im-sandbox.devmail.ru'

    # def on_start(self):
    #     self.client = HttpSession(
    #         base_url='https://u-stage-stable.v3.im-sandbox.devmail.ru',
    #         request_event=self.environment.events.request,
    #         user=self
    #     )

    def on_start(self):
        self.vkclient = DesktopClient(
            uin='autotest001@autotest.clients',
            api_url='https://u-stage-stable.v3.im-sandbox.devmail.ru',
            binary_api_url='https://ub-stage-stable.v3.im-sandbox.devmail.ru',
            api_ver=108,
            fix_otp='ONPREM',
            env='SANDBOX',
            session=self.client,
            polling=False,
            check_response=False
        )

    def on_stop(self):
        self.vkclient.wim_aim_endSession()

    @task
    def send_message(self):
        self.vkclient.send_basic_message(
            sn=self.vkclient.uin,
            text='Test123'
        )

    @task
    def test_task(self):
        self.vkclient.session.request('GET', 'https://u-stage-stable.v3.im-sandbox.devmail.ru/myteam-config.json')
