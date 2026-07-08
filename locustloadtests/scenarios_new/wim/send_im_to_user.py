import random

from locust import task

from base_new.user import VkTeamsUser, all_users_uin_list


class UserSendImToUserNew(VkTeamsUser):

    @task
    def send_im_to_user(self):
        self.user.wim_im_sendIM(
            t=all_users_uin_list[random.randint(0, len(all_users_uin_list))],
            message='test'
        )
