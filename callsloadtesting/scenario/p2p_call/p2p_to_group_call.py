import logging

from locust import task

from common.scenario import BaseUserScenario


logger = logging.getLogger(__name__)


class P2PToGroupCallScenario(BaseUserScenario):

    max_users_count = 3

    @task
    def p2p_to_group_call(self):

        bot_a, bot_b, bot_c = self.get_bots(self.max_users_count)

        bot_a_out_call = bot_a.make_p2p_call(to=bot_b, with_video=False)
        bot_b_in_call = bot_b.wait_call_and_accept(with_video=False)

        bot_a_out_call.add_participants(bot_c)

        bot_c_in_call = bot_c.wait_call_and_accept()

        for call in [bot_a_out_call, bot_b_in_call, bot_c_in_call]:
            call.hang_up()
