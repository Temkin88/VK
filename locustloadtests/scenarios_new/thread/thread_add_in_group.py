from locust import task

from base_new.user_with_group import VkTeamsUserWithGroup


class UserThreadAddInGroupNew(VkTeamsUserWithGroup):
    @task
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
