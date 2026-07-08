from locust import task

from base.user import VkTeamsUser


class UserGetUserInfo(VkTeamsUser):

    @task
    def get_user_profile(self):

        self.user.rapi_getUserInfo(
            sn=self.user.uin
        )
