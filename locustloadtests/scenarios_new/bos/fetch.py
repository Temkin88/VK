from locust import task

from base_new.user import VkTeamsUser


class UserFetchEventsNew(VkTeamsUser):

    @task
    def fetch_events(self):
        self.user.fetch(rewrite=False)
