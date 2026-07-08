import pathlib
import random

from locust import task, constant_throughput

from base.user import VkTeamsUser, all_users_uin_list


class IMQASupplyUser(VkTeamsUser):

    wait_time = constant_throughput(5)

    @task(1)
    def send_file(self):
        self.user.upload_file(
            pathlib.Path('file.txt')
        )

    @task(50)
    def get_user_profile(self):

        self.user.rapi_getUserInfo(
            sn=self.user.uin
        )

    @task(10)
    def thread_add_in_group(self):
        msg_id = self.user.send_basic_message(
            sn=self.massive_group_id,
            text='msg for thread add'
        )
        thread_id = self.user.add_thread(
            chat_id=self.massive_group_id,
            msg_id=msg_id
        )
        self.user.send_basic_message(
            sn=thread_id,
            text='msg for thread add'
        )

    @task(20)
    def thread_add_in_channel(self):
        msg_id = self.user.send_basic_message(
            sn=self.massive_channel_id,
            text='msg for thread add'
        )
        thread_id = self.user.add_thread(
            chat_id=self.massive_channel_id,
            msg_id=msg_id
        )
        self.user.send_basic_message(
            sn=thread_id,
            text='msg for thread add'
        )

    @task(5)
    def thread_feed_get(self):
        self.user.rapi_thread_autosubscribe(
            chatId=self.massive_group_id
        )
        self.user.rapi_thread_feed_get()
        self.user.rapi_thread_autosubscribe(
            chatId=self.massive_group_id,
            enable=False
        )

    @task(10)
    def send_im_to_favorite(self):
        self.user.wim_im_sendIM(
            t=self.user.uin,
            message='test'
        )

    @task(15)
    def send_im_to_user(self):
        self.user.wim_im_sendIM(
            t=all_users_uin_list[random.randint(0, len(all_users_uin_list))],
            message='test'
        )

    @task(8)
    def send_im_to_channel(self):
        self.user.wim_im_sendIM(
            t=self.massive_channel_id,
            message='test'
        )

    @task(20)
    def send_im_to_group(self):
        self.user.wim_im_sendIM(
            t=self.massive_group_id,
            message='test'
        )

    @task(1)
    def fetch_events(self):

        self.user.fetch(rewrite=False)
