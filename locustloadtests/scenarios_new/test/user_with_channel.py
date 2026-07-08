from locust import task

from base_new.user_with_channel import VkTeamsUserWithChannel


class UserWithChannelTest(VkTeamsUserWithChannel):
    @task
    def thread_add_in_channel(self):
        print('test channel')
