from concurrent.futures import ThreadPoolExecutor, as_completed

import time
from locust import task
from imcommonsupplyclient.voip import RoomState
from common.simple_scenario import SimpleBaseUserScenario
from logging_config import logger
from config_loader import load_config

# Загрузка конфигурации
config = load_config()
p2p_params = config.get("p2p_parameters", {})


class P2PCallScenario(SimpleBaseUserScenario):

    def __init__(self, environment):
        super().__init__(environment)
        self.start_p2p_calls = p2p_params.get("start_p2p_calls", 1)
        self.total_iterations = p2p_params.get("total_iterations", 1)
        self.scale_iterations = p2p_params.get("scale_iterations", 0)
        self.call_duration = p2p_params.get("call_duration_sec", 60)
        self.wait_call_timeout = p2p_params.get("wait_call_timeout_sec", 5)

        self.max_parallel_calls = p2p_params.get("max_parallel_calls", 5)

    def calculate_bot_requirements(self):
        return self.max_parallel_calls * 2

    @task
    def run_test(self):
        """
        Запускает P2P-звонки параллельно, в рамках итераций.
        """
        logger.info("[TEST] Начинаем выполнение сценария P2P")
        bots = self.get_bots()

        for iteration in range(1, self.total_iterations + 1):
            p2p_calls = self.start_p2p_calls + (iteration - 1) * self.scale_iterations
            logger.info(f"[ITERATION {iteration}] Стартуем {p2p_calls} P2P звонков параллельно.")

            pairs = self._get_bot_pairs(bots, p2p_calls)

            with ThreadPoolExecutor(max_workers=self.max_parallel_calls) as executor:
                futures = [executor.submit(self.handle_call, caller, callee) for caller, callee in pairs]

                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        logger.error(f"[P2P] Ошибка в потоке: {e}")

            logger.info(f"[ITERATION {iteration}] Все звонки завершены.")
            if iteration != self.total_iterations:
                self.test_wait()

        logger.info("[TEST] Сценарий завершён, отключаемся.")
        self.environment.runner.quit()

    def handle_call(self, caller_bot, callee_bot):
        call_from_caller = None
        incoming_call = None
        try:
            # Caller инициирует звонок
            call_from_caller = caller_bot.make_p2p_call(to=callee_bot, with_video=False)
            logger.info(f'[P2P] Бот {caller_bot.account()} совершает звонок без видео')

            # Callee принимает звонок
            incoming_call = callee_bot.wait_incoming_call(timeout=self.wait_call_timeout)
            incoming_call.accept(with_video=False)
            logger.info(f'[P2P] Бот {callee_bot.account()} принимает звонок без видео')

            # Проверка участников до включения камеры
            call_from_caller.check_participants(
                participants=[callee_bot],
                media_connected=True,
                microphone_on=True,
                camera_on=False,
                room_state=RoomState.P2P_ONLY
            )
            incoming_call.check_participants(
                participants=[caller_bot],
                media_connected=True,
                microphone_on=True,
                camera_on=False,
                room_state=RoomState.P2P_ONLY
            )

            # Включение камеры и микрофона
            call_from_caller.unmute_camera()
            incoming_call.unmute_camera()
            call_from_caller.unmute_microphone()
            incoming_call.unmute_microphone()

            # Повторная проверка
            call_from_caller.check_participants(
                participants=[callee_bot],
                media_connected=True,
                microphone_on=True,
                camera_on=True,
                room_state=RoomState.P2P_ONLY
            )
            incoming_call.check_participants(
                participants=[caller_bot],
                media_connected=True,
                microphone_on=True,
                camera_on=True,
                room_state=RoomState.P2P_ONLY
            )

            logger.info(
                f"[P2P] Звонок между {caller_bot.account()} и {callee_bot.account()} установлен, ждём {self.call_duration} сек.")
            time.sleep(self.call_duration)

        except Exception as e:
            logger.error(f"[P2P] Ошибка при установке звонка между {caller_bot.name} и {callee_bot.name}: {e}")

        # Завершение звонка, даже если были ошибки
        try:
            if call_from_caller:
                call_from_caller.hang_up()
                logger.info(f'[P2P] Бот {caller_bot.account()} кладет трубку.')
        except Exception as e:
            logger.error(f"[P2P] Ошибка при завершении звонка (caller) между {caller_bot.name} и {callee_bot.name}: {e}")

        try:
            if incoming_call:
                incoming_call.hang_up()
        except Exception as e:
            logger.error(f"[P2P] Ошибка при завершении звонка (callee) между {caller_bot.name} и {callee_bot.name}: {e}")

    def _get_bot_pairs(self, bots, count):
        """
        Возвращает список пар (caller, callee) для звонков.
        """
        pairs = []
        max_pairs = len(bots) // 2
        if count > max_pairs:
            logger.warning(f"[BOT] Недостаточно ботов для {count} звонков. Используем максимум: {max_pairs}")
            count = max_pairs

        for i in range(count):
            pairs.append((bots[2 * i], bots[2 * i + 1]))

        return pairs
