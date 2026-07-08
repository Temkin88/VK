from locust import LoadTestShape

from scenario.conference_call.conference_call import ConferenceCallScenario
from scenario.conference_call.repeated_conference_call import RepeatedConferenceCallScenario

from scenario.p2p_call.p2p_call import P2PCallScenario


users_list = [ConferenceCallScenario, RepeatedConferenceCallScenario, P2PCallScenario]


class StagesShapeWithCustomUsers(LoadTestShape):

    stages = [
        {"duration": 60, "users": 20, "spawn_rate": 5, "user_classes": users_list},
        {"duration": 120, "users": 40, "spawn_rate": 5, "user_classes": users_list},
        {"duration": 180, "users": 60, "spawn_rate": 5, "user_classes": users_list},
        {"duration": 240, "users": 80, "spawn_rate": 5, "user_classes": users_list},
        {"duration": 300, "users": 100, "spawn_rate": 5, "user_classes": users_list},
        {"duration": 360, "users": 120, "spawn_rate": 5, "user_classes": users_list},
        {"duration": 420, "users": 140, "spawn_rate": 5, "user_classes": users_list},
        {"duration": 480, "users": 160, "spawn_rate": 5, "user_classes": users_list},
        {"duration": 540, "users": 180, "spawn_rate": 5, "user_classes": users_list},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                try:
                    tick_data = (stage["users"], stage["spawn_rate"], stage["user_classes"])
                except:
                    tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
