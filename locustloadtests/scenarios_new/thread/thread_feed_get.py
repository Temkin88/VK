from locust import task

from base_new.user_with_group import VkTeamsUserWithGroup


class UserThreadFeedGetNew(VkTeamsUserWithGroup):

    @task
    def thread_feed_get(self):
        self.user.rapi_thread_autosubscribe(
            chatId=self.massive_group_id
        )
        self.user.rapi_thread_feed_get()
        self.user.rapi_thread_autosubscribe(
            chatId=self.massive_group_id,
            enable=False
        )
