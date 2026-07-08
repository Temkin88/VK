import random

from locust import task

from base_new.user_with_group import VkTeamsUserWithGroup


class UserSendImToGroupNew(VkTeamsUserWithGroup):

    @task
    def send_im_to_group(self):
        self.user.wim_im_sendIM(
            t=self.massive_group_id,
            message='test'
        )
