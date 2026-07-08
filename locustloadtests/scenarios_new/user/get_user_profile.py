from locust import task

from base_new.user import VkTeamsUser


class UserGetUserInfoNew(VkTeamsUser):

    @task
    def get_user_profile(self):

        self.user.rapi_getUserInfo(
            sn=self.user.uin
        )
