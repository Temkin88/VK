from locust import task

from base_new.user_with_group import VkTeamsUserWithGroup


class UserWithGroupTest(VkTeamsUserWithGroup):
    @task
    def thread_add_in_group(self):
        print('test group')
