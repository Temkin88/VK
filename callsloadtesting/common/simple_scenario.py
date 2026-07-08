import time
import threading
from typing import Literal

from logging_config import logger

from locust import FastHttpUser
from locust.contrib.fasthttp import FastHttpSession

from imcommonsupplyclient.session import Session
from imcommonsupplyclient.account import Account
from imcommonsupplyclient.voip import VoIPBot, Call

from concurrent.futures import ThreadPoolExecutor

from config_loader import load_config  # загружаем YAML-конфиг

config = load_config()
test_params = config.get("test_parameters", {})


class SimpleBaseUserScenario(FastHttpUser):
    abstract = True

    """
    Получаем общие параметры из config.yml.
    """
    host = config.get("host")
    num_threads = config.get("num_threads")

    env: Literal["ICQ", "SAAS", "VKTI", "PRE_VKTI", "TARM", "PRE_TARM", "SANDBOX"] = "SANDBOX"

    def __init__(self, environment):
        super().__init__(environment)
        self.voip_bots: list[VoIPBot] = []
        self.accounts: list[Account] = []
        self.total_bots = None

    def set_lc_session(self, model: Session | Account | VoIPBot | Call):
        """
        Создаёт новую HTTP-сессию и привязывает её к объекту,
        через который потом будут делаться сетевые запросы
        (Session, Account, VoIPBot или Call).
        """
        ss = FastHttpSession(
            self.environment,
            base_url=self.host,
            network_timeout=self.network_timeout,
            connection_timeout=self.connection_timeout,
            max_redirects=self.max_redirects,
            max_retries=self.max_retries,
            insecure=True,
            concurrency=self.concurrency,
            user=self,
            client_pool=self.client_pool,
            ssl_context_factory=self.ssl_context_factory,
            headers=self.default_headers,
            proxy_host=self.proxy_host,
            proxy_port=self.proxy_port,
        )
        ss.headers = model.http_session.headers
        model.http_session = ss

    def on_start(self) -> None:
        supply_url = config.get("supply_url", "https://load.im-sandbox.devmail.ru/api")

        """
        Setup перед каждым тестом ВКС.
        Выполняется:
            Создание списка аккаунтов и ботов.
            Вычисление общего количество ботов, необходимых для теста.
            Создание сессии с системой управления аккаунтов и ботов через API.
            Получение ботов в многопоточном режиме.
            Пауза перед началом теста.
        """
        self._lock = threading.Lock()

        self.total_bots = self.calculate_bot_requirements()
        logger.info(f"[BOT] - Для теста необходимо {self.total_bots} ботов.")

        logger.info(f"[SESSION] Инициализирую сессию: supply_url={supply_url}, host={self.host}")
        self.im_session = Session(
            environment=self.env,
            domain=self.host,
            test_platform="IMVOIP",
            api_version=125,
            max_accounts_count=self.total_bots,
            supply_url=supply_url,
        )
        self.set_lc_session(self.im_session)
        self.im_session.init_session()

        logger.info(f"[BOT] - Запрашиваю {self.total_bots} ботов.")
        self.thread_init_bots()
        logger.info(f"[BOT] - {self.total_bots} ботов выделены успешно.")

    def test_wait(self):
        """
        Пауза для охлаждение системы.
        """
        cooldown = config.get("cooldown_duration_sec", 120)
        cooldown_minutes = round(cooldown / 60, 1)
        logger.info(f"[WAIT] - Пауза между итерациями - {cooldown_minutes} минут(ы)")
        time.sleep(cooldown)
        logger.info("[WAIT] - Пауза между итерациями окончена")

    def get_bots(self):
        return self.voip_bots

    def calculate_bot_requirements(self):
        raise NotImplementedError("Нужно реализовать calculate_bot_requirements в подклассе")

    def thread_init_bots(self):
        """
        Запрос ботов с использованием многопоточности через ThreadPoolExecutor.
        """
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            chunk_size = 5  # Оптимальное число чанков для докер-контейнера
            total_chunks = (self.total_bots + chunk_size - 1) // chunk_size

            def get_bots_chunk(chunk_id):
                start_idx = chunk_id * chunk_size
                end_idx = min(start_idx + chunk_size, self.total_bots)
                bots_to_get = end_idx - start_idx

                chunk_bots = []
                for _ in range(bots_to_get):
                    try:
                        bot = self.get_bot_threadsafe()
                    except Exception as e:
                        logger.error(f"[BOT] Ошибка при запросе бота: {e}")
                        raise e

                    chunk_bots.append(bot)
                return chunk_bots

            results = list(executor.map(get_bots_chunk, range(total_chunks)))

    def get_bot_threadsafe(self):
        """
        Получает свободную учётную запись из пула;
        Создаёт VoIP-бота на базе этой учётки;
        Регистрирует бота и аккаунт в списках (self.accounts, self.voip_bots);
        Делает всё это потокобезопасно, чтобы его можно было вызывать из ThreadPoolExecutor.
        """
        account = self.im_session.acquire_account()
        self.set_lc_session(account)

        bot = account.get_voip_bot(voip_config={
            "voip-api-version": 2,
            "callstat.impl": "callmon",
            "monitoring.recording_level_treshold": 2000
        })
        with self._lock:
            self.accounts.append(account)
            self.voip_bots.append(bot)

        return bot

    def on_stop(self):
        logger.info("Освобождаю ботов")
        for bot in self.get_bots():
            try:
                logger.info(f"[P2P] Освобождаю бота {bot.account()}")
                bot.release()
            except Exception as e:
                logger.warning(f"[P2P] Не удалось освободить бота: {e}")
        logger.info("Боты освобождены")
        logger.info("Конец теста")

