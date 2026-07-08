import pathlib

from locust import task

from base.user import VkTeamsUser


class UserSendFile(VkTeamsUser):

    @task
    def send_file(self):
        self.user.upload_file(
            pathlib.Path('file.txt')
        )
