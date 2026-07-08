import time
import threading
from logging_config import logger
from locust import task
from common.scenario import BaseUserScenario
from imcommonsupplyclient.voip import RoomState
from config_loader import load_config  # загрузка YAML-конфиг

'''
Загрузка YAML-конфиг
'''
config = load_config()
test_params = config.get("test_parameters", {})

class ConferenceCallScenario(BaseUserScenario):

    @task
    def conference_call(self):
        logger.info(
            f"[TEST] - === Итерация {self.iteration} из {self.iteration_count}: Создаётся {self.conferences_created} конференций ===")

        active_calls = []
        conference_participants_map = {}
        threads = []

        lock = threading.Lock()
        semaphore = threading.Semaphore(self.num_threads)  # ограничение потоков через семафор

        '''
        Подключение ботов.
        '''
        def thread_connect(conference_index):
            with semaphore:  # ← ограничение количества одновременных потоков
                # logger.info(f"[CONFERENCE] - Создание конференции #{conference_index + 1}...")
                call_link = self.voip_bots[conference_index * self.bots_per_conference].create_conference().conferenceUrl
                bot = self.voip_bots[conference_index * self.bots_per_conference]
                logger.info(f"[CONFERENCE] - Cоздается конференция {conference_index + 1}: user={bot.account()}, cсылка: {call_link}")

                unique_call, participants, calls = self._connect_bots_to_conference(conference_index, call_link)
                if unique_call:
                    with lock:
                        conference_participants_map[unique_call] = participants
                        active_calls.extend(calls)

        for i in range(self.conferences_created):
            t = threading.Thread(target=thread_connect, args=(i,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        logger.info("[WAIT] - Все боты подключены. Ожидание 15 минут...")
        time.sleep(config.get("conference_duration_sec", 900))

        logger.info("[CONFERENCE] - Начинаем завершение всех конференций...")

        threads = []

        '''
        Завершение вызова.
        '''

        def thread_hang_up(call):
            with semaphore:
                try:
                    participants = conference_participants_map.get(call, [])
                    call.check_participants(participants=participants, room_state=RoomState.JOINED)
                    logger.info(
                        f"[BOT] - Проверка участников перед завершением вызова выполнена успешно: call_id={call.call_id}, bot_id={call.bot_id}"
                    )

                    call.hang_up()
                    logger.info(
                        f"[BOT] - Вызов завершен: call_id={call.call_id}, bot_id={call.bot_id}"
                    )
                except Exception as error:
                    error_type = type(error).__name__
                    logger.error(f"[BOT] - [{error_type}] Ошибка при завершении вызова call_id={call.call_id}, bot_id={call.bot_id}: {error}", exc_info=False)

        for call in active_calls:
            t = threading.Thread(target=thread_hang_up, args=(call,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        logger.info(f"[TEST] - === Итерация {self.iteration} завершена ===")

        self._cooldown()


        if self.iteration < self.iteration_count:
            self.conferences_created += self.conferences_scale
            self.iteration += 1
        else:
            logger.info("[TEST] - Достигнуто максимальное количество итераций. Завершаем тест.")
            self.environment.runner.quit()

    '''
    Функция подключения ботов.
    Каждый набор ботов подключается к своей ВКС конференции.
    '''
    def _connect_bots_to_conference(self, conference_index, call_link):
        participants = []
        calls = []
        unique_call = None

        for j in range(self.bots_per_conference):
            bot_index = conference_index * self.bots_per_conference + j
            voip_bot = self.voip_bots[bot_index]

            try:
                call = voip_bot.make_call_by_link(call_link=call_link, with_video=False)
                self.set_lc_session(call)

                if j == 0:
                    unique_call = call

                logger.info(
                    f"[BOT] - Успешно подключён к конференции #{conference_index + 1} "
                    f"user={voip_bot.account()}, bot={voip_bot.id}, session_id={voip_bot.account().session.session_id}"
                )
                participants.append(voip_bot.account())
                calls.append(call)

            except Exception as error:
                error_type = type(error).__name__
                logger.error(
                    f"[BOT] - [{error_type}] Ошибка при подключении бота {voip_bot} к конференции #{conference_index + 1}: {error}")

        for call in calls:
            try:
                call.check_participants(participants=participants, room_state=RoomState.JOINED)
                logger.info(
                    f"[BOT] - Проверка участников выполнена для вызова call_id={call.call_id}, bot_id={call.bot_id}"
                )
            except Exception as error:
                error_type = type(error).__name__
                logger.error(f"[BOT] - [{error_type}] Ошибка при проверке участников для вызова call_id={call.call_id}, bot_id={call.bot_id}: {error}")

        return unique_call, participants, calls

    '''
    Охлаждение системы между итерациями.
    '''
    def _cooldown(self):
        logger.info("[WAIT] - Пауза между итерациями - 2 минуты")
        time.sleep(config.get("cooldown_duration_sec"))
        logger.info("[WAIT] - Пауза между итерациями окончена")
