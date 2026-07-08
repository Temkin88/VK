import time
import logging

from locust import task

from common.scenario import BaseUserScenario


logger = logging.getLogger(__name__)


class RepeatedConferenceCallScenario(BaseUserScenario):

    def on_start(self) -> None:
        super().on_start()

        bots = self.get_bots(self.max_users_count)

        first_bot, *other_bots = bots

        self.call_link = first_bot.create_conference().conferenceUrl

    @task
    def conference_call(self):
        calls = []

        for voip_bot in self.voip_bots:
            try:
                call = voip_bot.make_call_by_link(call_link=self.call_link, with_video=False)
                self.set_lc_session(call)

                calls.append(call)
            except Exception as error:
                logger.error(error)

        for i in range(15):
            time.sleep(i)
            # cross_check_participants(calls=calls, participants=bots, microphone_on=True, camera_on=False)

        for call in calls:
            try:
                call.hang_up()
            except Exception as error:
                logger.error(error)
