import logging

from locust import task

from common.scenario import BaseUserScenario


logger = logging.getLogger(__name__)


class GroupCallFromCallsTabScenario(BaseUserScenario):

    @task
    def group_call_from_calls_tab(self):

        bots = self.get_bots(self.max_users_count)

        first_bot, *other_bots = bots

        calls = [first_bot.make_group_call(other_bots, with_video=False)]

        for bot in other_bots:
            calls.append(bot.wait_call_and_accept(with_video=False))

        for call in calls:
            call.hang_up()
