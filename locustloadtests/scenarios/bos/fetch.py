from locust import task

from base.user import VkTeamsUser


class UserFetchEvents(VkTeamsUser):

    @task
    def fetch_events(self):

        self.user.fetch(rewrite=False)
