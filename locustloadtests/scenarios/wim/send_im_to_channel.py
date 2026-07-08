import random

from locust import task

from base.user import VkTeamsUser


class UserSendImToChannel(VkTeamsUser):

    @task
    def send_im_to_channel(self):
        self.user.wim_im_sendIM(
            t=self.massive_channel_id,
            message='test'
        )
