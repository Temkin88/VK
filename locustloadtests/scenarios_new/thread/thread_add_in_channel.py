from locust import task

from base_new.user_with_channel import VkTeamsUserWithChannel


class UserThreadAddInChannelNew(VkTeamsUserWithChannel):
    @task
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
