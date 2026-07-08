import logging
import time

from locust import task

from imcommonsupplyclient.voip import RoomState
from common.scenario import BaseUserScenario

logger = logging.getLogger(__name__)

class CallsLoadTest(BaseUserScenario):
    def on_start(self):
        super().on_start()

        # repeated conference call
        bots = self.get_bots(self.max_users_count)
        first_bot, *other_bots = bots
        self.call_link = first_bot.create_conference().conferenceUrl

    @task(100)
    def conference_call(self):
        call_link = self.voip_bots[0].create_conference().conferenceUrl
        calls = []

        for voip_bot in self.voip_bots:
            try:
                call = voip_bot.make_call_by_link(call_link=call_link, with_video=False)
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

    @task(100)
    def repeated_conference_call(self):
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

    @task(100)
    def p2p_call(self):
        bot_a, bot_b = self.get_bots(self.max_users_count)
        bot_a_call = bot_a.make_p2p_call(to=bot_b, with_video=False)
        bot_b_call = bot_b.wait_incoming_call(timeout=5)
        bot_b_call.accept(with_video=False)

        try:
            bot_a_call.check_participants(
                participants=bot_b,
                media_connected=True,
                microphone_on=True,
                camera_on=False,
                room_state=RoomState.P2P_ONLY,
            )
            bot_b_call.check_participants(
                participants=bot_a,
                media_connected=True,
                microphone_on=True,
                camera_on=False,
                room_state=RoomState.P2P_ONLY,
            )

            bot_a_call.unmute_camera()
            bot_b_call.unmute_camera()
            bot_a_call.check_participants(participants=bot_b, media_connected=True, camera_on=True)
            bot_b_call.check_participants(participants=bot_a, media_connected=True, camera_on=True)

        except Exception as error:
            logger.error(error)

        finally:
            bot_a_call.hang_up()
