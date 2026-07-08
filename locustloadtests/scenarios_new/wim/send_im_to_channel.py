import random

from locust import task

from base_new.user_with_channel import VkTeamsUserWithChannel


class UserSendImToChannelNew(VkTeamsUserWithChannel):

    @task
    def send_im_to_channel(self):
        self.user.wim_im_sendIM(
            t=self.massive_channel_id,
            message='test'
        )
