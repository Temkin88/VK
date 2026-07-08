import time
import threading
from typing import Literal

from logging_config import logger
from locust import FastHttpUser
from locust.contrib.fasthttp import FastHttpSession

from imcommonsupplyclient.session import Session
from imcommonsupplyclient.account import Account
from imcommonsupplyclient.voip import VoIPBot, Call

from config_loader import load_config  # загружаем YAML-конфиг

config = load_config()
test_params = config.get("test_parameters", {})


class BaseUserScenario(FastHttpUser):
    abstract = True

    host = config.get("host")
    iteration = 1
    conferences_created = test_params.get("conferences_created")
    bots_per_conference = test_params.get("bots_per_conference")
    conferences_scale = test_params.get("conferences_scale")
    iteration_count = test_params.get("iteration_count")
    num_threads = test_params.get("num_threads")

    abstract = True

    env: Literal["ICQ", "SAAS", "VKTI", "PRE_VKTI", "TARM", "PRE_TARM", "SANDBOX"] = "SANDBOX"

    def set_lc_session(self, model: Session | Account | VoIPBot | Call):
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

    def get_bot_threadsafe(self):
        account = self.im_session.acquire_account()
        self.set_lc_session(account)

        bot = account.get_voip_bot(voip_config={
            "voip-api-version": 2,
            "callstat.impl": "callmon",
            "monitoring.recording_level_treshold": 2000
        })
        self.set_lc_session(bot)

        with self._lock:
            self.accounts.append(account)
            self.voip_bots.append(bot)

        return bot

    def get_bots(self, count: int = 1):
        if count == 1:
            if self.voip_bots:
                return self.voip_bots[0]
            else:
                return self.get_bot_threadsafe()
        elif count <= len(self.voip_bots):
            return self.voip_bots[:count]

        for _ in range(count - len(self.voip_bots)):
            self.get_bot_threadsafe()

        return self.voip_bots[:count]

    def on_start(self) -> None:
        logger.info("[BOT] - Выделяем учетные записи для ботов...")
        self.accounts: list[Account] = []
        self.voip_bots: list[VoIPBot] = []
        self._lock = threading.Lock()

        self.total_bots = ((self.iteration_count - 1) * self.conferences_scale + self.conferences_created) * self.bots_per_conference
        self.max_users_count = self.total_bots

        logger.info(f"[BOT] - Для теста необходимо {self.max_users_count} ботов.")

        self.im_session = Session(
            environment=self.env,
            domain=self.host,
            test_platform="IMVOIP",
            api_version=125,
            max_accounts_count=self.max_users_count * 2,
            supply_url=config.get("supply_url", "https://load.im-sandbox.devmail.ru/api"),
        )
        self.set_lc_session(self.im_session)
        self.im_session.init_session()

        threads = []
        bots_per_thread = self.max_users_count // self.num_threads
        remainder = self.max_users_count % self.num_threads

        def worker(count):
            for _ in range(count):
                self.get_bot_threadsafe()

        for i in range(self.num_threads):
            count = bots_per_thread + (1 if i < remainder else 0)
            t = threading.Thread(target=worker, args=(count,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        logger.info(f"[BOT] - {self.total_bots} ботов выделены успешно.")

        '''
        Охлаждение системы между итерациями.
        '''
        logger.info("[WAIT] - Пауза между итерациями - 2 минуты")
        time.sleep(config.get("cooldown_duration_sec"))
        logger.info("[WAIT] - Пауза между итерациями окончена")

    def on_stop(self):
        logger.info("[BOT] - Пробуем завершить сессии...")
        self.im_session.end_session()
        logger.info("[BOT] - Сессии завершены успешно.")
        logger.info("[TEST] - Конец теста.")
