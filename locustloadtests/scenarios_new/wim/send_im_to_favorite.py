import random

from locust import task

from base_new.user import VkTeamsUser


class UserSendImToFavoriteNew(VkTeamsUser):

    @task
    def send_im_to_favorite(self):
        self.user.wim_im_sendIM(
            t=self.user.uin,
            message='test'
        )
