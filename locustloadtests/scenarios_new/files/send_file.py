import pathlib

from locust import task

from base_new.user import VkTeamsUser


class UserSendFileNew(VkTeamsUser):

    @task
    def send_file(self):
        self.user.upload_file(
            pathlib.Path('file.txt')
        )
