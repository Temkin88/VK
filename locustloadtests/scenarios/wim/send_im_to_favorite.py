import random

from locust import task

from base.user import VkTeamsUser


class UserSendImToFavorite(VkTeamsUser):

    @task
    def send_im_to_favorite(self):
        self.user.wim_im_sendIM(
            t=self.user.uin,
            message='test'
        )
