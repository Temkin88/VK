import logging

from imcommonsupplyclient import VoIPBot
from locust import task

from common.scenario import BaseUserScenario


logger = logging.getLogger(__name__)


class GroupCallFromChatScenario(BaseUserScenario):

    def on_start(self) -> None:
        super().on_start()

        bots: list[VoIPBot] = self.get_bots(self.max_users_count)

        first_bot, *other_bots = bots

        self.chat_id = first_bot.create_chat(members=bots)

    @task
    def group_call_from_chat(self):
        bots: list[VoIPBot] = self.get_bots(self.max_users_count)

        first_bot, *other_bots = bots

        calls = [first_bot.make_chat_call(self.chat_id, other_bots, with_video=False)]

        for bot in other_bots:
            calls.append(bot.wait_call_and_accept(with_video=False))

        for call in calls:
            call.hang_up()
