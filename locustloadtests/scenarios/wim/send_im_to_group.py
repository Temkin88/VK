import random

from locust import task

from base.user import VkTeamsUser


class UserSendImToGroup(VkTeamsUser):

    @task
    def send_im_to_group(self):
        self.user.wim_im_sendIM(
            t=self.massive_group_id,
            message='test'
        )
